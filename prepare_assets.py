#!/usr/bin/env python3
"""Public builds deliberately do not accept or bundle original game data."""
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parent
for name in ('music.zip','font.ttf'):
    if not (root/'assets'/name).is_file():
        raise SystemExit('Missing redistributable runtime asset: '+name)
with zipfile.ZipFile(root/'assets/music.zip') as archive:
    assert 'copyright.txt' in archive.namelist() and 'COPYING' in archive.namelist()
print('Runtime assets ready. Users import original game data on their device after installation.')
