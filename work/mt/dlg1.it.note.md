# Note di consegna — dlg1

Traduzione completata: **1.248 righe**, UTF-8 senza BOM, nessuna intestazione.
Input e riferimento: `dlg1.tsv` e `reference.tsv`, nella stessa cartella.

## Voci

**Manga** — Voce ferma, misurata e dignitosa; frasi compiute, sentenze brevi e immagini di acciaio, fuoco, incudine e tempra.
Il calore affiora con discrezione; la filosofia resta pronunciabile, distinguendo sempre la forza personale dal potere esercitato sugli altri.

**Myrll** — Voce delicata ed esitante, con pause, autocorrezioni e immagini di radici, respiro, muschio e piccole vite.
La vulnerabilità convive con fermezza morale: quando difende Basilton, la gentilezza o la propria sopravvivenza, parla chiaramente senza diventare aggressiva.

## Registri del giocatore

- HEROIC: diretto, leale, frasi piene e dichiarazioni nette, senza aggiungere ironia.
- JOKER: colloquiale, battute, immagini concrete e ironia; conservate anche le punte crudeli presenti nell'originale.
- SCHOLAR: analitico e curioso, lessico più preciso, ragionamenti e richieste di spiegazioni.
- STOIC: conciso, controllato, con domande essenziali; conservato il significato delle espressioni affettive già presenti nell'inglese, senza amplificarle.

I 225 quartetti hanno tutti quattro traduzioni distinte. Le differenze sono state valutate durante la traduzione congiunta; l'unicità delle stringhe è soltanto il controllo strutturale aggiuntivo.

## Termini nuovi e decisioni

Queste rese non modificano `reference.tsv`; sono annotate per la revisione e l'eventuale estensione del glossario.

| Inglese | Resa adottata | Nota |
|---|---|---|
| Praesidiism | Presidiismo | Dottrina di Manga; nuova resa. |
| rune smith | fabbro runico | Derivazione da «forgiatura runica». |
| forge master | maestro fabbro / maestro della fucina | Titolo e descrizione del ruolo, secondo la frase. |
| rune dust | polvere runica | Non assimilata arbitrariamente a Rune Essence → Essenza runica. |
| Minotaur Empire | Impero dei Minotauri | Denominazione collettiva. |
| Barrens | Terre Aride | Regione di provenienza di Manga. |
| Southern Barrens | Terre Aride Meridionali | Variante geografica. |
| Tree-Father / Treefathers / tree-father | Padre degli Alberi / Padri degli Alberi | Uniformate le grafie del medesimo titolo. |
| forest-kin / forest kin | gente della foresta / appartenere alla foresta | Espressione relazionale, adattata alla sintassi. |
| Choking Vine | Vite Soffocante | Toponimo assente dal riferimento. |
| the purge | la purga | Evento storico nel racconto di Myrll. |
| the turning | la trasformazione | Mutamento delle sacerdotesse in driadi; distinto da rebirth → rinascita. |
| Numen realm | regno di Numen | «Numen» mantenuto; natura del termine da confermare. |
| Exile Of Xwin | Esule di Xwin | Titolo di Manga. |
| The Gentlest Spirit | Lo spirito più gentile | Titolo di Myrll. |

`rune-smithing` è stato ricondotto alla voce già vincolante `runesmithing` → **forgiatura runica**. `Rootweavers` usa **Tessiradici**, già nel riferimento; `High Priestess` usa **Somma Sacerdotessa**, coerente con il titolo di Althaea.

**Acorn** resta invariato perché qui è il nome proprio dell'amico di Basilton: si applica la regola esplicita sui nomi degli NPC. La coppia Acorn → Ghianda del glossario è stata applicata come traduzione del sostantivo comune, senza estenderla al nome del personaggio. Mantenuti anche i nomi propri non glossati, fra cui Agir, Akolasis, Ira, Eastwind e Xwin. Faerethil e Tirathlan restano invariati; il testo stesso spiega Faerethil.

## Passaggi dubbi e particolarità dell'originale

### Carovana, armi e pronomi

Il testo alterna caravan, it e them. Nelle righe 166 e 169 il plurale non ha un antecedente grammaticale chiaro: reso esplicitamente come «armi», in base alla missione. Nella 153 il secondo it è reso «carico». Da confermare nel ramo di dialogo in gioco.

- Riga 153: `NPC_MANGA_PLAYER_52215722-bdc2-40fb-96a1-6a8c4877e133_HEROIC`
- Riga 155: `NPC_MANGA_PLAYER_52215722-bdc2-40fb-96a1-6a8c4877e133_SCHOLAR`
- Riga 166: `NPC_MANGA_PLAYER_53ef28ce-5b2b-4c10-b0c5-c9a51ef1f15c_HEROIC`
- Riga 169: `NPC_MANGA_PLAYER_53ef28ce-5b2b-4c10-b0c5-c9a51ef1f15c_STOIC`

### «my smith and my steel»

«My smith» appare improprio nella bocca del fabbro stesso; interpretato come la sua arte di fabbro, senza introdurre un secondo personaggio.

