# -*- coding: utf-8 -*-
"""Nomi dell'equipaggiamento: set e gradi.

Le lingue ufficiali rendono questi nomi compositivamente, nessuna li lascia in
inglese (verificato: zero invariati su 189). Qui li rendo come composti italiani
originali, tenendo lo stesso registro del resto del glossario.

I 41 nomi di set compaiono due volte nel CSV, sotto le chiavi *_NAME e *_OF:
una traduzione copre entrambe le righe.

Due collisioni evitate di proposito:
  'Ripping' -> "Squarciante", non "Lacerante", che nel glossario e' gia' 'Rending'.
  'Gusting' -> "Raffica", coerente con lo spagnolo, per non sovrapporsi a 'Surging'.
"""

EQ = {
    # ---- nomi dei set ------------------------------------------------------
    "Aethershade": "Ombra d'Etere",
    "Blightseed": "Seme del Morbo",
    "Brutalclaw": "Artiglio Brutale",
    "Bullheart": "Cuore di Toro",
    "Burnward": "Guardia Ardente",
    "Chillhowl": "Ululato Gelido",
    "Dazzler": "Accecante",
    "Duskbloom": "Fiore del Crepuscolo",
    "Enflamed": "Infiammato",
    "Erupting": "Eruttante",
    "Feralbond": "Vincolo Ferino",
    "Forestlinked": "Legato alla Foresta",
    "Frostward": "Guardia Gelida",
    "Gloomfang": "Zanna Tenebrosa",
    "Goblin Caller": "Evocatore di Goblin",
    "Goblin Friend": "Amico dei Goblin",
    "Gorehorn": "Corno Cruento",
    "Graveveil": "Velo Sepolcrale",
    "Gusting": "Raffica",
    "Ironfist": "Pugno di Ferro",
    "Lifebloom": "Fiore della Vita",
    "Lionspear": "Lancia del Leone",
    "Momentum": "Slancio",
    "Moonthorn": "Spina Lunare",
    "Pathweaver": "Tessitore di Sentieri",
    "Pitfighter": "Lottatore da Fossa",
    "Precision Fang": "Zanna di Precisione",
    "Putrid": "Putrido",
    "Pyreweaver": "Tessitore di Fiamme",
    "Redsteel": "Acciaio Rosso",
    "Ripping": "Squarciante",
    "Rootbloom": "Fiore di Radici",
    "Rootbound": "Legato alle Radici",
    "Rumbler": "Rombante",
    "Shakers": "Scuotitori",
    "Shieldline": "Linea di Scudi",
    "Spiritbound": "Legato allo Spirito",
    "Stonehoove": "Zoccolo di Pietra",
    "Swiftstep": "Passo Rapido",
    "Thornborn": "Nato dalle Spine",
    "Tidestorm": "Tempesta di Marea",

    # ---- grado 1 -----------------------------------------------------------
    "Basic Amulet": "Amuleto Semplice",
    "Novice Emblem": "Emblema del Novizio",
    "Simple Sash": "Fascia Semplice",
    "Simple Bracer": "Bracciale Semplice",
    "Plain Talisman": "Talismano Comune",
    "Modest Band": "Anello Modesto",
    "Faded Rune": "Runa Sbiadita",
    "Cloth Lining": "Fodera di Stoffa",

    # ---- grado 2 -----------------------------------------------------------
    "Enhanced Amulet": "Amuleto Migliorato",
    "Adept Emblem": "Emblema dell'Adepto",
    "Reinforced Cincture": "Cintura Rinforzata",
    "Reinforced Bracer": "Bracciale Rinforzato",
    "Imbued Charm": "Ciondolo Imbevuto",
    "Polished Band": "Anello Lucidato",
    "Refined Rune": "Runa Raffinata",
    "Padded Undercoat": "Sottoveste Imbottita",

    # ---- grado 3 -----------------------------------------------------------
    "Studded Amulet": "Amuleto Borchiato",
    "Seeker Emblem": "Emblema del Cercatore",
    "Tempered Cincture": "Cintura Temprata",
    "Tempered Bracer": "Bracciale Temprato",
    "Runed Charm": "Ciondolo Runico",
    "Gilded Band": "Anello Dorato",
    "Engraved Rune": "Runa Incisa",
    "Layered Undercoat": "Sottoveste a Strati",

    # ---- grado 4 -----------------------------------------------------------
    "Mystic Amulet": "Amuleto Mistico",
    "Heroic Emblem": "Emblema Eroico",
    "Blessed Cincture": "Cintura Benedetta",
    "Empowered Bracer": "Bracciale Potenziato",
    "Arcane Charm": "Ciondolo Arcano",
    "Arcane Band": "Anello Arcano",
    "Empowered Rune": "Runa Potenziata",
    "Fortified Undercoat": "Sottoveste Fortificata",

    # ---- grado 5 -----------------------------------------------------------
    "Divine Amulet": "Amuleto Divino",
    "Mythic Emblem": "Emblema Mitico",
    "Mythic Cincture": "Cintura Mitica",
    "Mythic Bracer": "Bracciale Mitico",
    "Divine Charm": "Ciondolo Divino",
    "Mythic Band": "Anello Mitico",
    "Runic Masterpiece": "Capolavoro Runico",
    "Mythic Undercoat": "Sottoveste Mitica",

    # ---- grado 6 -----------------------------------------------------------
    "Celestial Amulet": "Amuleto Celestiale",
    "Celestial Emblem": "Emblema Celestiale",
    "Celestial Cincture": "Cintura Celestiale",
    "Celestial Bracer": "Bracciale Celestiale",
    "Celestial Charm": "Ciondolo Celestiale",
    "Celestial Band": "Anello Celestiale",
    "Perfected Rune": "Runa Perfezionata",
    "Celestial Undercoat": "Sottoveste Celestiale",
}
