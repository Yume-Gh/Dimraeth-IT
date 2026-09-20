# Incarico: traduzione dei dialoghi — lotto `dlg2`

Traduzione amatoriale di **Dimraeth** (Mudtek), RPG d'azione fantasy.
Quattordici categorie su sedici sono complete e approvate. Restano i dialoghi,
divisi in **cinque lotti per personaggio** perché la voce di ciascun NPC resti
coerente. Il primo lotto (Myrll e Manga) è **chiuso, importato e installato**.

Questo è il secondo: **Tamsin** e **Basilton**.

---

## Cosa fare

Tradurre la **seconda colonna** di `work/mt/dlg2.tsv` — 914 righe, 106.514
caratteri — e salvare come `work/mt/dlg2.it.tsv`.

| file | ruolo |
|---|---|
| `work/mt/dlg2.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/dlg2.it.tsv` | **output da produrre** |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.674 coppie EN→IT |

Composizione del lotto: Tamsin 484 righe, Basilton 430.
**160 quartetti** di tono, 57 righe `_BASE`, 217 righe di risposta dell'NPC.

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

Sono voci **opposte**, ed è la loro distanza a reggere il lotto. Leggi qualche
battuta di ciascuno prima di cominciare, decidi come suona quella persona in
italiano, e tieni quella voce per tutte le sue righe. La coerenza interna di un
personaggio conta più dell'eleganza della singola frase.

### Tamsin — la filatrice del villaggio

Giovane, calorosa, entusiasta. Parla in fretta, si interrompe, si corregge,
gesticola: le didascalie la mostrano che intreccia e scioglie le dita mentre
parla. Si espone emotivamente e poi teme di aver detto troppo.

Tiene al villaggio e lo protegge concretamente — fila, tesse stendardi e
protezioni — ed è curiosa del mondo, in particolare degli Antichi e delle loro
uova. Il filo narrativo del lotto è che **impara a porre un limite**: non può
continuare ad aiutare chiunque glielo chieda.

In italiano: **colloquiale, mosso, con esclamazioni e domande dirette**
(«Ah?», «Ahia.», «Affascinante, vero?»). Contrazioni ed elisioni sì. La sua
insicurezza è nel ritmo — frasi che ripartono, incisi — non in un lessico
dimesso: quando parla del suo mestiere è competente e precisa.

### Basilton — il giardiniere gentile

L'essere mite nato dalla foresta, amico di **Acorn**, difeso da Myrll contro i
**Padri degli Alberi**. Voce **mite ma ferma**: non alza mai il tono e non cede
mai il punto. Parla per sentenze brevi e immagini di rami, radici, giardino,
doni e cura. Registro alto, quasi liturgico quando nomina Ceres.

In italiano: **niente contrazioni, niente colloquialismi**. L'inglese gli evita
sistematicamente le forme contratte («I would rather», «Do not tell anyone»):
rendi quella distanza con la forma piena e con un ordine delle parole composto.
La gentilezza non deve diventare sottomissione — quando corregge il giocatore,
corregge davvero.

**Continuità con `dlg1`:** Myrll racconta di lui, del suo giardino e di come la
foresta lo tratti. Se una battuta di Basilton tocca gli stessi fatti, i nomi e
le rese devono coincidere (vedi la sezione seguente).

---

## Regole di formato — inderogabili

1. **Una riga di output per ogni riga di input**, stesso numero, stesso ordine.
2. **La prima colonna (la chiave) non si tocca mai.**
3. **Separatore: una tabulazione.** Il testo tradotto non deve contenerne.
4. **Codifica UTF-8**, accenti veri: `à è é ì ò ù`. Scrivi il file direttamente
   in UTF-8 — nel lotto precedente un passaggio per la pipe ASCII di PowerShell
   5.1 ha sostituito tutti i caratteri non ASCII e il file è stato da rifare.
5. **Nessun ritorno a capo dentro una traduzione.** Una riga = un record.
6. Niente intestazioni, commenti, numerazione o blocchi di codice.

### I segnaposto `<x1/>`

Vanno **ricopiati identici**, possono **cambiare posizione** se la sintassi
italiana lo richiede, ma **non possono sparire, duplicarsi né esserne inventati
di nuovi**. Una riga che ne perde uno viene **rifiutata** e resta in inglese.

---

## Terminologia — `reference.tsv` è la legge

2.674 coppie, frutto di cinque giri già approvati e installati. Quando un
termine del riferimento compare, usa **esattamente** la resa indicata: il
giocatore ha già quei nomi davanti nell'interfaccia, sulla mappa e
nell'inventario.

I **nomi propri di persona degli NPC restano in inglese** (Tamsin, Basilton,
Myrll, Manga, Alaric…), come hanno fatto i localizzatori ufficiali.

`Waygate` è **Varco**, `Sanctum` è **Santuario**, `beacon` è **segnalatore**,
`Deed` è **Incarico**, `Stamina` è **Vigore**.

### Termini fissati in `dlg1` — usarli identici

| Inglese | Resa |
|---|---|
| Acorn (l'amico di Basilton) | **Acorn** — è un nome proprio, non «Ghianda» |
| Tree-Father / Treefathers | **Padre degli Alberi / Padri degli Alberi** |
| forest-kin / forest kin | **gente della foresta** |
| the purge | **la purga** (l'evento storico che colpì gli elfi) |
| Rootweavers | **Tessiradici** |
| High Priestess | **Somma Sacerdotessa** |
| Old Ones | **Antichi** |
| Ceres | **Ceres** (invariato) |
| Barrens / Southern Barrens | **Terre Aride / Terre Aride Meridionali** |
| Choking Vine | **Vite Soffocante** |
| runesmithing | **forgiatura runica** |

Se un termine non è nel riferimento, traducilo sensatamente e **annotalo**.

---

## Come procedere

Blocchi di **100-150 righe**, in ordine, senza saltare nulla — ma **non spezzare
mai un gruppo di quattro varianti di tono fra due blocchi**. Se un blocco
finirebbe a metà di un gruppo, allungalo o accorcialo di qualche riga.

Concatena i blocchi in un unico `dlg2.it.tsv` alla fine.

---

## Verifica prima di consegnare

1. Le righe di `dlg2.it.tsv` sono **914**, come l'input.
2. Le chiavi sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` dell'input è presente nell'output, uguale.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese.
6. I **160 quartetti** sono interi e le quattro varianti si distinguono fra loro.
7. Il file è davvero UTF-8: riapri e controlla che gli accenti siano accenti.

---

## In fondo alla consegna, riporta

- come hai caratterizzato **la voce di Tamsin e quella di Basilton** in italiano,
  in due righe ciascuna: serve agli altri lotti e a chi rileggerà;
- i termini nuovi che hai deciso tu, in tabella `Inglese | Resa | Nota`;
- le righe su cui hai avuto dubbi di senso, **con la chiave**;
- le incoerenze notate **nel testo inglese originale**.

Le note del lotto precedente sono in `work/mt/dlg1.it.note.md`: stesso formato,
ed è stato utile così com'era.
