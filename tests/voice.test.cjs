const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const R=path.join(__dirname,'..'), D=JSON.parse(fs.readFileSync(R+'/index.html','utf8').match(/const DATA = (\{.*?\});\n/)[1]), V=JSON.parse(fs.readFileSync(R+'/src/voice/voice.json','utf8'));
test('every word, phrase and shop-name part has both recorded voices',()=>{
  const keys=[...D.words.map(w=>w[0]),...D.names.map(n=>n[0]),...Object.keys(D.namepat)];
  const missing=keys.filter(k=>!V[k]||V[k].length!==4);
  assert.deepEqual(missing,[],'run src/voice/gen.py for: '+missing.join(' '));
});
test('voice clips fit inside voice.mp3',()=>{
  const size=fs.statSync(R+'/voice.mp3').size;
  for(const [k,e] of Object.entries(V)) for(let i=0;i<e.length;i+=2) assert.ok(e[i]+e[i+1]<=size,k);
});
