const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm');
const html=fs.readFileSync('index.html','utf8'),script=html.match(/<script>([\s\S]*?)<\/script>/)[1];
test('built app has valid JavaScript and no unresolved build markers',()=>{
  new vm.Script(script);assert.doesNotMatch(html,/__(DATA|K|EN|VOICE|LEARNING|PROGRESS|BUILD|TZ|FONTTEXT)__/);
});
test('all kana vocabulary receives SRS cards, including restaurant staples',()=>{
  const data=JSON.parse(script.split(/\r?\n/).find(l=>l.startsWith('const DATA = ')).slice(13).replace(/;\s*$/,''));
  const a=script.indexOf('function buildCards()'),b=script.indexOf('const CARDS=',a);
  const context={WORDS:data.words,WMAP:Object.fromEntries(data.words.map(w=>[w[0],w])),CORE_ORDER:[],PH:data.phrases,PH_FIRST:[],hasKanji:w=>/[一-鿿]/.test(w),isKanji:c=>/[一-鿿]/.test(c),isPhrase:w=>[...data.phrases.signs,...data.phrases.talk].includes(w),KVG:data.kvg};
  vm.createContext(context);const cards=vm.runInContext(script.slice(a,b)+'buildCards()',context);
  for(const w of data.words) assert.ok(cards.includes('m:'+w[0]),w[0]);
  for(const word of ['ライス','つくね','ハイボール'])assert.ok(cards.includes('r:'+word));
});
test('service worker activation preserves other apps and notification state',async()=>{
  const handlers={},deleted=[];let work;
  const ctx={self:{addEventListener:(name,fn)=>handlers[name]=fn,clients:{claim:async()=>{}}},caches:{keys:async()=>['another-app-v1','menyomi-older','menyomi-fonts','menyomi-state'],delete:async k=>deleted.push(k)}};
  vm.runInNewContext(fs.readFileSync('sw.js','utf8'),ctx);
  handlers.activate({waitUntil(p){work=p;}});await work;assert.deepEqual(deleted,['menyomi-older']);
});
