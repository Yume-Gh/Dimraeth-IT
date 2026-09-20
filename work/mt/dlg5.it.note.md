# Note di consegna — dlg5

Traduzione completata: **787 righe**, UTF-8 senza BOM, nessuna intestazione.
Input e riferimento: `dlg5.tsv` e `reference.tsv`, nella stessa cartella. Il riferimento effettivamente presente contiene **2.756 coppie**, contro le 2.736 indicate nel brief: sono state seguite le rese del file attuale.

## Voci

**Corin** — Dichiarazioni brevi, ordini netti e aforismi duri. La disciplina trattiene una ferita; il rispetto emerge a fatica, senza cinismo aggiunto.

**Saqi** — Calorosa, energica e rumorosa; passa dal complimento all'ordine pratico. Italiano colloquiale senza storpiature, ospitalità come principio morale.

**Faustas** — Alto, cortese e preciso, con frasi compiute e spiegazioni leggibili. La goffaggine della proiezione lascia spazio alla gravità quando parla di Sylbos.

**Aelwynor** — Il registro più alto: solenne, cosmico, accusatorio. La voce preme nella mente, non è un normale discorso pronunciato; nel pentimento il ritmo si spezza e la maestà diventa ammissione di colpa.

**Suspicious Trader** — Gratitudine teatrale, negazione difensiva, poi confessione amara. Conservati i cambi di postura e il diverso peso delle frasi.

**Guard** — Deferenza, esitazioni e ammirazione imbarazzata; si tradisce nei gesti e nelle ripartenze.

**Lost Boy** — Entusiasmo infantile, domande semplici, esclamazioni e stupore; niente lessico da adulto in miniatura.

**Ronny** — Lamentele secche, amarezza e disprezzo. Interiezioni brusche e congedi sgarbati senza attenuazioni.

**Basilton's Note** — Etichetta funzionale; Basilton conserva il proprio nome.

## Registri del giocatore

- HEROIC: frasi piene e dirette, determinazione e senso del dovere; conservate anche le scelte crudeli previste dall'inglese.
- JOKER: colloquialità, ironia e immagini concrete; la leggerezza non cancella minacce o amarezza.
- SCHOLAR: lessico preciso, ragionamento e curiosità; conservati i giudizi analitici più freddi.
- STOIC: domande e dichiarazioni brevi, controllate; non sacrificato il contenuto solo per accorciare.

I **134 quartetti** sono stati tradotti insieme, senza spezzarli fra blocchi. Tutti hanno quattro stringhe distinte; questo controllo strutturale affianca la revisione dei registri, non la sostituisce.

## Termini nuovi e decisioni

Le scelte seguenti non modificano `reference.tsv`. Si annotano denominazioni e locuzioni rilevanti, non ogni parola comune della prosa.

