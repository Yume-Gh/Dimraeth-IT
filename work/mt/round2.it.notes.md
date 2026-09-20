# Note di traduzione — round2.it.tsv

Tradotte **1.237 righe**, senza salti e nello stesso ordine dell'input. Salvataggi progressivi in 10 blocchi: 1–130, 131–264, 265–388, 389–513, 514–641, 642–770, 771–898, 899–1017, 1018–1130, 1131–1237. Ogni blocco contiene da 100 a 150 righe.

## Registro e terminologia

- `ATTR_`, `EFFECT_`, `EQUIPMENT_`, `ITEM_`, `PASSIVE_` e `STACKEFFECT_`: formulazioni tecniche; numeri, soglie, durate, condizioni e tipi di danno conservati.
- `CINEMATIC_`: narrazione cadenzata; segnaposto conservati anche all'interno delle frasi che continuano nel sottotitolo seguente.
- `INSCENE_` e le corrispondenti copie `INTERACT_`: voce del narratore, dello studioso o del personaggio, secondo il testo. Traduzioni identiche per gli inglesi identici; distinte le varianti di contenuto.
- `SUBTITLE_`: conservato il tono cortese e sarcastico di Faustas.
- Nomi di ricette e incantesimi ricavati dal glossario aggiornato. La regola vincolante per `beacon` è «segnalatore»; nel testo visibile di questo file il termine non compare.
- Nessuna modifica a `reference.tsv` o alla traduzione precedente delle missioni.

## Termini nuovi e alias

Le proposte seguenti riguardano voci senza una corrispondenza autonoma nel glossario. I nomi propri di persona e i nomi geografici già stabiliti restano invariati.

| Inglese | Italiano adottato | Nota |
|---|---|---|
| Builder | Costruttore | Classe |
| Critical Rate | Probabilità di critico | Alias coerente con Critical Chance |
| Critical Multiplier | Moltiplicatore critico | Distinto dal nome della statistica Critical Damage |
| Healing Power | Potere curativo | Statistica |
| Minion | servitore | Creature evocate; statistiche «Probabilità di critico / Danno / Salute dei servitori» |
| Decay Channel | Canale del Decadimento | Effetto/passiva |
| Temporal Cleave | Fendente Temporale | Effetto/passiva |
| Third Strike | Terzo Colpo | Attacco nominato nel testo |
| Recovery | Recupero | Etichette «ridotto» e «aumentato» |
| Rejuvination | Ringiovanimento | Grafia originale anomala; etichette «ridotto» e «aumentato» |
| Burn Resistance / Burning Resistance | Resistenza all'ustione | Distinta dalla Resistenza al fuoco |
| Poison Resistance | Resistenza al veleno | Distinta dalla Resistenza al decadimento |
| Bleeding Resistance | Resistenza al sanguinamento | Effetto di resistenza agli accumuli |
| Chill Resistance | Resistenza al gelo | Distinta dalla Resistenza al ghiaccio |
| Dimraeth Mountains | Monti di Dimraeth | Toponimo |
| Imperial Son | Figlio Imperiale | Titolo di Antark |
| Dark Lord | Signore Oscuro | Titolo di Sylbos |
| Ogre Magi | Maghi Ogre | Gruppo citato nel filmato |
| Dark Gods | Dei Oscuri | Filmato |
| Worp Plant | Pianta di Worp | Specie non descritta ulteriormente |
| warding banner | stendardo protettivo | Coerente con ward stake e ward-stone |
| bell-tab | campanello segnalatore | Resa già proposta nel giro Quests, ancora priva di voce autonoma nel glossario |
| Earlwood Wall | Mura di Earlwood | Struttura difensiva |
| Goblin Crisis | Crisi dei Goblin | Evento storico |
| Giant Old One's Egg | Uovo dell'Antico Gigante | Vedi dubbio sotto |
| Everlast trees | alberi Everlast | Nome della specie conservato |
| Abandoned Farmsteads | Fattorie Abbandonate | Luogo |
| Ford of Garfael | Guado di Garfael | Luogo |
| Corrupted Tree | Albero Corrotto | Voce di conoscenza |
| Great Academy of Aldoria / Aldoria's Great Academy | Grande Accademia di Aldoria | Luogo/istituzione |
| spellcrafting | creazione di incantesimi | Nella frase: «per creare incantesimi» |
| minor concentration extract | estratto scarso di concentrazione | Non sostituito con Weak Magic Extract |
| minor health extract | estratto scarso di salute | Non sostituito con Weak Health Extract |
| Stone Foundation | Fondazione di Pietra | Ricetta; coerente con i materiali degli altri elementi edilizi |
| Magic Barrier | Barriera magica | Effetto del Gatto Argentato |
| ley lines | linee di forza | Elemento ambientale |
| Howl | Ululato | Forma breve dell'originale, distinta da Alpha Howl → Ululato Alfa |
| Perfect Vanish | Dissolvenza perfetta | Derivato da Vanish → Dissolvenza |
| Fire Aura | Aura di Fuoco | Effetto |
| Axe Arts | Arti dell'ascia | Disciplina |
| Minotaur Magic | Magia del Minotauro | Disciplina |

