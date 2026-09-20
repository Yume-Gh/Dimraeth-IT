# -*- coding: utf-8 -*-
"""Verifica che le traduzioni rispettino il glossario concordato.

Il problema pratico: 20.376 chiavi si traducono in lotti, distanti nel tempo,
magari da persone diverse. Senza un controllo automatico la terminologia divaga --
'Waygate' diventa 'Varco' in una categoria e 'Portale' in un'altra, e il giocatore
se ne accorge.

Quattro cose che i lotti precedenti hanno insegnato, tutte implementate qui:

1. Confronto per RADICE, non per forma esatta: l'italiano flette, quindi 'Cariche'
   deve poter comparire come 'carica'. Cerca la negligenza, non la morfologia.

2. Rese ALTERNATIVE dichiarate con '|': 'Sanguinamento|sanguinante' copre sia il
   sostantivo sia l'aggettivo ("bersagli sanguinanti"), e i termini a doppio
   significato che il controllo, non vedendo la schermata, non puo' distinguere.

3. Gli ESCAPE LETTERALI vanno neutralizzati: nei CSV la sequenza barra-n sono due
   caratteri, non un ritorno a capo, e incollano le parole vanificando i confini.

4. La TOKENIZZAZIONE deve coincidere con quella del generatore di cornici: un
   unico regex alternato, leftmost-longest, letto da sinistra a destra.
"""
import re

VOWELS = "aeiouàèéìòùAEIOU"
# parole funzione italiane: non portano informazione terminologica
FUNCTION_WORDS = {
    "di", "da", "del", "dello", "della", "dei", "degli", "delle", "dal", "dalla",
    "al", "alla", "allo", "ai", "agli", "alle", "il", "lo", "la", "le", "i", "gli",
    "un", "uno", "una", "e", "in", "con", "su", "per", "a", "the", "of", "d",
}
MIN_STEM = 4
WB = chr(92) + "b"          # confine di parola, costruito senza escape ambigui


def unescape_spans(text):
    """Sostituisce gli escape letterali con spazi, conservando le posizioni.

    "...cards" + barra + "nBetting Rounds" incolla le due parole e il confine di
    parola non scatta piu'. Due caratteri diventano due spazi, quindi gli offset
    restano identici.
    """
    for esc in (chr(92) + "n", chr(92) + "t", chr(92) + "r"):
        text = text.replace(esc, "  ")
    return text


def stem(word):
    """Radice approssimata: toglie le vocali finali, che portano la flessione."""
    w = word.lower().strip("'’")
    while len(w) > MIN_STEM and w[-1] in VOWELS:
        w = w[:-1]
    return w


def stems_of(phrase):
    """Radici significative di una resa italiana attesa."""
    out = []
    for tok in re.split(r"[\s'’/()-]+", phrase):
        tok = re.sub(r"[^\wÀ-ÿ]", "", tok)
        if not tok or tok.lower() in FUNCTION_WORDS:
            continue
        s = stem(tok)
        if len(s) >= MIN_STEM:
            out.append(s)
    return out


class Index:
    """Termini del glossario piu' un regex combinato per la scansione.

    Cercando un termine alla volta in ordine di lunghezza si sbaglia il parsing:
    in "Wave Strike Damage Increase" la lettura giusta e' [Wave Strike][Damage
    Increase], ma 'Strike Damage' e' piu' lungo di 'Wave Strike' e aggancia a
    cavallo del confine fra i due costituenti. Un'unica alternanza ordinata dal
    piu' lungo da' il leftmost-longest e allinea il controllo al generatore.
    """

    def __init__(self, rows):
        self.rows = rows
        self.by_term = {r[0]: r for r in rows}
        self.rx = (re.compile(WB + "(" + "|".join(re.escape(r[0]) for r in rows)
                              + ")" + WB) if rows else None)

    def __iter__(self):
        return iter(self.rows)

    def __len__(self):
        return len(self.rows)


DROPPED = []


def build_index(proposals):
    """Indice dei termini controllabili."""
    rows = []
    for en, (it, status, _note) in proposals.items():
        if status not in ("OK", "KEEP", "REVIEW") or not it.strip():
            continue
        alts = [a.strip() for a in it.split("|") if a.strip()]
        sts = []
        for a in alts:
            st = stems_of(a)
            if st:
                sts.append(st)
            else:
                # Una variante troppo corta produce zero radici e sparirebbe in
                # silenzio, lasciando credere che il termine sia coperto.
                DROPPED.append((en, a))
        if not sts:
            continue                   # resa troppo corta per un controllo utile
        rows.append((en, alts[0], sts, None))
    rows.sort(key=lambda r: -len(r[0]))
    return Index(rows)


def check_value(en_text, it_text, index, key=None, override=None):
    """Violazioni in una riga: termini presenti in inglese e assenti in italiano.

    'override' e' una funzione (key, termine) -> resa attesa alternativa, per i
    termini il cui significato dipende dalla schermata ('Straight' e' "Diretto"
    fra i nomi di attacco e "Scala" al tavolo da poker).
    """
    if not en_text or not it_text or index.rx is None:
        return []
    en_text = unescape_spans(en_text)
    it_low = unescape_spans(it_text.lower())
    out = []
    for m in index.rx.finditer(en_text):
        row = index.by_term.get(m.group(1))
        if row is None:
            continue
        en_term, it, sts, _p = row
        exp_it, exp_sts = it, sts
        if override is not None:
            alt = override(key, en_term)
            if alt:
                st = stems_of(alt)
                if st:
                    exp_it, exp_sts = alt, [st]
        # basta che UNA delle rese accettabili sia presente per intero
        if exp_sts and not any(all(s in it_low for s in st) for st in exp_sts):
            out.append((en_term, exp_it))
    return out


def check_category(en_map, it_map, index, sample=4, override=None):
    """Ritorna (righe_con_violazioni, violazioni, conteggio_per_termine, esempi)."""
    from collections import Counter
    per_term = Counter()
    rows = total = 0
    samples = []
    for k, en in en_map.items():
        it = it_map.get(k)
        if it is None or it == en:
            continue                   # non tradotta: non e' un errore di glossario
        v = check_value(en, it, index, key=k, override=override)
        if v:
            rows += 1
            total += len(v)
            for en_t, it_t in v:
                per_term[(en_t, it_t)] += 1
            if len(samples) < sample:
                samples.append((k, v[0][0], v[0][1]))
    return rows, total, per_term, samples
