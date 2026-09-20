# Note di consegna — dlg4

Traduzione completata: **1.279 righe**, UTF-8 senza BOM, nessuna intestazione.
Input e riferimento: `dlg4.tsv` e `reference.tsv`, nella stessa cartella. Modello di qualità e formato: `dlg2.it.tsv` e `dlg2.it.note.md`; consultati anche i lotti precedenti e, per le corde con campanelli, le missioni già tradotte.

## Voci

**Heimenthaldrik / Heimen** — Parlato popolare panitaliano, caldo e sentenzioso, con la precisione di chi studia testi antichi. La marca è stata spostata dalla pronuncia inglese alla sintassi: frasi coordinate, riprese brevi, ellissi, troncamenti sobri dell'infinito («parlar», «frugar», «tener»). Conservate le immagini di pietra, vena, scalpello, inchiostro e bottega già presenti nel testo. Nessun dialetto regionale, nessuna storpiatura ortografica, nessun «voi» per `ye`. Non occorre deformare ogni frase per far sentire la voce.

La scelta è stata fissata sui dieci esempi densi iniziali delle risposte (844–846 e 848–854), prima di tradurre il blocco esteso, e registrata in `dlg4_work/voice_decision.md`. `Aye` alterna «sì», «eh sì», «proprio così» secondo l'intenzione; `ye` diventa «tu» o soggetto sottinteso. Le didascalie restano narrative. Le 381 righe del giocatore rivolte a lui hanno esclusivamente il registro della loro variante, senza acquisire quello del nano. I passaggi filosofici conservano tutti gli interrogativi: il parlato popolare non implica semplificarne il contenuto.

| Prima: inglese | Dopo: italiano | Soluzione |
|---|---|---|
| Aye. Judge me by the work. I’ll stand by it. | Proprio così. Giudicami dal lavoro. Ne rispondo io. | Tre frasi brevi; responsabilità concreta dell'artigiano, nessuna imitazione d'accento. |
| I’ve not shied from a bit of ruin-divin’. | Non mi sono tirato indietro quando c'era da frugar tra le rovine. | Locuzione colloquiale e infinito troncato al posto del gerundio foneticamente marcato. |
| Aye, Heimen Thaldrik, son o’ stone and stubborn ink. A poet by heart, a dreamweaver by trade. | Sì, Heimen Thaldrik, figlio della pietra e d'inchiostro testardo. Poeta nel cuore, tessitore di sogni per mestiere. | Conservate le immagini materiali e il parallelismo, senza calcare `o’`. |
| I remember walkin’ those halls, readin’ the inscriptions, and knowin’ I was watched. | Ricordo quelle sale. Ci camminavo, leggevo le iscrizioni e sapevo che qualcuno mi osservava. | La catena di gerundi diventa una ripresa breve seguita da coordinate. |

Chiavi degli esempi, rispettivamente:

- Riga 844: `NPC_HEIMENTHALDRIK_RESPONSE_039c49c8-ce5a-4cb1-91c1-77c173f4568f`
- Riga 850: `NPC_HEIMENTHALDRIK_RESPONSE_0b0fcdd3-f34f-48ea-ab4f-55b7d4230c6b`
- Riga 854: `NPC_HEIMENTHALDRIK_RESPONSE_2306010f-e5b7-4f8b-bdc5-53c4cd5c13f5`
- Riga 852: `NPC_HEIMENTHALDRIK_RESPONSE_1b272e79-8c53-4fda-8e84-2a39d4430aed`