| Inglese | Resa | Nota |
|---|---|---|
| The Hearth at Road’s Edge | Il Focolare sul Ciglio della Strada | Nome completo della taverna di Saqi; assente dal riferimento. Non confuso con l'oggetto Earlwood Hearth → Focolare di Earlwood. |
| Road’s Edge | Ciglio della Strada | Forma breve della stessa taverna; mantenuta riconoscibile nel nome completo. |
| Iron Guardians | Guardiani di Ferro | Figure dei racconti di Barakthrum; non identificate con i golem, ai quali sono soltanto paragonate. |
| stone-born | nato nella pietra | Appellativo spiegato subito dalla nascita nelle sale della montagna. Non trasformato in una razza nuova. |
| the Truth, Beauty, and the Good | la Verità, la Bellezza e il Bene | Triade filosofica citata da Saqi come parole di Heimen. |
| Goblin-Slayer | Ammazza-Goblin | Soprannome scherzoso di Saqi, invariabile rispetto al genere. |
| Empire of Xwin | Impero di Xwin | Xwin invariato; non ampliato in Impero dei Minotauri quando l'inglese non lo fa. |
| the Principles | i Principi | Forma breve, coerente con Prime Principles → Principi Primi; non aggiunto «Primi» alla battuta. |
| logbook | registro | Registro delle scorte dei terreni Haylor; non «diario di bordo». Conservato il singolare dell'inglese. |
| ration ledgers | registri delle razioni | Riprende `it/Quests.csv`, missione `QUEST_OPENTHEBOOKS`; non è una nuova resa autonoma. |
| cache | scorta | Riprende la stessa missione già tradotta. Qui è un carico trasportato dalla carovana, non necessariamente un nascondiglio. |
| beacon kits / beacon wards | kit per i segnalatori / segnalatori di protezione | Derivazioni da beacon → segnalatore; conservata la funzione protettiva senza introdurre un nuovo oggetto nominato. |
| wayfinder duty / wayfinder routes | servizio dei Cercavia / percorsi dei Cercavia | Derivazioni da Wayfinder Line → Linea dei Cercavia, già vincolante. |
| grid | rete | Rete dei segnalatori, nel contesto della missione di Corin. |
| The Adventurer Captain | Il capitano degli avventurieri | Titolo di Corin. |
| The Venerable Wizard | Il venerabile mago | Titolo di Faustas. |
| One of the Scavengers | Uno degli sciacalli | Titolo della guardia; saccheggio dei caduti, non raccolta neutra di materiali. |
| Child oF Earlwood | Bambino di Earlwood | Titolo del bambino; regolarizzato il refuso nella maiuscola di «oF». |
| The "Hopeful" Shepherd | Il pastore "fiducioso" | Ironia del titolo di Ronny conservata nelle virgolette. |
| The young dwarf | La giovane nana | Titolo di Saqi, al femminile. |
| Basilton's Note | Nota di Basilton | Unica etichetta del personaggio; Note → Nota è già nel riferimento. |

**Rese vincolanti riutilizzate:** Re della Foresta, Padre delle Radici Selvatiche, Re Goblin, Maghi Ogre, Antichi Dei, Antichi, Dei Oscuri, Signore Oscuro, Varco, Santuario, albero antico, gente della foresta, Treant corrotto, Corruzione, Tenderberry, Tessiradici, campo avanzato, Bivio del Sentiero, Passaggio sul Fiume, Vecchio Ceppo e Mulino di Haylor. Wildwood e i nomi propri restano invariati. Il titolo del mercante usa Mercante sospetto, come nel riferimento.

Le voci di interfaccia a parola singola si applicano al loro significato: `rage` nella confessione di Aelwynor è «rabbia», non il nome dell'effetto di stato Furia; `mending` per le Tenderberry è «curarsi / cure», non il suffisso Risanante. `Stamina` non compare nell'input effettivo, pur essendo elencato nel brief.

## Genere del giocatore

Preferite costruzioni senza accordo: «Ce l'hai fatta», «aver dato una mano», «Il tuo aiuto è servito», «Ti basta, adesso?», «Che spettacolo!». I nomi e vocativi che sostengono il rapporto fra personaggi conservano il maschile previsto dal progetto. Non si sostiene che siano grammaticalmente impossibili da parafrasare: sono scelte per mantenere il ruolo o la voce.

### Maschili conservati