Forme di luogo derivate da nomi già vincolanti: Eastern Earlwood Entrance → Ingresso Est di Earlwood; Farmlands Roadside Camp → Campo sulla Strada delle Terre Coltivate; Farmlands North/South Waypoint → Punto di passaggio delle Terre Coltivate Nord/Sud; Heimen's Riverside Camp → Campo sul Fiume di Heimen; Lost Archeologist Camp → Campo dell'Archeologo Perduto; Earlwood Village Campfire → Falò del Villaggio di Earlwood.

Le varianti Forest's Edge Homestead e Golem's Garden usano le rese canoniche di Forests Edge Homestead e Golems Garden. Per `POI_WILDWOODROADSIDECAMP_LORE`, «Wildwood Path Camp» è reso «Campo sulla Strada di Wildwood», coerentemente con il nome Wildwood Roadside Camp del glossario e con la chiave dello stesso punto d'interesse.

## Dubbi di senso

- `CINEMATIC_INTRO_004`: «two souls from either side» può risultare ambiguo sul numero di persone. La traduzione indica due anime da fronti opposti, in accordo con Antark e Tolais nominati subito dopo.
- `INSCENE_WILDWOODFORESTPARTIII_NOTIF_7682E0` e la relativa notifica `INTERACT_WILDWOODFORESTP_ITEM_7682E0_NOTIF_2`: «Giant Old One's Egg» può indicare l'uovo di un Antico gigante oppure un enorme uovo di un Antico. Adottata la prima lettura nel titolo; la descrizione continua a parlare di un imponente uovo degli Antichi.
- `EFFECT_BLEEDINGRESISTANCE_DESC`, `EFFECT_BURNINGRESISTANCE_DESC`, `EFFECT_POISONRESISTANCE_DESC`: mantenuti riduzione del 50%, arrotondamento per eccesso e minimo 1. L'originale non esplicita con una formula se arrotondare il valore risultante o la riduzione; la traduzione non introduce una formula propria.
- `PASSIVE_FLAMEFEEDFRENZY_DESC`: «2 Spell Haste and 2% Attack Speed ... up to 24%». Conservati 2 senza percentuale per la Celerità magica, 2% per la Velocità d'attacco e il limite 24%, senza assegnare arbitrariamente il limite a una delle due statistiche.
- `PASSIVE_RIPPLINGECHOES_DESC`: «When Temporal Echo above 5 is applied» non chiarisce se la soglia riguardi gli accumuli appena applicati o quelli totali già presenti. Conservata l'espressione «oltre 5 accumuli», senza cambiarla in «almeno 5».
- `PASSIVE_ELVISHVELOCITY_DESC`: il testo abbreviato «+15% Movement» è reso «+15% Velocità di movimento», coerentemente con la descrizione del relativo effetto.
- `ITEM_*OIL*_DESC`: «split ... Damage» reso come conversione di parte del danno dell'arma, senza aggiungere una percentuale assente nella descrizione. Gli effetti del rivestimento mantengono il 50% esplicito.
- I composti degli archetipi, tra cui Ironhold, Cloudshadow, Deepvein e Hammerfall, non sono definiti dal glossario. Sono resi come nomi fantasy descrittivi; le proposte complete sono nella tabella sotto.

## Incoerenze dell'originale

