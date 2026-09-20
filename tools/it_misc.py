# -*- coding: utf-8 -*-
"""Voci di dizionario non legate alla UI.

Qui finiscono i nomi che una cornice non puo' generare in modo sicuro. Il caso
che ha aperto questo file: "<X> Power Increase" ha due strutture diverse in
inglese -- "Physical Power" e' aggettivo + nome ("potere fisico"), "Chill Power"
e' nome + nome ("potere del gelo"). Una cornice unica produce per forza un errore
su una delle due, quindi queste righe si traducono a mano.
"""

M = {
    "Physical Power Increase": "Aumento del potere fisico",
    "Magic Power Increase": "Aumento del potere magico",
    "Chill Power Increase": "Aumento del potere del gelo",
}
