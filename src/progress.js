// Pure progress operations, also exercised by node --test. Existing v2 saves remain readable.
const Progress = (() => {
  const object = v => v !== null && typeof v === 'object' && !Array.isArray(v);
  const finite = v => typeof v === 'number' && Number.isFinite(v) && v >= 0 && v <= Number.MAX_SAFE_INTEGER;
  const dict = () => Object.create(null);
  const localDay=t=>{const d=new Date(t-4*36e5);return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');};
  const fresh = () => ({version:2,cards:{},day:'',newToday:0,newBase:0,newPer:10,todayIds:[],extraNew:0,queue:[],removed:{},favorites:{},activity:{},activityRemoved:{},legacyDays:{},lessonSeen:{},lessonPassed:{},days:{},rdays:[],stamps:{},firsts:0,nrev:0});
  function validate(input, ids, words) {
    if(!object(input)||!object(input.cards)||Object.keys(input.cards).length>10000) return null;
    const out=fresh(), cardSet=new Set(ids), wordSet=new Set(words);
    for(const [id,c] of Object.entries(input.cards)) {
      if(!cardSet.has(id)||!object(c)||!['due','ivl','ease','reps','lapses'].every(k=>finite(c[k]))||c.ease<1||c.ease>100||!Number.isInteger(c.reps)||!Number.isInteger(c.lapses)) return null;
      if(['at','introduced'].some(k=>c[k]!==undefined&&!finite(c[k]))) return null;
      out.cards[id]={due:c.due,ivl:c.ivl,ease:c.ease,reps:c.reps,lapses:c.lapses,...(c.at!==undefined?{at:c.at}:{}),...(c.introduced!==undefined?{introduced:c.introduced}:{})};
    }
    if(input.day!==undefined&&(typeof input.day!=='string'||(input.day!==''&&!/^\d{4}-\d{2}-\d{2}$/.test(input.day)))) return null;
    out.day=input.day||'';
    for(const key of ['newToday','newBase','extraNew','tp']) { if(input[key]!==undefined&&!finite(input[key])) return null; if(input[key]!==undefined) out[key]=input[key]; }
    if(['newToday','newBase','extraNew'].some(key=>!Number.isInteger(out[key])||out[key]>10000)) return null;
    if(input.newPer!==undefined&&![5,10,20,30].includes(input.newPer)) return null;
    out.newPer=input.newPer||10;
    for(const key of ['todayIds','queue']) {
      if(input[key]!==undefined&&(!Array.isArray(input[key])||input[key].length>10000||input[key].some(id=>!cardSet.has(id)))) return null;
      out[key]=[...new Set(input[key]||[])];
    }
    for(const key of ['removed','lessonSeen','lessonPassed']) {
      if(input[key]!==undefined&&!object(input[key])) return null;
      out[key]=dict();
      for(const [id,at] of Object.entries(input[key]||{})) { if(!(key==='removed'?cardSet:wordSet).has(id)||!finite(at)) return null; out[key][id]=at; }
    }
    if(input.favorites!==undefined&&!object(input.favorites)) return null;
    out.favorites=dict();
    for(const [w,v] of Object.entries(input.favorites||{})) { if(!wordSet.has(w)||!object(v)||typeof v.on!=='boolean'||!finite(v.at)) return null; out.favorites[w]={on:v.on,at:v.at}; }
    if(input.days!==undefined&&!object(input.days)) return null;
    out.days=dict();
    for(const [day,v] of Object.entries(input.days||{})) { if(!/^\d{4}-\d{2}-\d{2}$/.test(day)||!Array.isArray(v)||v.length!==2||!v.every(finite)||v[0]>v[1]) return null; out.days[day]=v.slice(); }
    if(input.activity!==undefined&&!object(input.activity)) return null;
    out.activity=dict();
    for(const [day,entries] of Object.entries(input.activity||{})) {
      if(!/^\d{4}-\d{2}-\d{2}$/.test(day)||!object(entries)) return null;
      out.activity[day]=dict();
      for(const [id,v] of Object.entries(entries)) { if(!cardSet.has(id)||!object(v)||typeof v.ok!=='boolean'||!finite(v.at)) return null; out.activity[day][id]={ok:v.ok,at:v.at}; }
    }
    for(const field of ['legacyDays','activityRemoved']) {
      if(input[field]!==undefined&&!object(input[field])) return null;
      out[field]=dict();
      for(const [d,entries] of Object.entries(input[field]||{})) {
        if(!/^\d{4}-\d{2}-\d{2}$/.test(d)) return null;
        if(field==='legacyDays'){if(!Array.isArray(entries)||entries.length!==2||!entries.every(finite)||entries[0]>entries[1]) return null;out[field][d]=entries.slice();}
        else {if(!object(entries)) return null;out[field][d]=dict();for(const [id,at] of Object.entries(entries)){if(!cardSet.has(id)||!finite(at))return null;out[field][d][id]=at;}}
      }
    }
    // every day with a review, kept for good (days/activity only keep 90): the stamp book counts them
    if(input.rdays!==undefined&&(!Array.isArray(input.rdays)||input.rdays.length>40000||input.rdays.some(d=>typeof d!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(d)))) return null;
    out.rdays=[...new Set([...(input.rdays||[]),...Object.keys(out.days).filter(d=>out.days[d][1]>0)])].sort();
    if(input.stamps!==undefined&&!object(input.stamps)) return null;
    out.stamps=dict();
    for(const [k,at] of Object.entries(input.stamps||{})) { if(!/^[a-z_]{1,24}$/.test(k)||!finite(at)) return null; out.stamps[k]=at; }
    for(const key of ['firsts','nrev']) { if(input[key]!==undefined&&(!finite(input[key])||!Number.isInteger(input[key]))) return null; out[key]=input[key]||0; }
    if(input.nrev===undefined) out.nrev=Object.values(out.days).reduce((a,v)=>a+v[1],0);
    if(input.legacyDays===undefined) for(const [d,counts] of Object.entries(out.days)) {const es=Object.values(out.activity[d]||{});out.legacyDays[d]=[Math.max(0,counts[0]-es.filter(e=>e.ok).length),Math.max(0,counts[1]-es.length)];}
    if(input.newBase===undefined) out.newBase=Math.max(0,out.newToday-Object.values(out.cards).filter(c=>c.introduced&&localDay(c.introduced)===out.day).length);
    for(const [id,at] of Object.entries(out.removed)) if(out.cards[id]&&(out.cards[id].at||0)<=at) delete out.cards[id];
    return out;
  }
  const latest=(a={},b={})=>{
    const out={...a}; for(const [k,v] of Object.entries(b)) if(!out[k]||(typeof v==='number'?v:v.at)>(typeof out[k]==='number'?out[k]:out[k].at)) out[k]=v; return out;
  };
  function merge(a,b,dayKey) {
    if(!b) return structuredClone(a);
    const out={...a,cards:{...a.cards},removed:latest(a.removed,b.removed)};
    const stamp=c=>c.at??(c.due-(c.ivl||0)*864e5);
    for(const [id,c] of Object.entries(b.cards)) if(!out.cards[id]||stamp(c)>stamp(out.cards[id])) out.cards[id]={...c};
    for(const [id,at] of Object.entries(out.removed)) if(out.cards[id]&&(out.cards[id].at||0)<=at) delete out.cards[id];
    for(const key of ['favorites','lessonSeen','lessonPassed']) out[key]=latest(a[key],b[key]);
    out.queue=[...new Set([...(a.queue||[]),...(b.queue||[])])].filter(id=>!out.cards[id]);
    out.activity=structuredClone(a.activity||{});
    out.activityRemoved=structuredClone(a.activityRemoved||{});
    for(const [d,entries] of Object.entries(b.activityRemoved||{})) out.activityRemoved[d]=latest(out.activityRemoved[d],entries);
    for(const [d,entries] of Object.entries(out.activity)) for(const [id,e] of Object.entries(entries)) if(e.at<=(out.activityRemoved[d]?.[id]||0)) delete entries[id];
    for(const [d,v] of Object.entries(b.activity||{})) {
      const entries=out.activity[d]||{};
      // First encounter per card per day; the earliest result survives a concurrent merge.
      for(const [id,e] of Object.entries(v)) if(e.at>(out.activityRemoved[d]?.[id]||0)&&(!entries[id]||e.at<entries[id].at)) entries[id]={...e};
      out.activity[d]=entries;
    }
    for(const [d,entries] of Object.entries(out.activityRemoved)) for(const [id,at] of Object.entries(entries)) if(out.activity[d]?.[id]&&out.activity[d][id].at<=at) delete out.activity[d][id];
    out.legacyDays=structuredClone(a.legacyDays||a.days||{});
    for(const [d,v] of Object.entries(b.legacyDays||b.days||{})) { const m=out.legacyDays[d];out.legacyDays[d]=m?[Math.max(m[0],v[0]),Math.max(m[1],v[1])]:v.slice(); }
    out.days=structuredClone(out.legacyDays);
    if(b.day>a.day) { out.day=b.day; out.todayIds=(b.todayIds||[]).slice(); out.extraNew=b.extraNew||0; out.newBase=b.newBase??b.newToday??0; }
    else if(a.day===b.day) { out.todayIds=[...new Set([...(a.todayIds||[]),...(b.todayIds||[])])]; out.extraNew=Math.max(a.extraNew||0,b.extraNew||0); out.newBase=Math.max(a.newBase??a.newToday??0,b.newBase??b.newToday??0); }
    out.todayIds=(out.todayIds||[]).filter(id=>!(out.activityRemoved[out.day]?.[id]&&!out.activity[out.day]?.[id]));
    const introduced=Object.values(out.cards).filter(c=>c.introduced&&dayKey(c.introduced)===out.day).length;
    out.newToday=(out.newBase||0)+introduced;
    for(const [d,v] of Object.entries(out.activity)) { const es=Object.values(v), m=out.legacyDays[d]||[0,0]; out.days[d]=[m[0]+es.filter(e=>e.ok).length,m[1]+es.length]; }
    for(const d of Object.keys(out.days).sort().slice(0,-90)) for(const key of ['days','legacyDays','activity','activityRemoved']) delete out[key][d];
    out.rdays=[...new Set([...(a.rdays||[]),...(b.rdays||[]),...Object.keys(out.days).filter(d=>out.days[d][1]>0)])].sort();
    out.stamps={...(b.stamps||{})}; for(const [k,at] of Object.entries(a.stamps||{})) if(!out.stamps[k]||at<out.stamps[k]) out.stamps[k]=at;
    out.firsts=Math.max(a.firsts||0,b.firsts||0); out.nrev=Math.max(a.nrev||0,b.nrev||0);
    if((b.tp||0)>(a.tp||0)) { out.newPer=b.newPer; out.tp=b.tp; }
    return out;
  }
  async function commit(F,db,reference,local,read,dayKey) {
    return F.runTransaction(db,async tx=>{
      const snap=await tx.get(reference); let remote=null;
      if(snap.exists()){ remote=read(snap.data().s); if(!remote) throw new Error('invalid-remote-progress'); }
      const result=merge(local,remote,dayKey);
      // Keep the deployed envelope compatible with existing Firestore rules.
      tx.set(reference,{s:JSON.stringify(result),t:Date.now(),v:1});
      return result;
    });
  }
  return {fresh,validate,merge,commit};
})();
if(typeof module!=='undefined') module.exports=Progress;