| Riga | Chiave | Forma / motivo |
|---|---|---|
| 55 | `NPC_AELWYNOR_PLAYER_cfa397ae-01b0-4ae4-a846-9ee04d2eb478_STOIC` | «io sono intervenuto»: dichiarazione asciutta del giocatore. |
| 234 | `NPC_CORIN_PLAYER_c3ae5a0d-ca61-4dd6-bdf1-e780ab55e28b_JOKER` | «un salvatore»: ironia sul mancato ringraziamento. |
| 235 | `NPC_CORIN_PLAYER_c3ae5a0d-ca61-4dd6-bdf1-e780ab55e28b_SCHOLAR` | «un salvatore»: ruolo rivendicato dal giocatore. |
| 236 | `NPC_CORIN_PLAYER_c3ae5a0d-ca61-4dd6-bdf1-e780ab55e28b_STOIC` | «il tuo salvatore»: ruolo rivendicato dal giocatore. |
| 283 | `NPC_CORIN_RESPONSE_1dc95c89-f80e-4406-9975-a0a002a12f23` | «Salvatore?»: Corin riprende e contesta il termine del giocatore. |
| 300 | `NPC_CORIN_RESPONSE_7c0dbb58-7aee-47de-a4cb-35a602fd4cda` | «un altro avventuriero troppo sicuro di sé»: categoria in cui Corin aveva collocato il giocatore. |
| 310 | `NPC_CORIN_RESPONSE_a7e2cca4-ae98-45ea-9aba-27e3f695e3ec` | «compagno d’armi»: riconoscimento militare promesso da Corin. |
| 322 | `NPC_CORIN_RESPONSE_ccdf5334-7794-4e2e-80b1-68ca023a69c2` | «compagno d’armi»: stesso riconoscimento nel ramo alternativo. |
| 331 | `NPC_CORIN_RESPONSE_e68779a7-b4ca-4539-82b6-8c99e585f309` | «un altro avventuriero troppo sicuro di sé»: segmento ripetuto della riga 300. |
| 429 | `NPC_GUARD_GREETING_d6c4b593-9239-4637-be20-42f07a436069` | «avventuriero»: vocativo deferente della guardia. |
| 468 | `NPC_GUARD_RESPONSE_245e41e4-0f25-4f47-8e01-2543b94b4624` | «il grande avventuriero»: adulazione della guardia. |
| 469 | `NPC_GUARD_RESPONSE_5f86ab76-9f9f-4bff-9129-4de74516e6a2` | «valoroso avventuriero»: supplica. |
| 470 | `NPC_GUARD_RESPONSE_74b2ed44-8b35-470f-902d-aac74b7a94ba` | «valoroso avventuriero»: stessa supplica nel ramo alternativo. |
| 478 | `NPC_LOSTBOY_GREETING_02f67c80-bba3-4fe4-a81d-cb6a6cc2875c` | «Un vero avventuriero»: entusiasmo del bambino; il successivo complimento evita l’accordo («Che spettacolo!»). |
| 734 | `NPC_SUSPICIOUSTRADER_GREETING_ee08b7ff-5483-4ae9-b534-885433b4e3a1` | «Che tu sia benedetto, avventuriero»: gratitudine teatrale del mercante. |
| 777 | `NPC_SUSPICIOUSTRADER_RESPONSE_58a4e0d0-b2d4-4dea-9e02-6081e598d8f1` | «Amico»: familiarità strumentale del mercante durante la negazione. |

### Riferimenti indiretti e plurali

«Un avventuriero come te» (510) riguarda in primo luogo il bambino, ma include il protagonista nel paragone. Anche la 513 confronta il protagonista con Alaric. Segnalati per la revisione a schermo, pur non essendo accordi singolari aggiunti direttamente al giocatore.

- Riga 510: `NPC_LOSTBOY_RESPONSE_2be8f59c-2e9c-4d65-91e9-06e3d5bdbb2c`
- Riga 513: `NPC_LOSTBOY_RESPONSE_7935fc93-3c7c-4d6e-9512-02a70c8d3878`

«Entrambi» con Faustas (421) è un plurale misto possibile anche con protagonista donna. «Entrambi» con Saqi (696, 701) segue invece la convenzione del protagonista maschile. «Tesoro» (722, 731) è un appellativo utilizzabile per entrambi i sessi, non un accordo naturale maschile imposto al protagonista. Analogamente «padrona» nella 73 concorda con la metafora «scintilla», non assegna il femminile al giocatore.

- Riga 421: `NPC_FAUSTAS_RESPONSE_d5867822-a6d2-4d22-ba94-87a8a32e2c30`
- Riga 696: `NPC_SAQI_RESPONSE_36f1f642-4819-4ab8-92e6-05081a48e13a`
- Riga 701: `NPC_SAQI_RESPONSE_50310412-251a-4a0e-a7c2-cf12c4cd2087`
- Riga 722: `NPC_SAQI_RESPONSE_e074b3f6-5f61-49b5-ad37-1412fabbbeb8`
- Riga 731: `NPC_SAQI_RESPONSE_ff4d1948-153b-4bb5-a899-8e2de35d8875`
- Riga 73: `NPC_AELWYNOR_RESPONSE_8154698f-53d5-47b1-b8c3-921cf3393243`

