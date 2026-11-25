"""Stage only runtime assets for GitHub Pages, without tooling or source files."""
from pathlib import Path
import shutil
from build import ROOT

destination = ROOT / 'artifacts' / 'site'
destination.mkdir(parents=True, exist_ok=True)
for name in ['index.html', 'sw.js', 'manifest.webmanifest', 'voice.mp3', '.nojekyll',
             'icon-32.png', 'icon-180.png', 'icon-192.png', 'icon-512.png']:
    shutil.copyfile(ROOT / name, destination / name)
shutil.copytree(ROOT / 'fb', destination / 'fb', dirs_exist_ok=True)
print('Public assets staged in artifacts/site.')
