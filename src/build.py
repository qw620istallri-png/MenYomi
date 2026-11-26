"""Rebuild the static app with Python standard library only."""
import argparse
import hashlib
import json
from pathlib import Path
import runpy
import urllib.parse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

def render():
    template = (HERE / 'template.html').read_text(encoding='utf-8')
    data = json.loads((HERE / 'data.json').read_text(encoding='utf-8'))
    menu = runpy.run_path(str(HERE / 'menudata.py'))
    data.update(words=[[w, *v] for w, v in menu['W'].items()], types=menu['T'], regions=menu['R'], names=menu['NAMES'], namepat=menu['NAMEPAT_R'], mentions=menu['MENTIONS'], phrases=menu['PHRASES'], prices=menu['PRICES'])
    en = runpy.run_path(str(HERE / 'en.py'))
    explanations = runpy.run_path(str(HERE / 'explain.py'))
    def seasons(data):
        sz = runpy.run_path(str(HERE / 'seasons.py')); known = {w[0] for w in data['words']}
        return {'sekki': sz['SEKKI'], 'ko': sz['KO'], 'shun': {m: [w for w in ws if w in known] for m, ws in sz['SHUN'].items()}, 'hol': sz['HOLIDAYS']}
    values = {'DATA': data, 'K': json.loads((HERE / 'kanji.json').read_text(encoding='utf-8')), 'EN': {k: en[v] for k, v in dict(w='W_EN', k='K_EN', rad='RAD_EN', fro='FRO_EN', types='TYPES_EN').items()}, 'EXPL': explanations['X'], 'NX': explanations['NX'], 'PARTS': runpy.run_path(str(HERE / 'parts.py'))['P'], 'SEASONS': seasons(data), 'TZ': json.loads((HERE / 'tz.json').read_text(encoding='utf-8')), 'VOICE': json.loads((HERE / 'voice' / 'voice.json').read_text(encoding='utf-8'))}
    for key, value in values.items():
        template = template.replace('__' + key + '__', json.dumps(value, ensure_ascii=False, separators=(',', ':')))
    for key, filename in [('PROGRESS', 'progress.js'), ('LEARNING', 'learning.js'), ('AMBIENCE', 'ambience.js'), ('DOODLES', 'doodles.js')]:
        template = template.replace('__' + key + '__', (HERE / filename).read_text(encoding='utf-8'))
    chars = ''.join(sorted(set(c for c in template if '\u3040' <= c <= '\u9fff') | set(data['kd'])))
    template = template.replace('__FONTTEXT__', urllib.parse.quote(chars))
    version = hashlib.sha256(template.encode()).hexdigest()[:10]
    template = template.replace('__BUILD__', '2 · ' + version)
    head = '''<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,interactive-widget=resizes-content">
<meta name="theme-color" content="#f7f0e1">
<meta name="description" content="Lire les menus japonais écrits à la main.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="32x32" href="icon-32.png">
<link rel="apple-touch-icon" href="icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Menyomi">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
</head><body>
'''
    page = head + template + '\n</body></html>\n'
    sw_version = hashlib.sha256(page.encode() + (ROOT / 'voice.mp3').read_bytes()).hexdigest()[:12]
    worker = (HERE / 'sw.js').read_text(encoding='utf-8').replace('__VERSION__', sw_version)
    return {'index.html': page, 'sw.js': worker}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail when generated files are stale')
    args = parser.parse_args()
    stale = []
    for name, content in render().items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != content:
                stale.append(name)
        else:
            path.write_text(content, encoding='utf-8', newline='\n')
    if stale:
        parser.exit(1, 'Rebuild required: ' + ', '.join(stale) + '\n')
    print('Generated files verified.' if args.check else 'Built index.html and sw.js.')