- Riga 515: `NPC_MANGA_RESPONSE_3ac17e1a-310c-400e-9a7c-0d225ea90243`
- Riga 556: `NPC_MANGA_RESPONSE_810fc930-06a6-4508-853b-e723901bc140`
- Riga 609: `NPC_MANGA_RESPONSE_f6633faf-4bd9-4bc9-91bc-fb249fa7f4d4`

### «their path» nella variante HEROIC

Il possessivo their non ha un antecedente esplicito, mentre le altre tre varianti usano your path. Conservata «la loro strada» nella variante HEROIC, senza uniformare silenziosamente il contenuto.

- Riga 807: `NPC_MYRLL_PLAYER_654c0e52-4890-4bca-8674-531337e1793c_HEROIC`

### You singolare o collettivo

Nel racconto della trasformazione, you è stato inteso come riferito a Myrll e alle altre sacerdotesse. Le risposte parlano esplicitamente di us e we; usato quindi il plurale nei rispettivi quartetti e nella domanda a Ceres.

- Riga 702: `NPC_MYRLL_PLAYER_26a0f1bb-0177-4f6d-b11b-adffaeaadbbc_HEROIC`
- Riga 1010: `NPC_MYRLL_PLAYER_cd9a58a1-942f-424e-9882-5a8d2486e075_HEROIC`
- Riga 1038: `NPC_MYRLL_PLAYER_deebfb3a-3715-46a1-b937-99feb97571b6_BASE`

### Legame con la foresta

Myrll dice di essere stata abbandonata e separata dalla foresta, ma afferma anche che il boschetto le risponde ancora. Un altro ramo precisa che il legame persiste in parte. Conservate tutte queste sfumature: apparente tensione narrativa, non errore certo.

- Riga 1139: `NPC_MYRLL_RESPONSE_39c7f94f-8a12-4b0b-877c-70b028d6589f`
- Riga 1125: `NPC_MYRLL_RESPONSE_20521c41-0861-4d47-871c-0eb872a9cd9e`
- Riga 1158: `NPC_MYRLL_RESPONSE_577e950e-3304-4b60-b071-e90bfb74499f`

### «great old»

Interpretato come riferimento agli Antichi, coerentemente con le battute sui Varchi e con Old Ones → Antichi. La grafia e la denominazione inglesi non sono uniformi.

- Riga 1168: `NPC_MYRLL_RESPONSE_67702f6b-cb98-420c-841f-cb136929fc4a`

### Numen

Non è definito nel glossario se Numen sia un nome di luogo o la qualificazione di un piano spirituale. Resa prudente «regno di Numen», da confermare con il contesto più ampio.

- Riga 1239: `NPC_MYRLL_RESPONSE_f26e747b-a798-4e13-a396-e88895b5a5c2`

### Frase incompleta sul Treant

«He could no longer tell friend from foe, even a threat to the forest» ha una seconda parte grammaticalmente sospesa. Interpretata come «era ormai una minaccia persino per la foresta». È un punto da verificare contro il contesto narrativo.

- Riga 1244: `NPC_MYRLL_RESPONSE_f93952a8-641f-49a8-8893-f84f0576a209`

### Punteggiatura inglese

La risposta 490 e le sue riprese aprono una citazione prima di «Enough of the Mayor’s games» senza chiuderla prima del paragrafo successivo. Mantenuta la struttura. La 432 mescola virgolette tipografiche e dritte: normalizzata la coppia in italiano. Sono presenti anche capitalizzazioni variabili di Sanctum, Goblin, Dryad e Tree-Father; non implicano entità diverse.

- Riga 490: `NPC_MANGA_RESPONSE_100321b7-e056-4a3a-9e92-cc9d55f0a957`
- Riga 432: `NPC_MANGA_PLAYER_d98ed96e-47ff-4cb1-90f6-8aee6bcf8c4f_BASE`

## Verifica finale

- 1.248 record, stesso numero dell'input, con chiavi identiche e nello stesso ordine.
- Due colonne per record, separate da una sola tabulazione; nessun testo vuoto o ritorno a capo interno.
- Segnaposto `<x…/>` identici per valore e molteplicità in ogni riga.
- Nessuna riga coincidente con il testo inglese; revisione linguistica eseguita durante la traduzione di tutti i blocchi.
- 225 quartetti contigui, tutti nell'ordine HEROIC, JOKER, SCHOLAR, STOIC; nessun quartetto spezzato.
- Blocchi: 1–127, 128–252, 253–378, 379–503, 504–628, 629–753, 754–881, 882–1009, 1010–1134, 1135–1248.
- Terminologia verificata anche per varianti flessionali e grafiche; nessuna modifica all'input o al riferimento.
- UTF-8 verificato con accenti e punteggiatura Unicode effettivi. Un passaggio iniziale attraverso la pipe ASCII di Windows PowerShell 5.1 aveva sostituito i caratteri non ASCII: il file è stato ricostruito dalle traduzioni originali integre e riscritto direttamente con `Path.write_text(..., encoding="utf-8")` prima della validazione finale.

Non è stata eseguita una prova nel gioco: l'incarico riguarda il TSV, non l'integrazione. Restano quindi da verificare nel contesto interattivo soltanto i riferimenti narrativi segnalati sopra.
