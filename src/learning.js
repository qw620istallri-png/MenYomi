// Personal word list and daily practice reuse the existing cards.
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
