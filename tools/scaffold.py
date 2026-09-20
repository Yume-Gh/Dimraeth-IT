"""Prepara it/ partendo dall'inglese: le 16 categorie da tradurre in loco.

    python tools/scaffold.py            # non sovrascrive quello che esiste
    python tools/scaffold.py --force
"""
import argparse, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unityfile as uf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ap = argparse.ArgumentParser()
ap.add_argument("--src", default=os.path.join(ROOT, "source", "English"))
ap.add_argument("--it", default=os.path.join(ROOT, "it"))
ap.add_argument("--force", action="store_true")
a = ap.parse_args()

os.makedirs(a.it, exist_ok=True)
created = skipped = 0
for cat in uf.CATEGORIES:
    src, dst = os.path.join(a.src, cat + ".csv"), os.path.join(a.it, cat + ".csv")
    if not os.path.isfile(src):
        print(f"  {cat}: sorgente assente, esegui extract.py"); continue
    if os.path.isfile(dst) and not a.force:
        skipped += 1; continue
    shutil.copy2(src, dst); created += 1
print(f"it/: {created} file creati, {skipped} lasciati invariati")
print("Traduci la colonna Text lasciando intatta la colonna Key.")
print("Mantieni i placeholder {0}, {1} e i tag <b> <color=...> cosi' come sono.")
