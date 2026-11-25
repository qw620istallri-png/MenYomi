// Small learning paths and a personal word list reuse the existing cards and menu renderer.
const LESSON_WORDS=['焼鳥','唐揚げ','枝豆','冷奴','焼魚','味噌汁','生ビール','日本酒'];
let lessonRun=false, lessonBack=null;
const lessonCount=key=>LESSON_WORDS.filter(w=>S[key]&&S[key][w]).length;
const favorite=w=>!!(S.favorites[w]&&S.favorites[w].on);
function favoriteBtn(w){ return WMAP[w]?`<button class="btn ghost" type="button" data-favorite="${esc(w)}" aria-pressed="${favorite(w)}">${favorite(w)?tr('En favoris','Saved'):tr('Garder en favoris','Save word')}</button>`:''; }
document.addEventListener('click',e=>{
  const b=e.target.closest('[data-favorite]'); if(!b) return;
  const w=b.dataset.favorite; if(!WMAP[w]) return;
  e.preventDefault(); e.stopPropagation(); S.favorites[w]={on:!favorite(w),at:Date.now()}; store.set(SKEY,S);
  document.querySelectorAll('[data-favorite]').forEach(el=>{ if(el.dataset.favorite===w){ el.setAttribute('aria-pressed',String(favorite(w))); el.textContent=favorite(w)?tr('En favoris','Saved'):tr('Garder en favoris','Save word'); } });
},true);
function reviewPersonal(){
  const ids=WORDS.filter(w=>favorite(w[0])).map(w=>firstId(w[0])); if(!ids.length) return;
  cancelAuto(); REPLAY_ID=null; LAST_GRADE=null; SESSION={q:ids}; TESTRES=null; dlg.close(); location.hash='revisions'; showCard();
}
function reviewDifficult(){
  const ids=Object.entries(S.activity[today()]||{}).filter(([,e])=>!e.ok).map(([id])=>id);
  if(!ids.length) return; cancelAuto(); REPLAY_ID=null; LAST_GRADE=null; SESSION={q:ids}; TESTRES=null; location.hash='revisions'; showCard();
}
function dailyReport(){
  const es=Object.entries(S.activity[today()]||{}); if(!es.length) return '';
  const wrong=es.filter(([,e])=>!e.ok), words=[...new Set(wrong.map(([id])=>id.slice(2)))].filter(w=>WMAP[w]);
  return `<section class="session-report"><h3>${tr('Ton bilan du jour','Your day in review')}</h3><p>${es.length} ${tr('cartes travaillées','cards practised')} · ${es.filter(([,e])=>e.ok).length} ${tr('réussies au premier essai','right on the first try')}.</p>${wrong.length?`<p>${tr('À retrouver sans hésiter','Words to revisit')} : ${words.length?words.map(w=>`<span lang="ja">${esc(w)}</span>`).join(' · '):tr('les kanji écrits aujourd’hui','today’s handwritten kanji')}.</p><button class="btn" id="review-difficult">${tr('Retravailler mes hésitations','Practise my difficult cards')} (${wrong.length})</button>`:`<p>${tr('Tout juste au premier essai. Essaie maintenant un menu !','All correct on the first try. Try a menu now!')}</p>`}</section>`;
}
function renderLearningHome(){
  const host=document.getElementById('learning-home'); if(!host) return;
  const complete=lessonCount('lessonPassed')===LESSON_WORDS.length;
  host.innerHTML=`<div><b>${tr('Mon premier izakaya','My first izakaya')}</b><span>${complete?tr('8 mots retrouvés sur le menu','8 words found on the menu'):tr('Découvre 8 mots, puis retrouve-les sur un menu.','Learn 8 words, then find them on a menu.')}</span></div><button class="btn" type="button" id="lesson-open">${complete?tr('Revoir le parcours','Revisit the path'):lessonCount('lessonSeen')?tr('Continuer','Continue'):tr('Découvrir','Start')}</button>`;
  host.querySelector('#lesson-open').onclick=()=>openLesson();
}
function openLesson(index){
  cancelAuto(); lessonRun=false;
  const first=LESSON_WORDS.findIndex(w=>!S.lessonSeen[w]);
  const n=index===undefined?(first<0?LESSON_WORDS.length:first):index;
  document.getElementById('dlgslot').textContent=tr('Mon premier izakaya','My first izakaya');
  const body=document.getElementById('dlgbody');
  if(n>=LESSON_WORDS.length){
    const passed=lessonCount('lessonPassed');
    body.innerHTML=`<div class="lesson"><h2>${passed===8?tr('Tu sais les retrouver !','You can find them!'):tr('À toi de lire le menu','Your turn to read the menu')}</h2><p>${tr('Tu as découvert les 8 mots. Le défi ne te demandera que ceux-ci. Les erreurs restent des occasions de réessayer.','You have met all 8 words. The challenge only asks for these words. You can retry any mistakes.')}</p><div class="dwords">${LESSON_WORDS.map(w=>`<span lang="ja">${esc(w)}${S.lessonPassed[w]?' ✓':''}</span>`).join('')}</div><p>${passed}/8 ${tr('retrouvés','found')}</p><div class="row"><button class="btn k" id="lesson-menu">${tr('Les retrouver sur un menu','Find them on a menu')}</button><button class="btn" id="lesson-again">${tr('Revoir les mots','Revisit the words')}</button></div></div>`;
    body.querySelector('#lesson-menu').onclick=startLessonMenu; body.querySelector('#lesson-again').onclick=()=>openLesson(0);
  } else {
    const w=WMAP[LESSON_WORDS[n]];
    body.innerHTML=`<div class="lesson"><p class="mono">${n+1}/8 · ${tr('Découvrir les mots','Meet the words')}</p><h2>${esc(w[2])}</h2><canvas id="lesson-canvas" role="img" aria-label="${esc(w[0])}"></canvas><div class="answer"><div class="w" lang="ja">${esc(w[0])}</div><div class="rd" lang="ja">${esc(w[1])}${sayBtn(w[0],w[1])}</div><div class="ro">${esc(toRomaji(w[1]))}</div></div>${xp(w[0])}${wordChips(w[0])}<div class="row">${favoriteBtn(w[0])}${reviewBtn(firstId(w[0]))}</div><div class="lesson-actions"><button class="btn" id="lesson-prev" ${n?'':'disabled'}>${tr('Précédent','Previous')}</button><button class="btn k" id="lesson-next">${n===7?tr('Prêt pour le menu','Ready for the menu'):tr('Mot suivant','Next word')} →</button></div></div>`;
    body.querySelector('#lesson-prev').onclick=()=>openLesson(n-1);
    body.querySelector('#lesson-next').onclick=()=>{ S.lessonSeen[w[0]]=Date.now(); store.set(SKEY,S); renderLearningHome(); openLesson(n+1); };
  }
  if(!dlg.open) dlg.showModal();
  if(n<8) textCanvas(body.querySelector('canvas'),LESSON_WORDS[n],{seed:800+n,writer:makeWriter(rng(800+n),'kaisho','brush'),size:72,surface:'kinari',pad:.35});
  body.scrollTop=0;
}
function startLessonMenu(){
  lessonRun=true; lessonBack={type:document.getElementById('mtype').value,region:document.getElementById('mreg').value,mode:mmode,pool:qpool};
  mmode='meaning'; qpool='all'; dlg.close();
  if(!menuDone){ fillSelects(); menuDone=true; }
  document.getElementById('mtype').value='izakaya'; document.getElementById('mreg').value='';
  location.hash='menu'; if(!menuDone){ fillSelects(); menuDone=true; } genMenu();
}
function stopLessonMenu(){
  lessonRun=false; if(lessonBack){ document.getElementById('mtype').value=lessonBack.type; document.getElementById('mreg').value=lessonBack.region; mmode=lessonBack.mode; qpool=lessonBack.pool; lessonBack=null; }
  renderLearningHome();
}
function lessonQuest(){
  const q=document.getElementById('mquest'), done=lessonCount('lessonPassed');
  if(done===8){ q.innerHTML=`<div class="quest"><b>${tr('8 sur 8 : menu déchiffré !','8 out of 8: menu decoded!')}</b><button class="btn" id="lesson-finish">${tr('Terminer','Finish')}</button></div>`; q.querySelector('button').onclick=()=>{ stopLessonMenu(); newQuest(); openLesson(8); }; return; }
  const word=LESSON_WORDS.find(w=>!S.lessonPassed[w]); target=MENU.flat.findIndex(it=>it.w===word);
  const w=WMAP[word]; qmiss=false;
  q.innerHTML=`<div class="quest"><b>${esc(w[2])}</b><span class="mono">${done}/8</span><button class="btn" id="lesson-hint">${tr('Revoir ce mot','Revisit this word')}</button><button class="btn" id="lesson-exit">${tr('Quitter le parcours','Leave the path')}</button></div>`;
  q.querySelector('#lesson-hint').onclick=()=>{ toast(`${w[0]} · ${w[1]} · ${w[2]}`); };
  q.querySelector('#lesson-exit').onclick=()=>{ stopLessonMenu(); newQuest(); };
}
