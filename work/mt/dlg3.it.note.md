# Note di consegna — dlg3

Traduzione completata: **954 righe**, UTF-8 senza BOM, nessuna intestazione.
Input e riferimento: `dlg3.tsv` e `reference.tsv`, nella stessa cartella. Il riferimento effettivamente presente alla verifica contiene **2.715 coppie**, contro le 2.675 indicate nel brief: sono state seguite le rese del file attuale.

## Voci

**Eldorian** — Colloquiale, entusiasta, con esitazioni, ripartenze e piccole autocorrezioni; preciso quando descrive percorsi e pericoli.
Nei ricordi e nell'eco la voce si abbassa: l'affetto resta timido, con gesti concreti e senza amplificare gli inviti già presenti nell'originale.

**Alaric** — Misurato e grave nei giudizi, piano e diretto negli ordini; conservate le immagini di peso, cardine, ombra, lama e terreno sotto i piedi.
Le frasi restano pronunciabili, con autorevolezza affidata al contenuto e alle pause, senza alzare uniformemente il registro.

## Registri del giocatore

- HEROIC: dichiarazioni piene, lealtà e determinazione; conservate anche le scelte dure o ostili previste dall'inglese.
- JOKER: battute, immagini concrete e colloquialità, senza trasformare ogni intervento in una gag.
- SCHOLAR: precisione, osservazione, ragionamenti e richieste di prove; mantenute le differenze di contenuto rispetto agli altri toni.
- STOIC: frasi brevi e controllate, senza cancellare gli affetti espressamente presenti nell'originale.

I **161 quartetti** sono stati tradotti insieme e hanno tutti quattro rese distinte. L'unicità delle stringhe è un controllo strutturale aggiuntivo; la distinzione dei registri è stata valutata durante la traduzione e la rilettura.

## Termini nuovi e decisioni

Queste decisioni non modificano `reference.tsv`. La tabella raccoglie denominazioni e locuzioni rilevanti per i lotti successivi, non ogni sostantivo comune della prosa.

| Inglese | Resa | Nota |
|---|---|---|
| Chosen of the Forest | Prescelto della Foresta | Titolo di Alaric; il referente è maschile. |
| Green Knight | Cavaliere Verde | Figura che proclama il Prescelto per volontà di Ceres. |
| Veylenth Vordae | Veylenth Vordae | Denominazione elfica invariata. |
| Age of Elven Atrocity | Era dell'Atrocità Elfica | Glossa storica della Veylenth Vordae. |
| Indulgence | Indulgenza | Qualificazione dei Goblin come esseri di pura Indulgenza; mantenuta la maiuscola dell'originale. |
| Fae | Fae | Collettivo invariato; non identificato arbitrariamente con le sole fate. |
| tree-folk | gente degli alberi | Espressione collettiva; non introdotta una nuova specie distinta dai Treant. |
| forest gate | accesso alla foresta | Passaggio fisico ostruito dai rampicanti; distinto da Waygate → Varco. |
| discipline scout | ricognizione disciplinare | Uscita assegnata come punizione e addestramento; scout qui indica l'attività, non una persona. |
| perimeter pass | giro del perimetro | Percorso lungo campi, margine del bosco e vecchie postazioni. |
| scout posts / re-mark | postazioni degli esploratori / rifare i segnali | Ripristino delle indicazioni sbiadite; non introdotti segnalatori della meccanica beacon. |
| Guild Mentor | Mentore della Gilda | Ruolo di Rahaner. |
| Guild Shop | Negozio della Gilda | Attività gestita da Tamsin. |
| Faustas's Tower | Torre di Faustas | Nome del luogo; Faustas invariato. |
| elder tree | albero antico | Descrizione, non un nuovo titolo di NPC. |
| The Earlwood Guild Leader | Il capo della Gilda di Earlwood | Titolo di Alaric. |
| The Earlwood Scout | L'esploratore di Earlwood | Titolo di Eldorian, derivato da Scout → Esploratore. |

