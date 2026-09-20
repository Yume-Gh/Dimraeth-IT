# Note di consegna — dlg2

Traduzione completata: **914 righe**, UTF-8 senza BOM, nessuna intestazione.
Input e riferimento: `dlg2.tsv` e `reference.tsv`, nella stessa cartella. Continuità verificata con `dlg1.it.tsv` e `dlg1.it.note.md`.

## Voci

**Tamsin** — Voce calda, colloquiale e vivace, con esclamazioni, ripartenze, esitazioni e gesti che accompagnano il pensiero.
Il lessico del mestiere resta preciso; quando impara a porre limiti, la fermezza emerge senza cancellare la vulnerabilità o trasformarla in freddezza.

**Basilton** — Voce mite e composta, con forme distese, sentenze brevi e immagini di terra, radici, crescita, doni e cura.
La riverenza verso Ceres convive con una fermezza esplicita: corregge il giocatore senza alzare il tono e difende il valore delle vite affidate al suo giardino.

## Registri del giocatore

- HEROIC: diretto e risoluto, con frasi compiute, promesse e giudizi espliciti; conservata anche la durezza presente nell'originale.
- JOKER: colloquiale, ironico, con battute e immagini concrete; mantenute le punte sprezzanti e le battute poco opportune nei momenti dolorosi.
- SCHOLAR: preciso e analitico, attento a cause, prove, definizioni e conseguenze; lessico più ricco ma pronunciabile.
- STOIC: asciutto e controllato, senza aggiungere enfasi; non omesse informazioni quando l'originale gli assegna una battuta più lunga delle altre.

I **160 quartetti** sono stati tradotti insieme e conservano quattro rese distinte. Il controllo di unicità delle stringhe integra la revisione dei registri, ma non la sostituisce. Le differenze di contenuto già presenti fra le varianti non sono state uniformate.

## Termini nuovi e decisioni

Queste rese non modificano `reference.tsv`; sono annotate per la revisione e l'eventuale estensione del glossario.

| Inglese | Resa adottata | Nota |
|---|---|---|
| Forest Meet | Raduno della Foresta | Assemblea degli spiriti descritta da Basilton; non assimilata a un luogo già glossato. |
| Great Iniquities / Iniquity | Grandi Iniquità / Iniquità | Potenze contrapposte ai Principi Primi. |
| Old Gods | Antichi Dei | Distinti dagli Old Ones → Antichi. |
| Old Faith | Antica Fede | Denominazione delle lezioni; nel parlato non titolato, old faith / old religion → vecchia fede / vecchia religione. |
| Will | Volontà | Maiuscola nelle spiegazioni dottrinali di Tamsin; coerente con gli impieghi concettuali di `dlg1`. |
| Elven Tablet | Tavoletta Elfica | Oggetto nella Pozza del Ricordo; in descrizioni comuni anche «tavoletta» o «tavoletta elfica». |
| Eternal Forest | Foresta Eterna | Toponimo non presente nel riferimento. |
| Forest’s Edge | Margini della Foresta | Resa coerente con Forests Edge Homestead → Fattoria ai Margini della Foresta, senza aggiungere «Fattoria» dove l'originale non lo dice. |
| enchanted spindle | fuso incantato | Distinto dal telaio; lo strumento regola il filo impiegato negli stendardi. |
| ward-work | trama protettiva | Nel contesto della filatura di Tamsin; non è una nuova denominazione di oggetto. |
| enchanted soil | terra incantata | Terra del corpo di Basilton, usata per nutrire le piante. |
| fertiliser / fertilizer | fertilizzante | Uniformate le grafie britannica e americana; conservato il plurale dove presente. |
| pennant | gagliardetto | Distinto da banner → stendardo. |
| banner of light | stendardo di luce | Una delle possibili creazioni di Tamsin. |
| fish-scarecrows | spaventapasseri a forma di pesce | Rappresentazioni di JJ presso le coltivazioni, non strumenti per allontanare i pesci. |
| passing-ritual | rito di passaggio del dono | Il contesto descrive il trasferimento dei worp dal dominio di Ceres alle acque di Marina, non un'iniziazione personale. |
| memorial wall | muro dei caduti | Resa contestuale dell'invito a tornare vivi; da confermare se il luogo comprende anche altre categorie di defunti. |
| The Wildwood Golem | Il Golem di Wildwood | Titolo di Basilton. |
| The Earlwood Banner Weaver | La Tessitrice di Stendardi di Earlwood | Titolo di Tamsin. |

**Terminologia già fissata:** stendardo protettivo, pietra protettiva, gemma del custode, linfa dell'albero antico, acqua toccata dalle driadi, Libro degli incantesimi, Principi Primi, Re della Foresta, Trono della Foresta, Pozza del Ricordo, Corte dei Frammenti, Crisi dei Goblin, Varco e Santuario. Applicate anche le forme plurali e le varianti di apostrofo. `Rivercaller`, `Glimmerflax`, `Tenderberry` e `Thaumablossom` restano invariati secondo il riferimento. `Worp Plant` diventa «Pianta di Worp»; il sostantivo comune plurale resta «worp».

