# -*- coding: utf-8 -*-
"""Applicatore unico dei dizionari italiani a una categoria.

Tre problemi che i primi due lotti hanno fatto emergere, risolti qui in un posto solo:

1. Spazi significativi. Nel CSV esistono "Pet " e " (Best to Least)": lo spazio
   serve alla spaziatura del layout e va conservato, ma la ricerca nel dizionario
   deve avvenire sul testo ripulito, altrimenti ogni variante va inserita a mano.

2. Traduzioni identiche per scelta. "Mana", "Tab", "Treant" restano tali in italiano.
   Confrontare italiano e inglese per misurare l'avanzamento le conta per sempre
   come non tradotte: lo stato va dedotto dalla presenza nel dizionario, non
   dalla differenza fra i due valori.

3. Significati dipendenti dalla schermata: gli override per gruppo vincono su tutto.
"""
import csv, io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_dicts():
    """Dizionari disponibili, dal piu' specifico al piu' generico."""
    by_text = {}
    for mod, attr in (("it_ui_chrome", "T"), ("it_ui_labels", "L"),
                      ("it_ui_rest", "R"), ("it_misc", "M"),
                      ("it_system", "S"),
                      ("it_equipment", "EQ"),
                      ("it_places", "PLACES"),
                      ("it_items", "ITEMS"),
                      ("it_attributes", "ATTR"),
                      ("it_spells", "SPELLS"),
                      ("it_builditems", "BUILD")):
        try:
            m = __import__(mod)
            by_text.update(getattr(m, attr))
        except ImportError:
            pass
    try:
        from it_ui_labels import OVERRIDES_BY_GROUP as ov
    except ImportError:
        ov = {}
    return by_text, ov


def load_by_key():
    """Dizionari indicizzati per CHIAVE del CSV, non per testo inglese.

    Servono quando due chiavi condividono lo stesso inglese ma vogliono italiano
    diverso: EQUIPMENT_FROSTWARD_NAME e' "Guardia Gelida", mentre
    EQUIPMENT_FROSTWARD_OF e' la forma genitiva "della Guardia Gelida".
    """
    out = {}
    for mod, attr in (("it_bykey", "BY_KEY"),):
        try:
            out.update(getattr(__import__(mod), attr))
        except (ImportError, AttributeError):
            pass
    return out


def split_pad(v):
    """Separa gli spazi di bordo dal testo: ('  x ') -> ('  ', 'x', ' ')."""
    core = v.strip()
    if not core:
        return "", v, ""
    lead = v[:len(v) - len(v.lstrip())]
    trail = v[len(v.rstrip()):]
    return lead, core, trail


def lookup(key, en, by_text, overrides):
    """Resa italiana per una riga, conservando gli spazi di bordo dell'originale.

    Se nessun dizionario ha il nome per intero, prova la composizione: i gradi
    "+1".."+5" e i prefissi "Recipe"/"Spellbook" si spogliano e si ricompongono
    dalla base. Cosi' 90 basi coprono 371 nomi di oggetto.
    """
    bykey = load_by_key()
    if key in bykey:
        lead, _core, trail = split_pad(en)
        return lead + bykey[key] + trail
    grp = key.split("_")[1] if key and "_" in key else ""
    lead, core, trail = split_pad(en)
    ov = overrides.get(grp, {})
    it = ov.get(core) or ov.get(en) or by_text.get(core) or by_text.get(en)
    if it is None:
        import compose_names
        it = compose_names.resolve(
            core, lambda n: ov.get(n) or by_text.get(n))
    if it is None:
        return None
    return lead + it + trail


