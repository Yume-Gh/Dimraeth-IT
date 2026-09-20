"""Controlla i CSV italiani contro il sorgente inglese e la capienza dello slot.

    python tools/validate.py
    python tools/validate.py --game "E:/.../Dimraeth"   # aggiunge il test capienza
Uscita 0 se non ci sono errori bloccanti, 1 altrimenti.
"""
import argparse, csv, io, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unityfile as uf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMAT_REORDER = {"EQUIP_NAME_FORMAT", "EQUIP_NAME_FORMAT_NOPREFIX"}
PLACEHOLDER = __import__("re").compile(r"\{\d+(?::[^}]*)?\}")
TAG = __import__("re").compile(r"</?(b|i|u|s|color|size|sprite|link|align|font|mark|nobr)\b[^>]*>",
                               __import__("re").I)


def read_csv(path):
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8-sig")
    rows = list(csv.reader(io.StringIO(txt)))
    if not rows or rows[0][:2] != ["Key", "Text"]:
        raise ValueError("intestazione attesa 'Key,Text'")
    out, dups = {}, []
    for r in rows[1:]:
        if len(r) < 2 or not r[0]:
            continue
        if r[0] in out:
            dups.append(r[0])
        out[r[0]] = r[1]
    return raw, out, dups


def tag_profile(v):
    return collections.Counter(m.group(0).split("=")[0].rstrip(">").lower() + ">"
                               for m in TAG.finditer(v))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=os.path.join(ROOT, "source", "English"))
    ap.add_argument("--it", default=os.path.join(ROOT, "it"))
    ap.add_argument("--game", help="abilita il controllo di capienza dello slot")
    ap.add_argument("--max-untranslated", type=int, default=None)
    ap.add_argument("--no-glossary", action="store_true",
                    help="salta il controllo di coerenza terminologica")
    ap.add_argument("--strict-glossary", action="store_true",
                    help="le incoerenze di glossario diventano errori bloccanti")
    a = ap.parse_args()

    gidx = None
    if not a.no_glossary:
        try:
            from it_terms import PROPOSALS
            import glossary_check as gc
            gidx = gc.build_index(PROPOSALS)
            try:
                from it_ui_labels import OVERRIDES_BY_GROUP as _OV
            except ImportError:
                _OV = {}

            def _override(key, en_term):
                if not key or "_" not in key:
                    return None
                return _OV.get(key.split("_")[1], {}).get(en_term)
            govr = _override
        except ImportError:
            print("glossario non disponibile, controllo terminologico saltato\n")

    cap = {}
    if a.game:
        assets = os.path.join(a.game, "Dimraeth_Data", "sharedassets1.assets")
        import patch as _patch
        picked, probs, _src = _patch.resolve_slots(assets)
        data = b""
        for pb in probs:
            print(f"  slot: {pb}")
        cap = {k: v.size for k, v in picked.items()}
        del data

    errors = warnings = 0
    untranslated_tot = keys_tot = 0
    gloss_data = []
    print(f"{'categoria':13s}{'chiavi':>8s}{'mancanti':>10s}{'extra':>7s}"
          f"{'plchldr':>9s}{'tag':>6s}{'vuote':>7s}{'=EN':>7s}{'byte':>10s}{'slot':>10s}")
    print("-" * 87)
    for cat in uf.CATEGORIES:
        fsrc = os.path.join(a.src, cat + ".csv")
        fit = os.path.join(a.it, cat + ".csv")
        if not os.path.isfile(fsrc):
            print(f"{cat:13s}  sorgente inglese assente -> esegui extract.py"); errors += 1; continue
        if not os.path.isfile(fit):
            print(f"{cat:13s}  it/{cat}.csv assente"); errors += 1; continue
        try:
            _, en, _ = read_csv(fsrc)
            raw, it, dups = read_csv(fit)
        except (ValueError, UnicodeDecodeError) as e:
            print(f"{cat:13s}  CSV illeggibile: {e}"); errors += 1; continue

        missing = [k for k in en if k not in it]
        extra = [k for k in it if k not in en and not k.startswith("_ITPAD_")]
        # Alcune chiavi SONO il formato di assemblaggio di un nome: riordinarle e
        # usare slot che l'inglese non tocca e' lo scopo, non un errore.
        # Spagnolo e portoghese fanno lo stesso con EQUIP_NAME_FORMAT.
        ph = [k for k in en if k in it and k not in FORMAT_REORDER
              and sorted(PLACEHOLDER.findall(en[k])) != sorted(PLACEHOLDER.findall(it[k]))]
        tg = [k for k in en if k in it and tag_profile(en[k]) != tag_profile(it[k])]
        empty = [k for k in it if k in en and en[k].strip() and not it[k].strip()]
        same = [k for k in en if k in it and en[k] == it[k] and en[k].strip()]
        size = len(raw)
        slot = cap.get(cat)
        over = slot is not None and size > slot
        errors += len(missing) > 0
        errors += len(dups) > 0
        errors += len(ph) > 0
        errors += bool(over)
        warnings += (len(tg) > 0) + (len(empty) > 0) + (len(extra) > 0)
        untranslated_tot += len(same); keys_tot += len(en)
        if gidx:
            gloss_data.append((cat, en, it))
        flag = lambda n: f"{n}!" if n else "-"
        print(f"{cat:13s}{len(it):>8d}{flag(len(missing)):>10s}{flag(len(extra)):>7s}"
              f"{flag(len(ph)):>9s}{flag(len(tg)):>6s}{flag(len(empty)):>7s}"
              f"{len(same):>7d}{size:>10d}"
              f"{(str(slot) + ('!' if over else '')) if slot else '-':>10s}")
        for label, items in (("chiavi mancanti", missing), ("chiavi duplicate", dups),
                             ("placeholder non corrispondenti", ph),
                             ("tag di formattazione diversi", tg)):
            if items:
                print(f"     {label} ({len(items)}): {', '.join(items[:6])}"
                      f"{' ...' if len(items) > 6 else ''}")
        if over:
            print(f"     SLOT INSUFFICIENTE: {size}B > {slot}B, servono {size - slot}B in meno")

    print("-" * 87)

    if gidx and gloss_data:
        import glossary_check as gc
        from collections import Counter
        tot_rows = tot_viol = 0
        all_terms = Counter()
        shown = 0
        lines = []
        for cat, en, it in gloss_data:
            rows_, viol, per_term, samples = gc.check_category(
                en, it, gidx, override=govr)
            if viol:
                tot_rows += rows_; tot_viol += viol
                all_terms.update(per_term)
                lines.append((cat, rows_, viol, samples))
        if tot_viol:
            print(f"\nGLOSSARIO: {tot_viol} incoerenze su {tot_rows} righe tradotte")
            for cat, rows_, viol, samples in lines:
                print(f"  {cat:13s} {rows_:5d} righe, {viol:5d} incoerenze")
                for k, en_t, it_t in samples[:2]:
                    print(f"       {k}: atteso '{it_t}' per '{en_t}'")
                    shown += 1
            print(f"\n  termini piu' disattesi:")
            for (en_t, it_t), n in all_terms.most_common(8):
                print(f"    {en_t:24s} -> {it_t:28s} {n:5d} righe")
            if a.strict_glossary:
                errors += 1
            else:
                warnings += 1
        else:
            done = sum(1 for _, en, it in gloss_data
                       for k in en if k in it and it[k] != en[k])
            print(f"\nGLOSSARIO: nessuna incoerenza ({done:,} righe tradotte controllate)")

    pct = 100 * (1 - untranslated_tot / keys_tot) if keys_tot else 0
    print(f"tradotto: {keys_tot - untranslated_tot:,}/{keys_tot:,} chiavi ({pct:.1f}%)"
          f"   -- '=EN' conta i valori identici all'inglese")
    print(f"errori bloccanti: {errors}   avvisi: {warnings}")
    if a.max_untranslated is not None and untranslated_tot > a.max_untranslated:
        print(f"non tradotte {untranslated_tot} > soglia {a.max_untranslated}")
        errors += 1
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
