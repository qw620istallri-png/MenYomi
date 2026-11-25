const {test}=require('node:test');
const assert=require('node:assert/strict');
const P=require('../src/progress.js');
const ids=['r:焼鳥','m:焼鳥','r:ライス','m:ライス'],words=['焼鳥','ライス'];
const card=(at,extra={})=>({due:at+86400000,ivl:1,ease:2.5,reps:1,lapses:0,at,...extra});
const day=t=>new Date(t).toISOString().slice(0,10);
const read=s=>P.validate(JSON.parse(s),ids,words);
test('legacy progress migrates without losing its cards',()=>{
  const old={cards:{'r:焼鳥':card(1)},day:'2026-11-25',newToday:1,newPer:20};
  const result=P.validate(old,ids,words);assert.deepEqual(result.cards,old.cards);assert.equal(result.newPer,20);assert.deepEqual(result.queue,[]);
});
test('invalid imports never yield an applicable state',()=>{
  for(const bad of [null,{}, {cards:null},{cards:[]},{cards:{'r:焼鳥':{due:'wrong'}}},{cards:{'r:焼鳥':card(NaN)}},{cards:{'r:unknown':card(1)}},{cards:{},newPer:0},{cards:{},todayIds:['bad']},{cards:{},favorites:{'ライス':{on:'true',at:1}}}]) assert.equal(P.validate(bad,ids,words),null);
});
test('merge keeps newer ratings and counts distinct introductions across devices',()=>{
  const t=Date.UTC(2026,10,25,12),a=P.fresh(),b=P.fresh();a.day=b.day=day(t);a.newToday=b.newToday=1;
  a.cards['r:焼鳥']=card(t,{introduced:t});b.cards['r:ライス']=card(t+1,{introduced:t+1});
  b.cards['r:焼鳥']=card(t+2,{introduced:t});
  const merged=P.merge(a,b,day);assert.equal(merged.cards['r:焼鳥'].at,t+2);assert.equal(merged.newToday,2);assert.equal(Object.keys(merged.cards).length,2);
});
test('undo tombstones survive merging an old cloud snapshot',()=>{
  const old=P.fresh(),undone=P.fresh();old.cards['r:焼鳥']=card(10);undone.removed['r:焼鳥']=11;
  assert.equal(P.merge(undone,old,day).cards['r:焼鳥'],undefined);
  undone.cards['r:焼鳥']=card(12);assert.equal(P.merge(undone,old,day).cards['r:焼鳥'].at,12);
});
test('undo restores the daily budget and removes its first-attempt result after sync',()=>{
  const at=Date.UTC(2026,10,25,12),old=P.fresh(),undone=P.fresh(),d=day(at);
  old.day=undone.day=d;old.cards['r:焼鳥']=card(at,{introduced:at});old.newToday=1;old.activity[d]={'r:焼鳥':{ok:false,at}};old.days[d]=[0,1];
  undone.removed['r:焼鳥']=at+1;undone.activityRemoved[d]={'r:焼鳥':at+1};
  const merged=P.merge(undone,old,day);assert.equal(merged.newToday,0);assert.deepEqual(merged.days[d],[0,0]);
  undone.activity[d]={'r:焼鳥':{ok:true,at:at+2}};
  assert.deepEqual(P.merge(undone,old,day).days[d],[1,1]);
});
test('removed favourites stay removed and study records deduplicate',()=>{
  const a=P.fresh(),b=P.fresh();a.favorites['ライス']={on:true,at:1};b.favorites['ライス']={on:false,at:2};
  a.activity['2026-11-25']={'r:焼鳥':{ok:false,at:1}};b.activity['2026-11-25']={'r:焼鳥':{ok:true,at:2},'m:ライス':{ok:true,at:3}};
  const merged=P.merge(a,b,day);assert.equal(merged.favorites['ライス'].on,false);assert.deepEqual(merged.days['2026-11-25'],[1,2]);
  assert.deepEqual(P.merge(merged,merged,day),merged);
});
test('transaction retry preserves two concurrent devices and never mutates their local state',async()=>{
  let value=null,version=0,retries=0;
  const F={async runTransaction(db,fn){for(let i=0;i<5;i++){const v=version;let write;const snapshot=value;
    const result=await fn({async get(){await new Promise(r=>setImmediate(r));return {exists:()=>snapshot!==null,data:()=>snapshot};},set(ref,data){write=data;}});
    if(v!==version){retries++;continue;}value=write;version++;return result;
  }throw Error('too many retries');}};
  const a=P.fresh(),b=P.fresh();a.cards['r:焼鳥']=card(10);b.cards['r:ライス']=card(11);
  await Promise.all([P.commit(F,{},'users/test',a,read,day),P.commit(F,{},'users/test',b,read,day)]);
  assert.ok(retries>0);assert.equal(Object.keys(read(value.s).cards).length,2);assert.equal(Object.keys(a.cards).length,1);
});
test('invalid remote data aborts before any write',async()=>{
  let wrote=false;const F={runTransaction:(_,fn)=>fn({get:async()=>({exists:()=>true,data:()=>({s:'{"cards":null}'})}),set(){wrote=true;}})};
  await assert.rejects(P.commit(F,{},'test',P.fresh(),read,day),/invalid-remote/);assert.equal(wrote,false);
});