**Rese già vincolanti riutilizzate:** Foresta Eterna, Iniquità, Dei Oscuri, Re Goblin, Re della Foresta, Treant corrotto, Mulino di Haylor, Pozza del Ricordo, Sede della Gilda, Bacheca degli incarichi, Stufato del Cacciatore e i suoi ingredienti. `Banner Weaver` riprende **Tessitrice di Stendardi** dal titolo di Tamsin. `Bashers` riprende **Picchiatori** da Goblin Basher → Goblin Picchiatore. Fangra resta invariato, coerentemente con Cucciolo di Fangra. `Aelwynor, the Wildroot Father` usa **Aelwynor, il Padre delle Radici Selvatiche**, non una nuova traduzione dell'epiteto.

L'**eco** di Eldorian resta prosa: «eco», con accordi al femminile singolare, senza assimilarla a Eco temporale o Fenditura d'eco. `Temporal eyes` diventa «occhi, scintillanti di magia temporale», riferito a Eldorian. `Echo` come verbo diventa «rispecchiare». `Old-gods rite` è un «rito degli antichi dèi»: non è stato trasformato in un rito degli Antichi, nome proprio associato ai Varchi.

## Genere del giocatore

Preferite formulazioni senza accordo: «Eccoti di nuovo», «hai dimostrato le tue capacità», «torna sulle tue gambe», «aspettati di tutto», «non farti cogliere alla sprovvista», «mi farebbe piacere la tua compagnia». Evitati anche participi personali facilmente aggirabili: «Hai guadagnato una parte della mia fiducia» e «Ho visto come combatti».

### Forme maschili conservate da rileggere a schermo

Sono scelte motivate dalla funzione affettiva del vocativo o dal motivo narrativo dell'eroe, non dall'impossibilità grammaticale assoluta di riscrivere la battuta.

| Riga | Chiave | Forma e motivo |
|---|---|---|
| 467 | `NPC_ELDORIAN_GREETING_b6e2c9a4-1f7d-8c3e-5a0b-9d4f2e7c1a6b` | «amico»: mantenuto il vocativo affettuoso di Eldorian. |
| 871 | `NPC_ELDORIAN_RESPONSE_3f4bc19f-9224-462d-9749-cf59794c2d1b` | «amico»: ripresa identica del saluto 467. |
| 907 | `NPC_ELDORIAN_RESPONSE_9385889f-384c-4f06-a158-9f9c2a3fc059` | «Devi essere un vero eroe»: ruolo che Eldorian ammira e vuole emulare. |
| 913 | `NPC_ELDORIAN_RESPONSE_9c753fad-c97c-462a-a67a-d11190f8ccc7` | «Anche tu, amico»: mantenuto il vocativo. |
| 943 | `NPC_ELDORIAN_RESPONSE_d884dc27-50f0-4c6e-b50a-2df9f3a95b90` | «un grande eroe, come Alaric e come te»: il nome maschile riguarda direttamente Eldorian, ma il paragone include il giocatore; segnalato per prudenza editoriale. |

### Plurale collettivo

«Siamo soldati» include il giocatore e Eldorian, uomo: il maschile plurale è compatibile anche con un gruppo misto. Non è un accordo singolare imposto al giocatore. Conservato nelle seguenti varianti:

- Riga 743: `NPC_ELDORIAN_PLAYER_b197157e-d862-4150-8505-ae7ee2fa71d6_HEROIC`
- Riga 744: `NPC_ELDORIAN_PLAYER_b197157e-d862-4150-8505-ae7ee2fa71d6_JOKER`
- Riga 746: `NPC_ELDORIAN_PLAYER_b197157e-d862-4150-8505-ae7ee2fa71d6_STOIC`

