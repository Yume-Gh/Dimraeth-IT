# -*- coding: utf-8 -*-
"""Morfologia italiana per la traduzione per modelli.

Il metodo delle cornici funziona in inglese perche' "your X" non cambia forma.
In italiano l'articolo e il possessivo concordano col genere del termine che
finisce nello slot: "il tuo Vigore" ma "la tua Velocita' d'attacco". Senza
questo dato le cornici producono frasi sgrammaticate.

Il genere si deduce dalla desinenza, che in italiano e' molto regolare; le
eccezioni (soprattutto i nomi in -e, ambigui) sono elencate a mano.

Serve inoltre la forma AGGETTIVALE PLURALE per le frasi "against X enemies":
"contro i nemici ustionati", non "contro i nemici Ustione".
"""

# nomi la cui desinenza non rivela il genere, o lo rivela male
GENDER_EXCEPTIONS = {
    "Etere": "m", "Gelo": "m", "Vigore": "m", "Potere": "m", "Danno": "m",
    "Taglio": "m", "Stordimento": "m", "Sanguinamento": "m", "Veleno": "m",
    "Decadimento": "m", "Fuoco": "m", "Ghiaccio": "m", "Vuoto": "m",
    "Bonus": "m", "Round": "m", "Ingombro": "m", "Nutrimento": "m",
    "Assalto": "m", "Contagio": "m", "Innesco": "m", "Clone": "m",
    "Eco": "f", "Ustione": "f", "Scossa": "f", "Furia": "f", "Salute": "f",
    "Resistenza": "f", "Armatura": "f", "Concentrazione": "f", "Durata": "f",
    "Penetrazione": "f", "Perforazione": "f", "Fenditura": "f", "Onda": "f",
    "Ondata": "f", "Carica": "f", "Cariche": "f", "Frenesia": "f",
    "Mutilazione": "f", "Convergenza": "f", "Corruzione": "f", "Pressione": "f",
    "Interruzione": "f", "Rigenerazione": "f", "Epidemia": "f",
    "Inoculazione": "f", "Danza": "f", "Grandine": "f", "Scivolata": "f",
}

# forma aggettivale plurale maschile, per "contro i nemici ..."
ADJ_PLURAL = {
    "Ustione": "ustionati",
    "Sanguinamento": "sanguinanti",
    "Veleno": "avvelenati",
    "Avvelenato": "avvelenati",
    "Gelo": "assiderati",
    "Assiderato": "assiderati",
    "Stordimento": "storditi",
    "Stordito": "storditi",
    "Furia": "infuriati",
    "Scossa": "folgorati",
    "Lacerato": "lacerati",
    "Decadimento": "in decadimento",
}


def gender(it_term):
    """'m' o 'f' per un termine italiano. Desinenza, con eccezioni esplicite."""
    t = it_term.strip()
    if t in GENDER_EXCEPTIONS:
        return GENDER_EXCEPTIONS[t]
    head = t.split()[0] if t.split() else t
    if head in GENDER_EXCEPTIONS:
        return GENDER_EXCEPTIONS[head]
    low = head.lower().rstrip(":%")
    if low.endswith(("zione", "sione", "tà", "tü", "ità", "udine", "igine")):
        return "f"
    if low.endswith("a"):
        return "f"
    if low.endswith(("o", "i")):
        return "m"
    return "m"                      # ripiego: il maschile e' il default italiano


def article(it_term, definite=True):
    """Articolo concordato. Non gestisce l'elisione: nelle cornici l'articolo
    precede sempre il possessivo ('il tuo', 'la tua'), dove non serve."""
    g = gender(it_term)
    if definite:
        return "il" if g == "m" else "la"
    return "un" if g == "m" else "una"


def possessive(it_term, person="tuo"):
    """'tuo'/'tua' concordato col termine."""
    return person if gender(it_term) == "m" else person[:-1] + "a"


def adj_plural(it_term):
    """Forma aggettivale plurale, o None se non dichiarata."""
    t = it_term.strip()
    return ADJ_PLURAL.get(t) or ADJ_PLURAL.get(t.split()[0] if t.split() else t)


def slots_for(terms_it):
    """Slot morfologici derivati, da unire a {t0..} e {n0..} nella cornice.

    Per ogni termine produce {art0} {poss0} {adj0}, cosi' una cornice italiana
    puo' scrivere "Aumenta {art0} {poss0} {t0} di {n0}" e concordare da sola.
    """
    out = {}
    for i, t in enumerate(terms_it):
        g = gender(t)
        out[f"art{i}"] = article(t)
        out[f"poss{i}"] = possessive(t)
        # articolo con elisione, per quando non c'e' il possessivo in mezzo:
        # "l'Accumulo", non "il Accumulo"
        out[f"artE{i}"] = ("l'" if t[:1].lower() in "aeiou"
                           else ("il " if g == "m" else "la "))
        out[f"di{i}"] = "del" if g == "m" else "della"
        out[f"tutto{i}"] = "tutto" if g == "m" else "tutta"
        out[f"mass{i}"] = "massimo" if g == "m" else "massima"
        # desinenza per far concordare un participio scritto nella cornice:
        # "{t0} Focalizzat{g0}" -> "Uncino Focalizzato" / "Danza Focalizzata"
        out[f"g{i}"] = "o" if g == "m" else "a"
        out[f"gp{i}"] = "i" if g == "m" else "e"
        # {adj} e' il PLURALE AGGETTIVALE ("nemici ustionati"); {low} e' il
        # semplice minuscolo. Tenerli distinti evita l'errore che ha prodotto
        # "Aumento del potere assiderati" per "Chill Power Increase".
        out[f"low{i}"] = t.lower()
        adj = adj_plural(t)
        out[f"adj{i}"] = adj if adj else t.lower()
    return out