- `ITEM_TOXICOIL1_DESC` fino a `ITEM_TOXICOIL5_DESC` dichiarano Poison Damage; `ITEM_TOXICOIL_DESC` ed `EFFECT_TOXICOILCOATING_DESC` dichiarano Decay Damage. Conservati rispettivamente Danno da veleno e Danno da decadimento.
- `EFFECT_ASHENESCALATION_DESC` parla di Fire Damage; `PASSIVE_ASHENESCALATION_DESC` di Burning Damage. Conservati Danno da fuoco e Danno da ustione.
- `EFFECT_PERMAFROSTRHYTHM_DESC` parla di Spell Haste; `PASSIVE_PERMAFROSTRHYTHM_DESC` descrive invece una riduzione diretta dei tempi di recupero dell'1% per accumulo consumato. Nessuna uniformazione delle meccaniche.
- `EFFECT_TEMPOCONVERSION_DESC` dice «next attack»; `PASSIVE_TEMPOCONVERSION_DESC` specifica «next Third Strike». La distinzione rimane.
- `EFFECT_AMBUSH_DESC` specifica il prossimo attacco automatico; `EQUIPMENT_REDSTEEL_BONUS_6` parla del prossimo colpo e `PASSIVE_AMBUSH_DESC` del prossimo attacco a segno. Conservate le rispettive formulazioni.
- `EFFECT_PUMMEL_DESC` specifica tre colpi contundenti in rapida successione; bonus di equipaggiamento e passiva parlano genericamente di colpi rapidi sullo stesso nemico. Non aggiunto il numero dove manca.
- `ITEM_EARLWOODFEAST_DESC` dichiara un bonus a tutti gli attributi fisici e mentali; `ITEM_EARLWOODFEAST_EFFECT` elenca soltanto Salute, Vigore e Concentrazione massimi. Entrambi tradotti come scritti.
- `ITEM_BURNSALVE*_DESC` descrive un «salve» fatto anche con stoffa, formulazione insolita per un unguento. Non trasformato arbitrariamente in una benda.
- Alcuni libri degli incantesimi, tra cui `ITEM_SPELLBOOKEMPOWERALLY_DESC`, `ITEM_SPELLBOOKENTANGLINGROOTS_DESC`, `ITEM_SPELLBOOKPOISONSPORES_DESC`, `ITEM_SPELLBOOKSAVAGECLAW_DESC`, `ITEM_SPELLBOOKSPIRITSWAP_DESC` e `ITEM_SPELLBOOKWATERSURGE_DESC`, omettono la frase sull'uso e sugli attributi richiesti. Non aggiunta.
- `ITEM_SPELLBOOKPOISONSPORES_NAME` e `_DESC` indicano Poison Mist, benché la chiave contenga POISONSPORES. Usata la resa vincolante Nebbia velenosa, mantenendo le chiavi.
- `EFFECT_REJUVINATIONDOWN` e `EFFECT_REJUVINATIONUP` usano «Rejuvination» anziché «Rejuvenation». Il testo italiano è regolare; le chiavi restano identiche.
- Le chiavi contengono altre grafie anomale come `INNOCULATION`, `HEATOAKMILL`, `CONFLAGURATION` e `RECIPERECIPEEARLWOODBED`; sono tutte conservate.
- Le copie `INSCENE_` e `INTERACT_` a volte differiscono per contenuto, maiuscole o spazi finali. Non sono state fuse; ogni record resta presente. Per esempio le interazioni dei cadaveri includono descrizioni diverse dalle semplici tracce degli eventi di scena.
- Non sono state rilevate righe in portoghese. «SCRIPTURA PRINCIPIORUM» è un titolo latino sulla copertina di un libro e rimane invariato.

## Verifiche

- 1.237 record in ingresso e in uscita, con chiavi identiche e nello stesso ordine.
- UTF-8 senza BOM; una sola tabulazione per record, nessuna traduzione vuota, nessun ritorno a capo interno o carattere di sostituzione.
- Segnaposto conservati con la stessa grafia e molteplicità in tutte le 101 righe interessate.
- Numeri verificati automaticamente: stessi valori e stessa molteplicità, normalizzando soltanto il separatore decimale italiano (0.5 → 0,5).
- Traduzioni ripetute coerenti. Tre stringhe rimangono intenzionalmente identiche: `ATTR_HPPercent`, `ATTR_TMPL_HEALTH`, `ATTR_TMPL_HPPERCENT`, composte soltanto da HP, percentuali e segnaposto.
- Nomi nelle ricette e nei libri degli incantesimi verificati contro `reference.tsv`; documentate sopra le sole varianti e la nuova Fondazione di Pietra.
- Nessun reimport o avvio del gioco eseguito.