**Nomi propri:** Acorn resta invariato, secondo la decisione esplicita di `dlg1`. Mantenuti anche Fairweather, Duratianus, Aldoron, Mor’daneth, Elaria, Adlan, Agir, Marina, Akolasis e JJ. Tender, Plump, Rosary e Dandelion sono conservati come nomi individuali delle piante personificate da Basilton, non tradotti come specie botaniche. `Scriptura Principiorum` resta il titolo latino del testo. `Numen realm` mantiene «regno di Numen», già adottato in `dlg1`. Nel binomio «Adlan, giustizia. Ira, ira.» il secondo «ira» è il dominio del dio, in continuità con `dlg1`.

## Passaggi dubbi e particolarità dell'originale

### Piante indicate con pronomi impliciti

Nel saluto sul giardino malato, «They speak to Acorn and me» non nomina esplicitamente le piante. Il contesto delle aiuole e le successive risposte le identificano come referente; adottato il femminile plurale. Nel lutto per la singola pianta, invece, Basilton usa «him»: conservata la personificazione maschile tramite «germoglio» e i relativi pronomi.

- Riga 3: `NPC_BASILTON_GREETING_24aa2568-63a5-405d-bd58-71ac5a12f817`
- Riga 366: `NPC_BASILTON_RESPONSE_5d2b31d3-08a7-45db-bf33-77cb2fe4bf80`
- Riga 379: `NPC_BASILTON_RESPONSE_87db223b-941b-49fb-b64a-889ee6f1bc76`

### «lesser gods to Ceres and her lord» e «supremacy of the will»

La prima costruzione inglese non specifica con precisione il rapporto gerarchico: resa «divinità minori al servizio di Ceres e del suo signore». Non aggiunto il nome Agir, pur menzionato da Tamsin in un altro ramo. La lotta per la «supremacy of the will» è resa come lotta per imporre la propria volontà; non introdotta una meccanica di gioco ulteriore. Entrambe le interpretazioni meritano conferma nel contesto cosmologico.

- Riga 429: `NPC_BASILTON_RESPONSE_fde29186-6b24-48e2-916a-3a05bb08dc0f`

### Racconto di JJ: esche, ami e pesce

«Double worps» è reso come una doppia dose di worp su ciascun lato della barca. L'inglese passa poi a quattro esche ma due ami: mantenute entrambe le quantità, senza correggere una possibile distinzione fra esche e ami. «The fish guided them home» può indicare JJ oppure i pesci collettivamente: scelto il singolare «il pesce», in base al ruolo di JJ nel racconto; da confermare.

- Riga 826: `NPC_TAMSIN_RESPONSE_3740b998-3db4-4776-b386-445d4d11df8e`

### Rito del dono e significato di Forest’s Edge

«Passing-ritual» è insolito e non definito altrove nel lotto: esplicitato il passaggio del dono tra i due domini divini. «Forest’s Edge» potrebbe essere la zona della Fattoria ai Margini della Foresta o un'indicazione geografica più ampia: conservata la forma breve, senza identificazioni aggiunte.

- Righe 886 e 896: `NPC_TAMSIN_RESPONSE_b13e1979-996a-4e95-8417-10d6e06fadde`, `NPC_TAMSIN_RESPONSE_cb3c0539-9163-4078-9d16-95354977a788`
- Righe 836, 845 e 869: `NPC_TAMSIN_RESPONSE_471a421d-57de-4864-80b9-00308309ef9d`, `NPC_TAMSIN_RESPONSE_58065457-1632-4811-86d7-cf764fb106f1`, `NPC_TAMSIN_RESPONSE_9c3379be-b2ee-466a-9158-4da95ad6ebc7`

### Rivenditore: singolare e plurale

Nella ricerca si alternano «someone», «them», «they», mentre il ritrovamento e le conseguenze parlano di «him». Non è chiaro dal TSV se il plurale indichi più complici o sia un pronome neutro inglese. Conservata l'alternanza del testo: plurale nelle accuse e nella ricerca, singolare maschile una volta identificato il rivenditore. Non aggiunti complici espliciti.

- Riga 654 e relativo quartetto: `NPC_TAMSIN_PLAYER_8c273ec5-2f2f-421e-bd94-25916d1c874e_HEROIC`
- Riga 840: `NPC_TAMSIN_RESPONSE_4b9488e5-5f33-4996-b241-317865172dc8`
- Riga 870: `NPC_TAMSIN_RESPONSE_9d43daa4-bbc2-4c5e-94eb-0bda6939fc66`
- Riga 875: `NPC_TAMSIN_RESPONSE_a14c25dd-fe48-4d04-a307-3bfecc11c28b`

### Golem e accademia

