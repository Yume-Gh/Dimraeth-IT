# -*- coding: utf-8 -*-
"""Motore dell'installer: trova il gioco, installa, rimuove, riferisce.

Separato dall'interfaccia perche' cosi' si puo' provare senza aprire finestre:

    python installer/core.py "E:/Games/Steam/steamapps/common/Dimraeth"

La logica di sostituzione e' la stessa di tools/patch.py, ma qui non si puo'
dare per scontato nulla sulla macchina di chi installa: il backup non esiste
ancora, la build del gioco puo' essere diversa da quella su cui e' stata fatta
la traduzione, e l'utente non sa leggere un traceback.
"""
import hashlib
import os
import shutil
import sys

if getattr(sys, "frozen", False):
    BASE = sys._MEIPASS                      # dentro l'exe di PyInstaller
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(os.path.dirname(BASE), "tools"))

import unityfile as uf

APPID = "2402680"
INSTALLDIR = "Dimraeth"
TARGET_LANG = "Russian"
BAK = ".dimraeth-it.bak"
LABEL_FROM = "Русский".encode("utf-8")            # 14 byte
LABEL_TO = "Italiano".encode("utf-8") + b" " * 6  # 14 byte, stessa lunghezza
VERSION = "1.2"
AUTORE = "Yume"
AUTORE_URL = "https://steamcommunity.com/id/yumexx/"
GIOCO_URL = "https://store.steampowered.com/app/%s/" % APPID


def payload_dir():
    return os.path.join(BASE, "payload")


def rel_paths(game):
    return (os.path.join(game, "Dimraeth_Data", "sharedassets1.assets"),
            os.path.join(game, "Dimraeth_Data", "il2cpp_data", "Metadata",
                         "global-metadata.dat"))


def sha(b):
    return hashlib.sha256(b).hexdigest()[:16]


# ---------------------------------------------------------------- ricerca ---

