const {test}=require('node:test'),assert=require('node:assert/strict'),vm=require('node:vm'),fs=require('node:fs');
const P=require('../src/progress.js');
const learning=fs.readFileSync('src/learning.js','utf8');
const page=fs.readFileSync('index.html','utf8');
const data=JSON.parse(page.split(/\r?\n/).find(l=>l.startsWith('const DATA = ')).slice(13).replace(/;\s*$/,''));
// An isolated DOM fixture exercises event wiring without a browser, fonts, network or user data.
function fixture(english=false){
  class Element{constructor(){this.nodes=new Map();this.value='';this.attrs={};this.classList={remove(){},add(){}};}set innerHTML(s){this.html=s;this.nodes.clear();for(const m of s.matchAll(/id="([^"]+)"/g))this.nodes.set('#'+m[1],new Element());}get innerHTML(){return this.html||'';}querySelector(s){if(s==='canvas')return {};return this.nodes.get(s);}querySelectorAll(){return [];}setAttribute(k,v){this.attrs[k]=v;}}
  const body=new Element(),slot=new Element(),type=new Element(),region=new Element();const elements={dlgbody:body,dlgslot:slot,mtype:type,mreg:region};
  const context={S:P.fresh(),WMAP:Object.fromEntries(data.words.map(w=>[w[0],w])),WORDS:data.words,document:{getElementById:id=>elements[id],addEventListener(){}},tr:(fr,en)=>english?en:fr,esc:s=>String(s),store:{set(){}},SKEY:'test',cancelAuto(){},LAST_GRADE:null,REPLAY_ID:null,SESSION:null,TESTRES:null,dlg:{open:false,showModal(){this.open=true;},close(){this.open=false;}},location:{hash:''},xp:()=>'',wordChips:()=>'',reviewBtn:()=>'',sayBtn:()=>'',toRomaji:s=>s,rng:()=>()=>.5,makeWriter:()=>({}),textCanvas(){},firstId:w=>'r:'+w,fillSelects(){context.menuDone=true;},genMenu(){context.generated=true;},menuDone:false,mmode:'meaning',qpool:'known',toast(){},today:()=> '2026-11-25',showCard(){},newQuest(){}};
  vm.createContext(context);vm.runInContext(learning,context);return{context,body,type};
}
test('personal practice uses saved words and resets a pending undo replay',()=>{
  const {context:c}=fixture();c.S.favorites['ライス']={on:true,at:1};c.REPLAY_ID='r:焼鳥';
  vm.runInContext('reviewPersonal()',c);assert.deepEqual(Array.from(c.SESSION.q),['r:ライス']);assert.equal(c.REPLAY_ID,null);assert.equal(c.location.hash,'revisions');
});
test('daily report offers only cards missed on their first encounter',()=>{
  const {context:c}=fixture();c.S.activity['2026-11-25']={'r:焼鳥':{ok:false,at:1},'r:ライス':{ok:true,at:2}};
  const report=vm.runInContext('dailyReport()',c);assert.match(report,/焼鳥/);assert.doesNotMatch(report,/ライス/);
  vm.runInContext('reviewDifficult()',c);assert.deepEqual(Array.from(c.SESSION.q),['r:焼鳥']);
});
test('drawing survives a resize with its undo history',()=>{
  const script=fs.readFileSync('src/template.html','utf8');const a=script.indexOf('class Pad{'),b=script.indexOf('// ---------- kanji dialog',a);
  const noop=()=>{};class Node{constructor(){this.clientWidth=300;this.children=[];}appendChild(x){this.children.push(x);}addEventListener(){}getContext(){return new Proxy({getImageData:()=>({width:this.width,height:this.height})},{get:(o,k)=>o[k]||noop,set:(o,k,v)=>(o[k]=v,true)});}}
  let disconnected=false;const c={document:{createElement:()=>new Node()},Ambience:{attachInk:()=>({refresh:noop,clear:noop,destroy:noop})},ResizeObserver:class{observe(){}disconnect(){disconnected=true;}},DPR:1,fillSurface:noop,drawRef:noop,clearTimeout:noop,cancelAnimationFrame:noop};
  vm.createContext(c);const Pad=vm.runInContext(script.slice(a,b)+'\nPad',c);const pad=new Pad(new Node(),'牛');pad.strokes=[[[10,20],[30,40]]];pad.snaps=[{width:300,height:300}];pad.el.clientWidth=600;pad.resize();
  assert.equal(pad.size,600);assert.deepEqual(pad.strokes,[[[10,20],[30,40]]]);assert.equal(pad.snaps.length,1);assert.equal(pad.snaps[0].width,600);pad.destroy();assert.equal(disconnected,true);
});
