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
  const S=512,bases={washi:[241,234,219],mineral:[222,219,209],shikkui:[240,238,229],kinari:[234,226,209],matcha:[225,230,218],sakura:[238,226,222]},base=bases[kind];
  const fine=valueNoise(S,70,151),broad=valueNoise(S,5,97),r=rng(915+kind.length);
  const c=noiseTile(S,43,(q,X,Y)=>{
    const granular=kind==='mineral'?15:kind==='washi'?8:kind==='sakura'?5:3;
    const n=(q()-.5)*granular+(fine(X,Y)-.5)*(kind==='mineral'?14:3)+(broad(X,Y)-.5)*(kind==='shikkui'?9:kind==='matcha'?15:4);
    return [base[0]+n,base[1]+n,base[2]+n];
  });
  const x=c.getContext('2d');
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
    for(let i=0;i<34;i++){const a=r()*S,b=r()*S;x.strokeStyle=i%2?'rgba(173,163,139,.10)':'rgba(255,255,252,.53)';x.beginPath();x.moveTo(a-90,b+20);x.quadraticCurveTo(a,b-22,a+100,b);x.stroke();}x.filter='none';
  }else if(kind==='matcha'){
    x.filter='blur(8px)';x.lineWidth=22;
    for(let i=0;i<32;i++){const a=r()*S,b=r()*S;x.strokeStyle=i%2?'rgba(115,133,99,.07)':'rgba(255,255,241,.35)';x.beginPath();x.moveTo(a,b);x.quadraticCurveTo(a+60,b-70,a+170,b-50);x.stroke();}x.filter='none';
    for(let i=0;i<800;i++){const a=r()*S,b=r()*S;x.strokeStyle='rgba(105,120,92,.07)';x.lineWidth=.4;x.beginPath();x.moveTo(a,b);x.lineTo(a+5,b+2);x.stroke();}
  }else if(kind==='sakura'){
    for(let i=0;i<13000;i++){const a=r()*S,b=r()*S;x.fillStyle=i%5?'rgba(255,250,241,.56)':'rgba(151,116,111,.09)';x.fillRect(a,b,.5+r()*1.3,.4+r()*.8);}
    for(let i=0;i<100;i++){const a=r()*S,b=r()*S;x.strokeStyle='rgba(255,251,242,.48)';x.lineWidth=.5;x.beginPath();x.moveTo(a,b);x.lineTo(a+10+r()*18,b+1+r()*3);x.stroke();}
  }
  return c.toDataURL();
}

  function apply(view){
    currentView=views.includes(view)?view:'revisions';const choice=selection(currentView),root=document.documentElement;
    if(!(choice.background in textures))textures[choice.background]=texture(choice.background);
    root.style.setProperty('--background-texture',textures[choice.background]?'url('+textures[choice.background]+')':'none');
    root.dataset.background=choice.background;return choice;
  }
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
  function paintInk(overlay,mask,wet,time=1700){
    const x=overlay.getContext('2d'),W=overlay.width,H=overlay.height;x.clearRect(0,0,W,H);if(wet<=0)return;
    x.globalCompositeOperation='source-over';x.drawImage(mask,0,0,W,H);x.globalCompositeOperation='source-in';
    const drift=Math.sin(time*.00045)*W*.025,g=x.createLinearGradient(-W*.1+drift,0,W*.95+drift,H*.6);
    for(const [stop,alpha] of [[0,.03],[.19,.03],[.215,.52],[.235,.16],[.26,.025],[.46,.025],[.48,.65],[.50,.18],[.53,.025],[.72,.025],[.745,.44],[.765,.08],[1,.025]])g.addColorStop(stop,'rgba(234,242,239,'+(alpha*wet)+')');
    x.fillStyle=g;x.fillRect(0,0,W,H);x.globalCompositeOperation='source-over';
  }
  function attachInk(host,sources){
    const overlay=document.createElement('canvas'),mask=document.createElement('canvas');overlay.className='ink-sheen';overlay.setAttribute('aria-hidden','true');host.appendChild(overlay);
    let frame=0,start=0,disposed=false;
    function refresh(){
      if(disposed)return;const size=sources[0].width;if(!size)return;overlay.width=mask.width=size;overlay.height=mask.height=sources[0].height;
      const x=mask.getContext('2d');x.clearRect(0,0,mask.width,mask.height);sources.forEach(c=>x.drawImage(c,0,0,mask.width,mask.height));
      start=performance.now();paintInk(overlay,mask,1);cancelAnimationFrame(frame);
      if(matchMedia('(prefers-reduced-motion: reduce)').matches){paintInk(overlay,mask,0);return;}
      const dry=now=>{if(disposed||!host.isConnected)return;if(document.hidden||(host.getClientRects&&!host.getClientRects().length)){clear();return;}const wet=Math.max(0,1-(now-start)/6500);paintInk(overlay,mask,wet,now-start);if(wet>0)frame=requestAnimationFrame(dry);};frame=requestAnimationFrame(dry);
    }
    function clear(){cancelAnimationFrame(frame);overlay.getContext('2d').clearRect(0,0,overlay.width,overlay.height);}
    return {refresh,clear,destroy(){disposed=true;clear();overlay.remove();}};
  }
  return {views,backgrounds,shadows,dayNumber,selection,paperSpec,apply,wood,paper,swing,paintInk,attachInk,get view(){return currentView;}};
})();
if(typeof module!=='undefined')module.exports=Ambience;
