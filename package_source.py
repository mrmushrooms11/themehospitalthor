#!/usr/bin/env python3
"""Create a public source ZIP, excluding private game data, art and signing keys."""
from pathlib import Path
import zipfile,sys
root=Path(__file__).resolve().parent
project=root.parent
output=Path(sys.argv[1]) if len(sys.argv)>1 else root/'Theme_Hospital_Thor_0.22_Source.zip'
optional={'thor_title.cthg','thor_vending.dat','receptionist.dat','receptionist.json'}
allowed_root={'AndroidManifest.xml','README.md','THOR_LICENSE.txt','TEST_RESULTS_0.22.txt','build.py','prepare_assets.py','package_source.py'}
def allowed(p):
 rel=p.relative_to(project);parts=rel.parts
 if any(x in {'.git','__pycache__','obj','host-build','build'} for x in parts):return False
 if p.suffix.lower() in {'.jks','.keystore','.apk','.idsig','.pyc','.o','.sav'}:return False
 if p.name in optional:return False
 if parts[0]=='corsixth-android':
  if len(parts)>1 and parts[1]=='assets':return False
  if 'Music' in parts:return False
  return True
 if parts[0]!='thor':return False
 tail=parts[1:]
 if len(tail)==1:return p.name in allowed_root
 if tail[0]=='assets':return len(tail)==2 and p.name in {'music.zip','font.ttf'}
 if tail[0] in {'src','notices','third_party_sources'}:return True
 if tail[0]=='tests':return p.suffix in {'.py','.lua','.java','.cpp','.c','.h'} and 'stubs' in tail or (len(tail)==2 and p.suffix in {'.py','.lua','.java','.cpp'})
 if tail[0]=='artwork':return p.suffix=='.py'
 return False
output.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
 for tree in ['corsixth-android','thor']:
  for p in sorted((project/tree).rglob('*')):
   if p.is_file() and allowed(p):z.write(p,p.relative_to(project))
print(output)
