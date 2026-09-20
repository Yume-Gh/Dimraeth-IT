# -*- coding: utf-8 -*-
"""Traduzione per modelli: scompone una riga in cornice + slot, traduce la cornice.

Le descrizioni delle abilita' non sono prosa: sono frasi a stampo. Lo schema
"Increase your <termine> by <numero>" copre da solo 409 righe. Tradurre 222 cornici
copre l'80% delle 2.496 descrizioni, perche' i termini negli slot sono gia' nel
glossario. Il resto va tradotto a mano: la coda lunga e' dove sta la prosa vera.

Una cornice usa slot numerati, non segnaposto anonimi, cosi' l'italiano puo'
riordinarli quando la sintassi lo richiede:

    EN  "Increase your {t0} by {n0}"
    IT  "Aumenta il tuo {t0} di {n0}"
"""
import re, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

NUM = re.compile(r"\d+(?:\.\d+)?%?")


# Voci di glossario che in queste frasi sono VERBI, non sostantivi.
# 'Increase' vale "Aumento" come etichetta di statistica, ma in
# "Increase your X by Y" e' l'imperativo "Aumenta". Se finisse in uno
# slot uscirebbe "Aumento your X": resta dentro la cornice, dove il
# verbo si coniuga correttamente.
VERB_LIKE = {"Increase", "Damage", "Charge"}


def build_term_regex(proposals, exclude=VERB_LIKE):
    """Regex dei termini del glossario, dal piu' lungo al piu' corto.

    L'ordine e' obbligatorio: senza di esso 'Attack Speed' verrebbe spezzato in
    'Speed', e lo slot conterrebbe il termine sbagliato.
    """
    terms = [k for k, (it, st, _n) in proposals.items()
             # REVIEW significa "da confermare in gioco", non "senza resa":
             # le proposte esistono, quindi entrano negli slot. Cambiare la voce
             # di glossario rigenera tutte le righe che la usano.
             if st in ("OK", "KEEP", "REVIEW") and it.strip()
             and k not in exclude]
    terms.sort(key=len, reverse=True)
    return re.compile(r"\b(" + "|".join(re.escape(t) for t in terms) + r")\b")


def decompose(text, term_re):
    """text -> (cornice, termini, numeri). La cornice usa {t0..} e {n0..}.

    Una sola passata con un regex combinato. Due passate non funzionano: la
    seconda rilegge gli slot prodotti dalla prima, e il regex dei numeri
    trasforma "{t0}" in "{t{n0}}" mangiandosi l'indice.
    """
    terms, nums = [], []
    combined = re.compile("(?P<term>" + term_re.pattern + ")|(?P<num>"
                          + NUM.pattern + ")")

    def take(m):
        if m.group("term") is not None:
            terms.append(m.group("term"))
            return "{t%d}" % (len(terms) - 1)
        nums.append(m.group("num"))
        return "{n%d}" % (len(nums) - 1)

    return combined.sub(take, text), terms, nums


def compose(frame_it, terms_it, nums):
    """Riempie una cornice italiana, articoli e accordi inclusi.

    Oltre a {t0..} e {n0..} mette a disposizione gli slot derivati di morph:
    {art0} {artE0} {poss0} {di0} {tutto0} {mass0} {adj0}. Cosi' la cornice
    dichiara l'accordo e non deve conoscere il genere del termine.
    """
    import morph
    try:
        return frame_it.format(**{f"t{i}": v for i, v in enumerate(terms_it)},
                               **{f"n{i}": v for i, v in enumerate(nums)},
                               **morph.slots_for(terms_it))
    except (KeyError, IndexError) as e:
        raise ValueError(f"slot mancante in {frame_it!r}: {e}")


def term_it(en_term, proposals):
    """Resa italiana di un termine, prendendo la prima delle alternative."""
    it = proposals[en_term][0]
    return it.split("|")[0].strip()


def translate(text, frames_it, proposals, term_re):
    """Traduzione per modello, oppure None se la cornice non e' registrata."""
    frame, terms, nums = decompose(text, term_re)
    frame_it = frames_it.get(frame)
    if frame_it is None:
        return None
    return compose(frame_it, [term_it(t, proposals) for t in terms], nums)


def survey(values, term_re, frames_it=None):
    """Statistiche di copertura: quante righe e quanti caratteri coprono le cornici."""
    import collections
    cnt = collections.Counter()
    chars = collections.Counter()
    for v in values:
        f, _t, _n = decompose(v, term_re)
        cnt[f] += 1
        chars[f] += len(v)
    done = sum(n for f, n in cnt.items() if frames_it and f in frames_it)
    return cnt, chars, done
