# -*- coding: utf-8 -*-
"""Adattatore per la traduzione automatica della prosa.

Nessun testo lascia questa macchina se non lo chiedi esplicitamente: il
comportamento predefinito e' l'ESPORTAZIONE su file. Mandare il copione di un
gioco a un servizio di terze parti e' una decisione di chi possiede il progetto,
non dello strumento, quindi l'invio diretto richiede una tua chiave API e il
flag --send.

Flusso:

    python tools/mt.py status
    python tools/mt.py glossary                 # glossario per il motore
    python tools/mt.py export --cat Quests      # work/mt/Quests.tsv
    ...  traduci quel file col motore che preferisci  ...
    python tools/mt.py import --cat Quests --file work/mt/Quests.it.tsv
    python tools/validate.py --game "<dir>"

L'import RIFIUTA le righe che hanno perso un segnaposto o un tag: restano in
inglese e vengono elencate, invece di entrare rotte nel gioco.
"""
import argparse, csv, io, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mt_mask
import batch
import apply_it

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "work", "mt")


def pending(cat):
    """Righe ancora da tradurre: {chiave: testo inglese}."""
    import frames
    from it_terms import PROPOSALS
    tre = frames.build_term_regex(PROPOSALS)
    by_text, ov = apply_it.load_dicts()
    FRAMES = {}
    for m, a in (("it_skills_frames", "FRAMES"), ("it_item_frames", "FRAMES_ITEMS"),
                 ("it_attributes", "ATTR_FRAMES")):
        try:
            FRAMES.update(getattr(__import__(m), a))
        except (ImportError, AttributeError):
            pass
    trans, _ = batch.translatable(cat)
    _h, rows = batch.load_it(cat)
    it = {r[0]: r[1] for r in rows if len(r) >= 2}
    out = {}
    for k, v in trans.items():
        if apply_it.lookup(k, v, by_text, ov) is not None:
            continue
        if frames.decompose(v, tre)[0] in FRAMES:
            continue
        if it.get(k) != v:
            continue                      # gia' tradotta a mano
        out[k] = v
    return out


def cmd_status(a):
    tot_rows = tot_chars = 0
    print(f"{'categoria':14s}{'righe':>8s}{'caratteri':>11s}")
    print("-" * 33)
    for cat in batch.uf.CATEGORIES:
        try:
            p = pending(cat)
        except FileNotFoundError:
            continue
        if not p:
            continue
        c = sum(len(v) for v in p.values())
        tot_rows += len(p)
        tot_chars += c
        print(f"{cat:14s}{len(p):>8d}{c:>11,d}")
    print("-" * 33)
    print(f"{'TOTALE':14s}{tot_rows:>8d}{tot_chars:>11,d}")
    print(f"{NL}I caratteri sono la base di calcolo dei motori a consumo.")


NL = chr(10)


def cmd_glossary(a):
    """Glossario nel formato TSV che DeepL e simili accettano (una coppia per riga)."""
    from it_terms import PROPOSALS
    os.makedirs(WORK, exist_ok=True)
    p = os.path.join(WORK, "glossary.tsv")
    n = 0
    with open(p, "w", encoding="utf-8", newline="") as f:
        for en, (it, status, _note) in sorted(PROPOSALS.items()):
            if status not in ("OK", "KEEP") or not it.strip():
                continue
            # al motore va UNA resa: la prima, che e' quella canonica
            f.write(f"{en}\t{it.split('|')[0].strip()}{NL}")
            n += 1
    print(f"{n} coppie -> {os.path.relpath(p, ROOT)}")
    print("Caricalo nel motore come glossario EN->IT: impone la terminologia")
    print("gia' fissata, invece di lasciarla reinventare a ogni riga.")


