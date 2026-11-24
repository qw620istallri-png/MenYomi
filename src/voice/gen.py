import sys, json, re, subprocess, os, dataclasses
sys.path.insert(0,'/tmp/claude-0/vvwork')
from vv import *
SID=int(sys.argv[3]) if len(sys.argv)>3 else 14
data=json.load(open(sys.argv[1],encoding='utf-8')); OUT=sys.argv[2]; os.makedirs(OUT+'/wav',exist_ok=True)
items={}
for w in data['words']: items.setdefault(w[0],w[1])
for n in data['names']: items.setdefault(n[0],n[1])
for k,v in data['namepat'].items(): items.setdefault(k,v)
syn=make(['1.vvm'])
VO={}
for row,v in zip(['アカサタナハマヤラワガザダバパァャ','イキシチニヒミリギジヂビピィ','ウクスツヌフムユルグズヅブプゥュヴ','エケセテネヘメレゲゼデベペェ','オコソトノホモヨロヲゴゾドボポォョ'],'アイウエオ'):
    for c in row: VO[c]=v
SMALL=set('ァィゥェォャュョヮ')
def norm(s):
    s=kata(s); s=re.sub(r'[^ァ-ヴー]','',s); o=''
    for c in s:
        if c=='ー' and o: c=VO.get(o[-1],'ー')
        o+=c
    o=o.replace('ヲ','オ').replace('ヂ','ジ').replace('ヅ','ズ'); r=''
    for c in o:
        if r and ((c=='イ' and VO.get(r[-1])=='エ') or (c=='ウ' and VO.get(r[-1])=='オ')): c=VO[r[-1]]
        r+=c
    return r
def split(s):
    m=[]
    for c in s:
        if c in SMALL and m: m[-1]+=c
        else: m.append(c)
    return m
fixed=[];fallback=[]
for i,(t,rd) in enumerate(items.items()):
    try: aq=syn.create_audio_query(t,SID)
    except Exception: aq=syn.create_audio_query(kata(rd),SID); fallback.append((t,rd,'(kana)'))
    exp=norm(rd)
    if norm(moras(aq.accent_phrases))!=exp:
        em=split(exp); counts=[len(ap.moras) for ap in aq.accent_phrases]
        if sum(counts)==len(em):
            parts=[];k=0
            for ap,c in zip(aq.accent_phrases,counts):
                ch=em[k:k+c]; k+=c; a=max(1,min(ap.accent,c))
                parts.append(''.join(ch[:a])+"'"+''.join(ch[a:]))
                parts.append('、' if ap.pause_mora else '/')
            kana=''.join(parts[:-1])
            aq.accent_phrases=syn.create_accent_phrases_from_kana(kana,SID); fixed.append((t,rd,kana))
        else:
            aq.accent_phrases=syn.create_accent_phrases(kata(rd),SID); fallback.append((t,rd,moras(aq.accent_phrases)))
    aq.speed_scale=0.95; aq.pre_phoneme_length=0.04; aq.post_phoneme_length=0.12
    open(f'{OUT}/wav/{i}.wav','wb').write(syn.synthesis(aq,SID))
json.dump(list(items.keys()),open(OUT+'/keys.json','w',encoding='utf-8'),ensure_ascii=False)
print(len(items),'clips'); print('fixed',len(fixed)); [print(' ',*f) for f in fixed]; print('fallback',len(fallback)); [print(' ',*f) for f in fallback]
