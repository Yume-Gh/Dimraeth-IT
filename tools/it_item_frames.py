# -*- coding: utf-8 -*-
"""Cornici per le descrizioni dei consumabili (Items).

Le sequenze \\n nelle chiavi sono DUE caratteri veri (barra + n), come nei CSV:
scriverle come ritorno a capo reale fa fallire silenziosamente la corrispondenza.
E' l'errore che ha tenuto fuori sette cornici di Skills senza dare alcun avviso.
"""

FRAMES_ITEMS = {
    "None": "Nessuno",

    "Restores {n0} {t0} over {n1} seconds.\\n {t1} can be refilled by resting.":
        "Ripristina {n0} di {t0} in {n1} secondi.\\n {t1} si ricarica riposando.",

    "Throw to restore {n0} ally {t0} over {n1} seconds.\\n {t1} can be refilled by resting.":
        "Lancialo per ripristinare {n0} di {t0} a un alleato in {n1} secondi.\\n "
        "{t1} si ricarica riposando.",

    "Cures {t0}.\\n {t1} can be refilled by resting.":
        "Cura {t0}.\\n {t1} si ricarica riposando.",

    "Use to gain {n0} {t0}.\\n {t1} can be refilled by resting.":
        "Usalo per ottenere {n0} di {t0}.\\n {t1} si ricarica riposando.",

    "Your attacks deal {n0} of their damage as {t0} for {n1} seconds.\\n {t1} can be refilled by resting.":
        "I tuoi attacchi infliggono {n0} del loro danno come {t0} per {n1} secondi.\\n "
        "{t1} si ricarica riposando.",

    "{t0} Potion +{n0}": "Pozione di {t0} +{n0}",
}
