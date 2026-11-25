// Menyomi offline cache. The version changes with every build so a new page replaces the old one.
const V='menyomi-e31466f4'; self.addEventListener('message',e=>{ if(e.data==='skip') self.skipWaiting(); }); const CORE=['./','index.html','manifest.webmanifest','voice.mp3','icon-192.png','icon-512.png','icon-180.png','icon-32.png'];
self.addEventListener('install',e=>{ e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())); });
self.addEventListener('activate',e=>{ e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V&&k!=='menyomi-fonts'&&k!=='menyomi-state').map(k=>caches.delete(k)))).then(()=>self.clients.claim())); });
self.addEventListener('periodicsync',e=>{ if(e.tag!=='menyomi-daily') return; e.waitUntil((async()=>{
  const c=await caches.open('menyomi-state'); const r=await c.match('due.json'); if(!r) return; const st=await r.json(); if(!st.on) return;
  const day=new Date().toDateString(); const lr=await c.match('last.txt'); if(lr&&(await lr.text())===day) return;
  const n=(st.due||[]).filter(d=>d<=Date.now()).length; if(!n) return;
  const fr=st.lang!=='en'; await self.registration.showNotification('Menyomi めん読み',{body:fr?(n+(n>1?' cartes t’attendent':' carte t’attend')):(n+(n>1?' cards are waiting':' card is waiting')),icon:'icon-192.png',badge:'icon-192.png',tag:'menyomi-daily',data:{url:'./#revisions'}});
  await c.put('last.txt',new Response(day)); })()); });
self.addEventListener('notificationclick',e=>{ e.notification.close(); e.waitUntil(clients.matchAll({type:'window',includeUncontrolled:true}).then(ws=>{ for(const w of ws){ if('focus' in w){ w.navigate&&w.navigate('./#revisions'); return w.focus(); } } return clients.openWindow('./#revisions'); })); });
self.addEventListener('fetch',e=>{ const u=new URL(e.request.url); if(e.request.method!=='GET') return;
  if(u.hostname==='fonts.googleapis.com'||u.hostname==='fonts.gstatic.com'){
    e.respondWith(caches.open('menyomi-fonts').then(async c=>{ const hit=await c.match(e.request); const net=fetch(e.request).then(r=>{ if(r.ok||r.type==='opaque') c.put(e.request,r.clone()); return r; }).catch(()=>hit); return hit||net; })); return; }
  if(u.origin!==location.origin) return;
  if(e.request.mode==='navigate'){ e.respondWith(fetch(e.request).then(r=>{ const cp=r.clone(); caches.open(V).then(c=>c.put('index.html',cp)); return r; }).catch(()=>caches.match('index.html'))); return; }
  e.respondWith(caches.match(e.request).then(h=>h||fetch(e.request)));
});