def _steam_libraries():
    """Tutte le cartelle libreria di Steam, dal registro e da libraryfolders.vdf."""
    roots = []
    try:
        import winreg
        for hive, key in ((winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam"),
                          (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam")):
            try:
                with winreg.OpenKey(hive, key) as k:
                    for name in ("SteamPath", "InstallPath"):
                        try:
                            roots.append(winreg.QueryValueEx(k, name)[0])
                        except OSError:
                            pass
            except OSError:
                pass
    except ImportError:
        pass

    libs = []
    for r in roots:
        r = os.path.normpath(r)
        if r not in libs:
            libs.append(r)
        vdf = os.path.join(r, "steamapps", "libraryfolders.vdf")
        try:
            with open(vdf, encoding="utf-8", errors="replace") as f:
                for line in f:
                    if '"path"' not in line:
                        continue
                    parts = line.split('"')
                    if len(parts) >= 4:
                        p = os.path.normpath(parts[3].replace("\\\\", "\\"))
                        if p not in libs:
                            libs.append(p)
        except OSError:
            pass
    return libs


def find_game():
    """Cartella del gioco, o None. Prima Steam, poi i percorsi tipici."""
    for lib in _steam_libraries():
        acf = os.path.join(lib, "steamapps", "appmanifest_%s.acf" % APPID)
        installdir = INSTALLDIR
        try:
            with open(acf, encoding="utf-8", errors="replace") as f:
                for line in f:
                    if '"installdir"' in line:
                        parts = line.split('"')
                        if len(parts) >= 4:
                            installdir = parts[3]
        except OSError:
            if not os.path.isfile(acf):
                continue
        cand = os.path.join(lib, "steamapps", "common", installdir)
        if is_game_folder(cand):
            return cand
    for lib in _steam_libraries():
        cand = os.path.join(lib, "steamapps", "common", INSTALLDIR)
        if is_game_folder(cand):
            return cand
    return None


def is_game_folder(path):
    if not path:
        return False
    assets, meta = rel_paths(path)
    return os.path.isfile(assets) and os.path.isfile(meta)


def game_running():
    """Il gioco tiene aperto sharedassets1.assets solo a tratti: si controlla il processo."""
    try:
        import subprocess
        out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq Dimraeth.exe"],
                             capture_output=True, text=True, timeout=15,
                             creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        return "Dimraeth.exe" in out.stdout
    except Exception:
        return False


# ------------------------------------------------------------------ stato ---

def backup_stale(assets, data=None):
    """Motivo per cui il backup non e' piu' una base valida, o None.

    Stessa guardia di tools/patch.py: la sostituzione e' byte-esatta, quindi un
    backup valido ha la stessa dimensione del file attuale e i suoi offset
    cadono ancora su payload che iniziano col BOM. Se il gioco viene
    aggiornato salta una delle due, e scrivere a quegli offset corromperebbe
    il file invece di tradurlo.
    """
    bak = assets + BAK
    if not os.path.exists(bak):
        return None
    if os.path.getsize(bak) != os.path.getsize(assets):
        return ("il backup ha una dimensione diversa dal file del gioco "
                "({:,} contro {:,} byte)".format(os.path.getsize(assets),
                                                 os.path.getsize(bak)))
    if data is None:
        with open(assets, "rb") as f:
            data = f.read()
    with open(bak, "rb") as f:
        picked, probs = uf.pick_slots(uf.scan(f.read()), TARGET_LANG)
    if probs:
        return "gli slot del backup non si risolvono piu'"
    bad = sorted(c for c, sl in picked.items()
                 if not data[sl.payload_off:sl.payload_off + sl.size].startswith(uf.BOM))
    if bad:
        return "gli offset del backup non corrispondono piu' al file del gioco"
    return None


def meta_backup_stale(meta):
    """True se il backup di global-metadata.dat viene da un'altra build.

    La rinomina scambia 14 byte con altri 14, quindi un backup valido e'
    esattamente il file attuale con l'etichetta rimessa in russo. Il controllo
    su sharedassets1.assets non basta: gli aggiornamenti riscrivono anche questo,
    e ripristinare un metadata vecchio romperebbe il gioco.
    """
    bak = meta + BAK
    if not os.path.exists(bak):
        return False
    if os.path.getsize(bak) != os.path.getsize(meta):
        return True
    with open(meta, "rb") as f, open(bak, "rb") as g:
        return f.read().replace(LABEL_TO, LABEL_FROM) != g.read()


def _scarta_backup_obsoleti(assets, meta):
    """Dopo un aggiornamento i file del gioco sono quelli nuovi scritti da
    Steam, senza traduzione: i backup vecchi non servono piu' a nulla, e
    rimetterli danneggerebbe il gioco. Si tolgono, e l'installazione riparte
    da zero come per un utente nuovo."""
    if backup_stale(assets) and os.path.exists(assets + BAK):
        os.remove(assets + BAK)
    if meta_backup_stale(meta):
        os.remove(meta + BAK)


def status(game):
    """(stato, dettaglio) leggibili da un essere umano."""
    if not is_game_folder(game):
        return "assente", "In questa cartella non c'e' Dimraeth."
    assets, meta = rel_paths(game)
    try:
        with open(assets, "rb") as f:
            data = f.read()
    except OSError as e:
        return "errore", "Non riesco a leggere il file del gioco: %s" % e
    motivo = backup_stale(assets, data)
    if motivo:
        return "aggiornato", ("Il gioco e' stato aggiornato e la traduzione non e' "
                              "piu' attiva. Premi «Installa la traduzione» "
                              "per rimetterla.")
    bak = assets + BAK
    if not os.path.exists(bak):
        return "originale", "Gioco originale, traduzione non installata."
    with open(bak, "rb") as f:
        same = f.read() == data
    if same:
        return "originale", "Traduzione rimossa, gioco riportato all'originale."
    return "installata", "Traduzione italiana installata."


# --------------------------------------------------------------- install ---

class Problema(Exception):
    """Errore con un messaggio gia' scritto per chi installa."""


def install(game, progress=lambda pct, testo: None):
    assets, meta = rel_paths(game)
    if not is_game_folder(game):
        raise Problema("In questa cartella non c'e' Dimraeth.\n\n"
                       "Serve quella che contiene Dimraeth.exe e Dimraeth_Data.")
    if game_running():
        raise Problema("Dimraeth e' aperto.\n\nChiudi il gioco e riprova.")
    if not os.access(assets, os.W_OK):
        raise Problema("Non ho il permesso di scrivere nei file del gioco.\n\n"
                       "Prova a lanciare l'installer come amministratore.")

    progress(5, "Leggo il file del gioco...")
    with open(assets, "rb") as f:
        data = f.read()

    # Gioco aggiornato dopo un'installazione precedente: il backup vecchio non
    # e' piu' una base valida (i suoi offset corromperebbero il file nuovo),
    # quindi gli slot si cercano nel file attuale, che e' l'originale di Steam.
    aggiornato = backup_stale(assets, data) is not None

    progress(15, "Cerco le tabelle della lingua...")
    bak = assets + BAK
    src = bak if os.path.exists(bak) and not aggiornato else assets
    with open(src, "rb") as f:
        picked, probs = uf.pick_slots(uf.scan(f.read()), TARGET_LANG)
    if probs:
        raise Problema("Questa versione del gioco non e' compatibile con la "
                       "traduzione.\n\nNon ho trovato le tabelle attese:\n  "
                       + "\n  ".join(probs[:4]))

    progress(30, "Controllo che i testi italiani ci stiano...")
    plan, troppo = [], []
    for cat in uf.CATEGORIES:
        f = os.path.join(payload_dir(), cat + ".csv")
        if not os.path.isfile(f):
            raise Problema("Pacchetto incompleto: manca %s.csv.\n\n"
                           "Riscarica l'installer." % cat)
        with open(f, "rb") as fh:
            payload = fh.read()
        if not payload.startswith(uf.BOM):
            payload = uf.BOM + payload.lstrip(uf.BOM)
        slot = picked[cat]
        if len(payload) > slot.size:
            troppo.append("%s (%+d byte)" % (cat, len(payload) - slot.size))
            continue
        plan.append((cat, slot, payload))
    if troppo:
        raise Problema("Questa versione del gioco non e' compatibile con la "
                       "traduzione: i testi italiani non ci stanno.\n\n"
                       + ", ".join(troppo) + "\n\n"
                       "Probabilmente il gioco e' stato aggiornato. "
                       "Serve una versione nuova della traduzione.")

    progress(45, "Creo il backup del gioco originale...")
    _scarta_backup_obsoleti(assets, meta)
    if not os.path.exists(bak):
        shutil.copy2(assets, bak)

    progress(60, "Scrivo i testi italiani...")
    out = data
    for cat, slot, payload in plan:
        out = uf.splice(out, slot, uf.pad_csv(payload, slot.size))
    if len(out) != len(data):
        raise Problema("Controllo interno fallito: la dimensione del file "
                       "sarebbe cambiata. Non ho modificato nulla.")
    if game_running():
        raise Problema("Dimraeth e' stato aperto durante l'installazione.\n\n"
                       "Chiudi il gioco e riprova. Non ho modificato nulla.")
    _atomic_write(assets, out)

    progress(85, "Rinomino la voce del menu...")
    # Se l'etichetta e' gia' "Italiano" da un'installazione precedente, non c'e'
    # niente da rinominare: e' comunque la voce che l'utente vedra' nel menu.
    # Trattarlo come fallimento mandava a schermo il nome russo, che e' sbagliato.
    voce = "Русский"
    try:
        with open(meta, "rb") as f:
            md = f.read()
        if md.count(LABEL_FROM) == 1:
            if not os.path.exists(meta + BAK):
                shutil.copy2(meta, meta + BAK)
            _atomic_write(meta, md.replace(LABEL_FROM, LABEL_TO))
            voce = "Italiano"
        elif md.count(LABEL_TO) >= 1:
            voce = "Italiano"
    except OSError:
        pass

    progress(100, "Fatto.")
    return {"categorie": len(plan), "etichetta": voce == "Italiano", "voce": voce}


def uninstall(game, progress=lambda pct, testo: None):
    assets, meta = rel_paths(game)
    if not is_game_folder(game):
        raise Problema("In questa cartella non c'e' Dimraeth.")
    if game_running():
        raise Problema("Dimraeth e' aperto.\n\nChiudi il gioco e riprova.")
    n = 0
    progress(30, "Ripristino i file originali...")
    # I backup di un'altra build non si rimettono: dopo un aggiornamento il
    # file del gioco e' gia' quello originale di Steam.
    if backup_stale(assets):
        os.remove(assets + BAK)
        n += 1
    if meta_backup_stale(meta):
        os.remove(meta + BAK)
        with open(meta, "rb") as f:
            md = f.read()
        if LABEL_TO in md:
            _atomic_write(meta, md.replace(LABEL_TO, LABEL_FROM))
        n += 1
    for p in (assets, meta):
        bak = p + BAK
        if os.path.exists(bak):
            shutil.copy2(bak, p)
            os.remove(bak)
            n += 1
    progress(100, "Fatto.")
    if not n:
        raise Problema("Non ho trovato nessun backup da ripristinare.\n\n"
                       "Se il gioco e' comunque in italiano, usa Steam: "
                       "Proprieta' -> File installati -> Verifica integrita'.")
    return {"ripristinati": n}


def _atomic_write(path, blob):
    """Scrive di fianco e poi sostituisce: un'interruzione non lascia un file mezzo scritto."""
    tmp = path + ".dimraeth-it.tmp"
    with open(tmp, "wb") as f:
        f.write(blob)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


# ------------------------------------------------------------------ prova ---

if __name__ == "__main__":
    g = sys.argv[1] if len(sys.argv) > 1 else find_game()
    print("gioco:", g)
    print("stato:", status(g) if g else "non trovato")