Gli accordi al femminile su Saqi sono conservati, fra cui «Sei nata qui?» (575). La guardia è indicata con `him` nell'originale: «la guardia» è il nome italiano del ruolo, non un cambio di sesso del personaggio. Il giocatore dà del tu alla singola guardia quando la riconosce, ma ordini e minacce si rivolgono al gruppo che risponde con `we/us`.

## Passaggi dubbi e particolarità dell'originale

### Aelwynor: voce mentale e lettura morale

La pressione sul cranio e l'avvolgimento dei pensieri restano espliciti. Nelle didascalie finali, `forces them out` diventa «le sospinge nella tua mente»: l'emissione delle parole resta coerente con la telepatia già stabilita, senza aggiungere un parlare a voce alta. «La Madre» è sempre Ceres. Il pentimento conserva «Mi sono avvolto nella rabbia» e la distinzione fra ricevere la volontà della Madre e conoscerne la mente.

- Riga 2: `NPC_AELWYNOR_GREETING_d75cc77a-cc85-4a0b-8c00-63a37612046f`
- Riga 62: `NPC_AELWYNOR_RESPONSE_05eb7fe7-80e9-42fc-8e32-351f3ea51ae9`
- Riga 63: `NPC_AELWYNOR_RESPONSE_1e93ba26-7d73-4040-b5c9-a52303051d4c`
- Riga 66: `NPC_AELWYNOR_RESPONSE_5558e408-b7f5-403c-bfe3-ede7c7ff05dd`
- Riga 72: `NPC_AELWYNOR_RESPONSE_739ee8f1-8cbe-46ba-8f8f-bc212d8b63d7`
- Riga 73: `NPC_AELWYNOR_RESPONSE_8154698f-53d5-47b1-b8c3-921cf3393243`
- Riga 75: `NPC_AELWYNOR_RESPONSE_c8713ebe-73aa-41b4-ba32-7a87be4b066b`
- Riga 76: `NPC_AELWYNOR_RESPONSE_ec7d382d-3c28-41db-8cae-8c91288e0716`
- Riga 77: `NPC_AELWYNOR_RESPONSE_fcadb20f-98dc-415b-80f8-ce1a07cbe1ef`

Le promesse di sonno e nuova forma restano tali: non trasformata la sconfitta in una morte necessariamente definitiva. I rami in cui il giocatore proclama la fine del Re non sono stati riscritti per allinearli alle risposte di riposo.

- Riga 15: `NPC_AELWYNOR_PLAYER_348a62c9-f6cb-46f9-93c2-0c49890a91f4_HEROIC`
- Riga 18: `NPC_AELWYNOR_PLAYER_348a62c9-f6cb-46f9-93c2-0c49890a91f4_STOIC`
- Riga 68: `NPC_AELWYNOR_RESPONSE_60d4aa41-71ec-43a4-9962-ff9d84b64f57`
- Riga 78: `NPC_AELWYNOR_RESPONSE_fe198474-b978-424a-bda5-a1d2b2579324`

Nel quartetto 44–47, HEROIC/JOKER attribuiscono la debolezza all'azione della Corruzione; SCHOLAR insiste invece sull'ordine «debolezza, poi Corruzione». È una divergenza dell'originale, conservata.

- Riga 44: `NPC_AELWYNOR_PLAYER_aa311ea1-e4dc-4b11-bc41-4b2a47c47d2f_HEROIC`
- Riga 45: `NPC_AELWYNOR_PLAYER_aa311ea1-e4dc-4b11-bc41-4b2a47c47d2f_JOKER`
- Riga 46: `NPC_AELWYNOR_PLAYER_aa311ea1-e4dc-4b11-bc41-4b2a47c47d2f_SCHOLAR`
- Riga 47: `NPC_AELWYNOR_PLAYER_aa311ea1-e4dc-4b11-bc41-4b2a47c47d2f_STOIC`

### Corin: vivi o morti, fortuna e cronologia

`Check on them and report back, alive or dead` può legarsi grammaticalmente al ritorno del giocatore, ma il senso operativo è verificare lo stato delle persone agli avamposti. Reso «Controlla e torna a riferire: vivi o morti», riferendo la coppia alla sorte da riportare. Il collegamento è interpretativo e va verificato nel ramo in gioco.

