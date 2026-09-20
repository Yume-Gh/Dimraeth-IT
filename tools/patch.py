"""Installa / rimuove la traduzione italiana sostituendo lo slot russo.

    python tools/patch.py status    --game "E:/.../Dimraeth"
    python tools/patch.py install   --game "E:/.../Dimraeth" [--label] [--dry-run]
    python tools/patch.py uninstall --game "E:/.../Dimraeth"

L'italiano prende il posto del russo perche' e' l'unico slot con margine di byte
in tutte le 16 categorie: la sostituzione resta byte-esatta e nessun offset del
file .assets si sposta. In gioco si seleziona "Русский" (o "Italiano" con --label).
"""
import argparse, hashlib, json, os, shutil, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unityfile as uf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_LANG = "Russian"
BAK = ".dimraeth-it.bak"
# etichetta nel menu: sostituzione byte-esatta, 14 byte UTF-8 entrambe
LABEL_FROM = "Русский".encode("utf-8")           # 14 byte
LABEL_TO = "Italiano".encode("utf-8") + b" " * 6  # 14 byte


NL = chr(10)


def backup_stale(assets, data=None):
    """Motivo per cui il backup NON e' piu' una base valida, o None se lo e'.

    La sostituzione e' byte-esatta: un backup buono ha la STESSA dimensione del
    file attuale, e gli offset dei suoi slot cadono ancora su payload CSV, che
    iniziano sempre col BOM sia in russo sia in italiano. Se Steam aggiorna il
    gioco salta l'una o l'altra condizione -- e scrivere a quegli offset
    corromperebbe il file nuovo invece di tradurlo, senza che nulla se ne
    accorga: lo splice conserva la lunghezza, quindi l'assert non scatta.
    """
    bak = assets + BAK
    if not os.path.exists(bak):
        return None
    if os.path.getsize(bak) != os.path.getsize(assets):
        return ("dimensione diversa dal backup ({:,} contro {:,} byte)"
                .format(os.path.getsize(assets), os.path.getsize(bak)))
    if data is None:
        with open(assets, "rb") as f:
            data = f.read()
    with open(bak, "rb") as f:
        picked, probs = uf.pick_slots(uf.scan(f.read()), TARGET_LANG)
    if probs:
        return "gli slot del backup non si risolvono piu': " + "; ".join(probs)
    bad = sorted(c for c, sl in picked.items()
                 if not data[sl.payload_off:sl.payload_off + sl.size]
                 .startswith(uf.BOM))
    if bad:
        return ("gli offset del backup non cadono piu' su un CSV: "
                + ", ".join(bad[:4]) + ("..." if len(bad) > 4 else ""))
    return None


def stale_help(motivo):
    return NL.join([
        "Il gioco risulta AGGIORNATO dopo l'ultimo install:",
        "  " + motivo,
        "",
        "Il backup non e' piu' una base valida per questo file. Scrivere agli",
        "offset che contiene corromperebbe il gioco invece di tradurlo.",
        "",
        "Cosa fare:",
        "  1. NON cancellare il backup vecchio: spostalo altrove e tienilo.",
        "  2. python tools/extract.py --game \"<gioco>\"",
        "  3. confrontare i nuovi source/English con quelli di prima:",
        "     - testo invariato  -> basta reinstallare dal backup nuovo;",
        "     - testo cambiato   -> le chiavi nuove vanno tradotte prima.",
    ])


def paths(game):
    return (os.path.join(game, "Dimraeth_Data", "sharedassets1.assets"),
            os.path.join(game, "Dimraeth_Data", "il2cpp_data", "Metadata",
                         "global-metadata.dat"))


def sha(b):
    return hashlib.sha256(b).hexdigest()[:16]


def game_running():
    """Il gioco tiene aperto sharedassets1.assets: scrivere mentre gira fallisce."""
    import subprocess
    try:
        out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq Dimraeth.exe", "/NH"],
                             capture_output=True, text=True, timeout=15).stdout
        return "Dimraeth.exe" in out
    except Exception:
        return False   # in caso di dubbio non blocca: os.replace fallira' comunque


