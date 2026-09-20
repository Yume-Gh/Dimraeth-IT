# -*- coding: utf-8 -*-
"""Traduzioni indicizzate per CHIAVE del CSV.

Nascono da un problema che i dizionari per testo non possono risolvere: il nome
di un set compare sotto due chiavi con lo STESSO inglese ma ruoli diversi.

    EQUIPMENT_FROSTWARD_NAME  "Frostward"  ->  "Guardia Gelida"
    EQUIPMENT_FROSTWARD_OF    "Frostward"  ->  "della Guardia Gelida"

Il nome completo di una runa non e' una stringa: il gioco lo assembla con
EQUIP_NAME_FORMAT. L'inglese usa "{0} {1} {2}" (affisso, set, base); spagnolo e
portoghese usano entrambi "{2} {0} {3}", cioe' riordinano E usano un quarto slot
che l'inglese non tocca -- la forma genitiva. Due localizzazioni romanze
indipendenti che concordano sono la prova migliore disponibile che quello e'
l'ordine giusto per una lingua come l'italiano.

Di conseguenza gli affissi diventano SOSTANTIVI, come in tedesco e spagnolo
('Sharp' -> "Schaerfe"/"Filo"): con l'ordine riordinato un aggettivo non
concorderebbe con la base, che cambia genere (Runa, Amuleto, Bracciale...).

Collisioni evitate: 'Hearty' non e' "Vigore" (gia' Stamina), 'Swift' non e'
"Velocita" (gia' Movement Speed), 'Slicing' non e' "Taglio" (gia' Strike),
'Charged' non e' "Carica" (gia' Charge).
"""