La SCHOLAR dello stesso quartetto parla genericamente dei soldati. Gli altri maschili personali, come «sei ancora ferito», «sei nato a Earlwood?» e «vai da solo», sono rivolti a Eldorian; «convinto» e «tenero» sono rivolti ad Alaric. Conservati i femminili relativi a Saqi e Tamsin.

## Passaggi dubbi e particolarità dell'originale

### «heartwood oak» e materiale del ponte

La locuzione non coincide letteralmente con una voce del riferimento. Nel contesto della raccolta di materiali è stata ricondotta a **Heart Oak → Quercia del Cuore**, anziché introdurre un materiale chiamato «durame di quercia». È un'interpretazione contestuale: da confrontare con l'obiettivo di raccolta in gioco.

- Riga 421: `NPC_ALARIC_RESPONSE_a9ed4b5d-febd-446e-8990-818890cd5e59`

### «Treant-wood … touched»

`Touched` è volutamente sospeso e non dice da quale forza. Reso «È… segnato», mantenendo l'indeterminatezza senza aggiungere «corrotto» o «sacro».

- Riga 439: `NPC_ALARIC_RESPONSE_d06af1fe-6236-44e1-905f-8f5890fae624`

### Il Re «bound»

Nel rito il Re è detto `bound`, senza specificare se si tratti di prigionia, vincolo magico o soggezione. Reso «vincolato», coerentemente con il successivo bisogno di rivolgersi direttamente a Ceres, senza inventare catene fisiche.

- Riga 367: `NPC_ALARIC_RESPONSE_2b6cfb43-2aed-4be2-a558-9e1644397cf9`

### Chi ha distrutto il ponte

Alaric attribuisce la distruzione ai Treant in due risposte, mentre altrove lascia aperta l'identità dei responsabili: «goblins, or something that hunts without banners». Conservata l'incertezza di quel ramo e la certezza degli altri. Potrebbe dipendere dall'ordine delle informazioni ottenute, che il TSV ordinato per chiave non permette di verificare.

- Riga 353: `NPC_ALARIC_RESPONSE_0846e5e8-0bd5-42c9-8ed8-14d1aae401fb`
- Riga 409: `NPC_ALARIC_RESPONSE_945f0739-967d-42e8-87a5-2990dd4741bb`
- Riga 413: `NPC_ALARIC_RESPONSE_9bb98b07-01b6-4f4c-ac9e-4231eb24b026`

### Volontà, Corruzione e perdita della ragione

Alaric distingue la Corruzione completa, accettata volontariamente, dalle creature impazzite ma ancora se stesse. Un'altra spiegazione dice invece che gli spiriti hanno perso la ragione e la pietà. Conservata la diversa intensità delle formulazioni: non è stato eliminato il tema della scelta per uniformare tutto a una possessione forzata. I dubbi di Eldorian sul giudizio di Ceres sono mantenuti come dubbi del personaggio.

- Riga 368: `NPC_ALARIC_RESPONSE_2cb4693a-f9b0-44b2-aeb5-3e399ea5e48a`
- Riga 384: `NPC_ALARIC_RESPONSE_60508905-5dff-43ba-aa4f-a433965f0ef1`
- Riga 418: `NPC_ALARIC_RESPONSE_a3c2f10b-8d86-4b7f-b487-4426d8f8f053`
- Riga 949: `NPC_ELDORIAN_RESPONSE_f621a57d-44e6-439e-b612-3d26706274c4`

### Apparizione di Aelwynor

Alaric colloca l'apparizione poco dopo la sconfitta dell'ultimo Re Goblin; Eldorian la associa alla nomina a Prescelto. Potrebbero essere lo stesso episodio o una semplificazione della leggenda: conservate entrambe le versioni, senza aggiungere una cronologia.

- Riga 415: `NPC_ALARIC_RESPONSE_9e1af266-7fe1-46bb-81d4-47c3e053ad0b`
- Riga 949: `NPC_ELDORIAN_RESPONSE_f621a57d-44e6-439e-b612-3d26706274c4`

