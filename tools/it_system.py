# -*- coding: utf-8 -*-
"""Messaggi di sistema (Errors) e prompt dei tutorial.

Attenzione agli spazi finali: "Move with " li ha, e servono alla spaziatura con
l'icona del tasto che il gioco concatena dopo. L'applicatore li conserva da solo,
ma qui le voci sono scritte senza, perche' la ricerca avviene sul testo ripulito.
"""

S = {
    # ---- stati e condizioni ------------------------------------------------
    "Empty": "Vuoto",
    "Sold out": "Esaurito",
    "No Target": "Nessun bersaglio",
    "Path blocked": "Percorso bloccato",
    "Invalid action": "Azione non valida",
    "Cannot be empty": "Non può essere vuoto",
    "No Matching Items": "Nessun oggetto corrispondente",
    "Requirements not met": "Requisiti non soddisfatti",
    "Invalid pet data": "Dati del compagno non validi",

    # ---- requisiti di costruzione -----------------------------------------
    "Required: Wall": "Richiede: muro",
    "Required: Table": "Richiede: tavolo",
    "Required: Foundation": "Richiede: fondazione",
    "Required: Door Frame": "Richiede: telaio della porta",

    # ---- risorse insufficienti --------------------------------------------
    "Not enough Health": "Salute insufficiente",
    "Not enough Stamina": "Vigore insufficiente",
    "Not enough Concentration": "Concentrazione insufficiente",
    "Not enough resources": "Risorse insufficienti",
    "Not enough gold to refund that": "Oro insufficiente per il rimborso",
    "Not enough gold to purchase that": "Oro insufficiente per l'acquisto",
    "Not enough inventory space for that": "Spazio nell'inventario insufficiente",
    "You do not have enough space for that": "Non hai spazio sufficiente",

    # ---- contenitori e inventario -----------------------------------------
    "Inventory is full": "Inventario pieno",
    "That chest is full.": "Quella cassa è piena.",
    "Pet Pen is full": "Il recinto è pieno",
    "Pet storage is full": "Il deposito dei compagni è pieno",
    "Pet inventory is empty.": "L'inventario del compagno è vuoto.",
    "That crafting slot is full.": "Quello slot di produzione è pieno.",
    "No empty slot to place the split stack.": "Nessuno slot libero per la pila divisa.",
    "Inventory full, dropping rune on the ground": "Inventario pieno, la runa cade a terra",
    "Too heavy, dropping excess.": "Troppo pesante, getto l'eccesso.",
    "You cannot carry that much weight": "Non puoi trasportare tutto quel peso",
    "You cannot carry that much weight.": "Non puoi trasportare tutto quel peso.",
    "Too heavy to travel. Store or drop some weight first.":
        "Troppo pesante per viaggiare. Deposita o getta del peso.",

    # ---- equipaggiamento ---------------------------------------------------
    "This item is locked": "Questo oggetto è bloccato",
    "You cannot drop that": "Non puoi gettarlo",
    "Cannot equip this item": "Non puoi equipaggiare questo oggetto",
    "Item is already equipped": "Oggetto già equipaggiato",
    "Only one {0} can be equipped": "Puoi equipaggiare un solo {0}",
    "Your level is too low to equip this item":
        "Il tuo livello è troppo basso per questo oggetto",
    "You do not have the required attributes": "Non hai gli attributi richiesti",
    "Missing attribute requirements: {0}": "Requisiti di attributo mancanti: {0}",
    "You can only have one bandage equipped": "Puoi equipaggiare una sola benda",
    "You can only have one burn salve equipped":
        "Puoi equipaggiare un solo unguento per ustioni",
    "You can only have one weapon oil equipped": "Puoi equipaggiare un solo olio per armi",
    "You can only have one poison cure equipped": "Puoi equipaggiare un solo antidoto",
    "You can only have one boon potion equipped":
        "Puoi equipaggiare una sola pozione del favore",
    "You can only have one health potion equipped":
        "Puoi equipaggiare una sola pozione di salute",
    "You can only have one stamina potion equipped":
        "Puoi equipaggiare una sola pozione di vigore",
    "You can only have one concentration potion equipped":
        "Puoi equipaggiare una sola pozione di concentrazione",
    "You can only have one offensive tool equipped":
        "Puoi equipaggiare un solo strumento offensivo",
    "You can only assign combat items to quick slots":
        "Negli slot rapidi puoi assegnare solo oggetti da combattimento",
    "Must be fully charged to leave the quick bar. Rest to refill.":
        "Deve essere completamente carico per lasciare la barra rapida. "
        "Riposa per ricaricarlo.",
    "Only food can go in the auto-eat slot.":
        "Nello slot di alimentazione automatica va solo cibo.",
    "Only drinks can go in the auto-drink slot.":
        "Nello slot di idratazione automatica vanno solo bevande.",
    "The auto-eat slot's stack is already full":
        "La pila dello slot di alimentazione è già piena",
    "The auto-drink slot's stack is already full":
        "La pila dello slot di idratazione è già piena",

    # ---- compagni ----------------------------------------------------------
    "Pets cannot be sold.": "I compagni non si possono vendere.",
    "Pets cannot be sold here.": "Qui non si possono vendere compagni.",
    "You don't own this pet.": "Questo compagno non è tuo.",
    "Only pets can be placed in the pet pen":
        "Nel recinto si possono mettere solo compagni",
    "Pets can't be stored in containers.":
        "I compagni non si possono mettere nei contenitori.",
    "Pets can't be placed in courier storage":
        "I compagni non si possono mettere nel deposito del corriere",
    "Cannot unequip pet while in courier mode.":
        "Non puoi rimuovere il compagno in modalità corriere.",
    "Empty the pet's inventory before unequipping.":
        "Svuota l'inventario del compagno prima di rimuoverlo.",
    "You cannot put your pet into their own backpack.":
        "Non puoi mettere il compagno nel suo stesso zaino.",
    "You are carrying too much weight to unequip this pet.":
        "Trasporti troppo peso per rimuovere questo compagno.",

    # ---- combattimento e bersagli -----------------------------------------
    "Target not an Ally": "Il bersaglio non è un alleato",
    "Target not in Range": "Bersaglio fuori portata",
    "Target needs at least {0} {1} stacks":
        "Il bersaglio necessita di almeno {0} cariche di {1}",
    "Spell On Cooldown": "Incantesimo in recupero",
    "This action is on cooldown": "Questa azione è in recupero",
    "You cannot do that during combat": "Non puoi farlo durante il combattimento",
    "Cannot respawn: a nearby ally is in combat":
        "Impossibile rinascere: un alleato vicino è in combattimento",
    "{0} race is required for this spell": "Questo incantesimo richiede la razza {0}",
    "{0} class is required for this spell": "Questo incantesimo richiede la classe {0}",
    "You have already unlocked this spell": "Hai già sbloccato questo incantesimo",

    # ---- albero delle abilita' --------------------------------------------
    "That node isn't purchased": "Quel nodo non è stato acquistato",
    "That node cannot be refunded": "Quel nodo non è rimborsabile",
    "Starting nodes cannot be refunded": "I nodi iniziali non sono rimborsabili",
    "Refund the nodes that depend on this one first":
        "Rimborsa prima i nodi che dipendono da questo",
    "This tier is not yet unlocked": "Questo grado non è ancora sbloccato",

    # ---- costruzione e ricette --------------------------------------------
    "You have already unlocked this recipe": "Hai già sbloccato questa ricetta",
    "You have already unlocked this buildable": "Hai già sbloccato questa costruzione",
    "Only the owner can dismantle this": "Solo il proprietario può smontarlo",
    "Cannot dismantle while items are present":
        "Non puoi smontarlo mentre contiene oggetti",
    "Cannot dismantle while another player is using it":
        "Non puoi smontarlo mentre un altro giocatore lo usa",
    "Equipment and pets can't be used at this station.":
        "Equipaggiamento e compagni non si possono usare a questa postazione.",

    # ---- mondo, incarichi, riposo -----------------------------------------
    "It must be night to sleep": "Devi aspettare la notte per dormire",
    "{0} has decayed away!": "{0} si è decomposto!",
    "{0} has decayed into {1}!": "{0} si è decomposto in {1}!",
    "This deed is already in progress": "Questo incarico è già in corso",
    "Everyone must leave the area before this deed can be taken":
        "Tutti devono lasciare l'area prima di accettare questo incarico",
    "You were moved to the Sanctum: a deed has sealed the area you logged out in":
        "Sei stato spostato al Santuario: un incarico ha sigillato l'area in cui "
        "ti eri disconnesso",

    # ---- nomi e server -----------------------------------------------------
    "World name is too long": "Il nome del mondo è troppo lungo",
    "Character name is too long": "Il nome del personaggio è troppo lungo",
    "Name must start with a letter": "Il nome deve iniziare con una lettera",
    "Name cannot contain two spaces in a row":
        "Il nome non può contenere due spazi consecutivi",
    "Name has too many accents stacked on one character":
        "Il nome ha troppi accenti sullo stesso carattere",
    "World name must be at least 2 characters":
        "Il nome del mondo deve avere almeno 2 caratteri",
    "Character name must be at least 2 characters":
        "Il nome del personaggio deve avere almeno 2 caratteri",
    "World name is already used or reserved":
        "Il nome del mondo è già in uso o riservato",
    "Character name is already used or reserved":
        "Il nome del personaggio è già in uso o riservato",
    "That name is reserved and cannot be used":
        "Quel nome è riservato e non si può usare",
    "That name is too long to save. Please use fewer characters":
        "Quel nome è troppo lungo da salvare. Usa meno caratteri",
    "Name can only contain letters, numbers, spaces, hyphens, apostrophes, and underscores":
        "Il nome può contenere solo lettere, numeri, spazi, trattini, apostrofi "
        "e trattini bassi",
    "Old Character already Selected": "Personaggio vecchio già selezionato",
    "The server has a different difficulty than this character":
        "Il server ha una difficoltà diversa da questo personaggio",
    "This server only allows new characters or returning players":
        "Questo server ammette solo personaggi nuovi o di ritorno",
    "You must choose a character which matches the difficulty of the world":
        "Devi scegliere un personaggio con la stessa difficoltà del mondo",

    # ---- prompt dei tutorial ----------------------------------------------
    "Move with": "Muoviti con",
    "Dash with": "Scatta con",
    "Attack with": "Attacca con",
    "Run by holding": "Corri tenendo premuto",
    "Cast spell with": "Lancia incantesimi con",
    "Block by Holding": "Para tenendo premuto",
    "Open your Inventory with": "Apri l'inventario con",
    "To pick up the item Press": "Per raccogliere l'oggetto premi",
    "Open build menu by holding": "Apri il menu costruzioni tenendo premuto",
    "Auto sprint in Settings Menu": "Scatto automatico nel menu Impostazioni",
    "Open your Map at any time with": "Apri la mappa in qualsiasi momento con",
    "Select a target and lock on with": "Seleziona un bersaglio e aggancialo con",
    "Walk up to the chest and interact": "Avvicinati alla cassa e interagisci",
    "Equip Gear to its Equipment Slot with":
        "Equipaggia l'attrezzatura nel suo slot con",
    "Equip Consumables to your Hotbar with":
        "Assegna i consumabili alla barra rapida con",
    "Build a Campfire and Cook a Droop Core":
        "Costruisci un falò e cuoci un Nucleo di Droop",
    "Find Map Crystals to fill in your Map.":
        "Trova i cristalli di mappa per completarla.",
    "Select the nearby Waygate to Fast Travel.":
        "Seleziona il Varco vicino per il viaggio rapido.",
    "Click or Drag Consumables into your Hotbar":
        "Clicca o trascina i consumabili nella barra rapida",
    "Track your New Quest in the Quest Menu with":
        "Segui la nuova missione nel menu Missioni con",
    "Click or Drag Equipment into its Equipment slot.":
        "Clicca o trascina l'equipaggiamento nel suo slot.",
    "Stay Nourished, remember to Eat or Drink regularly":
        "Resta nutrito: ricorda di mangiare o bere regolarmente",
    "Build: Select a tent, choose where to place, then press":
        "Costruisci: scegli una tenda, decidi dove posizionarla, poi premi",
    "Perfect Parry by blocking the moment an attack lands with":
        "Parata perfetta: para nell'istante in cui l'attacco arriva con",
    "Swap to Earlwood Map and select Earlwood Village Waygate.":
        "Passa alla mappa di Earlwood e seleziona il Varco del Villaggio.",
    "Rest at campfires to refill potions and other combat items.":
        "Riposa ai falò per ricaricare pozioni e altri oggetti da combattimento.",
    "Dismantle a building for resources by hovering it and holding":
        "Smonta una costruzione per recuperare risorse passandoci sopra e "
        "tenendo premuto",
    "Fast Travel to any Waygates you have discovered on your map at any time.":
        "Viaggia rapidamente verso qualsiasi Varco scoperto sulla mappa, in "
        "qualsiasi momento.",
    "Equip multiple pieces from the same set to activate a powerful Set Bonus!":
        "Equipaggia più pezzi dello stesso set per attivare un potente bonus del set!",
    "If you don't, your maximum Health, Concentration, and Stamina will decrease.":
        "Altrimenti la tua salute, concentrazione e vigore massimi caleranno.",
    "Do check the chests. Fortunes often hide in plain wood and rusty hinges":
        "Controlla le casse. Le fortune si nascondono spesso nel legno grezzo e "
        "nei cardini rugginosi",
}
