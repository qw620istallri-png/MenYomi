"""Build scenes-review.html: the app with everything hidden except the background and the window shadows.
Bar at the bottom: shadow scene, background and hour, each with ◀ ▶ (keys: ←/→ scene, ↑/↓ hour, B background)."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / 'index.html').read_text(encoding='utf-8')
out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'scenes-review.html'
css = '''<style>body>*:not(#shade):not(#veil):not(#light):not(#ground):not(#rvbar){display:none!important}html,body{min-height:100%;height:100%;overflow:hidden}
#rvbar{position:fixed;left:50%;bottom:max(14px,env(safe-area-inset-bottom));transform:translateX(-50%);z-index:99;display:flex;gap:6px;flex-wrap:nowrap;font:600 15px/1 system-ui,sans-serif}
#rvbar div{display:flex;align-items:center;background:#1b1814;color:#f7f0e1;border:2px solid #1b1814}
#rvbar button{all:unset;cursor:pointer;padding:10px 10px;font-size:16px}#rvbar span{padding:0 4px;min-width:64px;text-align:center;white-space:nowrap}
@media (max-width:520px){#rvbar{gap:4px;font-size:14px}#rvbar button{padding:10px 6px}#rvbar span{min-width:48px}}</style>'''
js = '''<div id="rvbar"><div><button data-d="s-">◀</button><span id="rvs"></span><button data-d="s+">▶</button></div><div><button data-d="b-">◀</button><span id="rvb"></span><button data-d="b+">▶</button></div><div><button data-d="h-">◀</button><span id="rvh"></span><button data-d="h+">▶</button></div></div>
<script>(function(){ const P=window.SHADE_POOL||[], BG=Ambience.backgrounds; let i=0, bi=0, hi=0; window.setShade=()=>{};
 const SI=window.SUNINFO(), R0=SI.rise, S0=SI.set, D0=S0-R0, nowH=()=>{ const d=new Date(); return d.getHours()+d.getMinutes()/60; };
 const HRS=[null,R0+.1,R0+.8,R0+D0*.25,SI.noon,S0-D0*.25,S0-.8,S0-.2,S0+.6,S0+3];
 const fmt=h=>{ h=(h+24)%24; const m=Math.round(h*60)%1440; return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0'); };
 const paint=()=>{ const h=HRS[hi]??nowH(); window.setShadeKind(P[i]); Ambience.background(BG[bi]); window.shadeHour((h+24)%24);
   document.getElementById('rvs').textContent=P[i]; document.getElementById('rvb').textContent=BG[bi]==='current'?'crème':BG[bi]; document.getElementById('rvh').textContent=(hi?'':'⏱ ')+fmt(h); };
 const step=(k,d)=>{ if(k==='s') i=(i+d+P.length)%P.length; if(k==='b') bi=(bi+d+BG.length)%BG.length; if(k==='h') hi=(hi+d+HRS.length)%HRS.length; paint(); };
 document.getElementById('rvbar').addEventListener('click',e=>{ const b=e.target.closest('[data-d]'); if(b) step(b.dataset.d[0],b.dataset.d[1]==='+'?1:-1); });
 addEventListener('keydown',e=>{ const k=e.key; if(k==='ArrowRight') step('s',1); else if(k==='ArrowLeft') step('s',-1); else if(k==='ArrowUp') step('h',1); else if(k==='ArrowDown') step('h',-1); else if(k==='b'||k==='B') step('b',1); else return; e.preventDefault(); });
 try{ localStorage.setItem('menyomi.onb','1'); }catch(e){} setTimeout(paint,80); })();</script>'''
out = src.replace('</head>', css + '</head>', 1)
k = out.rfind('</body>'); out = out[:k] + js + out[k:]
import re
out = re.sub(r'<title>[^<]*</title>', '<title>Fonds et ombres</title>', out, count=1)
out_path.write_text(out, encoding='utf-8'); print(out_path, len(out))