### Visione dei campi

La didascalia dice che i campi appaiono com'erano non molto tempo prima; subito dopo Eldorian precisa di non poterli mostrare com'erano *davvero*. Mantenuta la distinzione fra ricostruzione soggettiva, memoria e visione letterale. Le ripetizioni interne del secondo ramo sono già nell'inglese.

- Riga 927: `NPC_ELDORIAN_RESPONSE_bc5996ce-e2f3-45ba-85c5-a4ed400f04b4`
- Riga 934: `NPC_ELDORIAN_RESPONSE_cd595f86-b6a7-4a44-a055-b80ffc67f68a`

### Punizione e ricognizione

Il gioco di parole implicito in `scout` riguarda un giro di ricognizione, non l'affidamento di un altro esploratore. Le risposte su perimetro e segnali chiariscono la lettura. La punizione affidata da Rahaner resta distinta dall'uscita precedente compiuta di propria iniziativa.

- Riga 852: `NPC_ELDORIAN_RESPONSE_160cb85c-df02-43e0-9b2a-e229e988bc35`
- Riga 925: `NPC_ELDORIAN_RESPONSE_b79f2775-ee2a-4eaf-82f2-782df88d52de`

### Virgolette e dati del brief

L'inglese apre senza chiudere la citazione nella domanda sui profughi e nel primo paragrafo della risposta sulla ricostruzione del ponte. Conservata la struttura, come nel modello del lotto precedente. L'originale alterna inoltre virgolette dritte e tipografiche e capitalizzazioni diverse degli stessi nomi: le denominazioni italiane restano coerenti.

- Riga 318: `NPC_ALARIC_PLAYER_f2fff497-bfa5-461e-897a-0021175cfc2d_BASE`
- Riga 407: `NPC_ALARIC_RESPONSE_8e1a4880-76ef-4f0e-8c41-c39437724fe2`

I «237» interventi NPC del brief comprendono, contando le chiavi effettive, **217 RESPONSE, 18 GREETING e 2 TITLE**. Le altre righe sono 73 BASE e 644 varianti di tono. Eldorian ha effettivamente 494 righe e Alaric 460. Nessuna chiave, incluse quelle con identificatori non standard, è stata corretta o normalizzata.

## Verifica finale

- 954 record, chiavi identiche all'input e nello stesso ordine.
- Una sola tabulazione per record, due colonne, nessuna traduzione vuota o ritorno a capo interno.
- Segnaposto `<x…/>` identici per valore e molteplicità in ogni riga; conservati anche gli asterischi delle didascalie e dell'enfasi.
- Nessuna riga coincidente con il testo inglese; traduzione e rilettura di tutti i blocchi, più ricerca dei residui inglesi comuni.
- 161 quartetti contigui, nell'ordine HEROIC, JOKER, SCHOLAR, STOIC, tutti con quattro traduzioni distinte; nessun quartetto diviso tra blocchi.
- Blocchi: 1–122, 123–246, 247–370, 371–490, 491–617, 618–742, 743–850, 851–954.
- Le battute inglesi identiche hanno traduzioni identiche; uniformati i passaggi ripetuti nelle risposte.
- Terminologia confrontata con il riferimento anche per titoli abbreviati, plurali e grafie con apostrofi diversi.
- Accordi personali riletti distinguendo giocatore, interlocutore, narratore e soggetto generico.
- TSV scritto direttamente con `Path.write_text(..., encoding="utf-8")`, senza passaggio del testo attraverso una pipe PowerShell; riaperto in UTF-8 con verifica degli accenti effettivi e assenza di BOM o caratteri sostitutivi.
- Nessuna modifica all'input, al riferimento o ai lotti precedenti.

Non è stata eseguita una prova in gioco: la consegna riguarda il TSV e le note, non l'integrazione. I riferimenti narrativi e le forme maschili elencati sopra restano i punti da rileggere a schermo.
