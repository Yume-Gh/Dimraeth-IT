# -*- coding: utf-8 -*-
"""Descrizioni delle costruzioni e righe di statistica a struttura ambigua.

Le sequenze \\n sono due caratteri veri (barra + n), come nei CSV: vanno
conservate identiche o l'interruzione di riga in gioco sparisce.

Le voci ATTR_* qui sotto sono le 19 righe che avevo lasciato scoperte di
proposito: la cornice '{{n0}} {t0} {t1}' mescolava due strutture che in italiano
divergono ("Armatura contundente" con aggettivo, "Penetrazione da decadimento"
con complemento). Scritte a mano, una per una.
"""

BUILD = {
    # ---- righe di statistica, struttura decisa caso per caso --------------
    "{0} Bleeding Duration": "{0} Durata sanguinamento",
    "{0} Burning Duration": "{0} Durata ustione",
    "{0} Chill Duration": "{0} Durata gelo",
    "{0} Poison Duration": "{0} Durata veleno",
    "{0} Rage Duration": "{0} Durata furia",
    "{0} Blunt Armor": "{0} Armatura contundente",
    "{0} Strike Armor": "{0} Armatura da taglio",
    "{0} Thrust Armor": "{0} Armatura perforante",
    "{0} Blunt Piercing": "{0} Penetrazione contundente",
    "{0} Strike Piercing": "{0} Penetrazione da taglio",
    "{0} Thrust Piercing": "{0} Penetrazione perforante",
    "{0} Decay Piercing": "{0} Penetrazione da decadimento",
    "{0} Electricity Piercing": "{0} Penetrazione da elettricità",
    "{0} Ether Piercing": "{0} Penetrazione da etere",
    "{0} Fire Piercing": "{0} Penetrazione da fuoco",
    "{0} Poison Piercing": "{0} Penetrazione da veleno",
    "{0} Decay Resistance": "{0} Resistenza al decadimento",
    "{0} Electricity Resistance": "{0} Resistenza all'elettricità",
    "{0} Ether Resistance": "{0} Resistenza all'etere",

    # ---- etichette secche delle parti costruttive -------------------------
    "Door": "Porta",
    "Door Frame": "Telaio",
    "Fence": "Recinto",
    "Fence Gate": "Cancello",
    "Pillar": "Pilastro",
    "Roof": "Tetto",
    "Rug": "Tappeto",
    "Stairs": "Scale",
    "Wall": "Muro",
    "Window": "Finestra",

    # ---- strutture -------------------------------------------------------
    "A Heartwood door frame.": "Un telaio in durame.",
    "A Pinewood door frame.": "Un telaio di pino.",
    "A Stone door frame.": "Un telaio di pietra.",
    "A Stone floor for a home.": "Un pavimento di pietra per una casa.",
    "A building foundation made of Heart Oak.":
        "Una fondazione in Quercia del Cuore.",
    "A pinewood foundation for a home.": "Una fondazione di pino per una casa.",
    "A pinewood window that lets daylight through a wall.":
        "Una finestra di pino che lascia entrare la luce del giorno.",
    "A gate wide enough to walk a cart through.":
        "Un cancello abbastanza largo da farci passare un carro.",
    "Keeps your room closed.": "Tiene chiusa la stanza.",
    "Pathing made of stone.": "Un camminamento di pietra.",
    "Fencing from Basilton's Garden.": "Recinzione dal Giardino di Basilton.",
    "Fencing from Earlwood.": "Recinzione di Earlwood.",
    "Fencing from Heart Oak.": "Recinzione in Quercia del Cuore.",
    "Fencing from quarried stone.": "Recinzione in pietra di cava.",

    # ---- arredi ----------------------------------------------------------
    "A sturdy table for homes and halls.": "Un tavolo robusto per case e sale.",
    "Simple table for homes and halls.": "Un tavolo semplice per case e sale.",
    "Plain wooden chair for seating.": "Una semplice sedia di legno.",
    "A barrel chair from Earlwood Village.":
        "Una sedia a botte dal Villaggio di Earlwood.",
    "Low seat carved from Treant wood. Still twitches with life.":
        "Un sedile basso intagliato nel legno di Treant. Freme ancora di vita.",
    "A basic colored frayed rug.": "Un semplice tappeto logoro colorato.",
    "A basic colored linen rug.": "Un semplice tappeto di lino colorato.",
    "A floor rug made from alpha wolf fur.":
        "Un tappeto ricavato dalla pelliccia di un lupo alfa.",
    "A banner from Earlwood Village.": "Uno stendardo dal Villaggio di Earlwood.",
    "A wall-mounted banner from Earlwood Village.":
        "Uno stendardo da muro dal Villaggio di Earlwood.",
    "Pot plants from Earlwood Village.":
        "Piante in vaso dal Villaggio di Earlwood.",
    "Freestanding light for paths and yards.":
        "Una luce autoportante per sentieri e cortili.",
    "Large fire bowl for bright, steady light.":
        "Un ampio braciere per una luce intensa e costante.",
    "Large storage for gear and materials. Use as storage.":
        "Ampio deposito per attrezzatura e materiali. Usalo come deposito.",
    "Reliable storage for gear and materials. Use as storage.":
        "Deposito affidabile per attrezzatura e materiali. Usalo come deposito.",
    "A wooden training dummy.": "Un manichino da allenamento in legno.",
    "A large mounted fish. Purely decorative.":
        "Un grande pesce impagliato. Puramente decorativo.",

    # ---- trofei ----------------------------------------------------------
    "Grim trophy from a corrupted Treant.":
        "Un cupo trofeo ricavato da un Treant corrotto.",
    "Wall-mounted trophy from a felled Treant.":
        "Trofeo da muro ricavato da un Treant abbattuto.",
    "Wall-mounted trophy from a felled Goblin King.":
        "Trofeo da muro ricavato da un Re Goblin abbattuto.",

    # ---- letti e riposo --------------------------------------------------
    "A bed made from Heart Oak for sleeping and recovery. Use to sleep. \\n Grants the Well Rested Buff: \\n Monster XP Bonus: 15% \\n Reduced Nourishment Decay: 10% \\n Duration: 15 minutes":
        "Un letto in Quercia del Cuore per dormire e recuperare. Usalo per dormire. \\n Conferisce il Bonus Ben Riposato: \\n Bonus XP dai mostri: 15% \\n Calo del nutrimento ridotto: 10% \\n Durata: 15 minuti",
    "A sturdy village bed for sleeping and recovery. Use to sleep. \\n Grants the Well Rested Buff: \\n Monster XP Bonus: 15% \\n Reduced Nourishment Decay: 10% \\n Duration: 15 minutes":
        "Un robusto letto da villaggio per dormire e recuperare. Usalo per dormire. \\n Conferisce il Bonus Ben Riposato: \\n Bonus XP dai mostri: 15% \\n Calo del nutrimento ridotto: 10% \\n Durata: 15 minuti",
    "A bedroll for a rough night away from home. Use to sleep. \\n Grants the Well Rested Buff: \\n Monster XP Bonus: 10% \\n Reduced Nourishment Decay: 5% \\n Duration: 10 minutes":
        "Un giaciglio per una notte scomoda lontano da casa. Usalo per dormire. \\n Conferisce il Bonus Ben Riposato: \\n Bonus XP dai mostri: 10% \\n Calo del nutrimento ridotto: 5% \\n Durata: 10 minuti",
    "A weathered expedition tent for camp setups. Use to sleep. \\n Grants the Well Rested Buff: \\n Monster XP Bonus: 10% \\n Reduced Nourishment Decay: 5% \\n Duration: 10 minutes":
        "Una logora tenda da spedizione per allestire un campo. Usala per dormire. \\n Conferisce il Bonus Ben Riposato: \\n Bonus XP dai mostri: 10% \\n Calo del nutrimento ridotto: 5% \\n Durata: 10 minuti",

    # ---- postazioni di lavoro --------------------------------------------
    "Basic crafting station for tools and parts. Used to craft Tier I tools and parts.":
        "Postazione base per attrezzi e componenti. Serve a creare attrezzi e componenti di grado I.",
    "Brews simple potions and tonics.": "Prepara pozioni e tonici semplici.",
    "Cooks simple food and lights your camp.":
        "Cucina cibo semplice e illumina il campo.",
    "Indoor cooking station with steady heat. Cooks hearty meals.":
        "Postazione di cucina al chiuso a calore costante. Prepara pasti sostanziosi.",
    "Central hub for upgrading and repairing facilities in your base. Interact to view available upgrades.":
        "Centro nevralgico per migliorare e riparare le strutture della base. Interagisci per vedere i miglioramenti disponibili.",
    "A felt-topped table for a friendly game of Hold'em. Interact to take a seat; other players can pull up a chair and play against you.":
        "Un tavolo in panno per una partita amichevole di Hold'em. Interagisci per sederti; altri giocatori possono accomodarsi e sfidarti.",
    "A small waygate of your own. Once raised it appears on the Sanctum map and can be travelled to like any other.":
        "Un piccolo Varco tutto tuo. Una volta eretto compare sulla mappa del Santuario e vi si può viaggiare come a qualsiasi altro.",

    # ---- produzione ------------------------------------------------------
    "A coop for chickens. Periodically produces eggs for harvest.":
        "Un pollaio. Produce periodicamente uova da raccogliere.",
    "Periodically produces eggs for harvest.":
        "Produce periodicamente uova da raccogliere.",
    "A farm for Droops. Periodically produces Droop Cores for collection.":
        "Un allevamento di Droop. Produce periodicamente Nuclei di Droop da raccogliere.",
    "Periodically produces Droop Cores for harvest.":
        "Produce periodicamente Nuclei di Droop da raccogliere.",
    "A water well. Periodically produces Water for collection.":
        "Un pozzo d'acqua. Produce periodicamente Acqua da raccogliere.",
    "Periodically produces Water.": "Produce periodicamente Acqua.",
    "A quarry that periodically produces copper for collection.":
        "Una cava che produce periodicamente rame da raccogliere.",
    "A quarry that periodically produces stone for collection.":
        "Una cava che produce periodicamente pietra da raccogliere.",
    "A mill that periodically produces Heart Oak for collection.":
        "Un mulino che produce periodicamente Quercia del Cuore da raccogliere.",
    "A mill that periodically produces Wildwood Pine for collection.":
        "Un mulino che produce periodicamente Pino di Wildwood da raccogliere.",
    "Workers periodically harvest Copper Ore.":
        "I lavoratori raccolgono periodicamente Minerale di Rame.",
    "Workers periodically harvest Stone.":
        "I lavoratori raccolgono periodicamente Pietra.",
    "Workers periodically harvest Heart Oak.":
        "I lavoratori raccolgono periodicamente Quercia del Cuore.",
    "Workers periodically harvest Wildwood Pine.":
        "I lavoratori raccolgono periodicamente Pino di Wildwood.",

    # ---- coltivazioni ----------------------------------------------------
    "A farm plot sown with Brush Flax. Harvest the crop once it ripens.":
        "Un appezzamento seminato a Lino Selvatico. Raccogli quando matura.",
    "A farm plot sown with Emberbloom. Harvest the crop once it ripens.":
        "Un appezzamento seminato a Emberbloom. Raccogli quando matura.",
    "A farm plot sown with Singing Bellflower. Harvest the crop once it ripens.":
        "Un appezzamento seminato a Campanula Canterina. Raccogli quando matura.",
    "A farm plot sown with Tenderberry. Harvest the crop once it ripens.":
        "Un appezzamento seminato a Tenderberry. Raccogli quando matura.",
    "A farm plot sown with Thaumablossom. Harvest the crop once it ripens.":
        "Un appezzamento seminato a Thaumablossom. Raccogli quando matura.",
    "An apple tree grown from seed. Harvest the fruit once it ripens.":
        "Un melo cresciuto da seme. Raccogli il frutto quando matura.",
    "A patch of tilled soil. Purely decorative. Build anything on top of it.":
        "Una zona di terra arata. Puramente decorativa. Costruiscici sopra quel che vuoi.",

    # ---- decorazioni -----------------------------------------------------
    "A daisy patch. Purely decorative.": "Un'aiuola di margherite. Puramente decorativa.",
    "A sunflower patch. Purely decorative.": "Un'aiuola di girasoli. Puramente decorativa.",
    "A grass patch. Purely decorative.": "Una zona d'erba. Puramente decorativa.",
    "A green garden. Purely decorative.": "Un giardino verde. Puramente decorativo.",
    "An assortment from Basilton's Garden. Purely decorative.":
        "Un assortimento dal Giardino di Basilton. Puramente decorativo.",
}