- Riga 305: `NPC_CORIN_RESPONSE_908c2857-b990-45b7-9166-71dcab143ba4`
- Riga 326: `NPC_CORIN_RESPONSE_cf43930f-d001-4abd-8392-aca7a705f300`

`Luck is what people call discipline after they survive it` conserva la costruzione aspra: «Fortuna è il nome che la gente dà alla disciplina dopo esserne uscita viva». Non attenuato l'aforisma in una massima motivazionale. `grid` è interpretato come rete dei segnalatori. Il `gate` raggiunto dal campo è l'accesso fisico alla foresta, non un Varco degli Antichi.

- Riga 279: `NPC_CORIN_RESPONSE_0a5b29b0-51f6-4e11-b04e-29e29fa7b137`
- Riga 266: `NPC_CORIN_PLAYER_e4k9m2q7-a5c1-r8d3-b6f0-z1x7n4p2v9t5_BASE`
- Riga 296: `NPC_CORIN_RESPONSE_6a2c9e1d-4f7b-8c3e-0d5a-1f9b4c7e2d3a`

Corin dice che tutti gli esploratori sono morti, ma in un altro ramo Eldorian è già fuori a ripulire la strada. I record non sono ordinati secondo la cronologia di gioco: possibile differenza fra gruppi o fasi della missione, non contraddizione dimostrata. Non cambiato «tutti» in «quasi tutti».

- Riga 285: `NPC_CORIN_RESPONSE_3be2d1aa-b2af-40fe-9372-0c97eb17677a`
- Riga 290: `NPC_CORIN_RESPONSE_43427000-8722-4798-b48a-53e87cf0ca12`
- Riga 296: `NPC_CORIN_RESPONSE_6a2c9e1d-4f7b-8c3e-0d5a-1f9b4c7e2d3a`

### Faustas: l'eufemismo e la proiezione

`Misplaced` indica una destinazione sbagliata del teletrasporto: «ti ha fatto arrivare nel posto sbagliato», ripreso dal giocatore con «Nel posto sbagliato». Non significa che il mago abbia soltanto perso di vista il protagonista. Conservata la differenza fra il contraccolpo che devia l'incantesimo e il potere del rituale che trova un ricettacolo nel protagonista.

- Riga 338: `NPC_FAUSTAS_GREETING_92bb22f0-30ca-4f02-b1e3-ccbbe4028feb`
- Riga 341: `NPC_FAUSTAS_PLAYER_0fd21c71-44ee-4c38-8ee1-7606056e4410_HEROIC`
- Riga 342: `NPC_FAUSTAS_PLAYER_0fd21c71-44ee-4c38-8ee1-7606056e4410_JOKER`
- Riga 343: `NPC_FAUSTAS_PLAYER_0fd21c71-44ee-4c38-8ee1-7606056e4410_SCHOLAR`
- Riga 344: `NPC_FAUSTAS_PLAYER_0fd21c71-44ee-4c38-8ee1-7606056e4410_STOIC`
- Riga 416: `NPC_FAUSTAS_RESPONSE_a55517f7-2e81-4e2e-b6e6-b34677d8b874`
- Riga 423: `NPC_FAUSTAS_RESPONSE_f11d5d5e-5e22-4440-b429-b8aebc1990c6`
- Riga 426: `NPC_FAUSTAS_RESPONSE_f90fdd2a-681f-41b3-8ebe-052ad2d4b101`

### Saqi: registri, registro, scorta e sigilli

La battuta di consegna usa `ration ledgers` al plurale; le spiegazioni e gli altri rami usano `logbook` al singolare. Conservata questa differenza: «registri delle razioni» e «registro». La missione inglese `QUEST_OPENTHEBOOKS_TASKGROUP_2_TASK_0` chiede inoltre «ledgers and seal stamps», mentre Saqi chiede espressamente registro e scorta, «Nothing else». Disallineamento già nei testi sorgente, non corretto introducendo sigilli nei dialoghi.

