#!/usr/bin/env python3
"""Offline Android SDK build. Run from any directory; supply ANDROID_HOME and ANDROID_NDK_HOME."""
from pathlib import Path
import os,subprocess,zipfile,shutil
ROOT=Path(__file__).resolve().parent; REPO=ROOT.parent/'corsixth-android'
SDK=Path(os.environ['ANDROID_HOME']);NDK=Path(os.environ.get('ANDROID_NDK_HOME',str(SDK/'ndk/26.3.11579264')))
BT=SDK/'build-tools/35.0.0';JAR=SDK/'platforms/android-35/android.jar'; B=ROOT/'build';B.mkdir(exist_ok=True)
def run(args):subprocess.run([str(a) for a in args],check=True)
if os.environ.get('THOR_USE_PREBUILT') != '1':
 run([NDK/'ndk-build','-C',REPO,'APP_ABI=arm64-v8a','-j6'])
# Rebuild engine resources on every build. Original game assets are supplied separately.
STAGED=B/'public-assets'
if STAGED.exists():shutil.rmtree(STAGED)
STAGED.mkdir()
OPTIONAL={'thor_title.cthg','thor_vending.dat','receptionist.dat','receptionist.json'}
with zipfile.ZipFile(STAGED/'engine.zip','w',zipfile.ZIP_DEFLATED) as z:
 src=REPO/'jni/CorsixTH/CorsixTH'
 for folder in ['Lua','Bitmap','Graphics','Levels','Campaigns']:
  for p in (src/folder).rglob('*'):
   if p.is_file() and p.name not in OPTIONAL:z.write(p,p.relative_to(src))
 z.write(src/'CorsixTH.lua','CorsixTH.lua')
for name in ['music.zip','font.ttf']:
 if not (ROOT/'assets'/name).is_file():raise SystemExit('Missing assets/'+name+'; see README.md')
 shutil.copy(ROOT/'assets'/name,STAGED/name)
shutil.copytree(ROOT/'notices',STAGED/'notices')
classes=B/'classes';classes.mkdir(exist_ok=True)
run(['javac','-encoding','UTF-8','-source','8','-target','8','-classpath',JAR,'-d',classes,*sorted((ROOT/'src').rglob('*.java'))])
run(['jar','cf',B/'classes.jar','-C',classes,'.'])
dex=B/'dex';dex.mkdir(exist_ok=True)
run([BT/'d8','--lib',JAR,'--min-api','27','--output',dex,B/'classes.jar'])
run([BT/'aapt2','link','-I',JAR,'--manifest',ROOT/'AndroidManifest.xml','-o',B/'unaligned.apk','-A',STAGED,'--auto-add-overlay'])
with zipfile.ZipFile(B/'unaligned.apk','a',zipfile.ZIP_DEFLATED) as z:
 z.write(dex/'classes.dex','classes.dex')
 for p in (REPO/'libs/arm64-v8a').glob('*.so'):z.write(p,'lib/arm64-v8a/'+p.name)
run([BT/'zipalign','-f','-p','4',B/'unaligned.apk',B/'aligned.apk'])
key=Path(os.environ['THOR_SIGNING_KEY'])
if not key.is_file():raise SystemExit('Signing key missing; refusing to generate a replacement')
out=ROOT/'Theme_Hospital_Thor_0.22.apk'
run([BT/'apksigner','sign','--ks',key,'--ks-pass','env:THOR_STORE_PASSWORD','--key-pass','env:THOR_KEY_PASSWORD','--out',out,B/'aligned.apk'])
run([BT/'apksigner','verify','--verbose',out])
print(out)
