# Incarico: traduzione dei dialoghi — lotto `dlg3`

Traduzione amatoriale di **Dimraeth** (Mudtek), RPG d'azione fantasy.
Quattordici categorie su sedici sono complete e approvate. Restano i dialoghi,
divisi in **cinque lotti per personaggio** perché la voce di ciascun NPC resti
coerente. `dlg1` (Myrll, Manga) è chiuso e installato; `dlg2` (Tamsin,
Basilton) è in lavorazione.

Questo è il terzo: **Eldorian** e **Alaric**.

---

## Cosa fare

Tradurre la **seconda colonna** di `work/mt/dlg3.tsv` — 954 righe, 98.525
caratteri — e salvare come `work/mt/dlg3.it.tsv`.

| file | ruolo |
|---|---|
| `work/mt/dlg3.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/dlg3.it.tsv` | **output da produrre** |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.675 coppie EN→IT |

Composizione del lotto: Eldorian 494 righe, Alaric 460.
**161 quartetti** di tono, 73 righe `_BASE`, 237 righe di risposta dell'NPC.

---

## La cosa più importante: le quattro varianti di tono

Il giocatore sceglie una **personalità** a inizio partita, e ogni sua battuta
esiste in quattro versioni. Lo vedi dal suffisso della chiave:

| suffisso | personalità | come suona in italiano |
|---|---|---|
| `_HEROIC` | l'eroe tradizionale | diretto, schietto, cavalleresco. Frasi piene, niente ironia |
| `_JOKER` | il burlone | leggero, ironico, colloquiale. Battute e understatement |
| `_SCHOLAR` | lo studioso | preciso, curioso, lessico più ricco. Fa domande, cita, spiega |
| `_STOIC` | lo stoico | asciutto, controllato, poche parole. Mai enfasi esplicita |

Le quattro varianti della **stessa** battuta sono **righe adiacenti**, perché le
chiavi sono ordinate. **Traducile sempre insieme, mai separate fra due blocchi.**

Il punto non è renderle diverse per forza: è che **la differenza di registro
dell'inglese deve restare percepibile in italiano**. Se le quattro versioni
inglesi si distinguono e le tue quattro suonano uguali, la scelta del giocatore
non conta più niente — è l'errore più grave che si possa fare in questo file.

Le righe `_BASE` sono neutre, senza variante di personalità.

---

## ATTENZIONE PARTICOLARE IN QUESTO LOTTO: il genere del giocatore

Il gioco fa **scegliere il sesso del personaggio** (`Male` / `Female`), e
l'inglese lo aggira perché «you» non ha genere. L'italiano no: ogni aggettivo o
participio riferito al giocatore costringe a una scelta.

**Convenzione del progetto, fissata in `dlg1`: il giocatore è al MASCHILE.**
Manga lo accoglie con «Viandante, bentornato», «Viandante, benvenuto».

Due regole, in quest'ordine:

1. **Dove puoi, gira la frase e non far comparire il genere.** «Sei stanco?» →
   «Sei in forze?»; «Sei pronto?» → «Tutto pronto?»; «Sarai il benvenuto» →
   «Avrai il mio benvenuto». È sempre la soluzione migliore.
2. **Dove il genere è inevitabile, maschile.**

Attenzione a non confondere i due versi: quando è il **giocatore** a parlare a
un'NPC donna, l'accordo è **femminile** e va tenuto — in `dlg1` è corretto
«Tornerò quando sarai pronta» rivolto a Myrll.

In questo lotto il rischio è concentrato su **Eldorian**, che si rivolge al
giocatore in tono personale e affettuoso per buona parte delle sue righe.

---

## È parlato, non scritto

- **Italiano parlato e naturale.** Contrazioni, ellissi, ordine delle parole
  colloquiale dove l'inglese è colloquiale.
- **Non tradurre la sintassi inglese.** Una frase che in inglese scorre può
  risultare legnosa se ricalcata: riscrivila come la direbbe un italiano.
- **Il "tu" fra personaggi.** Il "lei" solo se il rapporto lo richiede davvero.
- **Mantieni interiezioni e pause.** Puntini, trattini ed esitazioni fanno parte
  della recitazione.
- **Non appiattire.** Se un personaggio è brusco, resti brusco anche in italiano.

---

## Le due voci di questo lotto

Come in `dlg2`, sono voci **opposte**, e la loro distanza regge il lotto: un
ragazzo che parla troppo e un comandante che pesa ogni parola.

### Eldorian — la giovane recluta

Esploratore alle prime armi, sotto **Rahaner** e **Alaric**. Entusiasta, si
lascia trasportare e poi si scusa («Oh, right, the forest gate! Sorry, got
carried away for a moment»). Si sminuisce con sincerità — «I do listen. I
just… fail at it sometimes» — ma non è sciocco: sul lavoro è competente e
preciso quando riferisce posizioni e ronde.

Ha una magia che è solo sua: un **eco luminoso** che nessun altro può lanciare
né vedere, se non è lui ad aprirlo. Quando ne parla il tono cambia e si fa
sommesso.

C'è un filo affettivo verso il giocatore: vuole portarlo nel suo posto
preferito, sotto la luna, e la cosa lo imbarazza. **Tienilo trattenuto**: è
timidezza, non corteggiamento esplicito. Qui si applica in pieno la regola sul
genere del giocatore, sopra.

