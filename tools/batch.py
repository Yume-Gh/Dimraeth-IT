# -*- coding: utf-8 -*-
"""Lavora la traduzione a lotti: esporta un sottoinsieme, poi lo reintegra.

Tradurre 20.376 chiavi in un colpo non e' praticabile ne' verificabile. Questo
strumento ritaglia lotti piccoli e rivedibili, e li rifonde in it/ quando sono pronti.

    # esporta le chiavi ancora da tradurre di un gruppo
    python tools/batch.py export --cat UI --name chrome --small-groups 3 --max-len 40
    python tools/batch.py export --cat UI --name menu --groups MAINMENU,SETTINGSSCREEN

    # dopo aver compilato la colonna Italian
    python tools/batch.py merge --file work/UI-chrome.csv

    python tools/batch.py list          # stato dei lotti
"""
import argparse, csv, io, os, re, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unityfile as uf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "work")
REFS = ["German", "Spanish", "Portuguese"]
NOTEXT = re.compile(r"^[\W\d_]*$")


def load(lang, cat):
    p = os.path.join(ROOT, "source", lang, cat + ".csv")
    if not os.path.isfile(p):
        return {}
    t = open(p, "rb").read().decode("utf-8-sig")
    return {r[0]: r[1] for r in csv.reader(io.StringIO(t))
            if len(r) >= 2 and r[0] and r[0] != "Key"}


def load_it(cat):
    p = os.path.join(ROOT, "it", cat + ".csv")
    t = open(p, "rb").read().decode("utf-8-sig")
    rows = list(csv.reader(io.StringIO(t)))
    return rows[0], rows[1:]


def group_of(key):
    p = key.split("_")
    return p[1] if len(p) > 1 else "(none)"


def translatable(cat):
    """Chiavi che richiedono davvero una traduzione.

    Esclude i valori senza testo (cifre, simboli) e quelli che tutte le lingue
    ufficiali hanno lasciato identici all'inglese: sono passanti per definizione.
    """
    en = load("English", cat)
    refs = [load(r, cat) for r in REFS]
    out = {}
    for k, v in en.items():
        if NOTEXT.match(v):
            continue
        pres = [r[k] for r in refs if k in r]
        if pres and all(x.strip() == v.strip() for x in pres):
            continue
        out[k] = v
    return out, refs


def cmd_export(a):
    os.makedirs(WORK, exist_ok=True)
    trans, refs = translatable(a.cat)
    _, it_rows = load_it(a.cat)
    it_map = {r[0]: r[1] for r in it_rows if len(r) >= 2}

    counts = collections.Counter(group_of(k) for k in trans)
    wanted = set(g.strip().upper() for g in a.groups.split(",")) if a.groups else set()

    sel = {}
    for k, v in trans.items():
        if it_map.get(k, "") != v:
            continue                      # gia' tradotta: fuori dal lotto
        g = group_of(k)
        ok = False
        if wanted and g.upper() in wanted:
            ok = True
        if a.small_groups and counts[g] <= a.small_groups:
            ok = True
        if not wanted and not a.small_groups:
            ok = True
        if ok and (a.max_len is None or len(v) <= a.max_len):
            sel[k] = v

    if not sel:
        print("nessuna chiave corrisponde ai filtri")
        return
    path = os.path.join(WORK, f"{a.cat}-{a.name}.csv")
    ref_maps = dict(zip(REFS, refs))
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(["Key", "English", "Italian"] + REFS)
        for k in sorted(sel):
            w.writerow([k, sel[k], ""] + [ref_maps[r].get(k, "") for r in REFS])
    print(f"{len(sel)} chiavi -> work/{os.path.basename(path)}")
    print(f"caratteri inglesi: {sum(len(v) for v in sel.values()):,}")
    gc = collections.Counter(group_of(k) for k in sel)
    print(f"gruppi nel lotto: {len(gc)}")


def cmd_merge(a):
    t = open(a.file, "rb").read().decode("utf-8-sig")
    rows = list(csv.reader(io.StringIO(t)))
    hdr = rows[0]
    i_k, i_it = hdr.index("Key"), hdr.index("Italian")
    new = {r[i_k]: r[i_it] for r in rows[1:]
           if len(r) > i_it and r[i_k] and r[i_it].strip()}
    if not new:
        sys.exit("la colonna Italian e' vuota: niente da reintegrare")

    cat = os.path.basename(a.file).split("-")[0]
    p = os.path.join(ROOT, "it", cat + ".csv")
    header, it_rows = load_it(cat)
    applied = skipped = 0
    for r in it_rows:
        if len(r) >= 2 and r[0] in new:
            r[1] = new[r[0]]
            applied += 1
    with open(p, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        w.writerows(it_rows)
    missing = set(new) - {r[0] for r in it_rows if r}
    print(f"it/{cat}.csv: {applied} chiavi aggiornate")
    if missing:
        print(f"  {len(missing)} chiavi del lotto non esistono in it/{cat}.csv: "
              f"{sorted(missing)[:5]}")


def cmd_list(a):
    for cat in uf.CATEGORIES:
        trans, _ = translatable(cat)
        try:
            _, it_rows = load_it(cat)
        except FileNotFoundError:
            continue
        it_map = {r[0]: r[1] for r in it_rows if len(r) >= 2}
        done = sum(1 for k, v in trans.items() if it_map.get(k, "") != v)
        if trans:
            bar = "#" * int(20 * done / len(trans))
            print(f"  {cat:13s} {done:5d}/{len(trans):5d}  "
                  f"{100*done/len(trans):5.1f}%  {bar}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("export")
    e.add_argument("--cat", required=True)
    e.add_argument("--name", required=True)
    e.add_argument("--groups", help="gruppi UI_<X>_ separati da virgola")
    e.add_argument("--small-groups", type=int,
                   help="includi i gruppi con al massimo N chiavi")
    e.add_argument("--max-len", type=int)
    m = sub.add_parser("merge")
    m.add_argument("--file", required=True)
    sub.add_parser("list")
    a = ap.parse_args()
    {"export": cmd_export, "merge": cmd_merge, "list": cmd_list}[a.cmd](a)


if __name__ == "__main__":
    main()
