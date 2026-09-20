# Note di traduzione — Quests.it.tsv

Tradotte tutte le **1.152 righe** di `Quests.tsv`, in ordine, con salvataggi progressivi nei blocchi 1–131, 132–264, 265–401, 402–529, 530–662, 663–788, 789–918, 919–1047 e 1048–1152. Nessuna missione è stata divisa tra due blocchi.

## Terminologia nuova

Queste voci non hanno una coppia autonoma in `reference.tsv`. Le rese sono proposte da aggiungere al glossario; i nomi delle missioni sono riportati direttamente nelle righe `_NAME` del TSV.

| Inglese | Italiano adottato |
|---|---|
| Brother Generals | Generali Fratelli |
| Corrupted Guardian | Guardiano corrotto |
| Corrupted Hunters | Cacciatori corrotti |
| Corrupted Wolves | Lupi corrotti |
| Forest Golem | Golem della Foresta |
| Grove Guardian | Guardiana del Boschetto |
| Hopeful Shepherd | Pastore fiducioso |
| Cordwyn Yard | Deposito di Cordwyn |
| Earlwood Quarry | Cava di Earlwood |
| Broken Waygate Clearing | Radura del Varco Infranto |
| Giant's Trench | Trincea del Gigante |
| Wayfinder Line | Linea dei Cercavia |
| Silent Path | Sentiero Silenzioso |
| Shining Fungus Grove | Boschetto dei Funghi Luminosi |
| Waywell | Pozzo del Cammino |
| Forest Entrance | Ingresso della Foresta |
| King's Path | Sentiero del Re |
| Trail Fork | Bivio del Sentiero |
| River Crossing | Passaggio sul Fiume |
| Old Stump | Vecchio Ceppo |
| Clear Spring | Sorgente Limpida |
| Nesting Hollow | Conca dei Nidi |
| Waystone Burrow | Tana della Pietra del Cammino |
| waystone | pietra del cammino |
| ward | protezione |
| ward-stone | pietra protettiva |
| ward stake | palo protettivo |
| elder-tree sap | linfa dell'albero antico |
| caretaker's gem | gemma del custode |
| dryad-touched water | acqua toccata dalle driadi |
| beacon | faro |
| bell-tab | campanello segnalatore |
| bell-rope | corda per campanelli |
| bell-line | corda con campanelli |
| chime | sonaglio |
| Forge Anvil | Incudine della Fucina |
| runesmithing | forgiatura runica |
| forward camp | campo avanzato |

Alcune forme brevi sono state ricavate dalle voci composte già vincolanti, senza introdurre una nuova traduzione: Beast Warden → Custode delle Bestie; Rivercaller → Rivercaller; Rootweaver → Tessiradici; Droop King → Re Droop; Corrupted Droop King → Re Droop Corrotto; Hoard King → Re del Tesoro; Northcut Camp → Campo di Northcut; Farmlands → Terre coltivate; Rune Essence → Essenza runica; Goblin Teeth → Denti di Goblin. Per la distruzione dell'equipaggiamento alla fucina è stato usato «frantuma», coerente con «Shatter Equipment» nel glossario.

## Dubbi di senso

- `QUEST_NAMINGFALSEGOODS_NAME` e `QUEST_SEEINGTHETRUEGOODS_NAME`: «Goods» è ambiguo rispetto alle missioni di Myrll, dedicate a creature, illusioni e corruzione. Adottati «Un nome ai falsi beni» e «Alla scoperta dei veri beni», mantenendo il significato aperto di «beni». Senza dialoghi non è possibile stabilire se il termine alluda a benefici ingannevoli, beni concreti o altro.
- `QUEST_KEYSOFBARKANDSTONE_TASKGROUP_1_TASK_0`: «elder-tree» può indicare un albero antico oppure un sambuco. Adottato «albero antico» nel contesto fantasy; la specie richiede conferma.
- `QUEST_MEASURETWICE_TASKGROUP_1_TASK_0`, `QUEST_MEASURETWICE_TASKGROUP_2_TASK_0`, `QUEST_MEASURETWICE_TASKGROUP_3_TASK_0`, `QUEST_MEASURETWICE_TASKGROUP_4_TASK_0`: «bell-tab» non è definito; «campanello segnalatore» è una resa funzionale dedotta dal posizionamento lungo il percorso. Titolo reso «Misure scrupolose» per richiamare la prudenza dell'espressione «measure twice».
- `QUEST_JUICYAMBUSH_NAME` e `QUEST_MEALYDETOUR_NAME`: titoli alimentari senza spiegazione negli obiettivi. Conservati «Un'imboscata succosa» e «Una deviazione farinosa»; l'eventuale gioco di parole va verificato nei dialoghi.
- `QUEST_GOODDAUGHTERS_DESC`: «different Dryads» può significare driadi insolite o semplicemente varie driadi. Adottato «Driadi diverse dalle altre», in relazione agli ultimi sussurri negli obiettivi.
- `QUEST_SPOTTEDHUNTEROPT1_NAME` e `QUEST_SPOTTEDHUNTEROPT2_NAME`: «Spotted» reso «avvistato», coerentemente con l'avventuriero trovato in pericolo; non «maculato».
- `QUEST_YARDANDCODE_NAME`: adottato «Cortile e codice». Il testo non esplicita se «code» sia un codice di condotta né se «yard» designi formalmente il cortile d'addestramento.
- `DEED_ALPHAWOLFBOUNTY_DESC`: l'insolito «Thin the head off the pack» è reso «Elimina il capobranco», in accordo con gli obiettivi della taglia.

