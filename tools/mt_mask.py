# -*- coding: utf-8 -*-
"""Mascheratura di segnaposto e tag prima di passare il testo a un motore.

Un traduttore automatico tratta "{0}" e "<color=#FFDA00>" come parole: li
traduce, li riordina, a volte li rompe. E la sequenza barra-n dei CSV, che e'
due caratteri veri, diventa facilmente uno spazio o sparisce.

Qui ogni elemento non traducibile viene sostituito da un segnaposto XML
"<x1/>", che i motori seri (DeepL con tag_handling=xml, o qualsiasi flusso
XLIFF) lasciano intatto e puo' riordinare senza danno. Al rientro si
ricostruisce, e se anche un solo token manca la riga viene RIFIUTATA: meglio
una riga non tradotta che una riga con l'interfaccia rotta.
"""
import re

# ordine importante: prima i tag piu' lunghi, poi i segnaposto, poi gli escape
PATTERNS = [
    re.compile(r"</?[a-zA-Z][^<>]*?>"),        # tag TextMeshPro: <b> <color=..> </i>
    re.compile(r"\{\d+(?::[^}]*)?\}"),          # segnaposto {0} {1:F1}
    re.compile(re.escape(chr(92)) + r"[nrt]"),  # escape letterali: barra + n/r/t
]


def mask(text):
    """text -> (testo mascherato, lista dei frammenti originali)."""
    tokens = []

    def take(m):
        tokens.append(m.group(0))
        return "<x%d/>" % len(tokens)

    out = text
    for pat in PATTERNS:
        out = pat.sub(take, out)
    return out, tokens


TOKEN = re.compile(r"<x(\d+)\s*/>")


def unmask(masked, tokens):
    """Ricostruisce il testo. Solleva ValueError se un token manca o e' inventato.

    Il rifiuto e' voluto: una riga che ha perso un <color> o un {0} manda a
    schermo markup grezzo o un buco al posto di un numero.
    """
    seen = set()

    def put(m):
        i = int(m.group(1))
        if not (1 <= i <= len(tokens)):
            raise ValueError(f"token <x{i}/> inesistente")
        seen.add(i)
        return tokens[i - 1]

    out = TOKEN.sub(put, masked)
    missing = set(range(1, len(tokens) + 1)) - seen
    if missing:
        raise ValueError(f"token persi dal motore: {sorted(missing)}")
    return out


def check_roundtrip(text):
    """Vero se mascherare e ricostruire restituisce l'originale."""
    m, t = mask(text)
    try:
        return unmask(m, t) == text
    except ValueError:
        return False
