// Menyomi offline cache. The version changes with every build so a new page replaces the old one.
const V='menyomi-a49c7450'; const CORE=['./','index.html','manifest.webmanifest','voice.mp3','icon-192.png','icon-512.png','icon-180.png','icon-32.png'];
self.addEventListener('install',e=>{ e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())); });
self.addEventListener('activate',e=>{ e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V&&k!=='menyomi-fonts').map(k=>caches.delete(k)))).then(()=>self.clients.claim())); });
self.addEventListener('fetch',e=>{ const u=new URL(e.request.url); if(e.request.method!=='GET') return;
  if(u.hostname==='fonts.googleapis.com'||u.hostname==='fonts.gstatic.com'){
    e.respondWith(caches.open('menyomi-fonts').then(async c=>{ const hit=await c.match(e.request); const net=fetch(e.request).then(r=>{ if(r.ok||r.type==='opaque') c.put(e.request,r.clone()); return r; }).catch(()=>hit); return hit||net; })); return; }
  if(u.origin!==location.origin) return;
  if(e.request.mode==='navigate'){ e.respondWith(fetch(e.request).then(r=>{ const cp=r.clone(); caches.open(V).then(c=>c.put('index.html',cp)); return r; }).catch(()=>caches.match('index.html'))); return; }
  e.respondWith(caches.match(e.request).then(h=>h||fetch(e.request)));
});
