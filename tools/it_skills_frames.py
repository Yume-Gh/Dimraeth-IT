# -*- coding: utf-8 -*-
"""Cornici italiane per le descrizioni di Skills.

Chiave: cornice inglese prodotta da frames.decompose. Valore: cornice italiana.
Gli slot {t0..} sono i termini del glossario, {n0..} i numeri. Gli slot derivati
li fornisce morph: {art0} {artE0} {poss0} {di0} {tutto0} {mass0} {adj0}.

Dove l'accordo sarebbe fragile ho preferito una costruzione invariante: "il valore
massimo di {t0}" invece di "{t0} massim-o/a". Costa una parola in più e non puo'
sbagliare genere, che su 2.496 righe generate automaticamente conta piu' dell'eleganza.
"""

FRAMES = {
    # --- le sei cornici che da sole coprono un terzo delle descrizioni ------
    "Increase your {t0} by {n0}":
        "Aumenta {art0} {poss0} {t0} di {n0}",
    "Increase your {t0} by {n0}.":
        "Aumenta {art0} {poss0} {t0} di {n0}.",
    "Increase your {t0} against {t1} enemies by {n0}":
        "Aumenta {art0} {poss0} {t0} contro i nemici {adj1} di {n0}",
    "Increase the maximum {t0} you can apply by {n0}.":
        "Aumenta di {n0} il valore massimo di {t0} applicabile.",
    "Increase the duration of your {t0} by {n0} second.":
        "Aumenta di {n0} secondo la durata {di0} {poss0} {t0}.",
    "Increase the duration of your {t0} by {n0} seconds.":
        "Aumenta di {n0} secondi la durata {di0} {poss0} {t0}.",
    "Increase {t0}-up by {n0}":
        "Aumenta {artE0}{t0} di {n0}",
    "Increase all {t0} by {n0}":
        "Aumenta di {n0} {tutto0} {art0} {t0}",

    # --- massimi e valori limite -------------------------------------------
    "Increase your max {t0} by {n0}.":
        "Aumenta di {n0} il valore massimo di {t0}.",
    "Increase your max {t0} by {n0}":
        "Aumenta di {n0} il valore massimo di {t0}",
    "Increase your maximum {t0} by {n0}.":
        "Aumenta di {n0} il valore massimo di {t0}.",
    "Increase the maximum {t0} you can hold by {n0}.":
        "Aumenta di {n0} il valore massimo di {t0} che puoi mantenere.",
    "Increase the maximum {t0} you can gain by {n0}.":
        "Aumenta di {n0} il valore massimo di {t0} ottenibile.",
    "Increase the maximum {t0} consumed by {n0} per point.":
        "Aumenta di {n0} per punto il valore massimo di {t0} consumato.",

    # --- danno contro stati alterati ---------------------------------------
    "Increase your damage vs. {t0} enemies by {n0}":
        "Aumenta di {n0} il tuo danno contro i nemici {adj0}",
    "Increase your damage against {t0} enemies by {n0}.":
        "Aumenta di {n0} il tuo danno contro i nemici {adj0}.",
    "Increase your damage against enemies below {n0} {t0} by {n1}.":
        "Aumenta di {n1} il tuo danno contro i nemici sotto {n0} di {t0}.",

    # --- danno di abilita' specifiche --------------------------------------
    "Increase the Damage of your {t0} by {n0}":
        "Aumenta di {n0} il danno {di0} {poss0} {t0}",
    "Increase the damage of your {t0} by {n0}":
        "Aumenta di {n0} il danno {di0} {poss0} {t0}",
    "Increase the damage of {t0} by {n0} per point.":
        "Aumenta di {n0} per punto il danno di {t0}.",
    "Increase {t0}'s damage by {n0} per point.":
        "Aumenta di {n0} per punto il danno di {t0}.",
    "Increase the damage dealt by {t0} by {n0}.":
        "Aumenta di {n0} il danno inflitto da {t0}.",
    "Increase the {t0} dealt by {t1} by {n0} per point.":
        "Aumenta di {n0} per punto il valore di {t0} inflitto da {t1}.",

    # --- tempi di recupero -------------------------------------------------
    "Decrease the cooldown of {t0} by {n0} per point.":
        "Riduce di {n0} per punto il tempo di recupero di {t0}.",
    "Reduce the cooldown of {t0} by {n0} per point.":
        "Riduce di {n0} per punto il tempo di recupero di {t0}.",

    # --- varie -------------------------------------------------------------
    "Increase your {t0} gain on hit by {n0}.":
        "Aumenta di {n0} il recupero di {t0} al colpo.",
    "Increase the slowing power of your {t0} by {n0}":
        "Aumenta di {n0} il potere rallentante {di0} {poss0} {t0}",
}