- Riga 569: `NPC_SAQI_PLAYER_1b4d6c23-39a4-4b5b-aba7-5d2c5c303331_BASE`
- Riga 576: `NPC_SAQI_PLAYER_2a7d9c1f-5e4b-8f3a-0c6d-1b9e4a7c2d5f_BASE`
- Riga 590: `NPC_SAQI_PLAYER_568c1c01-c559-474d-853d-792099bfb94b_HEROIC`
- Riga 591: `NPC_SAQI_PLAYER_568c1c01-c559-474d-853d-792099bfb94b_JOKER`
- Riga 592: `NPC_SAQI_PLAYER_568c1c01-c559-474d-853d-792099bfb94b_SCHOLAR`
- Riga 593: `NPC_SAQI_PLAYER_568c1c01-c559-474d-853d-792099bfb94b_STOIC`
- Riga 692: `NPC_SAQI_RESPONSE_228d81fb-c8aa-440a-a539-74008ac5e2ca`
- Riga 727: `NPC_SAQI_RESPONSE_ed135a30-86d0-4477-9ff3-068d5900de06`
- Riga 731: `NPC_SAQI_RESPONSE_ff4d1948-153b-4bb5-a899-8e2de35d8875`

Nel quartetto sulla patria mai conosciuta, `it` non esplicita l'antecedente. La risposta parla della cultura nanica e dei racconti del padre: «non averla mai conosciuta» rimanda alla patria/Barakthrum, senza suggerire che Saqi ignori il dolore stesso. SCHOLAR mantiene la formulazione più astratta «Non conoscere è già una ferita».

- Riga 581: `NPC_SAQI_PLAYER_33f03e66-a5af-4e9a-8cd3-06881a0777f5_HEROIC`
- Riga 582: `NPC_SAQI_PLAYER_33f03e66-a5af-4e9a-8cd3-06881a0777f5_JOKER`
- Riga 583: `NPC_SAQI_PLAYER_33f03e66-a5af-4e9a-8cd3-06881a0777f5_SCHOLAR`
- Riga 584: `NPC_SAQI_PLAYER_33f03e66-a5af-4e9a-8cd3-06881a0777f5_STOIC`
- Riga 711: `NPC_SAQI_RESPONSE_a38a82bf-3164-43e6-a776-741b8c92f45d`

`Something to mend` riguarda le cure, dato che il seguito richiede Tenderberry. Non trasformato in materiali per riparare equipaggiamento. Le città naniche restano chiuse agli estranei, anche nani; la successiva regola sul non ritorno è espressamente riferita a Heimen, non estesa arbitrariamente al protagonista.

- Riga 690: `NPC_SAQI_RESPONSE_174cc37f-23c1-494e-bb5e-adaf50af03ed`
- Riga 702: `NPC_SAQI_RESPONSE_589d7f1f-f8f9-4cf6-b5aa-e21c3caa28ce`
- Riga 698: `NPC_SAQI_RESPONSE_439144d7-7614-48cf-a9c0-e969542a47be`
- Riga 705: `NPC_SAQI_RESPONSE_5d5b9077-7a84-4ed6-b3ef-9ceaef58b440`
- Riga 710: `NPC_SAQI_RESPONSE_9f257223-24a6-4b85-8934-86ea67b452eb`
- Riga 713: `NPC_SAQI_RESPONSE_afc65fcf-2030-4536-9d2f-d4378d710d84`

### Guard, Lost Boy, Ronny e mercante

`I swear it on my post` è un giuramento sul posto/ruolo di guardia, reso «Lo giuro sul mio posto di guardia»: non introdotto un grado militare. Il bambino nega di essere stato catturato e chiama l'accaduto ricognizione: conservata la sua autodifesa, senza decidere per lui chi stia dicendo la verità. Ronny sostiene di non aver mai parlato con Befr pur essendo oggetto del suo aiuto: conservata l'ironia amara della situazione.

- Riga 469: `NPC_GUARD_RESPONSE_5f86ab76-9f9f-4bff-9129-4de74516e6a2`
- Riga 514: `NPC_LOSTBOY_RESPONSE_c51c1f18-57c6-45f3-98b8-1e1e93a2a518`
- Riga 547: `NPC_RONNY_RESPONSE_9740603a-934b-400f-8426-763a9a05ab90`

