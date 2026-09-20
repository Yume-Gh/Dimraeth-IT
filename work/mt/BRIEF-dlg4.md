# Incarico: traduzione dei dialoghi — lotto `dlg4`

Traduzione amatoriale di **Dimraeth** (Mudtek), RPG d'azione fantasy.
Quattordici categorie su sedici sono complete e approvate. Restano i dialoghi,
divisi in **cinque lotti per personaggio** perché la voce di ciascun NPC resti
coerente. `dlg1` (Myrll, Manga) e `dlg2` (Tamsin, Basilton) sono chiusi e
installati; `dlg3` (Eldorian, Alaric) è in lavorazione.

Questo è il quarto, ed è **il più grande**: **Heimenthaldrik**, **Befr** e
**Rahaner**.

---

## Cosa fare

Tradurre la **seconda colonna** di `work/mt/dlg4.tsv` — 1.279 righe, 126.161
caratteri — e salvare come `work/mt/dlg4.it.tsv`.

| file | ruolo |
|---|---|
| `work/mt/dlg4.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/dlg4.it.tsv` | **output da produrre** |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.715 coppie EN→IT |

Composizione: Heimenthaldrik 496 righe, Befr 455, Rahaner 328.
**226 quartetti** di tono, 79 righe `_BASE`, 277 risposte, 16 saluti.

---

## Questo lotto è fatto per tre quarti di battute del GIOCATORE

983 righe su 1.279 — il **77%** — sono battute del giocatore: 226 quartetti più
79 righe `_BASE`. Solo 296 righe sono parlate dai tre NPC.

Ne segue che **la distinzione fra le quattro varianti di tono è qui la qualità
principale del lavoro**, più che in ogni altro lotto. Se le quattro versioni
suonano uguali, in questo file hai sbagliato la parte maggiore dell'incarico.

| suffisso | personalità | come suona in italiano |
|---|---|---|
| `_HEROIC` | l'eroe tradizionale | diretto, schietto, cavalleresco. Frasi piene, niente ironia |
| `_JOKER` | il burlone | leggero, ironico, colloquiale. Battute e understatement |
| `_SCHOLAR` | lo studioso | preciso, curioso, lessico più ricco. Fa domande, cita, spiega |
| `_STOIC` | lo stoico | asciutto, controllato, poche parole. Mai enfasi esplicita |

Le quattro varianti della **stessa** battuta sono **righe adiacenti**, perché le
chiavi sono ordinate. **Traducile sempre insieme, mai separate fra due blocchi.**

Il punto non è renderle diverse per forza: è che **la differenza di registro
dell'inglese deve restare percepibile in italiano**. Le righe `_BASE` sono
neutre, senza variante di personalità.

---

## Il genere del giocatore

Il gioco fa **scegliere il sesso del personaggio** (`Male` / `Female`), e
l'inglese lo aggira perché «you» non ha genere. L'italiano no.

**Convenzione del progetto, già applicata in `dlg1` e `dlg2`: il giocatore è al
MASCHILE.** Due regole, in quest'ordine:

1. **Dove puoi, gira la frase e non far comparire il genere.** «Sei pronto?» →
   «Tutto pronto?»; «Sarai il benvenuto» → «Avrai il mio benvenuto».
2. **Dove il genere è inevitabile, maschile.**

Qui pesa soprattutto su **Befr**, che chiama il giocatore **«my friend» 62
volte**: rendilo sempre **«amico mio»**, non variarlo (vedi sotto).

Attenzione a non confondere i due versi: quando è il **giocatore** a parlare a
un'NPC donna, l'accordo è **femminile** e va tenuto.

---

## È parlato, non scritto

- **Italiano parlato e naturale.** Contrazioni, ellissi, ordine delle parole
  colloquiale dove l'inglese è colloquiale.
- **Non tradurre la sintassi inglese.** Riscrivi come lo direbbe un italiano.
- **Il "tu" fra personaggi.** Il "lei" solo se il rapporto lo richiede davvero.
- **Mantieni interiezioni e pause.** Puntini, trattini ed esitazioni fanno parte
  della recitazione.
- **Non appiattire.** Se un personaggio è brusco, resti brusco anche in italiano.

---

## Le tre voci di questo lotto

### Heimenthaldrik («Heimen») — il nano, ed è il problema difficile

