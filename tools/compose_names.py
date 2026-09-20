# -*- coding: utf-8 -*-
"""Risoluzione composizionale dei nomi di oggetto.

I 371 nomi di Items non sono 371 traduzioni: sono ~90 basi piu' tre schemi che si
ripetono.

    Lesser Health Potion +3          -> base + suffisso di grado
    Recipe Lesser Health Potion      -> prefisso "Recipe"
    Spellbook Erupt                  -> prefisso "Spellbook"

Il risolutore spoglia lo schema, traduce quel che resta consultando TUTTI i
dizionari (quindi riusa i nomi di costruzione gia' tradotti in it_places) e
ricompone in italiano. Ricorsivo: "Recipe Lesser Health Potion" spoglia il
prefisso e poi risolve la base.

Chi non risolve resta scoperto e appare nel conteggio: nessun ripiego silenzioso
che produrrebbe meta' inglese senza farlo notare.
"""
import re

# prefissi: (regex, template italiano con {0} = resto tradotto)
PREFIXES = [
    (re.compile(r"^Recipe\s+(.+)$"), "Ricetta: {0}"),
    (re.compile(r"^Spellbook\s+(.+)$"), "Libro degli incantesimi: {0}"),
]

# suffissi: (regex, template con {0} = base tradotta, {1} = parte catturata)
SUFFIXES = [
    (re.compile(r"^(.+?)\s*\+(\d+)$"), "{0} +{1}"),
]


def resolve(name, lookup_direct, depth=0):
    """Traduzione di un nome, o None se nessuno schema porta a una base nota.

    'lookup_direct' e' una funzione nome -> traduzione o None.
    """
    if depth > 4:
        return None
    direct = lookup_direct(name)
    if direct is not None:
        return direct
    for rx, tpl in SUFFIXES:
        m = rx.match(name)
        if m:
            base = resolve(m.group(1), lookup_direct, depth + 1)
            if base is not None:
                return tpl.format(base, m.group(2))
    for rx, tpl in PREFIXES:
        m = rx.match(name)
        if m:
            rest = resolve(m.group(1), lookup_direct, depth + 1)
            if rest is not None:
                return tpl.format(rest)
    return None
