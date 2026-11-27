"""Add stroke data (KanjiVG) and dictionary info (jamdict) to data.json for the kanji that new words bring.
Usage: python src/addchars.py --kvg <kanjivg 'kanji' folder> --db <jamdict.db>
Only missing characters are added; everything already in data.json is left as it is."""
import argparse, json, re, runpy, sqlite3, xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent

def parse(folder, ch):
    f = Path(folder) / ('%05x.svg' % ord(ch))
    if not f.exists(): return None
    txt = re.sub(r'<!DOCTYPE.*?]>', '', f.read_text(encoding='utf-8'), flags=re.S).replace(' kvg:', ' kvg_')
    root = ET.fromstring(txt)
    sp = [g for g in root.iter('{http://www.w3.org/2000/svg}g') if g.get('id', '').startswith('kvg:StrokePaths')][0]
    strokes, types = [], []
    def walk(g):
        comps = []
        for c in g:
            tag = c.tag.split('}')[1]
            if tag == 'path':
                strokes.append(re.sub(r'(\d+\.\d{1})\d+', r'\1', c.get('d'))); types.append(c.get('kvg_type') or '')
            elif tag == 'g':
                start = len(strokes); sub = walk(c)
                node = {'e': c.get('kvg_element'), 's': start, 'n': len(strokes) - start}
                if c.get('kvg_original'): node['o'] = c.get('kvg_original')
                if c.get('kvg_position'): node['p'] = c.get('kvg_position')
                if c.get('kvg_part'): node['pt'] = int(c.get('kvg_part'))
                if sub: node['c'] = sub
                comps.append(node)
        return comps
    top = walk(sp)
    return {'d': strokes, 't': types, 'c': top[0].get('c', []) if top else []}

def kinfo(db, ch):
    row = db.execute('select ID,stroke_count,grade,freq,jlpt from character where literal=?', (ch,)).fetchone()
    if not row: return None
    fr, en, on, kun = [], [], [], []
    for (gid,) in db.execute('select ID from rm_group where cid=?', (row[0],)):
        for v, l in db.execute('select value,m_lang from meaning where gid=?', (gid,)):
            if l == 'fr': fr.append(v)
            elif l == '': en.append(v)
        for t, v in db.execute('select r_type,value from reading where gid=?', (gid,)):
            if t == 'ja_on': on.append(v)
            elif t == 'ja_kun': kun.append(v)
    return [fr[:5], en[:4], on[:4], kun[:6], row[1], row[2], row[3], row[4]]

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--kvg', required=True); ap.add_argument('--db', required=True)
    a = ap.parse_args()
    path = HERE / 'data.json'; data = json.loads(path.read_text(encoding='utf-8'))
    menu = runpy.run_path(str(HERE / 'menudata.py'))
    chars = {c for w in menu['W'] for c in w if re.match(r'[一-鿿]', c)}
    db = sqlite3.connect(a.db); added = []
    for ch in sorted(chars):
        if ch not in data['kvg']:
            p = parse(a.kvg, ch)
            if p: data['kvg'][ch] = p; added.append(ch)
        if ch not in data['kd']:
            i = kinfo(db, ch)
            if i: data['kd'][ch] = i
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print('added', ''.join(added) or 'nothing')
