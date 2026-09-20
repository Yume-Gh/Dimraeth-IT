"""Costruisce il glossario deducendolo dalle traduzioni gia' presenti nel gioco.

Le chiavi *_NAME danno un allineamento perfetto fra lingue: stesso identificatore,
stessa entita'. Confrontando il valore di ogni lingua con l'inglese si capisce se i
localizzatori ufficiali hanno TRADOTTO il termine o l'hanno LASCIATO in inglese, che
e' la decisione di policy piu' importante da prendere prima di iniziare.

    python tools/glossary.py
Produce glossary/names.csv e glossary/terms.csv con una colonna IT da compilare.
"""
import argparse, csv, io, os, re, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unityfile as uf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = ["German", "Spanish", "Portuguese"]

# sequenza di parole capitalizzate non a inizio frase: candidato termine di gioco
TERM = re.compile(r"(?<![.!?\"'\n]\s)(?<!^)\b([A-Z][a-z]{2,}(?:\s+(?:of\s+)?[A-Z][a-z]{2,})*)\b")
STOP = {
    "The", "You", "Your", "This", "That", "There", "They", "When", "While", "With",
    "And", "But", "For", "Not", "All", "One", "Two", "New", "Now", "Then", "Only",
    "If", "It", "Its", "Was", "Were", "Has", "Have", "Had", "Can", "Will", "Would",
    "Press", "Hold", "Click", "Select", "Use", "Yes", "No", "None", "Level", "Max",
}


def load(lang, cat):
    p = os.path.join(ROOT, "source", lang, cat + ".csv")
    if not os.path.isfile(p):
        return {}
    txt = open(p, "rb").read().decode("utf-8-sig")
    return {r[0]: r[1] for r in csv.reader(io.StringIO(txt))
            if len(r) >= 2 and r[0] and r[0] != "Key"}


def verdict(en, others):
    """KEEP se tutte le lingue hanno lasciato l'inglese, TRANSLATE se nessuna."""
    present = [v for v in others if v]
    if not present:
        return "?", 0
    kept = sum(1 for v in present if v.strip() == en.strip())
    if kept == len(present):
        return "KEEP", kept
    if kept == 0:
        return "TRANSLATE", 0
    return "MIXED", kept


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "glossary"))
    ap.add_argument("--min-freq", type=int, default=8)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    en_all, ref_all = {}, {r: {} for r in REFS}
    for cat in uf.CATEGORIES:
        for k, v in load("English", cat).items():
            en_all[k] = (cat, v)
        for r in REFS:
            ref_all[r].update(load(r, cat))

    missing = [r for r in REFS if not ref_all[r]]
    if missing:
        print(f"lingue di riferimento assenti in source/: {missing}")
        print("  esegui: python tools/extract.py --game <dir> --lang " + " ".join(missing))

    # ---- nomi di entita' ----------------------------------------------------
    name_rows, stats = [], collections.Counter()
    by_cat = collections.defaultdict(collections.Counter)
    for k, (cat, en) in sorted(en_all.items()):
        if not k.endswith("_NAME") or not en.strip():
            continue
        others = [ref_all[r].get(k, "") for r in REFS]
        vd, kept = verdict(en, others)
        stats[vd] += 1
        by_cat[cat][vd] += 1
        name_rows.append([k, cat, en] + others + [vd, kept, ""])

    p_names = os.path.join(a.out, "names.csv")
    with open(p_names, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Key", "Category", "English"] + REFS + ["Verdict", "KeptBy", "Italian"])
        w.writerows(name_rows)

    # ---- termini ricorrenti nel corpo del testo -----------------------------
    freq = collections.Counter()
    for k, (cat, en) in en_all.items():
        if k.endswith("_NAME") or len(en) < 25:
            continue
        for m in TERM.finditer(en):
            t = m.group(1)
            if t.split()[0] in STOP or len(t) < 4:
                continue
            freq[t] += 1

    # rendering noto: se il termine e' anche il valore di una chiave *_NAME
    name_index = {}
    for row in name_rows:
        name_index.setdefault(row[2].strip(), row)

    term_rows = []
    for t, n in freq.most_common():
        if n < a.min_freq:
            continue
        ref = name_index.get(t)
        if ref:
            term_rows.append([t, n, "si"] + ref[3:6] + [ref[6], ""])
        else:
            term_rows.append([t, n, "no", "", "", "", "", ""])

    p_terms = os.path.join(a.out, "terms.csv")
    with open(p_terms, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Term", "Occurrences", "HasNameKey"] + REFS + ["Verdict", "Italian"])
        w.writerows(term_rows)

    # ---- rapporto -----------------------------------------------------------
    tot = sum(stats.values())
    print(f"\nglossary/names.csv : {len(name_rows):,} nomi di entita'")
    print(f"glossary/terms.csv : {len(term_rows):,} termini ricorrenti "
          f"(soglia {a.min_freq} occorrenze)")
    print(f"\npolicy usata dai localizzatori ufficiali su {tot:,} nomi:")
    for vd in ("TRANSLATE", "KEEP", "MIXED", "?"):
        if stats[vd]:
            print(f"  {vd:10s} {stats[vd]:5d}  {100*stats[vd]/tot:5.1f}%")
    print("\n  TRANSLATE = DE, ES e PT lo hanno tradotto -> traducilo")
    print("  KEEP      = tutte lo hanno lasciato in inglese -> lascialo")
    print("  MIXED     = disaccordo fra lingue -> decisione tua")
    print(f"\nper categoria:")
    print(f"  {'categoria':13s}{'tradotti':>10s}{'tenuti':>8s}{'misti':>7s}")
    for cat in uf.CATEGORIES:
        c = by_cat[cat]
        if sum(c.values()):
            print(f"  {cat:13s}{c['TRANSLATE']:>10d}{c['KEEP']:>8d}{c['MIXED']:>7d}")
    nmixed = len([r for r in term_rows if r[6] == "MIXED"])
    print(f"\nda decidere per primi: i {stats['MIXED']} nomi MIXED in names.csv "
          f"e i {len([r for r in term_rows if r[2]=='no'])} termini di terms.csv "
          f"senza chiave *_NAME.")


if __name__ == "__main__":
    main()
