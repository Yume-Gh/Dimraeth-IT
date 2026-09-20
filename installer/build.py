# -*- coding: utf-8 -*-
"""Costruisce Dimraeth-IT-Setup.exe.

    python installer/build.py

Raccoglie in installer/ tutto quello che deve finire nell'exe -- i sedici CSV
italiani e unityfile.py -- e poi lancia PyInstaller. Il risultato e' un file
solo: chi lo riceve non deve installare Python ne' altro.
"""
import glob
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NOME = "Dimraeth-IT-Setup"


def stage():
    """Copia dentro installer/ i file che l'exe deve contenere."""
    payload = os.path.join(HERE, "payload")
    os.makedirs(payload, exist_ok=True)
    for f in glob.glob(os.path.join(payload, "*.csv")):
        os.remove(f)
    csvs = sorted(glob.glob(os.path.join(ROOT, "it", "*.csv")))
    if len(csvs) != 16:
        sys.exit("attesi 16 CSV in it/, trovati %d" % len(csvs))
    tot = 0
    for f in csvs:
        shutil.copy2(f, payload)
        tot += os.path.getsize(f)
    shutil.copy2(os.path.join(ROOT, "tools", "unityfile.py"),
                 os.path.join(HERE, "unityfile.py"))
    print("payload: %d CSV, %.1f MB" % (len(csvs), tot / 1e6))


def build():
    sep = ";" if os.name == "nt" else ":"
    cmd = [sys.executable, "-m", "PyInstaller",
           "--onefile", "--windowed", "--clean", "--noconfirm",
           "--name", NOME,
           "--distpath", os.path.join(HERE, "dist"),
           "--workpath", os.path.join(HERE, "build"),
           "--specpath", os.path.join(HERE, "build"),
           "--add-data", os.path.join(HERE, "payload") + sep + "payload",
           "--hidden-import", "unityfile",
           os.path.join(HERE, "gui.py")]
    print("$", " ".join(cmd[:8]), "...")
    r = subprocess.run(cmd, cwd=HERE)
    if r.returncode:
        sys.exit("PyInstaller ha fallito (codice %d)" % r.returncode)
    exe = os.path.join(HERE, "dist", NOME + ".exe")
    print("\n%s  (%.1f MB)" % (exe, os.path.getsize(exe) / 1e6))
    return exe


if __name__ == "__main__":
    stage()
    build()
