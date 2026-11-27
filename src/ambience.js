// Calendar choices are independent of the SRS day and of the visitor's study progress.
const Ambience=(()=>{
  const views=['revisions','menu','atelier','main','kanji','vocab'];
  const backgrounds=['current','washi','mineral','shikkui','kinari','matcha','sakura'];
  const shadows=['momiji','sudare','bamboo','shoji','pine','fuji','ginkgo','noren','hanabira','furin','sakura','ame','chochin'];
  const mod=(n,m)=>(n%m+m)%m;
  function dayNumber(time=Date.now()){const d=new Date(time);return Math.floor(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate())/864e5);}
  function selection(view,time=Date.now()){
    const day=dayNumber(time),index=Math.max(0,views.indexOf(view));
    return {day,background:backgrounds[mod(day+index,7)],shadow:shadows[mod(day+index,13)],lanterns:3+mod(day+index,3)};
  }
  function random(seed){let a=seed>>>0;return()=>{a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
  function paperSpec(word,index=0,time=Date.now()){
    let hash=0;for(const c of word)hash=Math.imul(hash,31)+c.codePointAt(0)|0;
    const day=dayNumber(time),r=random(day*7919+hash),pattern=mod(day+index*2+hash,5);
    const patterns=[[[44,-7,37,16,-5]],[[7,-7,29,16,-22]],[[67,-7,31,16,16]],[[7,-6,25,15,-15],[73,-6,25,15,13]],[[-3,11,14,33,-8]]];
    const tapes=patterns[pattern].map(([left,top,width,height,angle])=>({left:left+(r()-.5)*3,top,width,height,angle:angle+(r()-.5)*5}));
    let fold=['br','none','bl','tr'][mod(day+index+hash,4)];if(fold==='tr'&&(pattern===2||pattern===3))fold='bl';
    return {tapes,fold,size:10+Math.round(r()*6),angle:(r()-.5)*5,pivot:pattern===1?'17% 4px':pattern===2?'82% 4px':pattern===4?'0% 30%':'50% 4px'};
  }
  let currentView='revisions';const textures={};let woodURL='';
  function texture(kind){
  if(kind==='current')return '';
  // the cloudy materials get a tile twice as large, so their soft patches do not visibly repeat
  const S=kind==='matcha'||kind==='shikkui'?1024:512,K=(S/512)**2,bases={washi:[241,234,219],mineral:[222,219,209],shikkui:[240,238,229],kinari:[234,226,209],matcha:[225,230,218],sakura:[238,226,222]},base=bases[kind];
  const fine=valueNoise(S,70*S/512,151),broad=valueNoise(S,5*S/512,97);let r;
  const c=noiseTile(S,43,(q,X,Y)=>{
    const granular=kind==='mineral'?15:kind==='washi'?8:kind==='sakura'?5:3;
    const n=(q()-.5)*granular+(fine(X,Y)-.5)*(kind==='mineral'?14:3)+(broad(X,Y)-.5)*(kind==='shikkui'?9:kind==='matcha'?15:4);
    return [base[0]+n,base[1]+n,base[2]+n];
  });
  const x=c.getContext('2d');
  // fibres and strokes are drawn nine times, shifted by one tile each way, so whatever crosses an edge comes back on the other side: no seams when the tile repeats
  const paint=()=>{
  if(kind==='washi'){
    for(let i=0;i<1800;i++){
      const a=r()*S,b=r()*S,l=3+r()*27,angle=r()*6.28;
      x.lineWidth=.35+r()*.7;x.strokeStyle=i%3?'rgba(110,89,54,.10)':'rgba(255,255,248,.62)';
      x.beginPath();x.moveTo(a,b);x.quadraticCurveTo(a+Math.cos(angle+.3)*l*.5,b+Math.sin(angle+.3)*l*.5,a+Math.cos(angle)*l,b+Math.sin(angle)*l);x.stroke();
    }
  }else if(kind==='mineral'){
    for(let i=0;i<22000;i++){x.fillStyle=i%3?'rgba(81,75,60,.09)':'rgba(255,255,250,.45)';x.beginPath();x.arc(r()*S,r()*S,.2+r()*.7,0,6.3);x.fill();}
    x.filter='blur(4px)';x.lineWidth=3;
    for(let i=0;i<26;i++){x.strokeStyle=i%2?'rgba(119,111,89,.04)':'rgba(255,255,250,.13)';const y=r()*S;x.beginPath();x.moveTo(r()*120,y);x.quadraticCurveTo(260,y-20+r()*40,S,y-14+r()*28);x.stroke();}x.filter='none';
  }else if(kind==='kinari'){
    for(let a=0;a<S;a+=3){
      const shift=(r()-.5)*1.2;x.lineWidth=.55+r()*.3;x.strokeStyle='rgba(124,105,73,.10)';x.beginPath();x.moveTo(a+shift,0);x.bezierCurveTo(a-.5,170,a+.5,350,a+shift,S);x.stroke();
      x.strokeStyle='rgba(255,253,240,.72)';x.beginPath();x.moveTo(0,a);x.lineTo(S,a);x.stroke();
    }
    for(let i=0;i<1800;i++){x.fillStyle='rgba(115,97,66,.055)';x.fillRect(r()*S,r()*S,1,2+r()*3);}
  }else if(kind==='shikkui'){
    x.filter='blur(5px)';x.lineWidth=14;
    for(let i=0;i<34*K;i++){const a=r()*S,b=r()*S;x.strokeStyle=i%2?'rgba(173,163,139,.10)':'rgba(255,255,252,.53)';x.beginPath();x.moveTo(a-90,b+20);x.quadraticCurveTo(a,b-22,a+100,b);x.stroke();}x.filter='none';
  }else if(kind==='matcha'){
    x.filter='blur(8px)';x.lineWidth=22;
    for(let i=0;i<32*K;i++){const a=r()*S,b=r()*S,t=(r()-.5)*1.2,l=.6+r()*.8;x.strokeStyle=i%2?'rgba(115,133,99,.07)':'rgba(255,255,241,.35)';x.save();x.translate(a,b);x.rotate(t);x.scale(l,l);x.beginPath();x.moveTo(0,0);x.quadraticCurveTo(60,-70,170,-50);x.stroke();x.restore();}x.filter='none';
    for(let i=0;i<800*K;i++){const a=r()*S,b=r()*S;x.strokeStyle='rgba(105,120,92,.07)';x.lineWidth=.4;x.beginPath();x.moveTo(a,b);x.lineTo(a+5,b+2);x.stroke();}
  }else if(kind==='sakura'){
    for(let i=0;i<13000;i++){const a=r()*S,b=r()*S;x.fillStyle=i%5?'rgba(255,250,241,.56)':'rgba(151,116,111,.09)';x.fillRect(a,b,.5+r()*1.3,.4+r()*.8);}
    for(let i=0;i<100;i++){const a=r()*S,b=r()*S;x.strokeStyle='rgba(255,251,242,.48)';x.lineWidth=.5;x.beginPath();x.moveTo(a,b);x.lineTo(a+10+r()*18,b+1+r()*3);x.stroke();}
  }
  };
  for(const dx of [-S,0,S]) for(const dy of [-S,0,S]){ r=rng(915+kind.length); x.save(); x.translate(dx,dy); paint(); x.restore(); }
  return c.toDataURL();
}

  function apply(view){
    currentView=views.includes(view)?view:'revisions';const choice=selection(currentView),root=document.documentElement;
    if(!(choice.background in textures))textures[choice.background]=texture(choice.background);
    root.style.setProperty('--background-texture',textures[choice.background]?'url('+textures[choice.background]+')':'none');
    root.style.setProperty('--background-size',tileSize(choice.background));root.dataset.background=choice.background;return choice;
  }
  // review page: show one background by name
  function background(kind){ if(!(kind in textures))textures[kind]=texture(kind); const root=document.documentElement; root.style.setProperty('--background-texture',textures[kind]?'url('+textures[kind]+')':'none'); root.style.setProperty('--background-size',tileSize(kind)); root.dataset.background=kind; }
  const tileSize=kind=>kind==='matcha'||kind==='shikkui'?'1024px 1024px':'512px 512px';
  function swing(element,strength=1){
    if(!element.animate||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
    element.getAnimations().forEach(a=>a.cancel());const paper=element.classList.contains('note');
    const base=parseFloat(element.style.getPropertyValue(paper?'--rot':'--plate-angle'))||0,amplitude=(paper?(element.dataset.tapes==='2'?.15:.55):.32)*strength;
    element.animate([base,base+amplitude,base-amplitude*.42,base+amplitude*.14,base].map((a,i)=>({transform:'rotate('+a+'deg)',offset:[0,.27,.55,.79,1][i]})),{duration:2400,easing:'ease-in-out'});
  }
  function wood(button,seed){
    if(!woodURL){const c=document.createElement('canvas');c.width=c.height=256;const x=c.getContext('2d'),r=random(204);
      for(let i=0;i<150;i++){const a=r()*256;x.strokeStyle='rgba(84,52,22,'+(.015+r()*.09)+')';x.lineWidth=.3+r()*.8;x.beginPath();x.moveTo(a,0);x.bezierCurveTo(a-8,90,a+8,180,a+(r()-.5)*8,256);x.stroke();}woodURL=c.toDataURL();}
    button.classList.add('wood-plaque');button.style.setProperty('--wood-grain','url('+woodURL+')');button.style.setProperty('--plate-angle',((random(seed)()-.5)*1.2).toFixed(2)+'deg');
    button.addEventListener('pointerenter',()=>swing(button,.45));button.addEventListener('pointerdown',()=>swing(button));
  }
  function paper(button,word,index){
    const spec=paperSpec(word,index);button.querySelectorAll('.paper-tape,.paper-curl').forEach(el=>el.remove());
    for(const tape of spec.tapes){const el=document.createElement('span');el.className='paper-tape';el.setAttribute('aria-hidden','true');Object.assign(el.style,{left:tape.left+'%',top:tape.top+'px',width:tape.width+'px',height:tape.height+'px',transform:'rotate('+tape.angle+'deg)'});button.appendChild(el);}
    button.dataset.tapes=String(spec.tapes.length);button.dataset.fold=spec.fold;button.style.transformOrigin=spec.pivot;button.style.setProperty('--rot',spec.angle.toFixed(2)+'deg');
    const s=spec.size+'px',canvas=button.querySelector('canvas'),clips={none:'none',br:'polygon(0 0,100% 0,100% calc(100% - '+s+'),calc(100% - '+s+') 100%,0 100%)',bl:'polygon(0 0,100% 0,100% 100%,'+s+' 100%,0 calc(100% - '+s+'))',tr:'polygon(0 0,calc(100% - '+s+') 0,100% '+s+',100% 100%,0 100%)'};
    canvas.style.clipPath=clips[spec.fold];
    if(spec.fold!=='none'){const el=document.createElement('span');el.className='paper-curl';el.setAttribute('aria-hidden','true');Object.assign(el.style,{width:s,height:s,left:spec.fold==='bl'?'0':'auto',right:spec.fold==='bl'?'auto':'0',top:spec.fold==='tr'?'0':'auto',bottom:spec.fold==='tr'?'auto':'0',transform:spec.fold==='bl'?'scaleX(-1)':spec.fold==='tr'?'scaleY(-1)':'none'});button.appendChild(el);}
    button.onpointerenter=()=>swing(button,.6);button.addEventListener('pointerdown',()=>swing(button));
  }
  // fresh sumi (see MoXi, Chu & Tai 2005, and Curtis 1997 for the behaviour), worked per stroke at half resolution:
  // the ink dries from the thin parts and edges towards the pools, in patches set by the paper's sizing; a faint sheen stays only
  // on the thick bead facing the window while it is wet; and a fibrous bleed (nijimi) creeps into the paper during the first second
  // and stays, wider on a big kanji and finer on a small one so the gaps between strokes stay open.
  const sm=(a,b,x)=>{x=Math.min(1,Math.max(0,(x-a)/(b-a)));return x*x*(3-2*x);};
  const mk=(w,h)=>{const c=document.createElement('canvas');c.width=w;c.height=h;return c;};
  let PAPER=null; // fibre and blotch fields on a 512 tile, made once
  function paperFields(){ if(PAPER) return PAPER; const T=512; let s=11; const rnd=()=>((s=(s*16807)%2147483647)/2147483647);
    const fc=mk(T,T),fx=fc.getContext('2d');fx.lineCap='round';
    for(let i=0;i<7000;i++){const px=rnd()*T,py=rnd()*T,an=rnd()*Math.PI,L=4+rnd()*16;fx.strokeStyle='rgba(0,0,0,'+(0.15+rnd()*0.5).toFixed(2)+')';fx.lineWidth=0.5+rnd()*0.9;fx.beginPath();fx.moveTo(px,py);fx.quadraticCurveTo(px+Math.cos(an)*L*.5+rnd()*3,py+Math.sin(an)*L*.5+rnd()*3,px+Math.cos(an)*L,py+Math.sin(an)*L);fx.stroke();}
    const bc=mk(T,T),bx=bc.getContext('2d');for(let i=0;i<2900;i++){bx.fillStyle='rgba(0,0,0,'+(rnd()*0.45).toFixed(2)+')';bx.beginPath();bx.arc(rnd()*T,rnd()*T,1+rnd()*6,0,7);bx.fill();}
    const b2=mk(T,T),b2x=b2.getContext('2d');b2x.filter='blur(1.5px)';b2x.drawImage(bc,0,0);
    const fd=fx.getImageData(0,0,T,T).data,bd=b2x.getImageData(0,0,T,T).data,FIB=new Float32Array(T*T),BLOT=new Float32Array(T*T);
    for(let i=0;i<T*T;i++){FIB[i]=fd[i*4+3]/255;BLOT[i]=Math.min(1,bd[i*4+3]/255*1.6);}
    return PAPER={T,FIB,BLOT}; }
  // src: a canvas holding one stroke (only its alpha is used). o.at: when it was laid (ms), o.pts: [[x,y,ms],...] the brush path in src pixels,
  // o.R: the stroke's width in src pixels, o.css: how big the kanji is on screen (px)
  function wetInk(src,o={}){
    const W=src.width,H=src.height,w=Math.ceil(W/2),h=Math.ceil(H/2),Rf=o.R||Math.min(W,H)*0.064,at=o.at??performance.now(),pts=o.pts||[],{T:PT,FIB,BLOT}=paperFields();
    const f=0.08+0.08*sm(140,420,o.css||300);
    const grab=blur=>{const c=mk(w,h),x=c.getContext('2d');if(blur)x.filter='blur('+blur.toFixed(1)+'px)';x.drawImage(src,0,0,w,h);return x.getImageData(0,0,w,h).data;};
    const dA=grab(0),dH=grab(Rf*0.18),dB=grab(Rf*f);
    let x0=w,y0=h,x1=-1,y1=-1;for(let y=0;y<h;y++)for(let x=0;x<w;x++)if(dA[(y*w+x)*4+3]>3){if(x<x0)x0=x;if(x>x1)x1=x;if(y<y0)y0=y;if(y>y1)y1=y;}
    if(x1<0)return null;const m=Math.ceil(Rf*0.5);x0=Math.max(0,x0-m);y0=Math.max(0,y0-m);x1=Math.min(w-1,x1+m);y1=Math.min(h-1,y1+m);
    const bw=x1-x0+1,bh=y1-y0+1,n=bw*bh,A=new Float32Array(n),HH=new Float32Array(n),TT=new Float32Array(n).fill(pts.length?pts[pts.length-1][2]:at),DRY=new Float32Array(n),G=new Float32Array(n),HL=new Float32Array(n);
    for(let y=0;y<bh;y++)for(let x=0;x<bw;x++){const i=y*bw+x,j=((y+y0)*w+x+x0)*4+3;A[i]=dA[j]/255;HH[i]=dH[j]/255;HL[i]=dB[j]/255;}
    // when the brush passed over each pixel: drying and bleeding start there
    const rr=Math.ceil(Rf*0.9);for(const [px,py,t] of pts){const cx=px/2-x0,cy=py/2-y0;for(let y=Math.max(0,Math.floor(cy-rr));y<=Math.min(bh-1,cy+rr);y++)for(let x=Math.max(0,Math.floor(cx-rr));x<=Math.min(bw-1,cx+rr);x++){if((x-cx)**2+(y-cy)**2>rr*rr)continue;const i=y*bw+x;if(TT[i]>t)TT[i]=t;}}
    const lx=-0.55,ly=-0.83;let tEnd=0;
    for(let y=0;y<bh;y++)for(let x=0;x<bw;x++){const i=y*bw+x,gx0=x+x0,gy0=y+y0,p=(gy0%PT)*PT+(gx0%PT),hh=HH[i];
      // thick, pooled ink stays wet the longest (ms); thin hairlines and dry streaks sink in almost at once
      DRY[i]=(300+3600*Math.pow(hh,1.8))*(0.75+0.5*BLOT[p]);if(A[i]>0.02)tEnd=Math.max(tEnd,TT[i]+DRY[i]);
      if(A[i]>0.02&&x>0&&y>0&&x<bw-1&&y<bh-1){const gx=HH[i+1]-HH[i-1],gy=HH[i+bw]-HH[i-bw],s2=(-gx*lx-gy*ly)*9,e=sm(0.40,0.56,gx0/w)*(1-sm(0.36,0.52,gy0/h));
        G[i]=(0.04*hh+sm(0.08,0.8,s2)*Math.pow(hh,1.6)*(0.55+0.6*BLOT[p]))*(0.45+1.1*e);}
      const out=Math.max(0,HL[i]-A[i]*0.9);HL[i]=out*1.35*(0.22+1.5*Math.pow(FIB[p],1.3))*(0.5+0.9*hh);}
    const wet=mk(bw,bh),halo=mk(bw,bh),iw=new ImageData(bw,bh),ih=new ImageData(bw,bh);let settled=false;
    // draws this stroke's wet look and its bleed as they are at `now`; false once it is dry and the bleed has settled
    function update(now){const D=iw.data,Hd=ih.data;D.fill(0);let live=false;
      for(let i=0;i<n;i++){const tr=TT[i];if(tr>now){live=true;continue;}const age=now-tr,q=i*4;
        const hv=HL[i];if(hv>0){Hd[q]=22;Hd[q+1]=18;Hd[q+2]=16;Hd[q+3]=Math.min(255,hv*sm(0,900,age)*0.5*255);if(age<900)live=true;}
        const a0=A[i];if(a0<0.02)continue;const wv=1-sm(DRY[i]-800,DRY[i],age);if(wv<=0)continue;live=true;
        const ga=Math.min(1,G[i]*wv*a0)*0.8,da=0.16*wv*a0,al=ga+da*(1-ga);if(al<=0.004)continue;
        // a darker wet body under a cool sheen, as one colour
        D[q]=Math.round(214*ga/al);D[q+1]=Math.round(224*ga/al);D[q+2]=Math.round(232*ga/al);D[q+3]=al*255;}
      wet.getContext('2d').putImageData(iw,0,0);halo.getContext('2d').putImageData(ih,0,0);if(!live)settled=true;return live;}
    return {x:x0*2,y:y0*2,w:bw*2,h:bh*2,wet,halo,update,get settled(){return settled;},end:tEnd};
  }
  // a pad's fresh ink: the wet look floats above the ink, the bleed sits under it and stays until the pad is cleared
  function attachInk(host,sources){
    const ink=sources[0],sheen=mk(1,1),bleed=mk(1,1);sheen.className='ink-sheen';bleed.className='ink-bleed';[sheen,bleed].forEach(c=>c.setAttribute('aria-hidden','true'));
    host.appendChild(sheen);host.insertBefore(bleed,ink);
    let frame=0,disposed=false,live=[],kept=[];const reduce=()=>matchMedia('(prefers-reduced-motion: reduce)').matches;
    const size=()=>{if(bleed.width!==ink.width||bleed.height!==ink.height){bleed.width=sheen.width=ink.width;bleed.height=sheen.height=ink.height;live=[];kept=[];}};
    const redrawKept=()=>{const b=bleed.getContext('2d');b.clearRect(0,0,bleed.width,bleed.height);kept.forEach(s=>b.drawImage(s.halo,s.x,s.y,s.w,s.h));};
    const loop=now=>{if(disposed||!host.isConnected){frame=0;return;}if(document.hidden){frame=requestAnimationFrame(loop);return;}
      const sx=sheen.getContext('2d');sx.clearRect(0,0,sheen.width,sheen.height);redrawKept();const b=bleed.getContext('2d');
      live=live.filter(s=>{const on=s.update(now);b.drawImage(s.halo,s.x,s.y,s.w,s.h);sx.drawImage(s.wet,s.x,s.y,s.w,s.h);if(!on)kept.push(s);return on;});
      frame=live.length?requestAnimationFrame(loop):0;};
    function add(src,pts){if(disposed||!src||!src.width)return;size();
      const s=wetInk(src,{pts,R:o_R(src),css:host.clientWidth});if(!s)return;
      if(reduce()){s.update(Infinity);kept.push(s);redrawKept();return;}
      live.push(s);if(!frame)frame=requestAnimationFrame(loop);}
    const o_R=src=>Math.min(src.width,src.height)*0.064;
    function refresh(){const src=sources[0];if(src&&src.width)add(src);}
    function undo(){if(live.length)live.pop();else kept.pop();redrawKept();sheen.getContext('2d').clearRect(0,0,sheen.width,sheen.height);}
    function clear(){cancelAnimationFrame(frame);frame=0;live=[];kept=[];[sheen,bleed].forEach(c=>c.getContext('2d').clearRect(0,0,c.width,c.height));}
    return {add,refresh,undo,clear,destroy(){disposed=true;clear();sheen.remove();bleed.remove();}};
  }
  return {views,backgrounds,shadows,dayNumber,selection,paperSpec,apply,background,wood,paper,swing,wetInk,attachInk,get view(){return currentView;}};
})();
if(typeof module!=='undefined')module.exports=Ambience;