In italiano: **mosso, colloquiale, con partenze e ripartenze**. Contrazioni ed
elisioni sì. Le didascalie lo mostrano che deglutisce, sbatte le palpebre, si
raddrizza cercando un contegno: quei gesti sono parte della voce, non
decorazione — rendili con la stessa concretezza.

### Alaric — il comandante di Earlwood

Autorità del villaggio. **Misurato e grave**: sceglie le parole una per una, e
le didascalie lo dicono apertamente. Parla per giudizi e sentenze — sulla forza,
sul comando, sul dovere — e valuta le persone come casi morali: Saqi che è
schietta perché «le parole morbide non sempre sono gentili», Corin con «un'ombra
dura alle spalle. Non cattiveria. Non debolezza. Una ferita che ha imparato a
portare una lama».

Non è però solenne a ogni riga: quando dà ordini è **piano e diretto**, e
l'inglese gli concede le contrazioni («We'll see him supplied», «they're
raiding»). Non irrigidirlo in un registro aulico uniforme: la gravità sta nel
peso di ciò che dice, non in un lessico alto costante.

Immagini ricorrenti da conservare: il **peso**, il **cardine**, l'**ombra**, la
**lama**, il **terreno sotto i piedi**.

---

## Regole di formato — inderogabili

1. **Una riga di output per ogni riga di input**, stesso numero, stesso ordine.
2. **La prima colonna (la chiave) non si tocca mai.**
3. **Separatore: una tabulazione.** Il testo tradotto non deve contenerne.
4. **Codifica UTF-8**, accenti veri: `à è é ì ò ù`. Scrivi il file direttamente
   in UTF-8 — in un lotto precedente un passaggio per la pipe ASCII di
   PowerShell 5.1 ha sostituito tutti i non-ASCII e il file è stato da rifare.
5. **Nessun ritorno a capo dentro una traduzione.** Una riga = un record.
6. Niente intestazioni, commenti, numerazione o blocchi di codice.

### I segnaposto `<x1/>`

Vanno **ricopiati identici**, possono **cambiare posizione** se la sintassi
italiana lo richiede, ma **non possono sparire, duplicarsi né esserne inventati
di nuovi**. Una riga che ne perde uno viene **rifiutata** e resta in inglese.

---

## Terminologia — `reference.tsv` è la legge

2.675 coppie, frutto di cinque giri già approvati e installati. Quando un
termine del riferimento compare, usa **esattamente** la resa indicata: il
giocatore ha già quei nomi davanti nell'interfaccia, sulla mappa e
nell'inventario.

I **nomi propri di persona degli NPC restano in inglese**: Eldorian, Alaric,
Rahaner, Saqi, Corin, Tamsin, Basilton, Myrll, Manga.

### Termini che ricorrono in questo lotto

| Inglese | Resa |
|---|---|
| Waygate | **Varco** |
| Sanctum | **Santuario** |
| Guild | **Gilda** |
| Corruption | **Corruzione** |
| Dryad / Dryads | **Driade / Driadi** |
| Treant / Treants | **Treant** — invariato anche al plurale: «i Treant» |
| Goblin / Goblins | **Goblin** — invariato anche al plurale |
| Old Ones | **Antichi** |
| Wildwood, Mirkea, Earlwood | invariati |
| Stamina | **Vigore** |
| Deed | **Incarico** |
| beacon | **segnalatore** |

**Occhio a `echo`.** L'eco di Eldorian è **prosa**, non una meccanica: rendilo
liberamente («eco», «riverbero»). Non confonderlo con l'incantesimo *Temporal
Echo* → **Eco temporale**, né con *Echo Rift* → **Fenditura d'eco**, che sono
termini vincolanti dell'interfaccia. Nel lotto compare anche `echo` come verbo
(«mortal hierarchies echo the gods' order»): lì è «rispecchiare», «riflettere».

Se un termine non è nel riferimento, traducilo sensatamente e **annotalo**.

---

## Come procedere

Blocchi di **100-150 righe**, in ordine, senza saltare nulla — ma **non spezzare
mai un gruppo di quattro varianti di tono fra due blocchi**. Se un blocco
finirebbe a metà di un gruppo, allungalo o accorcialo di qualche riga.

Concatena i blocchi in un unico `dlg3.it.tsv` alla fine.

---

## Verifica prima di consegnare

1. Le righe di `dlg3.it.tsv` sono **954**, come l'input.
2. Le chiavi sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` dell'input è presente nell'output, uguale.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese.
6. I **161 quartetti** sono interi e le quattro varianti si distinguono fra loro.
7. Il file è davvero UTF-8: riapri e controlla che gli accenti siano accenti.
8. Gli accordi riferiti al **giocatore** sono al maschile, o aggirati.

---

## In fondo alla consegna, riporta

- come hai caratterizzato **la voce di Eldorian e quella di Alaric** in italiano,
  in due righe ciascuna: serve agli altri lotti e a chi rileggerà;
- i termini nuovi che hai deciso tu, in tabella `Inglese | Resa | Nota`;
- **le righe in cui hai dovuto forzare il genere del giocatore**, con la chiave:
  sono quelle da rileggere a schermo;
- le righe su cui hai avuto dubbi di senso, **con la chiave**;
- le incoerenze notate **nel testo inglese originale**.

Le note dei lotti precedenti sono in `work/mt/dlg1.it.note.md`: stesso formato,
ed è stato utile così com'era.