Il mercante elenca `bands` senza definire la categoria degli oggetti: «fasce», senza convertirle in anelli sulla sola supposizione. `Wards` resta «protezioni». La promessa di «raddoppiare la magia» resta una promessa del venditore, non è stata riscritta come statistica verificata. `I go where the roads allow and the blades don't` è ellittico: mantenuta la contrapposizione «Vado dove le strade lo permettono e le lame no», senza inventare un divieto specifico.

- Riga 781: `NPC_SUSPICIOUSTRADER_RESPONSE_974c5a04-8a79-4342-beec-d23b2e834aa0`
- Riga 782: `NPC_SUSPICIOUSTRADER_RESPONSE_b6200907-d2c4-4562-8294-64f710ca431c`

### Refusi, punteggiatura e conteggi

Nell'originale compaiono virgolette miste o non abbinate (per esempio 334 e 405) e punteggiatura mancante nelle `_BASE` (266, 378). Regolarizzate dove necessario, senza cambiare chiavi o segnaposto. Il titolo `Child oF Earlwood` contiene una maiuscola anomala; il titolo italiano è regolare.

- Riga 334: `NPC_CORIN_RESPONSE_f9cdc70c-6400-4ae8-8f8e-a4f14e948d6e`
- Riga 405: `NPC_FAUSTAS_RESPONSE_03d6ed3e-85b5-4355-89c2-b21a70754365`
- Riga 266: `NPC_CORIN_PLAYER_e4k9m2q7-a5c1-r8d3-b6f0-z1x7n4p2v9t5_BASE`
- Riga 378: `NPC_FAUSTAS_PLAYER_904350d3-b7bf-409e-866e-6aaf4da2661f_BASE`
- Riga 515: `NPC_LOSTBOY_TITLE`

I **206 record non giocatore** del brief comprendono anche **8 titoli e 1 etichetta del nome**. Le battute vere e proprie sono **197**: 20 saluti e 177 risposte. I personaggi con dialoghi sono otto; la nona voce è la sola etichetta della nota di Basilton. Non sono righe mancanti.

## Verifica finale

- **787 record**: Corin 257, Saqi 180, Faustas 90, Aelwynor 79, Mercante sospetto 55, Guard 50, Lost Boy 38, Ronny 37, Basilton's Note 1.
- Chiavi identiche, nello stesso ordine; nessuna chiave duplicata. Una sola tabulazione per record, testo non vuoto, nessun ritorno a capo interno.
- **1.030 occorrenze di segnaposto**: valori e molteplicità identici riga per riga. Ricostruzione in memoria con `tools/mt_mask.py` e `dlg5.tokens.json` senza rifiuti; asterischi delle didascalie conservati.
- **134 quartetti**, 536 varianti, **45 righe BASE**. Quattro rese distinte per ogni quartetto, oltre alla revisione linguistica dei registri.
- Blocchi: **1–131, 132–261, 262–391, 392–521, 522–651, 652–787**. Tutti fra 100 e 150 righe, nessun quartetto spezzato.
- Nessuna riga identica all'inglese; nessun residuo emerso dalla scansione degli indicatori inglesi comuni. Nomi propri e denominazioni vincolanti invariati dove richiesto.
- Controllo aggiuntivo di **378 corrispondenze** terminologiche e di nomi rilevanti, con gestione di plurali, apostrofi e confini di parola: nessuna discrepanza.
- **113 gruppi di segmenti ripetuti** di oltre 50 caratteri inglesi, separati dai segnaposto: resa italiana identica in tutti i rami. Controllati anche i testi integralmente duplicati.
- File assemblato e scritto direttamente con `Path.write_text(..., encoding="utf-8")`; riapertura con decodifica UTF-8 rigorosa, senza BOM né caratteri sostitutivi. Verificati gli accenti `à è é ì ò ù`.
- Nessuna modifica all'input, al riferimento o ai lotti precedenti. Questa consegna produce TSV e note; non comprende importazione, installazione o verifica a schermo nel gioco.

**Criterio riutilizzabile:** nei lotti con molti personaggi, fissare le voci prima della traduzione e riprenderle a ogni cambio. Separare il controllo dei quartetti da quello dei monologhi ripetuti nei rami. Per le ambiguità operative, confrontare dialoghi e obiettivi delle missioni; documentare i disallineamenti senza riscrivere silenziosamente la trama o le risorse richieste.