def atomic_write(path, data, recheck=None):
    """Scrive in modo atomico, ricontrollando subito prima dello scambio.

    Il controllo iniziale sul gioco in esecuzione e' soggetto a una corsa: fra
    la verifica e la scrittura passano secondi, e nel frattempo il gioco puo'
    essere lanciato. Inoltre Unity non tiene sempre il file aperto -- legge
    sharedassets1.assets al caricamento della scena e poi puo' rilasciarlo --
    quindi l'assenza di blocco NON dimostra che il gioco sia chiuso.
    """
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    if recheck is not None and recheck():
        os.remove(tmp)
        raise RuntimeError("il gioco risulta in esecuzione: scrittura annullata")
    try:
        os.replace(tmp, path)
    except PermissionError:
        os.remove(tmp)
        raise RuntimeError(f"{os.path.basename(path)} e' bloccato da un altro "
                           "processo: chiudi il gioco e riprova")


def ensure_backup(path):
    bak = path + BAK
    if not os.path.exists(bak):
        print(f"  backup -> {os.path.basename(bak)}")
        shutil.copy2(path, bak)
    else:
        print(f"  backup already present: {os.path.basename(bak)}")
    return bak


def _bak_bytes(assets, off, size):
    with open(assets + BAK, "rb") as f:
        f.seek(off)
        return f.read(size)


def resolve_slots(assets):
    """Slot bersaglio, validi anche su un file gia' patchato.

    Gli slot venivano identificati dal contenuto, ma dopo l'install contengono
    italiano e non sono piu' riconoscibili come russi. Poiche' la sostituzione e'
    byte-esatta, gli offset del backup restano validi sul file attuale: se il
    backup c'e', e' lui la fonte di verita'.
    """
    bak = assets + BAK
    src = bak if os.path.exists(bak) else assets
    with open(src, "rb") as f:
        data = f.read()
    picked, probs = uf.pick_slots(uf.scan(data), TARGET_LANG)
    return picked, probs, os.path.basename(src)


def is_patched(assets):
    """Patchato = differisce dal backup. Senza backup non si puo' affermare."""
    bak = assets + BAK
    if not os.path.exists(bak):
        return None
    with open(assets, "rb") as f1, open(bak, "rb") as f2:
        return f1.read() != f2.read()


def cmd_status(a):
    assets, meta = paths(a.game)
    for p in (assets, meta):
        if not os.path.isfile(p):
            sys.exit(f"non trovato: {p}")
    data = open(assets, "rb").read()
    picked, probs, src = resolve_slots(assets)
    patched = is_patched(assets)
    motivo = backup_stale(assets, data)
    print(f"assets : {assets}")
    print(f"         {len(data):,} byte, sha {sha(data)}")
    print(f"backup : {'presente' if os.path.exists(assets + BAK) else 'ASSENTE'}")
    print(f"slot {TARGET_LANG}: {len(picked)}/16 individuati (da {src})"
          + (f"  {probs}" if probs else ""))
    if motivo:
        print(f"stato  : GIOCO AGGIORNATO - {motivo}")
        print("         la traduzione non e' piu' installata; il backup e' obsoleto.")
    elif patched is None:
        print("stato  : originale (nessun backup, quindi mai patchato)")
    else:
        n = sum(1 for s in picked.values()
                if data[s.payload_off:s.payload_off + s.size] != _bak_bytes(
                    assets, s.payload_off, s.size))
        print(f"stato  : {'PATCHATO' if patched else 'originale'}"
              f"  ({n}/16 categorie sostituite)")
    md = open(meta, "rb").read()
    n_from, n_to = md.count(LABEL_FROM), md.count(LABEL_TO)
    print(f"etichetta menu: 'Русский' x{n_from}, 'Italiano' x{n_to}"
          f"  -> {'rinominata' if n_to else 'originale'}")
    mf = os.path.join(ROOT, "install-manifest.json")
    if os.path.isfile(mf):
        m = json.load(open(mf))
        print(f"ultimo install: {m.get('when')} ({m.get('translated_keys')} chiavi)")


