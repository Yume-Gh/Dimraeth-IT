"""Applica le proposte di tools/it_terms.py al glossario e riporta i buchi.

    python tools/apply_terms.py
Aggiunge a glossary/terms.csv le colonne Italian, Status, Note.
In glossary/names.csv precompila Italian per le voci KEEP (restano in inglese).
"""
import csv, io, os, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from it_terms import PROPOSALS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = os.path.join(ROOT, "glossary")


def read(path):
    txt = open(path, "rb").read().decode("utf-8-sig")
    r = csv.reader(io.StringIO(txt))
    return next(r), list(r)


def write(path, header, rows):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# ---------------- terms.csv ----------------
p = os.path.join(G, "terms.csv")
header, rows = read(p)
for col in ("Italian", "Status", "Note"):
    if col not in header:
        header.append(col)
i_term, i_it = header.index("Term"), header.index("Italian")
i_st, i_note = header.index("Status"), header.index("Note")
width = len(header)

stats, gaps = collections.Counter(), []
for row in rows:
    row += [""] * (width - len(row))
    term = row[i_term]
    if term in PROPOSALS:
        it, st, note = PROPOSALS[term]
        row[i_it], row[i_st], row[i_note] = it, st, note
        stats[st] += 1
    else:
        row[i_st] = "TODO"
        stats["TODO"] += 1
        gaps.append(term)
write(p, header, rows)

# ---------------- names.csv: KEEP = resta l'inglese ----------------
pn = os.path.join(G, "names.csv")
hn, rn = read(pn)
j_en, j_vd, j_it = hn.index("English"), hn.index("Verdict"), hn.index("Italian")
prefilled = 0
for row in rn:
    row += [""] * (len(hn) - len(row))
    if row[j_vd] == "KEEP" and not row[j_it]:
        row[j_it] = row[j_en]
        prefilled += 1
write(pn, hn, rn)

# ---------------- rapporto ----------------
tot = sum(stats.values())
print(f"glossary/terms.csv  {tot} termini")
for k, label in (("OK", "proposta pronta"), ("KEEP", "nome proprio, invariato"),
                 ("REVIEW", "da vedere in gioco"), ("DROP", "falso positivo"),
                 ("TODO", "senza proposta")):
    if stats[k]:
        print(f"  {k:7s} {stats[k]:4d}  {label}")
usable = stats["OK"] + stats["KEEP"]
print(f"\n  applicabili subito: {usable}/{tot} ({100*usable/tot:.0f}%)")
print(f"  da decidere in gioco: {stats['REVIEW'] + stats['TODO']}")
print(f"  scartabili senza pensarci: {stats['DROP']}")
if gaps:
    print(f"\ntermini senza proposta ({len(gaps)}): {', '.join(gaps[:25])}"
          f"{' ...' if len(gaps) > 25 else ''}")
print(f"\nglossary/names.csv  {prefilled} voci KEEP precompilate con l'inglese")
