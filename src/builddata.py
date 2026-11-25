import xml.etree.ElementTree as ET, json, os, re, sqlite3, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from menudata import W, T, R, NAMES, NAMEPAT_R, MENTIONS
HERE=os.path.dirname(os.path.abspath(__file__))
KV=os.path.join(HERE,'kvgall','kanji')

chars=set()
for w in W: chars|=set(w)
for t in T.values():
    chars|=set(t['jp'])
    for s in t['sections']: chars|=set(s[0])
    for n in t['names']: chars|=set(n.replace('{n}',''))
for r in R.values(): chars|=set(r['jp'])
for n,_ in NAMES: chars|=set(n)
chars|=set('〇一二三四五六七八九十百千円税込各種0123456789')
chars|=set('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽっゃゅょアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポッャュョー')
chars.discard(' ')

def parse(ch):
    f=os.path.join(KV,'%05x.svg'%ord(ch))
    if not os.path.exists(f): return None
    txt=open(f,encoding='utf-8').read()
    txt=re.sub(r'<!DOCTYPE.*?]>','',txt,flags=re.S).replace(' kvg:',' kvg_')
    root=ET.fromstring(txt)
    sp=[g for g in root.iter('{http://www.w3.org/2000/svg}g') if g.get('id','').startswith('kvg:StrokePaths')][0]
    strokes=[];types=[]
    def walk(g):
        comps=[]
        for c in g:
            tag=c.tag.split('}')[1]
            if tag=='path':
                d=re.sub(r'(\d+\.\d{1})\d+',r'\1',c.get('d'))
                strokes.append(d); types.append(c.get('kvg_type') or '')
            elif tag=='g':
                start=len(strokes); sub=walk(c)
                node={'e':c.get('kvg_element'),'s':start,'n':len(strokes)-start}
                if c.get('kvg_original'): node['o']=c.get('kvg_original')
                if c.get('kvg_position'): node['p']=c.get('kvg_position')
                if c.get('kvg_part'): node['pt']=int(c.get('kvg_part'))
                if sub: node['c']=sub
                comps.append(node)
        return comps
    top=walk(sp)
    return {'d':strokes,'t':types,'c':top[0].get('c',[]) if top else []}

kvg={}
missing=[]
for ch in sorted(chars):
    if ch in '0123456789': continue
    p=parse(ch)
    if p: kvg[ch]=p
    else: missing.append(ch)
kvg['〇']={"d": ["M54,18c-19,0-33,15-33,35c0,19,14,34,33,34c19,0,31-15,31-34c0-20-12-35-31-35c-4,0-7,1-10,3"], "t": [""], "c": []}
print('missing', ''.join(missing))

# components: collect elements used
def elems(nodes,acc):
    for n in nodes:
        if n.get('e'): acc.add(n['e'])
        if n.get('o'): acc.add(n['o'])
        elems(n.get('c',[]),acc)
compset=set()
for ch,v in kvg.items(): elems(v['c'],compset)
# components get their own stroke data too, so their sheet can be drawn by hand like any kanji
for ch in sorted(compset):
    if ch in kvg or len(ch)!=1: continue
    p=parse(ch)
    if p: kvg[ch]=p

db=sqlite3.connect(os.path.join(HERE,'..','dl','jamdict.db'))
def kinfo(ch):
    row=db.execute('select ID,stroke_count,grade,freq,jlpt from character where literal=?',(ch,)).fetchone()
    if not row: return None
    cid=row[0]
    fr=[];en=[];on=[];kun=[]
    for (gid,) in db.execute('select ID from rm_group where cid=?',(cid,)):
        for v,l in db.execute('select value,m_lang from meaning where gid=?',(gid,)):
            if l=='fr': fr.append(v)
            elif l=='': en.append(v)
        for t,v in db.execute('select r_type,value from reading where gid=?',(gid,)):
            if t=='ja_on': on.append(v)
            elif t=='ja_kun': kun.append(v)
    return [fr[:5], en[:4], on[:4], kun[:6], row[1], row[2], row[3], row[4]]

kd={}
for ch in sorted(set(kvg)|compset):
    if re.match(r'[一-鿿㐀-䶿]',ch):
        i=kinfo(ch)
        if i: kd[ch]=i
words=[[w,r,f] for w,(r,f) in W.items()]
data={'kvg':kvg,'kd':kd,'words':words,'types':T,'regions':R,'names':NAMES,'namepat':NAMEPAT_R,'mentions':MENTIONS}
out=json.dumps(data,ensure_ascii=False,separators=(',',':'))
open(os.path.join(HERE,'data.json'),'w',encoding='utf-8').write(out)
print('kvg',len(kvg),'kd',len(kd),'words',len(words),'bytes',len(out.encode()))
# chars to subset fonts
open(os.path.join(HERE,'fontchars.txt'),'w',encoding='utf-8').write(''.join(sorted(chars|set('¥（）・…★')))+'0123456789')
# components lacking kanjidic info
print('comps w/o info', ''.join(sorted(c for c in compset if c not in kd)))
