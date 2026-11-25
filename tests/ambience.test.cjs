const {test}=require('node:test'),assert=require('node:assert/strict'),A=require('../src/ambience.js');
const day=n=>new Date(2026,10,25+n,12).getTime();
test('each screen gets a distinct background and shadow for the same local day',()=>{
  for(let n=0;n<100;n++){
    const choices=A.views.map(v=>A.selection(v,day(n)));
    assert.equal(new Set(choices.map(c=>c.background)).size,6);
    assert.equal(new Set(choices.map(c=>c.shadow)).size,6);
  }
});
test('independent coprime cycles visit every background/shadow pair',()=>{
  for(const view of A.views){const pairs=new Set();for(let n=0;n<91;n++){const c=A.selection(view,day(n));pairs.add(c.background+'|'+c.shadow);}assert.equal(pairs.size,91);}
});
test('lantern scenes always contain at least three lanterns',()=>{
  const counts=new Set();for(let n=-100;n<500;n++)for(const view of A.views){const c=A.selection(view,day(n));assert.ok(c.lanterns>=3&&c.lanterns<=5);counts.add(c.lanterns);}assert.deepEqual([...counts].sort(),[3,4,5]);
});
test('paper tape and folds are deterministic, varied, and never fold under a pinned right corner',()=>{
  const variations=new Set();for(let n=0;n<100;n++){
    const spec=A.paperSpec('営業中',1,day(n));assert.deepEqual(spec,A.paperSpec('営業中',1,day(n)));
    assert.ok(spec.tapes.length>=1&&spec.tapes.length<=2);assert.ok(spec.size>=10&&spec.size<=16);assert.ok(['none','br','bl','tr'].includes(spec.fold));
    if(spec.tapes.some(t=>t.left>=60))assert.notEqual(spec.fold,'tr');
    variations.add(JSON.stringify(spec));
  }assert.equal(variations.size,100);
});
