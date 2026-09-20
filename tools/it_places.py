# -*- coding: utf-8 -*-
"""Nomi di costruzioni (BuildItems) e luoghi (POIMarkers).

Coerenze imposte dal glossario: Earlwood e Wildwood restano invariati (nomi
propri), 'Heart Oak' e' "Quercia del Cuore", 'Heartwood' e' "Durame", 'Pinewood'
e' "Pino", 'Waygate' e' "Varco", 'Waypoint' e' "Punto di passaggio".

Una collisione evitata: 'Shrine' -> "Sacrario", non "Santuario", che nel glossario
e' gia' 'Sanctum' -- la base del giocatore. Due luoghi con lo stesso nome italiano
sarebbero indistinguibili sulla mappa.
"""

PLACES = {
    # ---- costruzioni: arredi e strutture -----------------------------------
    "Alpha Fur Rug": "Tappeto di Pelliccia Alfa",
    "Barrel Chair": "Sedia a Botte",
    "Brazier": "Braciere",
    "Old Campfire": "Vecchio Falò",
    "Frayed Rug": "Tappeto Logoro",
    "Linen Rug": "Tappeto di Lino",
    "Oak Cabinet": "Credenza di Quercia",
    "Sleeping Bag": "Sacco a Pelo",
    "Large Tent": "Tenda Grande",
    "Tent": "Tenda",
    "Lost Archeologist Tent": "Tenda dell'Archeologo Perduto",
    "Poker Table": "Tavolo da Poker",
    "Facility Center": "Centro Servizi",
    "Water Well": "Pozzo d'Acqua",
    "Waypoint": "Punto di passaggio",
    "Wood Planks": "Tavole di Legno",
    "Wood Wall": "Muro di Legno",
    "Stone Pathing": "Lastricato di Pietra",

    # ---- costruzioni: pino ------------------------------------------------
    "Pinewood Chair": "Sedia di Pino",
    "Pinewood Chest": "Cassa di Pino",
    "Pinewood Door": "Porta di Pino",
    "Pinewood Mill": "Mulino di Pino",
    "Pinewood Table": "Tavolo di Pino",
    "Pinewood Torch": "Torcia di Pino",
    "Pinewood Tree Garden": "Giardino di Pini",
    "Pine Window": "Finestra di Pino",
    "Wildwood Pine Door Frame": "Telaio di Pino di Wildwood",
    "Wildwood Pine Floor": "Pavimento di Pino di Wildwood",
    "Wildwood Pine Pillar": "Pilastro di Pino di Wildwood",
    "Wildwood Pine Stairs": "Scale di Pino di Wildwood",
    "Wildwood Pine Wall": "Muro di Pino di Wildwood",

    # ---- costruzioni: durame e quercia del cuore --------------------------
    "Heartwood Chest": "Cassa in Durame",
    "Heartwood Door Frame": "Telaio in Durame",
    "Heartwood Floor": "Pavimento in Durame",
    "Heartwood Pillar": "Pilastro in Durame",
    "Heartwood Table": "Tavolo in Durame",
    "Heartwood Wall": "Muro in Durame",
    "Heart Oak Bed": "Letto di Quercia del Cuore",
    "Heart Oak Fence": "Recinto di Quercia del Cuore",
    "Heart Oak Fence Gate": "Cancello di Quercia del Cuore",

    # ---- costruzioni: pietra, fango, Earlwood -----------------------------
    "Stone Door": "Porta di Pietra",
    "Stone Door Frame": "Telaio di Pietra",
    "Stone Fence": "Recinto di Pietra",
    "Stone Fence Gate": "Cancello di Pietra",
    "Stone Floor": "Pavimento di Pietra",
    "Stone Wall": "Muro di Pietra",
    "Stone Quarry": "Cava di Pietra",
    "Copper Quarry": "Cava di Rame",
    "Mud Fence": "Recinto di Fango",
    "Mud Fence Gate": "Cancello di Fango",
    "Earlwood Banner": "Stendardo di Earlwood",
    "Earlwood Bed": "Letto di Earlwood",
    "Earlwood Fence": "Recinto di Earlwood",
    "Earlwood Fence Gate": "Cancello di Earlwood",
    "Earlwood Pot Plant": "Pianta in Vaso di Earlwood",
    "Tall Earlwood Pot Plant": "Pianta Alta in Vaso di Earlwood",
    "Earlwood Wall Banner": "Stendardo da Muro di Earlwood",

    # ---- costruzioni: coltivazioni e allevamenti --------------------------
    "Empty Plot": "Appezzamento Vuoto",
    "Apple Tree Plot": "Appezzamento di Meli",
    "Emberbloom Plot": "Appezzamento di Emberbloom",
    "Thaumablossom Plot": "Appezzamento di Thaumablossom",
    "Tenderberry Plot": "Appezzamento di Tenderberry",
    "Singing Bellflower Plot": "Appezzamento di Campanula Canterina",
    "Brush Flax Plot": "Appezzamento di Lino Selvatico",
    "Basilton Garden": "Giardino di Basilton",
    "Chicken Coop": "Pollaio",
    "Droop Farm": "Allevamento di Droop",
    "Daisy Patch": "Aiuola di Margherite",
    "Sunflower Patch": "Aiuola di Girasoli",
    "Grass Patch": "Zona d'Erba",
    "Dirt Patch": "Zona di Terra",

    # ---- costruzioni: trofei ----------------------------------------------
    "Treant Stool": "Sgabello di Treant",
    "Treant Trophy": "Trofeo di Treant",
    "Corrupted Treant Trophy": "Trofeo di Treant Corrotto",
    "Goblin King Trophy": "Trofeo del Re Goblin",

    # ---- luoghi: campi e accampamenti -------------------------------------
    "Abandoned Camp": "Campo Abbandonato",
    "Corin's Camp": "Campo di Corin",
    "Corin's Campfire": "Falò di Corin",
    "Heimen's Camp": "Campo di Heimen",
    "Riverside Camp": "Campo sul Fiume",
    "Corrupted Riverside Camp": "Campo Corrotto sul Fiume",
    "Farmlands Old Camp": "Vecchio Campo delle Terre Coltivate",
    "Earlwood Farmlands Roadside Camp":
        "Campo sulla Strada delle Terre Coltivate di Earlwood",
    "Wildwood Roadside Camp": "Campo sulla Strada di Wildwood",
    "North Ruins Camp": "Campo delle Rovine Nord",
    "South Ruins Camp": "Campo delle Rovine Sud",
    "South Lookout Camp": "Campo d'Osservazione Sud",
    "West Lookout Camp": "Campo d'Osservazione Ovest",
    "West River Camp": "Campo del Fiume Ovest",
    "Under Root Camp": "Campo Sottoradice",
    "The Twisting Woods Camp": "Campo dei Boschi Tortuosi",
    "The Sealed Approach Camp": "Campo dell'Accesso Sigillato",
    "Northcut Camp Campfire": "Falò del Campo di Northcut",
    "Lost Archeologist Campfire": "Falò dell'Archeologo Perduto",
    "The Guild's Communal Campfire": "Il Falò Comune della Gilda",

    # ---- luoghi: insediamenti e strutture ---------------------------------
    "Abandoned Homestead": "Fattoria Abbandonata",
    "Nearby Farmstead": "Fattoria Vicina",
    "Forests Edge Homestead": "Fattoria ai Margini della Foresta",
    "Haylor's Mill": "Mulino di Haylor",
    "Earlwood Forge": "Fucina di Earlwood",
    "Northern Outpost": "Avamposto Settentrionale",
    "Roadside Outpost": "Avamposto sulla Strada",
    "Earlwood Crossroads": "Crocevia di Earlwood",
    "Earlwood Entrance": "Ingresso di Earlwood",
    "Dwarven Road": "Strada Nanica",

    # ---- luoghi: boschi, boschetti, sentieri ------------------------------
    "Hidden Grove": "Boschetto Nascosto",
    "Corrupted Grove": "Boschetto Corrotto",
    "Eastern Forest Grove": "Boschetto della Foresta Orientale",
    "Sisters' Grove": "Boschetto delle Sorelle",
    "Rivercaller's Grove": "Boschetto di Rivercaller",
    "Golems Garden": "Giardino dei Golem",
    "Moonridge Vale": "Valle di Moonridge",
    "The Forest Path": "Il Sentiero della Foresta",
    "Forest Path Start": "Inizio del Sentiero della Foresta",
    "Forest Path Overlook": "Belvedere del Sentiero della Foresta",
    "The Twisting Woods": "I Boschi Tortuosi",
    "The Greater Wildwood": "Il Grande Wildwood",
    "Wildwood Center": "Centro di Wildwood",
    "Farmlands North": "Terre Coltivate Nord",
    "Farmlands South": "Terre Coltivate Sud",
    "Corrupted Thicket Entrance": "Ingresso della Boscaglia Corrotta",

    # ---- luoghi: caverne e rovine -----------------------------------------
    "Dark Caverns": "Caverne Oscure",
    "Wildwood Caverns": "Caverne di Wildwood",
    "The Gnawed Tunnels": "I Tunnel Rosicchiati",
    "Goblin Cave Entrance": "Ingresso della Caverna dei Goblin",
    "Goblin Cave Mouth": "Imbocco della Caverna dei Goblin",
    "The Hoard Halls": "Le Sale del Tesoro",
    "The Hoard King's Den": "La Tana del Re del Tesoro",
    "Wildwood Ruins": "Rovine di Wildwood",
    "Northern Lost Ruin": "Rovina Perduta Settentrionale",
    "Old Ones' Ruins": "Rovine degli Antichi",
    "Beast-Occupied Ruins": "Rovine Occupate dalle Bestie",
    "The Ruins of Lost Lament": "Le Rovine del Lamento Perduto",
    "The Sealed Approach": "L'Accesso Sigillato",
    "The Shard Court": "La Corte dei Frammenti",
    "Lost Guardian": "Guardiano Perduto",
    "Pool of Remembrance": "Pozza del Ricordo",
    # 'Shrine' resta distinto da 'Sanctum' ("Santuario", la base del giocatore)
    "Over-run Shrine": "Sacrario Invaso",

    # ---- luoghi: punti di viaggio -----------------------------------------
    "Earlwood Road Waygate": "Varco della Strada di Earlwood",
    "Earlwood South Waygate": "Varco Sud di Earlwood",
    "Wildwood East Waygate": "Varco Est di Wildwood",
    "Wildwood North Waygate": "Varco Nord di Wildwood",
    "The Sanctum Waygate": "Il Varco del Santuario",
    "Beast Occupied Ruins Waypoint": "Punto di passaggio delle Rovine Occupate",
    "Forest Depths Waypoint": "Punto di passaggio delle Profondità della Foresta",
    "Over-run Shrine Waypoint": "Punto di passaggio del Sacrario Invaso",
    "The Lost Caverns Tutorial": "Tutorial delle Caverne Perdute",
}