## Archetipi nuovi

| Inglese | Italiano adottato |
|---|---|
| Aerie Defender | Difensore del Nido |
| Ancestral Mystic | Mistico Ancestrale |
| Beastland Mystic | Mistico delle Terre Ferine |
| Blossom Soulcaller | Evocatore di Anime dei Fiori |
| Bogland Healer | Guaritore delle Torbiere |
| Bridge Keeper | Custode del Ponte |
| Cloudshadow Assassin | Assassino dell'Ombra delle Nubi |
| Colossal Brawler | Rissoso Colossale |
| Deepvein Stalker | Predatore delle Vene Profonde |
| Defender of the Realm | Difensore del Regno |
| Dewdrop Spy | Spia della Rugiada |
| Elemental Binder | Vincolatore Elementale |
| Eternal Sculptor | Scultore Eterno |
| Forest Whisperer | Sussurratore della Foresta |
| Forgewright | Artefice della Fucina |
| Granite Sentinel | Sentinella di Granito |
| Grassland Ambusher | Assalitore delle Praterie |
| Hammerfall Berserker | Berserker del Martello Tonante |
| Hoofed Fury | Furia degli Zoccoli |
| Horned Vanguard | Avanguardia Cornuta |
| Ironhold Warden | Custode di Roccaferrea |
| Labyrinth Guardian | Guardiano del Labirinto |
| Marsh Berserker | Berserker delle Paludi |
| Master Architect | Mastro Architetto |
| Mire Engineer | Ingegnere del Pantano |
| Monumental Mason | Muratore Monumentale |
| Nature's Artisan | Artigiano della Natura |
| Nectarblade Fighter | Guerriero della Lama di Nettare |
| Nestmaster Engineer | Ingegnere Maestro dei Nidi |
| Night's Whisper | Sussurro della Notte |
| Pebble Sneak | Furtivo dei Ciottoli |
| Petal Constructor | Costruttore dei Petali |
| Pixie Spellweaver | Tessincantesimi Folletto |
| Plainswalker Mage | Mago Viandante delle Pianure |
| Prairie Seer | Veggente della Prateria |
| Runeforge Mage | Mago della Fucina Runica |
| Savanna Craftsman | Artigiano della Savana |
| Sky Sorcerer | Stregone del Cielo |
| Spirit Guardian | Guardiano degli Spiriti |
| Steppe Vanguard | Avanguardia della Steppa |
| Stone Spiritist | Spiritista della Pietra |
| Swamp Warlock | Stregone della Palude |
| Sylvan Protector | Protettore Silvano |
| Talon Knight | Cavaliere dell'Artiglio |
| Thistleshield Warden | Custode dello Scudo di Cardi |
| Underbridge Rogue | Furfante del Sottoponte |
| Windspirit Shaman | Sciamano dello Spirito del Vento |

## Nomi nuovi dei bonus di equipaggiamento

| Inglese | Italiano adottato |
|---|---|
| Nightglass | Vetro Notturno |
| Bleed Claw | Artiglio Sanguinante |
| Empowered Claw | Artiglio Potenziato |
| Calloused Skin | Pelle Callosa |
| Dazzling Rejection | Repulsione Abbagliante |
| Toxinleaf | Foglia Tossica |
| Everburn | Ardore Eterno |
| Water Remnants | Residui d'Acqua |
| Extra Heart | Cuore Aggiuntivo |
| Rotwound | Ferita Marcescente |
| More Goblins | Più Goblin |
| Goblin Party | Gruppo di Goblin |
| Big Friend | Grande Amico |
| Gravecross | Croce Sepolcrale |
| Frostbiting Gust | Raffica Assiderante |
| Quickleaf | Foglia Rapida |
| Guided Fang | Zanna Guidata |
| Putrid Eruption | Eruzione Putrida |
| Expansive Eruption | Eruzione Espansiva |
| Riptear | Squarcio Lacerante |
| Bloody Slashes | Tagli Sanguinosi |
| Root Strike | Colpo di Radice |
| Charged Shockwave | Onda di Shock Caricata |
| Stun And Shatter | Stordisci e Frantuma |
| Ceres Blessing | Benedizione di Ceres |
| Ceres Wrath | Ira di Ceres |
| Circle Of Thorns | Cerchio di Spine |