def cmd_reference(a):
    """Riferimento terminologico COMPLETO: glossario + tutti i nomi gia' tradotti.

    Il glossario per i motori contiene solo i termini di meccanica. Chi traduce
    la prosa ha bisogno anche dei nomi propri gia' fissati -- luoghi, oggetti,
    set, creature, abilita' -- altrimenti il testo nuovo divergera' da quello
    che il giocatore ha gia' davanti.
    """
    from it_terms import PROPOSALS
    os.makedirs(WORK, exist_ok=True)
    pairs = {}
    for en, (it, status, _n) in PROPOSALS.items():
        if status in ("OK", "KEEP") and it.strip():
            pairs[en] = it.split("|")[0].strip()
    by_text, _ov = apply_it.load_dicts()
    for en, it in by_text.items():
        pairs.setdefault(en, it)
    p = os.path.join(WORK, "reference.tsv")
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write("English	Italiano" + NL)
        for en in sorted(pairs, key=lambda x: x.lower()):
            if len(en) > 60:
                continue                  # frasi intere: non sono terminologia
            f.write(f"{en}	{pairs[en]}" + NL)
    print(f"{sum(1 for e in pairs if len(e) <= 60)} coppie -> "
          f"{os.path.relpath(p, ROOT)}")


def cmd_export(a):
    """Esporta una o piu' categorie in UN file.

    Un file solo evita a chi traduce otto passaggi separati, e le chiavi sono
    gia' univoche fra categorie. La mappa chiave->categoria viaggia a parte,
    cosi' l'import sa in quale CSV rimettere ogni riga.
    """
    import collections
    os.makedirs(WORK, exist_ok=True)
    cats = [c.strip() for c in a.cat.split(",") if c.strip()]
    name = a.name or (cats[0] if len(cats) == 1 else "batch")
    p, owner = {}, {}
    for c in cats:
        for k, v in pending(c).items():
            p[k] = v
            owner[k] = c
    if a.min_len:
        p = {k: v for k, v in p.items() if len(v) >= a.min_len}
    if a.match:
        # Serve per i dialoghi: si esporta un personaggio alla volta, cosi' le
        # quattro varianti di tono di ogni battuta restano nello stesso lotto e
        # la voce del personaggio non cambia da un file all'altro.
        import re
        rx = re.compile(a.match)
        p = {k: v for k, v in p.items() if rx.search(k)}
    keys = sorted(p)
    if a.limit:
        keys = keys[:a.limit]
    src = os.path.join(WORK, f"{name}.tsv")
    tok = os.path.join(WORK, f"{name}.tokens.json")
    cmap = os.path.join(WORK, f"{name}.cats.json")
    tokens = {}
    with open(src, "w", encoding="utf-8", newline="") as f:
        for k in keys:
            masked, t = mt_mask.mask(p[k])
            tokens[k] = t
            # il TSV vuole una riga per record: i ritorni a capo veri non esistono
            # in questi CSV, ma tabulazioni impreviste romperebbero il formato
            f.write(k + "\t" + masked.replace("\t", " ") + NL)
    json.dump(tokens, open(tok, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump({k: owner[k] for k in keys}, open(cmap, "w", encoding="utf-8"),
              ensure_ascii=False)
    chars = sum(len(p[k]) for k in keys)
    per = collections.Counter(owner[k] for k in keys)
    for c in cats:
        print(f"   {c:14s} {per.get(c, 0):5d} righe")
    print(f"{len(keys)} righe, {chars:,} caratteri -> {os.path.relpath(src, ROOT)}")
    print(f"{NL}Traduci la SECONDA colonna lasciando intatti i segnaposto <x1/>.")
    print("Con DeepL: tag_handling=xml, cosi' li tratta come tag e non li traduce.")


def _import_multi(a, tok, cmap):
    """Import di un file che contiene piu' categorie insieme.

    Le righe si raggruppano per categoria e ogni it/<cat>.csv viene riscritto
    una volta sola. Una riga che ha perso un segnaposto viene rifiutata come
    sempre: resta in inglese e finisce nell'elenco.
    """
    import collections
    tokens = json.load(open(tok, encoding="utf-8"))
    owner = json.load(open(cmap, encoding="utf-8"))
    trans, rejected, unknown, problems = {}, 0, 0, []
    with open(a.file, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip(NL).rstrip(chr(13))
            if not line or "\t" not in line:
                continue
            k, _sep, tr = line.partition("\t")
            if k not in tokens or k not in owner:
                unknown += 1
                continue
            try:
                trans[k] = mt_mask.unmask(tr, tokens[k])
            except ValueError as e:
                rejected += 1
                if len(problems) < 10:
                    problems.append((k, str(e)))
    applied = collections.Counter()
    for cat in sorted(set(owner.values())):
        header, rows = batch.load_it(cat)
        touched = False
        for r in rows:
            if len(r) >= 2 and r[0] in trans and owner.get(r[0]) == cat:
                r[1] = trans[r[0]]
                applied[cat] += 1
                touched = True
        if touched:
            p = os.path.join(ROOT, "it", cat + ".csv")
            with open(p, "w", encoding="utf-8-sig", newline="") as f:
                w = csv.writer(f, lineterminator="\r\n")
                w.writerow(header)
                w.writerows(rows)
    for cat in sorted(applied):
        print(f"   {cat:14s} {applied[cat]:5d} righe importate")
    print(f"totale {sum(applied.values())} importate, {rejected} rifiutate"
          + (f", {unknown} chiavi sconosciute" if unknown else ""))
    for k, why in problems:
        print(f"   RIFIUTATA {k}: {why}")


def cmd_import(a):
    tok = os.path.join(WORK, f"{a.cat}.tokens.json")
    cmap = os.path.join(WORK, f"{a.cat}.cats.json")
    if os.path.isfile(cmap):
        return _import_multi(a, tok, cmap)
    if not os.path.isfile(tok):
        sys.exit(f"token mancanti: {tok}. Rifai l'export.")
    tokens = json.load(open(tok, encoding="utf-8"))
    header, rows = batch.load_it(a.cat)
    byk = {r[0]: r for r in rows if r}

    applied = rejected = unknown = 0
    problems = []
    with open(a.file, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip(NL).rstrip(chr(13))
            if not line or "\t" not in line:
                continue
            k, _sep, tr = line.partition("\t")
            if k not in tokens or k not in byk:
                unknown += 1
                continue
            try:
                restored = mt_mask.unmask(tr, tokens[k])
            except ValueError as e:
                rejected += 1
                if len(problems) < 8:
                    problems.append((k, str(e)))
                continue
            if len(byk[k]) >= 2:
                byk[k][1] = restored
                applied += 1

    p = os.path.join(ROOT, "it", a.cat + ".csv")
    with open(p, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        w.writerows(rows)
    print(f"{a.cat}: {applied} righe importate, {rejected} rifiutate"
          + (f", {unknown} chiavi sconosciute" if unknown else ""))
    for k, why in problems:
        print(f"   RIFIUTATA {k}: {why}")
    if rejected:
        print(f"{NL}Le righe rifiutate restano in inglese. Ritradurle a mano,"
              " oppure rilanciarle al motore con i tag protetti.")
    print(f"{NL}Ora: python tools/validate.py --game \"<cartella del gioco>\"")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    sub.add_parser("glossary")
    sub.add_parser("reference")
    e = sub.add_parser("export")
    e.add_argument("--cat", required=True)
    e.add_argument("--limit", type=int)
    e.add_argument("--name", help="nome del file di uscita quando le categorie sono piu' d'una")
    e.add_argument("--match", help="regex sulla CHIAVE: esporta solo le righe che corrispondono")
    e.add_argument("--min-len", type=int, default=0)
    i = sub.add_parser("import")
    i.add_argument("--cat", required=True)
    i.add_argument("--file", required=True)
    a = ap.parse_args()
    {"status": cmd_status, "glossary": cmd_glossary,
     "reference": cmd_reference,
     "export": cmd_export, "import": cmd_import}[a.cmd](a)


if __name__ == "__main__":
    main()