# ---------------------------------------------------------------------------
# Secondo lotto. Qui gli slot {t1} {t2} sono prefisso-di-ramo + abilita':
# l'inglese dice "Rending Strike", l'italiano "Fendente Lacerante". Le cornici
# invertono l'ordine ({t2} {t1}), cosa possibile perche' gli slot sono numerati.
# ---------------------------------------------------------------------------
FRAMES.update({
    "Increase the {t0} applied by {t1} {t2} by {n0} per point.":
        "Aumenta di {n0} per punto il valore di {t0} applicato da {t2} {t1}.",
    "Increase the additional {t0} applied by {t1} {t2} by {n0} per point.":
        "Aumenta di {n0} per punto il valore aggiuntivo di {t0} applicato da {t2} {t1}.",
    "Increase the {t0} gained by {t1} {t2} by {n0} per point.":
        "Aumenta di {n0} per punto il valore di {t0} ottenuto da {t2} {t1}.",
    "Increase the maximum {t0} consumed by {t1} {t2} by {n0} per point.":
        "Aumenta di {n0} per punto il valore massimo di {t0} consumato da {t2} {t1}.",
    "Increase the max {t0} consumed by {t1} {t2} by {n0} per point.":
        "Aumenta di {n0} per punto il valore massimo di {t0} consumato da {t2} {t1}.",
    "Increase the maximum {t0} consumed and {t1} applied by {t2} {t3} by {n0} per point.":
        "Aumenta di {n0} per punto il valore massimo di {t0} consumato e di {t1} "
        "applicato da {t3} {t2}.",
    "Increase the {t0}-up of {t1} by {n0} per point.":
        "Aumenta di {n0} per punto {artE0}{t0} di {t1}.",

    # rapporti di conversione fra risorse
    "Improve {t0} {t1}'s {t2}-to-{t3} conversion ratio by {n0} step per point.":
        "Migliora di {n0} passo per punto il rapporto di conversione da {t2} a {t3} "
        "di {t1} {t0}.",
    "Improve {t0} {t1}'s {t2} to {t3} conversion ratio by {n0} step per point.":
        "Migliora di {n0} passo per punto il rapporto di conversione da {t2} a {t3} "
        "di {t1} {t0}.",

    # costi e recuperi
    "Reduce the {t0} cost of {t1} by {n0} per point.":
        "Riduce di {n0} per punto il costo in {t0} di {t1}.",
    "Reduce the {t0} and {t1} cost of {t2} by {n0} per point.":
        "Riduce di {n0} per punto il costo in {t0} e {t1} di {t2}.",
    "Reduce the cooldown of {t0}'s {t1} by {n0} per point.":
        "Riduce di {n0} per punto il tempo di recupero di {t1} ({t0}).",

    # bonus condizionati
    "Increase your {t0} by {n0} against enemies who are under {n1} {t1}.":
        "Aumenta {art0} {poss0} {t0} di {n0} contro i nemici sotto {n1} di {t1}.",
    "Increase the bonus damage gained from {t0} consumed beyond the first {n0} by {n1} per point.":
        "Aumenta di {n1} per punto il danno bonus ottenuto da ogni {t0} consumato "
        "oltre i primi {n0}.",
    "Increase the damage gained per {t0} consumed by {n0} per point and the maximum damage increase by {n1} per point.":
        "Aumenta di {n0} per punto il danno ottenuto per ogni {t0} consumato e di {n1} "
        "per punto l'aumento massimo di danno.",

    # cornici a due effetti: nel CSV la barra-n e' letterale e va conservata
    "Increase your {t0} by {n0} \\n Increase your {t1} by {n1}.":
        "Aumenta {art0} {poss0} {t0} di {n0} \\n Aumenta {art1} {poss1} {t1} di {n1}.",
    "Increase your {t0} by {n0} \\n Increase your {t1} against {t2} enemies by {n1}":
        "Aumenta {art0} {poss0} {t0} di {n0} \\n Aumenta {art1} {poss1} {t1} contro "
        "i nemici {adj2} di {n1}",
    "Increase your {t0} by {n0} \\n Increase the maximum {t1} you can apply by {n1}.":
        "Aumenta {art0} {poss0} {t0} di {n0} \\n Aumenta di {n1} il valore massimo "
        "di {t1} applicabile.",
    "Increase your {t0} by {n0}. \\n Increase the maximum {t1} you can apply by {n1}.":
        "Aumenta {art0} {poss0} {t0} di {n0}. \\n Aumenta di {n1} il valore massimo "
        "di {t1} applicabile.",
    "Increase the maximum {t0} you can apply by {n0}. \\n Increase your {t1} by {n1}":
        "Aumenta di {n0} il valore massimo di {t0} applicabile. \\n Aumenta {art1} "
        "{poss1} {t1} di {n1}",
    "Increase your {t0} by {n0} \\n Increase the duration of your {t1} by {n1} seconds.":
        "Aumenta {art0} {poss0} {t0} di {n0} \\n Aumenta di {n1} secondi la durata "
        "{di1} {poss1} {t1}.",
    "Increase your {t0} by {n0} \\n Increase {t1}-up by {n1}":
        "Aumenta {art0} {poss0} {t0} di {n0} \\n Aumenta {artE1}{t1} di {n1}",
})

