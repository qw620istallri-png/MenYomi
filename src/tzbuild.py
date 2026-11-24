# Builds tz.json: IANA time zone -> [lat, lon] (whole degrees) from the system tz database, links included.
import json,re
def dms(s):
    sg=-1 if s[0]=='-' else 1; s=s[1:]; d=int(s[:2]) if len(s) in (4,6) else int(s[:3]); r=s[2:] if len(s) in (4,6) else s[3:]
    return sg*(d+int(r[:2])/60+(int(r[2:4])/3600 if len(r)>2 else 0))
Z={}
for l in open('/usr/share/zoneinfo/zone.tab'):
    if l.startswith('#'): continue
    f=l.split('\t'); m=re.match(r'([+-]\d+)([+-]\d+)',f[1]); Z[f[2].strip()]=[round(dms(m.group(1))),round(dms(m.group(2)))]
for l in open('/usr/share/zoneinfo/zone1970.tab'):
    if l.startswith('#'): continue
    f=l.split('\t'); m=re.match(r'([+-]\d+)([+-]\d+)',f[1]); Z.setdefault(f[2].strip(),[round(dms(m.group(1))),round(dms(m.group(2)))])
for _ in range(3):
    for l in open('/usr/share/zoneinfo/tzdata.zi'):
        if l.startswith('L '):
            _,tgt,lnk=l.split()
            if tgt in Z and lnk not in Z: Z[lnk]=Z[tgt]
json.dump(Z,open('tz.json','w'),separators=(',',':'),sort_keys=True)
print(len(Z), len(json.dumps(Z,separators=(',',':'))), Z.get('Europe/Paris'), Z.get('Asia/Calcutta'), Z.get('Asia/Tokyo'), Z.get('Europe/Brussels'))
