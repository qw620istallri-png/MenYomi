const {test,before,after}=require('node:test');
const fs=require('node:fs');
const {initializeTestEnvironment,assertSucceeds,assertFails}=require('@firebase/rules-unit-testing');
const {doc,setDoc,getDoc,deleteDoc}=require('firebase/firestore');
let env;
before(async()=>{env=await initializeTestEnvironment({projectId:'demo-menyomi',firestore:{host:'127.0.0.1',port:8087,rules:fs.readFileSync('firestore.rules','utf8')}});});
after(async()=>{await env?.cleanup();});
test('only the owner can write and read progress',async()=>{
  const owner=env.authenticatedContext('owner').firestore(),other=env.authenticatedContext('other').firestore(),anon=env.unauthenticatedContext().firestore();
  await assertSucceeds(setDoc(doc(owner,'users/owner'),{s:'{"cards":{}}',t:1,v:2}));
  await assertSucceeds(getDoc(doc(owner,'users/owner')));
  await assertFails(getDoc(doc(other,'users/owner')));
  await assertFails(setDoc(doc(other,'users/owner'),{s:'{}',t:1,v:2}));
  await assertFails(getDoc(doc(anon,'users/owner')));
  await assertFails(setDoc(doc(anon,'users/anon'),{s:'{}',t:1,v:2}));
});
test('old clients stay compatible; malformed and oversized writes fail',async()=>{
  const db=env.authenticatedContext('validation').firestore(),ref=doc(db,'users/validation');
  await assertSucceeds(setDoc(ref,{s:'{}',t:1,v:1}));
  for(const payload of [{s:{},t:1,v:2},{s:'{}',t:'x',v:2},{s:'{}',t:1,v:3},{s:'{}',t:1,v:2,admin:true},{s:'x'.repeat(900001),t:1,v:2}]) await assertFails(setDoc(ref,payload));
  await assertFails(deleteDoc(ref));
});