## Incoerenze e stringhe anomale dell'originale

- `QUEST_GOBLINACADEMICII_TASKGROUP_0_TASK_0`, `_TASK_1`, `_TASK_2`: la parte II richiede nuovamente gli appunti primo, secondo e terzo, come la parte I. La parte III passa al settimo, ottavo e nono. Numeri conservati.
- `QUEST_BREADFORSTEEL_TASKGROUP_1_DESC`: il gruppo richiede «frutta e verdura», ma gli obiettivi elencano Carne di Bestia, Tenderberry e Mele. Descrizione e obiettivi conservati.
- `QUEST_SCOUTOLDCAMPS_TASKGROUP_0_TASK_1` e `_TASK_2`: «northern camp» e «north camp» potrebbero designare lo stesso campo. Conservata la distinzione lessicale «campo settentrionale» / «campo a nord».
- `QUEST_TRAVELLINGMERCHANTA_NAME`, `QUEST_TRAVELLINGMERCHANTA_TASKGROUP_0_DESC` e `_TASK_0`: «Traveling Merchant A», «Keep Open» e «keep open» sembrano stringhe di sviluppo. Tradotte senza eliminarle, preservando il suffisso A e la differenza di maiuscola iniziale.
- `QUEST_CLEARINGOUTBIGCATS_*`: la chiave menziona grandi felini, il testo parla di cacciatori corrotti e gli obiettivi chiedono di uccidere lupi corrotti. Tradotto il testo visibile, chiavi conservate.
- `QUEST_MEALYDETOUR_DESC` parla di avventurieri, mentre `QUEST_MEALYDETOUR_TASKGROUP_1_DESC` e `_TASK_0` parlano di profughi. Analoga variazione tra profughi e avventurieri nelle missioni `QUEST_CORINSFOLLOWERSI_*` e `QUEST_CORINSFOLLOWERSII_*`. Differenze conservate.
- `QUEST_AMBUSHATTHECIRCLE_TASKGROUP_1_DESC`: «Fight off the reinforcements» accompagna un obiettivo che chiede di trovare Basilton; il combattimento è nel gruppo seguente. Non riallineati i gruppi.
- `QUEST_THEHOPEFULSHEPARD_TASKGROUP_5_DESC` e `_TASK_0`: conclusione presso Befr, benché descrizione e apertura parlino del Pastore fiducioso. Potrebbe essere intenzionale; destinatario conservato.
- `QUEST_TENDERBERRYBLOOMII_DESC`: «a large harvest ... has bloomed» sovrappone raccolto e fioritura. Conservata l'immagine dell'originale.
- Le grafie anomale nelle chiavi, tra cui `THEETSNEEDED`, `TOOTHSNEEDED`, `RUINSRESEARCEHR`, `THEHOPEFULSHEPARD`, `VERSUSBENEATHTHEBARK` e `HORDEKINGSBOUNTY`, sono rimaste identiche. Anche l'ordine lessicografico dei gruppi (`10` prima di `1`) è preservato.
- Non sono state rilevate righe in portoghese in questo file.

## Verifiche

- 1.152 record in ingresso e 1.152 in uscita; UTF-8 senza BOM.
- Prima colonna identica e nello stesso ordine.
- Esattamente una tabulazione per record; nessun testo vuoto e nessun ritorno a capo interno.
- Segnaposto conservati con identica grafia e molteplicità in tutte le 36 righe interessate.
- Nessuna riga con testo lasciato identico all'inglese.
- Coerenza delle traduzioni ripetute e dei titoli citati negli obiettivi verificata.
- Controllo delle espressioni composte presenti in `reference.tsv`; sole variazioni grammaticali necessarie, ad esempio «nel Santuario» per «in the Sanctum».
- Nessun reimport o avvio del gioco eseguito, come previsto dall'incarico.