def apply_to(cat, by_text=None, overrides=None, verbose=True):
    """Compila it/<cat>.csv per ogni chiave coperta dai dizionari. Ritorna (applicate, restanti)."""
    if by_text is None:
        by_text, overrides = load_dicts()
    import batch
    trans, _ = batch.translatable(cat)
    en = {}
    src = os.path.join(ROOT, "source", "English", cat + ".csv")
    for r in csv.reader(io.StringIO(open(src, "rb").read().decode("utf-8-sig"))):
        if len(r) >= 2 and r[0] and r[0] != "Key":
            en[r[0]] = r[1]
    header, rows = batch.load_it(cat)

    # Le chiavi con override esplicito passano comunque: translatable() scarta i
    # valori fatti solo di segnaposto, ma EQUIP_NAME_FORMAT ("{0} {1} {2}") e'
    # proprio una di quelle -- ed e' la stringa che riordina il nome degli oggetti.
    forced = set(load_by_key())
    applied = 0
    for r in rows:
        if len(r) < 2 or (r[0] not in trans and r[0] not in forced):
            continue
        it = lookup(r[0], en.get(r[0], ""), by_text, overrides)
        if it is not None and r[1] != it:
            r[1] = it
            applied += 1
    p = os.path.join(ROOT, "it", cat + ".csv")
    with open(p, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        w.writerows(rows)

    remaining = {k: v for k, v in trans.items()
                 if lookup(k, v, by_text, overrides) is None}
    if verbose:
        print(f"{cat}: {applied} righe scritte, "
              f"{len(trans) - len(remaining)}/{len(trans)} coperte dal dizionario, "
              f"{len(remaining)} da tradurre")
    return applied, remaining


def coverage(cat, by_text=None, overrides=None):
    """Chiavi coperte, dai dizionari OPPURE dalle cornici.

    Contare solo i dizionari sottostima il lavoro fatto: le righe generate per
    modello non compaiono in nessun dizionario per testo, quindi risultavano
    scoperte pur essendo tradotte.
    """
    if by_text is None:
        by_text, overrides = load_dicts()
    import batch, frames
    from it_terms import PROPOSALS
    FRAMES = {}
    for _m, _a in (("it_skills_frames", "FRAMES"),
                   ("it_item_frames", "FRAMES_ITEMS"),
                   ("it_attributes", "ATTR_FRAMES")):
        try:
            FRAMES.update(getattr(__import__(_m), _a))
        except ImportError:
            pass
    tre = frames.build_term_regex(PROPOSALS)
    trans, _ = batch.translatable(cat)
    # Terza fonte: le righe gia' diverse dall'inglese in it/. Sono quelle
    # tradotte a mano o importate da un traduttore esterno, che non compaiono
    # ne' nei dizionari ne' nelle cornici e risultavano invisibili al conteggio.
    try:
        _h, rows = batch.load_it(cat)
        itmap = {r[0]: r[1] for r in rows if len(r) >= 2}
    except FileNotFoundError:
        itmap = {}
    done = 0
    for k, v in trans.items():
        if lookup(k, v, by_text, overrides) is not None:
            done += 1
            continue
        if FRAMES:
            f, _t, _n = frames.decompose(v, tre)
            if f in FRAMES:
                done += 1
                continue
        if itmap.get(k, v) != v:
            done += 1
    return done, len(trans)


if __name__ == "__main__":
    import batch
    cats = sys.argv[1:] or batch.uf.CATEGORIES
    tot_d = tot_n = 0
    for c in cats:
        try:
            d, n = coverage(c)
        except FileNotFoundError:
            continue
        tot_d += d
        tot_n += n
        if n:
            bar = "#" * int(20 * d / n)
            print(f"  {c:13s} {d:5d}/{n:5d}  {100*d/n:5.1f}%  {bar}")
    if tot_n:
        print(f"  {'TOTALE':13s} {tot_d:5d}/{tot_n:5d}  {100*tot_d/tot_n:5.1f}%")


def apply_frames(cat, verbose=True):
    """Genera per modelli le righe di una categoria e le scrive in it/<cat>.csv.

    Complementare a apply_to: quella copre i testi presenti nei dizionari per
    corrispondenza esatta, questa genera le frasi a stampo dalle cornici.
    """
    import batch, frames
    from it_terms import PROPOSALS
    FRAMES = {}
    for _m, _a in (("it_skills_frames", "FRAMES"),
                   ("it_item_frames", "FRAMES_ITEMS"),
                   ("it_attributes", "ATTR_FRAMES")):
        try:
            FRAMES.update(getattr(__import__(_m), _a))
        except ImportError:
            pass
    tre = frames.build_term_regex(PROPOSALS)

    en = {}
    src = os.path.join(ROOT, "source", "English", cat + ".csv")
    for r in csv.reader(io.StringIO(open(src, "rb").read().decode("utf-8-sig"))):
        if len(r) >= 2 and r[0] and r[0] != "Key":
            en[r[0]] = r[1]
    trans, _ = batch.translatable(cat)
    header, rows = batch.load_it(cat)

    written = failed = 0
    for r in rows:
        if len(r) < 2 or r[0] not in trans:
            continue
        v = en.get(r[0], "")
        if r[1] != v:
            continue                       # gia' tradotta: non la tocco
        frame, terms, nums = frames.decompose(v, tre)
        fit = FRAMES.get(frame)
        if not fit:
            continue
        try:
            r[1] = frames.compose(
                fit, [frames.term_it(x, PROPOSALS) for x in terms], nums)
            written += 1
        except Exception:
            failed += 1
    with open(os.path.join(ROOT, "it", cat + ".csv"), "w",
              encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        w.writerows(rows)
    if verbose:
        print(f"{cat}: {written} righe generate per modello"
              + (f", {failed} fallite" if failed else ""))
    return written, failed