def cmd_install(a):
    assets, meta = paths(a.game)
    if not os.path.isfile(assets):
        sys.exit(f"non trovato: {assets}")
    itdir = a.it or os.path.join(ROOT, "it")

    print("verifica CSV italiani e capienza slot")
    data = open(assets, "rb").read()
    motivo = backup_stale(assets, data)
    if motivo:
        sys.exit(NL + "INSTALL ANNULLATO." + NL + stale_help(motivo))
    picked, probs, src = resolve_slots(assets)
    if probs:
        sys.exit("slot non risolti:\n  " + "\n  ".join(probs))
    if src.endswith(BAK):
        print("  slot letti dal backup: il file risulta gia' patchato, lo riscrivo")

    plan, fatal = [], []
    for cat in uf.CATEGORIES:
        f = os.path.join(itdir, cat + ".csv")
        if not os.path.isfile(f):
            fatal.append(f"{cat}: it/{cat}.csv assente")
            continue
        payload = open(f, "rb").read()
        if not payload.startswith(uf.BOM):
            payload = uf.BOM + payload.lstrip(uf.BOM)
        slot = picked[cat]
        if len(payload) > slot.size:
            fatal.append(f"{cat}: {len(payload)}B > slot {slot.size}B "
                         f"(eccesso {len(payload) - slot.size}B)")
            continue
        plan.append((cat, slot, payload))
        print(f"  {cat:13s} {len(payload):>8d}B / {slot.size:>8d}B  "
              f"margine {slot.size - len(payload):>7d}B")
    if fatal:
        sys.exit("\nINSTALL ANNULLATO:\n  " + "\n  ".join(fatal))

    if a.dry_run:
        print("\n--dry-run: nessun file modificato. Il piano e' valido.")
        return

    print("\nscrittura")
    ensure_backup(assets)
    out = data
    for cat, slot, payload in plan:
        out = uf.splice(out, slot, uf.pad_csv(payload, slot.size))
    assert len(out) == len(data), "la dimensione del file e' cambiata"
    try:
        atomic_write(assets, out, recheck=game_running)
    except RuntimeError as e:
        sys.exit(f"\nINSTALL ANNULLATO: {e}\n"
                 "Nessun file e' stato modificato.")
    print(f"  sharedassets1.assets aggiornato ({len(plan)} categorie)")

    if a.label:
        md = open(meta, "rb").read()
        n = md.count(LABEL_FROM)
        if n != 1:
            print(f"  etichetta: 'Русский' trovata {n} volte, salto "
                  f"(attesa 1; rinomina manuale)")
        else:
            ensure_backup(meta)
            atomic_write(meta, md.replace(LABEL_FROM, LABEL_TO))
            print("  etichetta menu: 'Русский' -> 'Italiano'")

    json.dump({"when": datetime.datetime.now().isoformat(timespec="seconds"),
               "slot": TARGET_LANG, "categories": [c for c, _, _ in plan],
               "label_renamed": bool(a.label),
               "assets_sha": sha(out),
               "base_sha": sha(open(assets + BAK, "rb").read())},
              open(os.path.join(ROOT, "install-manifest.json"), "w"), indent=2)
    print("\nfatto. In gioco: Impostazioni -> Lingua -> "
          f"{'Italiano' if a.label else 'Русский'}")


def cmd_uninstall(a):
    if game_running():
        sys.exit("Dimraeth e' in esecuzione: chiudi il gioco e riprova.")
    assets, meta = paths(a.game)
    motivo = backup_stale(assets)
    if motivo and not a.force:
        sys.exit(NL + "UNINSTALL ANNULLATO." + NL + stale_help(motivo) + NL + NL
                 + "Ripristinare qui il backup vecchio riporterebbe indietro"
                 + NL + "sharedassets1.assets lasciando aggiornato il resto del"
                 + NL + "gioco. Se sai quello che fai: --force.")
    restored = 0
    for p in (assets, meta):
        bak = p + BAK
        if os.path.exists(bak):
            shutil.copy2(bak, p)
            print(f"  ripristinato {os.path.basename(p)}")
            restored += 1
    if not restored:
        print("nessun backup trovato. Usa Steam -> Proprieta' -> "
              "File locali -> Verifica integrita'.")
    mf = os.path.join(ROOT, "install-manifest.json")
    if os.path.exists(mf):
        os.remove(mf)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("status", "install", "uninstall"):
        s = sub.add_parser(name)
        s.add_argument("--game", required=True)
        if name == "install":
            s.add_argument("--it")
            s.add_argument("--label", action="store_true",
                           help="rinomina l'etichetta del menu in 'Italiano'")
            s.add_argument("--dry-run", action="store_true")
        if name == "uninstall":
            s.add_argument("--force", action="store_true",
                           help="ripristina anche se il backup e' obsoleto")
    a = ap.parse_args()
    {"status": cmd_status, "install": cmd_install, "uninstall": cmd_uninstall}[a.cmd](a)


if __name__ == "__main__":
    main()