Nano poeta e consigliere: «Heimen Thaldrik, son o' stone and stubborn ink. A
poet by heart, a dreamweaver by trade». Sa la storia (l'era imperiale elfica, i
templi di Ceres), forgia libri di incantesimi, e si offre come testimone e
consigliere del villaggio. Calore da taverna e precisione da studioso nella
stessa battuta. Giura «by stone and song».

**L'inglese gli dà un dialetto marcato**, e non è un vezzo occasionale:
**92 delle sue 115 battute** portano almeno una marca. Sono 173 in tutto:
`walkin'`, `readin'`, `speakin'` (91 gerundi elisi), `aye` e `ain't` (51),
`ye` per *you* (25), `o'` per *of*, `me` per *my*.

**Come renderlo in italiano — leggi questo due volte.**

Le marche inglesi sono **fonetiche**: segnalano una pronuncia. L'italiano non ha
un marcatore fonetico equivalente che non sia **regionale**, e un nano che parla
bergamasco o napoletano lo colloca su una mappa reale: sbagliato in un fantasy,
e ridicolo. Quindi:

- **Non usare un dialetto italiano regionale.** Mai.
- **Non inventare storpiature ortografiche.** In italiano sembrano errori di
  battitura, non accento.
- **Sposta la marca dalla FONETICA alla SINTASSI e al LESSICO.** È lì che
  l'italiano segnala il parlato popolare:
  - **troncamento dell'infinito**: «parlar chiaro», «andar per», «aver visto»;
  - **lessico concreto e artigiano**: pietra, vena, inchiostro, martello,
    filone, stampo — Heimen pensa per immagini di cava e di bottega;
  - **frasi brevi, paratattiche**, congiunzioni povere («e», «ma», «però»);
  - **sentenze e modi di dire**, che gli vengono naturali;
  - **elisioni colloquiali sobrie**: «'sto», «po'», «pe'» no — fermati a «'sto»
    e «po'», che sono panitaliani.
- `aye` → «sì», «eh sì», «proprio così»: **vàrialo**, perché 51 «sì» secchi
  appiattiscono. `ye` → semplicemente «tu»: il «voi» sarebbe deferenza, e qui
  non c'è.
- La marca va **solo nelle sue battute**. Le 381 righe del giocatore rivolte a
  lui non hanno dialetto nell'originale: non aggiungercelo.

L'obiettivo: chi legge deve sentire **un parlato popolare, caldo e sentenzioso**,
senza riuscire a dire di quale regione sia. Se una frase ti sembra macchietta,
è troppo.

### Befr — il vecchio mercante della carovana

Anziano, gioviale, affettuoso, un po' teatrale. Apre il pannello laccato del suo
carro per mostrare le cianfrusaglie luccicanti. Cortesia ornata e calorosa:
«What a splendid day to cross paths», «You have come at a fortuitous time».

Due tic verbali che sono la sua firma, da rendere **sempre allo stesso modo**:

| inglese | occorrenze | resa |
|---|---:|---|
| `Ho ho!` | 52 | **«Ho ho!»** — tienilo così, è una risata, non una parola |
| `my friend` | 62 | **«amico mio»** — sempre, senza variarlo |

Per il resto: italiano **pieno e cortese**, senza contrazioni brusche, con la
gentilezza un po' cerimoniosa di chi ha molti anni e vende bene. Non farlo
diventare sdolcinato: sotto la cordialità c'è un mercante.

### Rahaner — il veterano con un braccio solo

Comandante del perimetro, superiore di Eldorian. Asciutto, ironico per
sottrazione: «Well now, fresh boots on the path. Not many choose Earlwood these
days, not unless they're brave or foolish».

Parla per **frasi corte e chiuse**, spesso in coppie che si bilanciano:
«Readiness is useful. Nostalgia for it is dangerous». Quel ritmo binario è la
sua voce: **conservalo**, non scioglierlo in periodi lunghi.

Quando guarda indietro agli anni di servizio non è sentimentale — elenca
«duty, skill, endurance» e dice apertamente che l'orgoglio non è la prima
parola che gli viene. **Non aggiungere calore che l'inglese non mette.**

Ordini e informazioni operative: **piani e diretti**, senza enfasi.

---

## Regole di formato — inderogabili

