# builds scenes-review.html: the app page with everything hidden except the window shadows; tap/arrows cycle scenes, swipe or up/down change the hour
src=open('kanji-pinceau.html',encoding='utf-8').read()
css='<style>body>*:not(#shade):not(#veil):not(#light){display:none!important}html,body{min-height:100%;height:100%;overflow:hidden;touch-action:none;cursor:pointer}</style>'
js='''<script>(function(){ const P=window.SHADE_POOL||[]; let i=0, hi=3; window.setShade=()=>{}; const SI=window.SUNINFO(), R0=SI.rise, S0=SI.set, D0=S0-R0; const HRS=[R0-.3,R0+.1,R0+.8,R0+D0*.25,SI.noon,S0-D0*.25,S0-.8,S0-.2,S0+.6,S0+3].map(h=>(h+24)%24);
 try{ localStorage.setItem('menyomi.onb','1'); }catch(e){}
 const show=()=>{ window.setShadeKind(P[i]); }; const go=d=>{ i=(i+d+P.length)%P.length; show(); }; const hr=d=>{ hi=(hi+d+HRS.length)%HRS.length; window.shadeHour(HRS[hi]); };
 setTimeout(()=>{ window.shadeHour(HRS[hi]); show(); },60);
 addEventListener('keydown',e=>{ const k=e.key; if(k==='ArrowRight'||k===' '||k==='Enter') go(1); else if(k==='ArrowLeft') go(-1); else if(k==='ArrowUp') hr(1); else if(k==='ArrowDown') hr(-1); else return; e.preventDefault(); });
 let sx=0, sy=0; addEventListener('pointerdown',e=>{ sx=e.clientX; sy=e.clientY; });
 addEventListener('pointerup',e=>{ const dx=e.clientX-sx, dy=e.clientY-sy; if(Math.abs(dy)>50&&Math.abs(dy)>Math.abs(dx)) hr(dy<0?1:-1); else if(Math.abs(dx)>50) go(dx<0?1:-1); else go(e.clientX<innerWidth/3?-1:1); }); })();</script>'''
out=css+src
k=out.rfind('</body>'); out=out[:k]+js+out[k:]
import re; out=re.sub(r'<title>[^<]*</title>','<title>Scènes d’ombres</title>',out,count=1)
open('scenes-review.html','w',encoding='utf-8').write(out); print(len(out))

open('review-test.html','w',encoding='utf-8').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>'+out+'</body></html>')