# ---------------------------------------------------------------------------
# Righe compatte di Spells: "<tipo di danno>: (SIGLA:valore)".
# Le sigle sono codici di scalatura (PB contundente, MF fuoco, ...). Verificato
# su 294 confronti: tedesco, spagnolo e portoghese le lasciano TUTTE invariate
# e traducono solo l'etichetta. Quindi la cornice le riporta identiche.
# ---------------------------------------------------------------------------
SCALING_CODES = ("PB", "PS", "PT", "PX", "MF", "MA", "MD", "MI", "ME", "MH", "MU")
for _c in SCALING_CODES:
    FRAMES["{t0}: (%s:{n0})" % _c] = "{t0}: (%s:{n0})" % _c

FRAMES.update({
    # il valore e' interamente un termine di glossario
    "{t0}": "{t0}",
    "{t0}: {n0}": "{t0}: {n0}",

    # Passives: contributi degli attributi
    "Adventure provides an additional {n0} {t0}":
        "L'avventura fornisce {n0} {t0} in più",
    "Strength provides an additional {n0} {t0}":
        "La forza fornisce {n0} {t0} in più",
})

# ---------------------------------------------------------------------------
# Nomi dei nodi dell'albero delle abilita'.
#
# Due inversioni sistematiche rispetto all'inglese:
#   "Attack Speed Increase" -> "Aumento di Velocita' d'attacco"  (testa a sinistra)
#   "Rending Hook"          -> "Uncino Lacerante"                (aggettivo a destra)
# La seconda e' possibile perche' gli slot sono numerati: la cornice scrive {t1} {t0}.
#
# Dove la cornice contiene un participio uso {g0}, la desinenza concordata col
# genere dello slot, invece di fissare il maschile.
# ---------------------------------------------------------------------------
FRAMES.update({
    "{t0} Increase": "Aumento di {t0}",
    "Max {t0} Increase": "Aumento di {t0} max",
    "{t0} Boost": "Potenziamento di {t0}",
    "{t0} on Hit": "{t0} al colpo",
    "{t0}-up Increase": "Aumento di {artE0}{t0}",
    "Attack Damage Increase": "Aumento del danno d'attacco",

    # prefisso di ramo + abilita': l'italiano inverte l'ordine
    "{t0} {t1}": "{t1} {t0}",
    "{t0} {t1} Increase": "Aumento di {t1} {t0}",
    "{t0} {t1} Increase I": "Aumento di {t1} {t0} I",
    "{t0} {t1} Increase II": "Aumento di {t1} {t0} II",
    "{t0} {t1} Increase III": "Aumento di {t1} {t0} III",

    # danno contro stati alterati: serve la forma aggettivale plurale
    "{t0} vs. {t1}": "{t0} vs. {adj1}",
    "Damage vs. {t0}": "Danno vs. {adj0}",
    "Increased Damage vs. {t0}": "Danno aumentato vs. {adj0}",
    "Damage % vs. below {n0} {t0}": "Danno % vs. sotto {n0} di {t0}",

    # danno per tipo
    "{t0} Damage Increase": "Aumento del danno da {t0}",
    "{t0} Damage Increase I": "Aumento del danno da {t0} I",
    "{t0} Damage Increase II": "Aumento del danno da {t0} II",
    "{t0} Damage Increase III": "Aumento del danno da {t0} III",
    "Critical {t0} Chance Increase": "Aumento della probabilità di critico da {t0}",

    # riduzioni: {t1} resta generico, non do per scontato che sia il recupero
    "{t0} {t1} Reduction I": "Riduzione {di1} {t1} di {t0} I",
    "{t0} {t1} Reduction II": "Riduzione {di1} {t1} di {t0} II",
    "{t0} {t1} Reduction III": "Riduzione {di1} {t1} di {t0} III",
    "{t0} {t1} Decrease I": "Riduzione {di1} {t1} di {t0} I",
    "{t0} {t1} Decrease II": "Riduzione {di1} {t1} di {t0} II",
    "{t0} {t1} Decrease III": "Riduzione {di1} {t1} di {t0} III",
    "{t0} Cost Reduction I": "Riduzione del costo in {t0} I",
    "{t0} Cost Reduction II": "Riduzione del costo in {t0} II",
    "{t0} Cost Reduction III": "Riduzione del costo in {t0} III",

    # participi: desinenza concordata
    "Focused {t0}": "{t0} Focalizzat{g0}",
    "Inoculated {t0}": "{t0} Inoculat{g0}",
    "Inoculated {t0} Increase I": "Aumento di {t0} Inoculat{g0} I",
    "Inoculated {t0} Increase II": "Aumento di {t0} Inoculat{g0} II",
    "Inoculated {t0} Increase III": "Aumento di {t0} Inoculat{g0} III",
    "Repeating {t0}": "{t0} Ripetut{g0}",
    "{t0} Arrow Increase I": "Aumento di Freccia {t0} I",
    "{t0} Arrow Increase II": "Aumento di Freccia {t0} II",
    "{t0} Arrow Increase III": "Aumento di Freccia {t0} III",
})
