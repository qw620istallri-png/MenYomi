import json, hashlib
full=open('kanji-pinceau.html',encoding='utf-8').read()
ver=hashlib.sha1(full.encode()+open('voice.mp3','rb').read()).hexdigest()[:8]
import shutil; shutil.copy('voice.mp3','site/voice.mp3'); shutil.copytree('fb','site/fb',dirs_exist_ok=True)
head='''<!doctype html>
<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#f7f0e1">
<meta name="description" content="Lire les menus japonais écrits à la main.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="32x32" href="icon-32.png">
<link rel="apple-touch-icon" href="icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Menyomi">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
</head><body>
'''
open('site/index.html','w',encoding='utf-8').write(head+full+'\n</body></html>\n')
man={"name":"Menyomi めん読み","short_name":"Menyomi","description":"Lire les menus japonais écrits à la main.","lang":"fr","start_url":"./","scope":"./","display":"standalone","orientation":"any","background_color":"#f7f0e1","theme_color":"#f7f0e1",
 "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"}]}
open('site/manifest.webmanifest','w',encoding='utf-8').write(json.dumps(man,ensure_ascii=False,indent=1))
sw='''// Menyomi offline cache. The version changes with every build so a new page replaces the old one.
const V='menyomi-%s'; const CORE=['./','index.html','manifest.webmanifest','voice.mp3','icon-192.png','icon-512.png','icon-180.png','icon-32.png'];
self.addEventListener('install',e=>{ e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())); });
self.addEventListener('activate',e=>{ e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V&&k!=='menyomi-fonts').map(k=>caches.delete(k)))).then(()=>self.clients.claim())); });
self.addEventListener('fetch',e=>{ const u=new URL(e.request.url); if(e.request.method!=='GET') return;
  if(u.hostname==='fonts.googleapis.com'||u.hostname==='fonts.gstatic.com'){
    e.respondWith(caches.open('menyomi-fonts').then(async c=>{ const hit=await c.match(e.request); const net=fetch(e.request).then(r=>{ if(r.ok||r.type==='opaque') c.put(e.request,r.clone()); return r; }).catch(()=>hit); return hit||net; })); return; }
  if(u.origin!==location.origin) return;
  if(e.request.mode==='navigate'){ e.respondWith(fetch(e.request).then(r=>{ const cp=r.clone(); caches.open(V).then(c=>c.put('index.html',cp)); return r; }).catch(()=>caches.match('index.html'))); return; }
  e.respondWith(caches.match(e.request).then(h=>h||fetch(e.request)));
});
'''%ver
open('site/sw.js','w',encoding='utf-8').write(sw)
open('site/.nojekyll','w').write('')
print(ver)
