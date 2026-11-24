const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:600,height:400},deviceScaleFactor:1});
 await p.goto('file://'+process.cwd()+'/test.html#vocab'); await p.waitForTimeout(2500);
 const out=await p.evaluate(async()=>{ const k=7; const c=document.createElement('canvas'); document.body.appendChild(c);
   textCanvas(c,'麺',{seed:12345,writer:makeWriter(rng(777),'kaisho','brush',{weight:0.9}),size:58*k,surface:'red',color:'#fff6e6',pad:0.14,minW:76*k,minH:76*k,
    after:(lx,W,H)=>{ lx.save(); lx.lineWidth=3.2*k*DPR; lx.strokeRect(5*k*DPR,5*k*DPR,W-10*k*DPR,H-10*k*DPR); lx.restore(); }});
   await new Promise(r=>setTimeout(r,500)); const r={dim:[c.width,c.height]}; const s=Math.min(c.width,c.height); for(const n of [512,192,180,32]){ const o=document.createElement('canvas'); o.width=o.height=n; const x=o.getContext('2d'); x.imageSmoothingQuality='high'; x.drawImage(c,(c.width-s)/2,(c.height-s)/2,s,s,0,0,n,n); r[n]=o.toDataURL('image/png'); } return r; });
 console.log(out.dim); for(const n of [512,192,180,32]) require('fs').writeFileSync(`site/icon-${n}.png`,Buffer.from(out[n].split(',')[1],'base64'));
 await b.close(); })();