Basilton dice di essere l'unico golem nato a Wildwood e di non averne mai incontrato uno della propria taglia o longevità. Tamsin ricorda invece un professore golem all'Accademia: non è una contraddizione, perché cambia l'ambito geografico e Basilton non nega l'esistenza dei golem altrove. Mantenuti i limiti delle sue affermazioni.

- Righe 357 e 385: `NPC_BASILTON_RESPONSE_3cbce591-68cb-453e-8a85-0fbc80545925`, `NPC_BASILTON_RESPONSE_94fe520a-dd57-4da7-bfc0-a741866dd359`
- Riga 820: `NPC_TAMSIN_RESPONSE_202936c6-c3e4-4e51-be59-fb3dfc3217ab`

### Oscillazioni fra varianti di tono

Alcuni quartetti non sono semplici riscritture della stessa proposizione. Per esempio, nella reazione alle dimensioni di Basilton, HEROIC le presenta come un vantaggio di forza, mentre le altre varianti negano che lo rendano meno golem. Inoltre alcune righe STOIC sono più lunghe delle altre. Conservate queste differenze, senza imporre al contenuto una coerenza assente dall'originale.

- Righe 224–227: `NPC_BASILTON_PLAYER_a0eb3452-86c5-44b9-a6a7-6c9e2c5036ac_HEROIC` e le altre tre varianti.
- Riga 54: `NPC_BASILTON_PLAYER_21ff9083-1b2a-4bf5-b586-a2ea3a0f6006_STOIC`
- Riga 771: `NPC_TAMSIN_PLAYER_e98b9eb5-5e2a-4e2c-9795-6eeada72628b_STOIC`

### Punteggiatura, grammatica e identificatori

Alcune domande `_BASE` non hanno punto interrogativo; integrata la punteggiatura italiana. «I am sure your parents worried sick about you» manca dell'ausiliare: interpretato come preoccupazione attuale, coerentemente con le altre varianti. Le chiavi con identificatori inconsueti sono state conservate alla lettera.

- Riga 126: `NPC_BASILTON_PLAYER_6295b246-8560-4b0e-854e-3c904721331d_BASE`
- Riga 577: `NPC_TAMSIN_PLAYER_5a20e342-e3cb-439f-a113-90ce3bb6231d_STOIC`
- Righe 649 e 658: `NPC_TAMSIN_PLAYER_89408d7d-f0d2-486a-affa-98ab016f6f80_BASE`, `NPC_TAMSIN_PLAYER_8c81b8f6-6be0-421a-bc51-b4b52098d7e3_BASE`
- Riga 6: `NPC_BASILTON_GREETING_dffgddf-d3fc-4850-a6f4-c172bfa0d474`
- Riga 705: `NPC_TAMSIN_PLAYER_aB7k9D2f-X3pQ-8mL0-zT5v-Nc92Hq7R4yKs_BASE`

## Verifica finale

- 914 record: Basilton 430, Tamsin 484; chiavi identiche all'input e nello stesso ordine.
- Due colonne per record, separate da una sola tabulazione; nessun testo vuoto o ritorno a capo interno.
- **966 occorrenze di segnaposto**, identiche per valore e molteplicità in ciascuna riga.
- Nessuna riga coincidente con l'inglese; traduzione e revisione linguistica di tutti i blocchi. La scansione aggiuntiva non ha rilevato residui dei comuni indicatori inglesi controllati.
- 160 quartetti contigui nell'ordine HEROIC, JOKER, SCHOLAR, STOIC; 640 rese distinte all'interno dei rispettivi quartetti.
- 57 righe `_BASE`. I restanti 217 record comprendono 204 `_RESPONSE`, 11 `_GREETING` e 2 `_TITLE`.
- Blocchi: 1–130, 131–263, 264–393, 394–526, 527–657, 658–789, 790–914. Nessun quartetto spezzato.
- Controllo terminologico con il riferimento, comprese forme plurali e apostrofi tipografici; controllo automatico aggiuntivo su 35 termini e nomi rilevanti.
- Identiche traduzioni per i testi inglesi integralmente ripetuti e per i segmenti narrativi lunghi ripetuti nei diversi rami. Conservati gli asterischi delle didascalie.
- File scritto direttamente con `Path.write_text(..., encoding="utf-8")`, senza pipe PowerShell; riapertura con decodifica UTF-8 rigorosa, assenza di BOM e di caratteri sostitutivi, presenza verificata di tutti gli accenti `à è é ì ò ù`.
- Nessuna modifica all'input, al glossario o al lotto precedente.

Non è stata eseguita una prova nel gioco né un'importazione: la consegna riguarda il TSV e le note. I dubbi narrativi sopra indicati restano da verificare nei rispettivi rami interattivi.

**Criterio riutilizzabile:** il confronto terminologico deve normalizzare gli apostrofi e riconoscere i plurali, ma rispettare i confini di parola: `forest kin` non deve scattare su `Forest King`. La distinzione dei registri richiede la lettura congiunta dei quartetti; conteggi, unicità e confronto dei segnaposto sono controlli complementari.