BY_KEY = {
    # ---- template di assemblaggio del nome --------------------------------
    "EQUIP_NAME_FORMAT": "{2} {0} {3}",
    "EQUIP_NAME_FORMAT_NOPREFIX": "{1} {2}",

    # ---- forma genitiva dei set (slot {3}) --------------------------------
    "EQUIPMENT_AETHERSHADE_OF": "dell'Ombra d'Etere",
    "EQUIPMENT_BLIGHTSEED_OF": "del Seme del Morbo",
    "EQUIPMENT_BRUTALCLAW_OF": "dell'Artiglio Brutale",
    "EQUIPMENT_BULLHEART_OF": "del Cuore di Toro",
    "EQUIPMENT_BURNWARD_OF": "della Guardia Ardente",
    "EQUIPMENT_CHILLHOWL_OF": "dell'Ululato Gelido",
    "EQUIPMENT_CONVERGENCE_OF": "della Convergenza",
    "EQUIPMENT_DAZZLER_OF": "dell'Accecante",
    "EQUIPMENT_DUSKBLOOM_OF": "del Fiore del Crepuscolo",
    "EQUIPMENT_ENFLAMED_OF": "dell'Infiammato",
    "EQUIPMENT_ERUPTING_OF": "dell'Eruttante",
    "EQUIPMENT_FERALBOND_OF": "del Vincolo Ferino",
    "EQUIPMENT_FORESTLINKED_OF": "del Legato alla Foresta",
    "EQUIPMENT_FROSTWARD_OF": "della Guardia Gelida",
    "EQUIPMENT_GLOOMFANG_OF": "della Zanna Tenebrosa",
    "EQUIPMENT_GOBLINCALLER_OF": "dell'Evocatore di Goblin",
    "EQUIPMENT_GOBLINFRIEND_OF": "dell'Amico dei Goblin",
    "EQUIPMENT_GOREHORN_OF": "del Corno Cruento",
    "EQUIPMENT_GRAVEVEIL_OF": "del Velo Sepolcrale",
    "EQUIPMENT_GUSTING_OF": "della Raffica",
    "EQUIPMENT_IRONFIST_OF": "del Pugno di Ferro",
    "EQUIPMENT_LIFEBLOOM_OF": "del Fiore della Vita",
    "EQUIPMENT_LIONSPEAR_OF": "della Lancia del Leone",
    "EQUIPMENT_MOMENTUM_OF": "dello Slancio",
    "EQUIPMENT_MOONTHORN_OF": "della Spina Lunare",
    "EQUIPMENT_PATHWEAVER_OF": "del Tessitore di Sentieri",
    "EQUIPMENT_PITFIGHTER_OF": "del Lottatore da Fossa",
    "EQUIPMENT_PRECISIONFANG_OF": "della Zanna di Precisione",
    "EQUIPMENT_PUTRID_OF": "del Putrido",
    "EQUIPMENT_PYREWEAVER_OF": "del Tessitore di Fiamme",
    "EQUIPMENT_REDSTEEL_OF": "dell'Acciaio Rosso",
    "EQUIPMENT_RIPPING_OF": "dello Squarciante",
    "EQUIPMENT_ROOTBLOOM_OF": "del Fiore di Radici",
    "EQUIPMENT_ROOTBOUND_OF": "del Legato alle Radici",
    "EQUIPMENT_RUMBLER_OF": "del Rombante",
    "EQUIPMENT_SHAKERS_OF": "degli Scuotitori",
    "EQUIPMENT_SHATTERING_OF": "della Frantumazione",
    "EQUIPMENT_SHIELDLINE_OF": "della Linea di Scudi",
    "EQUIPMENT_SPIRITBOUND_OF": "del Legato allo Spirito",
    "EQUIPMENT_STONEHOOVE_OF": "dello Zoccolo di Pietra",
    "EQUIPMENT_SWIFTSTEP_OF": "del Passo Rapido",
    "EQUIPMENT_THORNBORN_OF": "del Nato dalle Spine",
    "EQUIPMENT_TIDESTORM_OF": "della Tempesta di Marea",

    # ---- affissi delle rune come sostantivi (slot {0}) --------------------
    "ATTR_PREFIX_Armor": "Solidità",
    "ATTR_PREFIX_AttackSpeed": "Rapidità",
    "ATTR_PREFIX_BluntDamage": "Fracasso",
    "ATTR_PREFIX_BluntPiercing": "Frattura",
    "ATTR_PREFIX_Concentration": "Focalizzazione",
    "ATTR_PREFIX_ConcentrationRegen": "Meditazione",
    "ATTR_PREFIX_CriticalChance": "Filo",
    "ATTR_PREFIX_CriticalDamage": "Letalità",
    "ATTR_PREFIX_DecayDamage": "Avvizzimento",
    "ATTR_PREFIX_DecayPiercing": "Putrefazione",
    "ATTR_PREFIX_ElectricityDamage": "Folgore",
    "ATTR_PREFIX_ElectricityPiercing": "Scarica",
    "ATTR_PREFIX_Encumbrance": "Leggerezza",
    "ATTR_PREFIX_EtherDamage": "Etere",
    "ATTR_PREFIX_EtherPiercing": "Fase",
    "ATTR_PREFIX_FireDamage": "Fiamma",
    "ATTR_PREFIX_FirePiercing": "Arsura",
    "ATTR_PREFIX_GuardEfficiency": "Fermezza",
    "ATTR_PREFIX_HealingPower": "Restaurazione",
    "ATTR_PREFIX_Health": "Robustezza",
    "ATTR_PREFIX_HealthRegen": "Riparazione",
    "ATTR_PREFIX_IceDamage": "Brina",
    "ATTR_PREFIX_IcePiercing": "Incrinatura",
    "ATTR_PREFIX_MagicPiercing": "Dissoluzione",
    "ATTR_PREFIX_MagicPower": "Misticismo",
    "ATTR_PREFIX_MinionCriticalChance": "Crudeltà",
    "ATTR_PREFIX_MinionDamage": "Comando",
    "ATTR_PREFIX_MinionHealth": "Rinforzo",
    "ATTR_PREFIX_MovementSpeed": "Sveltezza",
    "ATTR_PREFIX_PhysicalPiercing": "Squarcio",
    "ATTR_PREFIX_PhysicalPower": "Ferocia",
    "ATTR_PREFIX_PoisonPiercing": "Tossicità",
    "ATTR_PREFIX_Resistance": "Salvaguardia",
    "ATTR_PREFIX_SpellHaste": "Fretta",
    "ATTR_PREFIX_Stamina": "Tenacia",
    "ATTR_PREFIX_StaminaRegen": "Ristoro",
    "ATTR_PREFIX_StrikeDamage": "Recisione",
    "ATTR_PREFIX_StrikePiercing": "Rottura",
    "ATTR_PREFIX_ThrustDamage": "Trafittura",
    "ATTR_PREFIX_ThrustPiercing": "Scissione",
}
