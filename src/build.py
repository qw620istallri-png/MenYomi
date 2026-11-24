import json, urllib.parse, re, os
t=open('template.html',encoding='utf-8').read()
v1=open('../template.html',encoding='utf-8').read()
k=v1[v1.index('const K = {')+len('const K = '):]
k=k[:k.index('\n};')+3]
data=open('data.json',encoding='utf-8').read()
fc=open('fontchars.txt',encoding='utf-8').read()
jp=lambda x: set(re.findall(r'[\u3040-\u30ff\u3400-\u9fff\uff01-\uff60]',x))
fc=''.join(sorted(set(fc)|jp(t)|jp(k)|set(json.loads(data)['kd'].keys())))
ns={}; exec(open('en.py',encoding='utf-8').read(),ns)
en=json.dumps({'w':ns['W_EN'],'k':ns['K_EN'],'rad':ns['RAD_EN'],'fro':ns['FRO_EN'],'types':ns['TYPES_EN']},ensure_ascii=False,separators=(',',':'))
nx={}; exec(open('explain.py',encoding='utf-8').read(),nx)
t=t.replace('__EXPL__',json.dumps(nx['X'],ensure_ascii=False,separators=(',',':'))).replace('__NX__',json.dumps(nx['NX'],ensure_ascii=False,separators=(',',':')))
import datetime,zoneinfo,hashlib
_bt=datetime.datetime.now(zoneinfo.ZoneInfo('Europe/Paris'))
t=t.replace('__BUILD__',_bt.strftime('%Y.%m.%d · %H:%M')+' · '+hashlib.sha1(t.encode()).hexdigest()[:6])
t=t.replace('__TZ__',open('tz.json',encoding='utf-8').read())
t=t.replace('__VOICE__',open('voice.json',encoding='utf-8').read())
t=t.replace('__EN__',en).replace('__K__',k).replace('__FONTTEXT__',urllib.parse.quote(fc))
t=t.replace('const DATA = __DATA__;','const DATA = __DATA__;')
full=t.replace('__DATA__',data)
open('kanji-pinceau.html','w',encoding='utf-8').write(full)
open('test.html','w',encoding='utf-8').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>'+full+'</body></html>')
print(len(full))