**Befr** — Italiano pieno, cortese e lievemente cerimonioso. Conservati la teatralità dei gesti, le immagini vegetali, la cordialità e la fermezza del mercante quando si parla di lavoro. Tutti i 62 `my friend` sono «amico mio»; le grafie della risata sono uniformate a «Ho ho!» (conteggio dell'originale precisato più avanti).

**Rahaner** — Frasi corte e chiuse, spesso in coppia: «Essere pronti serve. Averne nostalgia è pericoloso». Gli ordini restano operativi; nel ricordo del servizio sono conservati dovere, capacità, resistenza e responsabilità per il sangue versato, senza aggiungere nostalgia affettuosa o orgoglio.

## Registri del giocatore

- HEROIC: diretto, risoluto, frasi compiute; promesse, dovere e giudizi espliciti, compresa la durezza dell'originale.
- JOKER: colloquiale, ironico, immagini comiche e battute anche fuori luogo; non attenuate le risposte sprezzanti.
- SCHOLAR: preciso e analitico, attento a prove, criteri, cause e conseguenze. Sintassi pronunciabile, senza introdurre erudizione assente.
- STOIC: breve e controllato; conservate le informazioni essenziali anche quando l'originale assegna una battuta più lunga del consueto.

I **226 quartetti** sono stati letti e tradotti insieme, senza dividerli tra blocchi. Contengono quattro rese distinte ciascuno. Il controllo di unicità delle stringhe è un controllo complementare: la revisione del registro è stata svolta sulle quattro battute affiancate.

Esempio, richiesta sulle esercitazioni (1149–1152):

| Tono | Resa |
|---|---|
| HEROIC | Esercitazioni. Cosa mi offrono che il campo di battaglia non possa darmi? |
| JOKER | Esercitazioni. Stessi lividi di uno scontro, meno goblin. Dov'è il bello? |
| SCHOLAR | Esercitazioni invece di esperienza sul campo. Cosa migliorano che il combattimento non migliori? |
| STOIC | Esercitazioni. Perché non combattere e basta? |

Le 79 righe `_BASE` restano neutre. Le differenze di contenuto fra varianti non sono state eliminate per renderle più simili.

## Termini nuovi e decisioni

Queste rese non modificano `reference.tsv`. I nomi e i termini non presenti nel riferimento sono riportati per la revisione e l'eventuale promozione.

| Inglese | Resa | Nota |
|---|---|---|
| Mount Grandor | Monte Grandor | Conservato il nome proprio; tradotta soltanto la designazione geografica. |
| Lumen Realm | regno di Lumen | Non corretto in Numen: il lotto scrive Lumen. Vedi i dubbi sotto. |
| Faustas's Rest | Riposo di Faustas | Toponimo distinto testualmente da Faustas's Tower → Torre di Faustas. Possibile denominazione pregressa: da verificare in gioco. |
| Elven Imperial era | era imperiale elfica | Denominazione storica, senza introdurre un nuovo nome di impero. |
| Emissary / Emissaries | Emissario / Emissari | Maiuscola dove l'originale tratta la funzione divina come titolo; continuità semantica con gli «emissari» dei lotti precedenti. |
| dreamweaver | tessitore di sogni | Autodefinizione poetica di Heimen, non presentata come una classe di gioco. |
| by stone and song | per la pietra e il canto | Formula caratteristica del nano. |
| Scroll of Retraining | Pergamena di Riaddestramento | Nome citato nel dialogo, non trovato nel riferimento né fra i nomi degli oggetti esportati. Da confermare nel gioco. |
| Skill Return Scroll | Pergamena di Recupero Abilità | Stessa riserva del nome precedente; non sostituito con un oggetto diverso presente nel catalogo. |
| Skill Return Book | Libro di Recupero Abilità | Stessa riserva; conservata la distinzione fra libro e pergamena. |
| Adventurers’ Guild | Gilda degli Avventurieri | Espansione della denominazione già fissata «Gilda»; non implica un'organizzazione unica, che Rahaner nega esplicitamente. |
| new blood | recluta | Appellativo ricorrente di Rahaner; grammaticalmente femminile ma riferibile a entrambi i sessi, senza accordi femminili sul giocatore. |
| The Travelling Merchant | Il Mercante Itinerante | Titolo di Befr. |
| Dwarven Poet | Poeta Nanico | Titolo di Heimen. |
| The Earlwood Guild Trainer | L'Addestratore della Gilda di Earlwood | Titolo di Rahaner. |

**Continuità con testi già installati:** `bell-line(s)` → «corda/corde con campanelli», già in `it/Quests.csv`, chiavi `QUEST_YARDANDCODE_TASKGROUP_1_DESC` e `..._TASK_0`–`..._TASK_3`. Per `bell-line traps`, «trappole con corde e campanelli». Non confuso con `bell-tab` → «campanello segnalatore».

**Terminologia vincolante applicata:** Nano/Nani, Treant, Goblin, Corrotto/Corruzione, Varco, Santuario, Libro degli incantesimi, Antichi, Antichi Dei, Iniquità, Foresta Eterna, Re della Foresta, Principi Primi, Purga Elfica, alberi Everlast, fertilizzante, Sede della Gilda, Pino di Wildwood, pietra del cammino. `way-stones` è la variante con trattino e plurale di `waystone`: resa «pietre del cammino», senza inventare un termine nuovo. Nomi personali conservati, compresi Erynor e Armin.

**Omonimie del riferimento:** le etichette dell'interfaccia non sono sostituzioni indiscriminate della prosa. `deed` nella riflessione storica (704) indica un'azione, non un Incarico; `straight` in «straight to the ledger» non indica né il Diretto del pugilato né una combinazione di carte; `will` può essere verbo o volontà. `acorn` nella battuta del giocatore (786) è la ghianda comune, non il nome dello scoiattolo. Nessuna alterazione delle rese canoniche quando il termine designa davvero l'oggetto o la meccanica.

## Genere del giocatore

Prima scelta: aggirare l'accordo quando l'italiano resta naturale. Esempi effettivi: «Eccoti a casa» nei saluti di Befr; «Ho salvato la pelle per un soffio» (492); «Ho salvato la pelle a stento» (1021); «Non sono alle prime armi» (1147–1148); «quando hai messo piede qui» (1224, 1234, 1255); «Quando vuoi cominciare» (1237). `Sono d'accordo`, `felice`, `capace` e `viandante` non fissano il sesso del giocatore.

I maschili conservati sono soprattutto appellativi e nomi di relazione. «Amico mio» è imposto dal brief: **62 occorrenze in 49 righe**, tutte elencate qui. Nella colonna delle note sono indicati anche gli altri maschili della stessa riga.

| Riga | Chiave | Maschile conservato |
|---|---|---|
| 1 | `NPC_BEFR_GREETING_0185671-7cc0-4745-ada8-a32aa6e1a811` | amico mio × 1; vecchio compagno (similitudine) |
| 3 | `NPC_BEFR_GREETING_877f3d34-f6c2-402f-87c0-3a3c8304cf01` | amico mio × 1 |
| 4 | `NPC_BEFR_GREETING_M8n7b-6c97-4438-9b45-1d973e69f2a0` | amico mio × 1 |
| 5 | `NPC_BEFR_GREETING_c1ad0d31-6c97-4438-9b45-1d973e69f2a0` | amico mio × 1 |
| 359 | `NPC_BEFR_RESPONSE_0212bf0a-0787-416a-b899-c4a0d7419f8e` | amico mio × 1 |
| 362 | `NPC_BEFR_RESPONSE_051f25fa-2aae-4b17-9568-0dd81cefe854` | amico mio × 2 |
| 366 | `NPC_BEFR_RESPONSE_0ab69d08-89aa-429c-851b-279460a0e0c3` | amico mio × 1 |
| 368 | `NPC_BEFR_RESPONSE_0f92ff0f-4971-4049-82d4-f4ea7aa831e6` | amico mio × 2; un eroe, un buon amico di Befr |
| 369 | `NPC_BEFR_RESPONSE_11571785-af5d-48e1-af46-79e7c43d71c1` | amico mio × 1 |
| 370 | `NPC_BEFR_RESPONSE_14026b6c-68fc-4d72-bbda-cefe18ce4815` | amico mio × 1 |
| 372 | `NPC_BEFR_RESPONSE_17c9f86a-0de1-4c5a-99ef-c3ac9d5c676f` | amico mio × 1 |
| 375 | `NPC_BEFR_RESPONSE_25973546-a0d7-4872-8b74-48ff076b8667` | amico mio × 1 |
| 376 | `NPC_BEFR_RESPONSE_298b7408-b401-47cf-b8f7-98a86c09b317` | amico mio × 2 |
| 377 | `NPC_BEFR_RESPONSE_29e00116-deef-4c56-a389-8a5712895fe2` | amico mio × 1 |
| 378 | `NPC_BEFR_RESPONSE_2d41bb0d-7cd0-4c15-9638-0b320962f07f` | amico mio × 1; un eroe, un buon amico di Befr |
| 379 | `NPC_BEFR_RESPONSE_2d7162cc-3f0b-45a2-987f-1cc33e9a5fd8` | amico mio × 1 |
| 382 | `NPC_BEFR_RESPONSE_3e3743c9-9588-4196-b9a8-cfb1d4c41475` | amico mio × 1 |
| 386 | `NPC_BEFR_RESPONSE_49dd76a5-60b9-4b29-acf5-d537ce889189` | amico mio × 1 |
| 388 | `NPC_BEFR_RESPONSE_4c8881cd-4904-4d96-b78e-2b74e3b1a0f8` | amico mio × 2 |
| 389 | `NPC_BEFR_RESPONSE_4ca3459c-ce9e-4c3b-bca7-2fcee700112b` | amico mio × 2; mio abilissimo compagno |
| 390 | `NPC_BEFR_RESPONSE_4ce65f3f-66df-4fcf-b871-17731bc1b8d0` | amico mio × 1 |
| 391 | `NPC_BEFR_RESPONSE_4eb18059-e89c-4a4f-8f51-d19147e6e5dc` | amico mio × 1 |
| 396 | `NPC_BEFR_RESPONSE_61e63cfa-92b6-4a60-9629-2f4dbfc412fc` | amico mio × 1 |
| 398 | `NPC_BEFR_RESPONSE_68ef03af-4d05-44ce-88b2-f419cf83dcf8` | amico mio × 1 |
| 399 | `NPC_BEFR_RESPONSE_69279dbf-ca98-44eb-9a06-cdaff81d5570` | amico mio × 1 |
| 402 | `NPC_BEFR_RESPONSE_71f15e5c-8076-4343-9145-0b69cfb4be7e` | amico mio × 2 |
| 404 | `NPC_BEFR_RESPONSE_781ba44a-0bac-4c1e-8056-67420ea0519d` | amico mio × 2 |
| 405 | `NPC_BEFR_RESPONSE_7b5e726e-257a-40b0-9603-d352db5602e1` | amico mio × 1 |
| 409 | `NPC_BEFR_RESPONSE_8b69c4ea-53b8-4fc6-ada2-97f31be76df2` | amico mio × 1 |
| 411 | `NPC_BEFR_RESPONSE_8dee24c4-b506-40fc-ad7e-0791081a3851` | amico mio × 1 |
| 412 | `NPC_BEFR_RESPONSE_9356993d-f18e-4779-81d3-e5684a44ac8c` | amico mio × 2 |
| 413 | `NPC_BEFR_RESPONSE_95d2f952-f458-4d26-945b-14da4c995c4b` | amico mio × 1; amico |
| 417 | `NPC_BEFR_RESPONSE_a2b9ea84-6c1c-47ed-9331-a6b874a4c2d4` | amico mio × 1 |
| 418 | `NPC_BEFR_RESPONSE_a44308ff-3ce2-4dad-aea7-326cad78ecc7` | amico mio × 1 |
| 420 | `NPC_BEFR_RESPONSE_a58f9b2f-e31b-4514-8779-ab6c9ebf54e1` | amico mio × 1 |
| 421 | `NPC_BEFR_RESPONSE_a8e5ef1c-8f49-49e6-a7b7-61fc0fa3f633` | amico mio × 1 |
| 422 | `NPC_BEFR_RESPONSE_a99cb744-65bc-4f36-8011-aec5a95afe5b` | amico mio × 1 |
| 423 | `NPC_BEFR_RESPONSE_abb0e7ae-5a38-4b18-9131-d387436f2a9b` | amico mio × 1 |
| 425 | `NPC_BEFR_RESPONSE_b01a12e8-1b06-48e9-8de0-22a1161a1a74` | amico mio × 1 |
| 426 | `NPC_BEFR_RESPONSE_b29534e5-b8d6-44fa-98bd-4d55153b2107` | amico mio × 2; mio abilissimo compagno |
| 429 | `NPC_BEFR_RESPONSE_b3595b77-471a-436d-ac3c-b7a36c9e35a2` | amico mio × 2 |
| 430 | `NPC_BEFR_RESPONSE_ba11cf6c-db0c-4bab-91c5-b1fda849e436` | amico mio × 2 |
| 436 | `NPC_BEFR_RESPONSE_d1084584-9e44-4b5f-aa06-170a1206a8c9` | amico mio × 1 |
| 441 | `NPC_BEFR_RESPONSE_e0161d95-8915-4792-96ee-879305bdb806` | amico mio × 1 |
| 442 | `NPC_BEFR_RESPONSE_e3ab8df8-573f-4caf-b10d-8ed971832a91` | amico mio × 1 |
| 444 | `NPC_BEFR_RESPONSE_e44d7c2a-6df6-4a6a-9b19-99e1d867b9d9` | amico mio × 1 |
| 447 | `NPC_BEFR_RESPONSE_e9434b8f-c096-4578-a111-efd6a47b51ad` | amico mio × 1 |
| 448 | `NPC_BEFR_RESPONSE_eb7b9d30-d3d5-4914-b397-4960295f85bf` | amico mio × 2 |
| 452 | `NPC_BEFR_RESPONSE_fb5532df-636f-4228-9a3a-3d8709fce572` | amico mio × 2 |

Altri appellativi o riferimenti maschili al giocatore:

| Riga | Chiave | Forma / motivo |
|---|---|---|
| 2 | `NPC_BEFR_GREETING_0eea57b1-7cc0-4745-ada8-a32aa6e1a811` | amico |
| 363 | `NPC_BEFR_RESPONSE_05c1c03c-2118-409f-9bb5-ed0e3a9daddf` | amico |
| 407 | `NPC_BEFR_RESPONSE_81892444-4b76-4483-a6c4-566bd9705eda` | amico |
| 410 | `NPC_BEFR_RESPONSE_8d260c3e-d0b5-4e77-9103-0d84ac3c45d9` | amico |
| 435 | `NPC_BEFR_RESPONSE_cc0f1f86-0bea-4885-80df-e8dbbc5f6371` | amico |
| 453 | `NPC_BEFR_RESPONSE_fbd78655-22ef-4285-bf7e-5e4fc3f5730b` | amico |
| 456 | `NPC_HEIMENTHALDRIK_GREETING_1153ff1b-94a1-4891-8b30-b7626a9e7a69` | amico |
| 461 | `NPC_HEIMENTHALDRIK_GREETING_c3f8b9c1-23a7-41b2-bdf7-97fa7c2ea3f9` | straniero; vecchio amico nella similitudine narrativa |
| 462 | `NPC_HEIMENTHALDRIK_GREETING_f2e134e0-2071-4d90-9076-c307bcda4661` | amico |
| 477 | `NPC_HEIMENTHALDRIK_PLAYER_0d16f0b3-292b-46a4-bf5e-9eae25d24acc_HEROIC` | dei degni: appartenenza alla categoria menzionata da Heimen |
| 478 | `NPC_HEIMENTHALDRIK_PLAYER_0d16f0b3-292b-46a4-bf5e-9eae25d24acc_JOKER` | fra i degni |
| 479 | `NPC_HEIMENTHALDRIK_PLAYER_0d16f0b3-292b-46a4-bf5e-9eae25d24acc_SCHOLAR` | Degno, secondo il suo criterio |
| 480 | `NPC_HEIMENTHALDRIK_PLAYER_0d16f0b3-292b-46a4-bf5e-9eae25d24acc_STOIC` | uno dei degni |
| 880 | `NPC_HEIMENTHALDRIK_RESPONSE_521989f3-4155-43b9-a6dc-646f1a3cbbeb` | amico |
| 887 | `NPC_HEIMENTHALDRIK_RESPONSE_60cae554-65dc-468d-946d-3ea1e85f0d50` | amico |
| 888 | `NPC_HEIMENTHALDRIK_RESPONSE_61c00505-dcb4-4690-a0fa-33b281595f35` | amico |
| 890 | `NPC_HEIMENTHALDRIK_RESPONSE_6776e723-3326-4641-8835-3a096cfa0318` | amico |
| 892 | `NPC_HEIMENTHALDRIK_RESPONSE_68f104b0-50ad-4c32-8916-f7c02d9ea0bf` | un alleato fidato |
| 912 | `NPC_HEIMENTHALDRIK_RESPONSE_9802343e-9de7-44ed-9a60-0f37a1947819` | amico |
| 915 | `NPC_HEIMENTHALDRIK_RESPONSE_9cfce4ec-cb8e-4028-8001-f219207bbd60` | amico |
| 921 | `NPC_HEIMENTHALDRIK_RESPONSE_ae03b010-ae3f-4766-a51f-8bae2330e8df` | amico |
| 922 | `NPC_HEIMENTHALDRIK_RESPONSE_afc20315-c892-4b2e-a816-a21e085ce094` | un alleato fidato |
| 925 | `NPC_HEIMENTHALDRIK_RESPONSE_b23134dd-2339-40ce-adf8-a19666b2e475` | amico |
| 938 | `NPC_HEIMENTHALDRIK_RESPONSE_ea7920ac-b9bd-48e5-925a-5d3a458cc333` | amico |
| 939 | `NPC_HEIMENTHALDRIK_RESPONSE_ea9882cc-6347-42d2-84a0-c4c5fccee292` | un alleato fidato |
| 1238 | `NPC_RAHANER_RESPONSE_631e4e7d-50e2-46d1-83b8-7e7677f37b2c` | avventuriero |
| 1264 | `NPC_RAHANER_RESPONSE_c6adf253-c4a1-4199-9000-2a56b43f2b79` | avventuriero |

Accordi collettivi che comprendono il giocatore: «uniti / pronti» con Heimen (572); «soli» riferito alla condizione dei mortali (643); «riusciti» riferito al gruppo impegnato nella difesa (968); «inesperti / pronti» nell'istruzione rivolta al gruppo di novizi (1217, 1246). Sono maschili plurali collettivi, non femminili assegnati al protagonista.

- Riga 572: `NPC_HEIMENTHALDRIK_PLAYER_520a9bc0-5d27-4610-a9b1-64e75b1dbdb1_HEROIC`
- Riga 643: `NPC_HEIMENTHALDRIK_PLAYER_7942bb7d-0b9b-4759-b6e3-e45b3a484651_SCHOLAR`
- Riga 968: `NPC_RAHANER_PLAYER_1650d2d1-4de2-4863-9e9f-3dce2ff19f53_JOKER`
- Riga 1217: `NPC_RAHANER_RESPONSE_2adf05ab-644f-4e54-b4f4-a85bdb223a0d`
- Riga 1246: `NPC_RAHANER_RESPONSE_79511860-3c34-4ecf-8d2e-9fe5311e04fa`

«Degno» nella risposta 388 riguarda invece Befr, che riprende il giudizio espresso dal giocatore: non è un accordo sul protagonista. Gli accordi su Saqi e Myrll restano femminili; «saldo / solido» riferiti a un luogo e i participi concordati con oggetti recuperati non sono stati scambiati per accordi sul giocatore.

## Passaggi dubbi e particolarità dell'originale

### Lumen, Numen e Riposo di Faustas

Befr parla di `Lumen Realm`; i lotti precedenti usano anche `Numen realm`. Mancano elementi per identificarli o correggere l'uno nell'altro. Conservato «regno di Lumen».

- Riga 428: `NPC_BEFR_RESPONSE_b30a3865-62e5-4d10-a67e-099b532cd81c`
- Riga 450: `NPC_BEFR_RESPONSE_ecb950b7-b0e6-4a86-871a-8965447fd7a2`

Rahaner nomina `Faustas's Rest`, assente dal riferimento, mentre Alaric parla della `Faustas's Tower` e l'interfaccia esportata associa la chiave `AREA_FAUSTASREST` al testo «Earlwood». È una possibile incoerenza di denominazioni dell'originale, non la prova che i tre nomi siano intercambiabili. Adottato «Riposo di Faustas», senza sostituirlo arbitrariamente con la Torre di Faustas o Earlwood.

- Riga 1187: `NPC_RAHANER_PLAYER_f65b9696-f8a8-42b1-8473-e77ea3c87e76_HEROIC`
- Riga 1188: `NPC_RAHANER_PLAYER_f65b9696-f8a8-42b1-8473-e77ea3c87e76_JOKER`
- Riga 1189: `NPC_RAHANER_PLAYER_f65b9696-f8a8-42b1-8473-e77ea3c87e76_SCHOLAR`
- Riga 1190: `NPC_RAHANER_PLAYER_f65b9696-f8a8-42b1-8473-e77ea3c87e76_STOIC`

### Oggetti di riassegnazione

I tre nomi nella risposta di Rahaner non compaiono in `reference.tsv` e non sono stati trovati fra i nomi degli oggetti esportati. Il catalogo contiene invece un `Elixir of Rebirth` relativo agli attributi: non c'è base per usarlo al posto delle tre risorse dichiarate dal dialogo. Conservati tre nomi distinti con le rese in tabella. Serve una verifica in gioco per sapere se siano nomi obsoleti, oggetti futuri o contenuti non esportati.

- Riga 1253: `NPC_RAHANER_RESPONSE_982a9838-9f45-4a89-a758-0f3815878b23`

### Il braccio di Rahaner

Il saluto 953 descrive esplicitamente il suo unico braccio. Il saluto 952 e le risposte 1207 e 1214 gli fanno invece incrociare «le braccia». Incoerenza anatomica già inglese: conservate le didascalie e segnalata, senza inventare protesi o correggere il gesto in silenzio.

- Riga 952: `NPC_RAHANER_GREETING_12055d53-3dcf-4bb1-9e2f-52a7599b80bb`
- Riga 953: `NPC_RAHANER_GREETING_7fa56c56-287b-462b-8442-60f5c4ddfcf3`
- Riga 1207: `NPC_RAHANER_RESPONSE_13b27ed4-e0bb-4b4c-8100-96401351d8fd`
- Riga 1214: `NPC_RAHANER_RESPONSE_2224d9de-8a99-4fc8-9ba6-362982a101c4`

### La poesia di Erynor e la cronologia

Il poema annuncia di raggiungere un ultimo lettore e si dichiara «perduto nell'eternità». La contraddizione è discussa esplicitamente dalle risposte del giocatore: mantenuta, insieme alla riflessione di Heimen sul futuro non conoscibile. Non aggiunte rime italiane che avrebbero cambiato il contenuto. `Yours is a kind` diventa «La tua è una stirpe», riferito al lettore nano Heimen, non al giocatore.

- Riga 862: `NPC_HEIMENTHALDRIK_RESPONSE_2eb97d96-753f-41c1-a837-2bb7e1cd4188`
- Riga 893: `NPC_HEIMENTHALDRIK_RESPONSE_6e0d46cb-9c6f-4ac3-9b71-d0173b67e9c3`
- Riga 802: `NPC_HEIMENTHALDRIK_PLAYER_eabb2061-dc7a-459a-b9fc-51a829d36881_HEROIC`
- Riga 803: `NPC_HEIMENTHALDRIK_PLAYER_eabb2061-dc7a-459a-b9fc-51a829d36881_JOKER`
- Riga 804: `NPC_HEIMENTHALDRIK_PLAYER_eabb2061-dc7a-459a-b9fc-51a829d36881_SCHOLAR`
- Riga 805: `NPC_HEIMENTHALDRIK_PLAYER_eabb2061-dc7a-459a-b9fc-51a829d36881_STOIC`

L'albero è descritto come abbattuto dagli abitanti; il successivo racconto sulle mura cita un attacco di cinquant'anni prima. Non è detto esplicitamente che quel singolo albero sia stato abbattuto proprio allora: mantenuta l'associazione narrativa senza aggiungere una data all'abbattimento. Il paradosso «fare ciò che riteniamo giusto / alla fine sarà giusto» è lasciato come dubbio morale del personaggio, non riscritto in una tesi più coerente.

- Riga 901: `NPC_HEIMENTHALDRIK_RESPONSE_7decc159-43c2-47ff-961d-dae214e1aa9e`
- Riga 948: `NPC_HEIMENTHALDRIK_RESPONSE_fbe397b3-b6cb-42f1-8b13-e3f360a9375d`
- Riga 894: `NPC_HEIMENTHALDRIK_RESPONSE_709fcb45-4d19-4f2a-b916-6a227b18e2a7`
- Riga 949: `NPC_HEIMENTHALDRIK_RESPONSE_fcd1610e-f187-47c5-89d3-b5df34bb9c9f`

### Pronomi e metafore operative

Nel quartetto su Sylbos (31–34), `it` rimanda verosimilmente alla corruzione. Usati «con tutto questo» e costruzioni con «ne/ci» per evitare di fissare un genere pronominale sbagliato. Nella lode di Befr, `the road pushed back` (399) è una metafora ellittica: interpretata come strada resa più sicura, non come un movimento fisico della strada.

- Riga 31: `NPC_BEFR_PLAYER_1cb0bafe-5e84-4aa7-8556-430b353de796_HEROIC`
- Riga 32: `NPC_BEFR_PLAYER_1cb0bafe-5e84-4aa7-8556-430b353de796_JOKER`
- Riga 33: `NPC_BEFR_PLAYER_1cb0bafe-5e84-4aa7-8556-430b353de796_SCHOLAR`
- Riga 34: `NPC_BEFR_PLAYER_1cb0bafe-5e84-4aa7-8556-430b353de796_STOIC`
- Riga 399: `NPC_BEFR_RESPONSE_69279dbf-ca98-44eb-9a06-cdaff81d5570`

Nel quartetto 963–966, `place the lines if I cross one` combina in modo insolito «piazzare» una linea e «incontrarla». Il ramo riguarda la posa delle corde con campanelli. La resa parla di «punto da attrezzare» o «postazione», cioè una posizione incontrata lungo il tragitto, mantenendo il limite posto dal giocatore al proprio impegno. Questa interpretazione va confermata nel ramo interattivo.

- Riga 963: `NPC_RAHANER_PLAYER_12c2d36a-e0f4-4468-b044-e3026dab8596_HEROIC`
- Riga 964: `NPC_RAHANER_PLAYER_12c2d36a-e0f4-4468-b044-e3026dab8596_JOKER`
- Riga 965: `NPC_RAHANER_PLAYER_12c2d36a-e0f4-4468-b044-e3026dab8596_SCHOLAR`
- Riga 966: `NPC_RAHANER_PLAYER_12c2d36a-e0f4-4468-b044-e3026dab8596_STOIC`

### Divergenze fra varianti e informazioni non anticipate

Nel quartetto 669–672, HEROIC/JOKER accettano consigli e musica, mentre SCHOLAR trova decisivi i libri degli incantesimi; solo quest'ultimo parla esplicitamente di sintonizzazione con il Varco. Nel quartetto 681–684, HEROIC chiede lo scopo di Heimen, gli altri il nome. Nel quartetto 1018–1021, SCHOLAR osserva un numero sospetto di creature; HEROIC combatte per uscire, JOKER fugge, STOIC scampa a stento. Queste differenze sono dell'originale: conservate.

- Riga 669: `NPC_HEIMENTHALDRIK_PLAYER_9f320364-4e5f-49c1-93f7-dd8fce9834e4_HEROIC`
- Riga 670: `NPC_HEIMENTHALDRIK_PLAYER_9f320364-4e5f-49c1-93f7-dd8fce9834e4_JOKER`
- Riga 671: `NPC_HEIMENTHALDRIK_PLAYER_9f320364-4e5f-49c1-93f7-dd8fce9834e4_SCHOLAR`
- Riga 672: `NPC_HEIMENTHALDRIK_PLAYER_9f320364-4e5f-49c1-93f7-dd8fce9834e4_STOIC`
- Riga 681: `NPC_HEIMENTHALDRIK_PLAYER_a14f65e4-8f52-40e4-b7d5-021a591933c1_HEROIC`
- Riga 682: `NPC_HEIMENTHALDRIK_PLAYER_a14f65e4-8f52-40e4-b7d5-021a591933c1_JOKER`
- Riga 683: `NPC_HEIMENTHALDRIK_PLAYER_a14f65e4-8f52-40e4-b7d5-021a591933c1_SCHOLAR`
- Riga 684: `NPC_HEIMENTHALDRIK_PLAYER_a14f65e4-8f52-40e4-b7d5-021a591933c1_STOIC`
- Riga 1018: `NPC_RAHANER_PLAYER_6b02d1b6-7900-4e87-b1df-e5a2e9a1652c_HEROIC`
- Riga 1019: `NPC_RAHANER_PLAYER_6b02d1b6-7900-4e87-b1df-e5a2e9a1652c_JOKER`
- Riga 1020: `NPC_RAHANER_PLAYER_6b02d1b6-7900-4e87-b1df-e5a2e9a1652c_SCHOLAR`
- Riga 1021: `NPC_RAHANER_PLAYER_6b02d1b6-7900-4e87-b1df-e5a2e9a1652c_STOIC`

Heimen rivela solo dopo il rito che gli effetti potrebbero richiedere anni; il giocatore può contestarglielo. Non anticipata questa informazione nelle istruzioni del rito e non corretto il personaggio: la reazione è prevista dal testo.

- Riga 810: `NPC_HEIMENTHALDRIK_PLAYER_f32604e5-c7dc-4dca-9010-f442f0010479_HEROIC`
- Riga 811: `NPC_HEIMENTHALDRIK_PLAYER_f32604e5-c7dc-4dca-9010-f442f0010479_JOKER`
- Riga 812: `NPC_HEIMENTHALDRIK_PLAYER_f32604e5-c7dc-4dca-9010-f442f0010479_SCHOLAR`
- Riga 813: `NPC_HEIMENTHALDRIK_PLAYER_f32604e5-c7dc-4dca-9010-f442f0010479_STOIC`
- Riga 857: `NPC_HEIMENTHALDRIK_RESPONSE_2823faad-25aa-49d1-9ed6-b454f4cd2f2b`
- Riga 909: `NPC_HEIMENTHALDRIK_RESPONSE_930cf9e5-119f-4440-9dcb-c38b34f99020`
- Riga 937: `NPC_HEIMENTHALDRIK_RESPONSE_e7860ad6-e365-44dc-a823-18333b942e8f`

### Risate, punteggiatura e conteggi del brief

Il brief sintetizza 52 risate `Ho ho!`, ma il file contiene 39 `Ho ho!`, 12 `Ho ho,`, una `Ho ho ho!`, più due `Hoho!` senza spazio: **54 occorrenze totali**. Uniformate tutte a «Ho ho!», mantenendo invece `Oho` e il singolo `Ho` come interiezioni diverse. Le due grafie senza spazio si trovano nelle righe 379 e 410; la risata tripla nella 401.

- Riga 379: `NPC_BEFR_RESPONSE_2d7162cc-3f0b-45a2-987f-1cc33e9a5fd8`
- Riga 410: `NPC_BEFR_RESPONSE_8d260c3e-d0b5-4e77-9103-0d84ac3c45d9`
- Riga 401: `NPC_BEFR_RESPONSE_6f48c351-b8bc-4a0d-99b4-1c2f7c0ad42a`

Sono state regolarizzate la punteggiatura delle righe `_BASE` e costruzioni inglesi incomplete (per esempio «Your defences are fallen and once again come to me for help?»). Chiavi anomale, comprese `M8n7b...` e `p12p435`, conservate esattamente.

Il totale non giocatore di 296 record comprende anche i **tre titoli**: le battute effettive sono 293 (277 risposte e 16 saluti). Analogamente, i 115 record non giocatore di Heimen includono il titolo; i saluti e le risposte sono 114. Il totale richiesto di 1.279 resta invariato.

## Verifica finale

- **1.279 record**: Befr 455, Heimenthaldrik 496, Rahaner 328. Chiavi identiche all'input, stesso ordine, nessun duplicato.
- Una sola tabulazione per record, due colonne, nessun testo vuoto, nessun ritorno a capo interno alla traduzione.
- **850 occorrenze di segnaposto**: stessi valori e molteplicità riga per riga. Ricostruzione eseguita in memoria con `tools/mt_mask.py` e `dlg4.tokens.json`, senza rifiuti.
- **226 quartetti integri**, 904 varianti; 79 righe `_BASE`. Quattro stringhe distinte per ogni quartetto, oltre alla revisione del registro.
- Blocchi: 1–128, 129–258, 259–388, 389–517, 518–646, 647–775, 776–902, 903–1030, 1031–1158, 1159–1279. Tutti fra 100 e 150 righe; nessun quartetto spezzato.
- Nessuna riga identica all'inglese. Nessun residuo trovato dalla scansione degli indicatori inglesi comuni; traduzione e revisione linguistica dell'intero lotto.
- Controllo terminologico sul riferimento, con apostrofi normalizzati, plurali e confini di parola; controllo automatico aggiuntivo di **446 corrispondenze** di termini e nomi rilevanti, senza segnalazioni.
- Identica resa per i testi inglesi integralmente ripetuti e per i segmenti lunghi ripetuti nei diversi rami. Asterischi delle didascalie conservati.
- Tutti i 62 `my friend` → «amico mio»; tutte le 54 risate della famiglia `Ho ho` → «Ho ho!». Nessuna marca regionale per Heimen, nessuna sua marca aggiunta alle battute del giocatore.
- File scritto direttamente con `Path.write_text(..., encoding="utf-8")`, riaperto con decodifica UTF-8 rigorosa: senza BOM, senza caratteri sostitutivi, presenza verificata di `à è é ì ò ù`.
- Nessuna modifica all'input, al riferimento o ai lotti precedenti. Nessuna importazione o installazione e nessuna prova nel gioco: questa consegna riguarda il TSV e le note.

**Criterio riutilizzabile:** per un dialetto privo di equivalente non regionale, trasferire la marca in ritmo, sintassi e lessico senza simulare la pronuncia. Nei dialoghi ramificati, controllare sia i quartetti sia i segmenti narrativi ripetuti; verificare i termini mancanti anche nelle missioni già installate. I nomi di oggetti o luoghi discordanti vanno documentati con la chiave, non uniformati sulla sola somiglianza.