1. **Una riga di output per ogni riga di input**, stesso numero, stesso ordine.
2. **La prima colonna (la chiave) non si tocca mai.**
3. **Separatore: una tabulazione.** Il testo tradotto non deve contenerne.
4. **Codifica UTF-8**, accenti veri: `à è é ì ò ù`. Scrivi il file direttamente
   in UTF-8 con `Path.write_text(..., encoding="utf-8")` — in un lotto
   precedente un passaggio per la pipe ASCII di PowerShell 5.1 ha sostituito
   tutti i non-ASCII e il file è stato da rifare.
5. **Nessun ritorno a capo dentro una traduzione.** Una riga = un record.
6. Niente intestazioni, commenti, numerazione o blocchi di codice.

### I segnaposto `<x1/>`

Vanno **ricopiati identici**, possono **cambiare posizione** se la sintassi
italiana lo richiede, ma **non possono sparire, duplicarsi né esserne inventati
di nuovi**. Una riga che ne perde uno viene **rifiutata** e resta in inglese.

---

## Terminologia — `reference.tsv` è la legge

2.715 coppie, frutto di sei giri già approvati e installati. Quando un termine
del riferimento compare, usa **esattamente** la resa indicata: il giocatore ha
già quei nomi davanti nell'interfaccia, sulla mappa e nell'inventario.

I **nomi propri di persona degli NPC restano in inglese**: Heimen, Heimen
Thaldrik, Befr, Rahaner, Eldorian, Alaric, Tamsin, Basilton, Myrll, Manga,
Corin, Saqi, Faustas.

### Termini che ricorrono in questo lotto

| Inglese | Resa |
|---|---|
| Dwarf / Dwarves | **Nano / Nani** — minuscolo nel parlato: «noi nani» |
| Treant / Treants | **Treant** — invariato anche al plurale |
| Goblin / Goblins | **Goblin** — invariato anche al plurale |
| Corrupted / Corruption | **Corrotto / Corruzione** |
| Waygate | **Varco** |
| Sanctum | **Santuario** |
| Spellbook | **Libro degli incantesimi** |
| Old Ones | **Antichi** |
| Iniquities | **Iniquità** |
| Eternal Forest | **Foresta Eterna** |
| Earlwood, Wildwood, Mirkea | invariati |
| Stamina | **Vigore** |
| Deed | **Incarico** |

Se un termine non è nel riferimento, traducilo sensatamente e **annotalo**.

---

## Come procedere

Blocchi di **100-150 righe**, in ordine, senza saltare nulla — ma **non spezzare
mai un gruppo di quattro varianti di tono fra due blocchi**. Se un blocco
finirebbe a metà di un gruppo, allungalo o accorcialo di qualche riga.

Concatena i blocchi in un unico `dlg4.it.tsv` alla fine.

**Consiglio specifico per questo lotto:** decidi la voce di Heimen sui primi
dieci esempi densi di dialetto, **scrivi come l'hai risolta**, e poi tienila
ferma per tutte le sue 115 battute. È la scelta che, se deriva a metà file, si
nota di più.

---

## Verifica prima di consegnare

1. Le righe di `dlg4.it.tsv` sono **1.279**, come l'input.
2. Le chiavi sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` dell'input è presente nell'output, uguale.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese.
6. I **226 quartetti** sono interi e le quattro varianti si distinguono.
7. Il file è davvero UTF-8: riapri e controlla che gli accenti siano accenti.
8. Gli accordi riferiti al **giocatore** sono al maschile, o aggirati.
9. Il dialetto di Heimen è **solo** nelle sue battute, e non è regionale.
10. `Ho ho!` e `amico mio` sono resi sempre allo stesso modo.

---

## In fondo alla consegna, riporta

- **come hai risolto la voce di Heimen**, con tre o quattro esempi prima/dopo:
  è la decisione più importante del lotto e va documentata per chi rileggerà;
- come hai caratterizzato **Befr** e **Rahaner**, due righe ciascuno;
- i termini nuovi che hai deciso tu, in tabella `Inglese | Resa | Nota`;
- **le righe in cui hai dovuto forzare il genere del giocatore**, con la chiave;
- le righe su cui hai avuto dubbi di senso, **con la chiave**;
- le incoerenze notate **nel testo inglese originale**.

Le note dei lotti precedenti sono in `work/mt/dlg1.it.note.md` e
`work/mt/dlg2.it.note.md`: stesso formato, ed è stato utile così com'era.
