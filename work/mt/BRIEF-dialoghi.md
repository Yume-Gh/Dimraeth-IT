# Incarico: traduzione dei dialoghi — lotto `dlg1`

Ultimo blocco della traduzione amatoriale di **Dimraeth** (Mudtek), RPG d'azione
fantasy. Quattordici categorie su sedici sono complete e approvate: restano i
dialoghi, il 41% dell'intero progetto.

I dialoghi sono divisi in **cinque lotti per personaggio**, così la voce di
ciascun NPC resta coerente. Questo è il primo: **Myrll** e **Manga**.

---

## Cosa fare

Tradurre la **seconda colonna** di `work/mt/dlg1.tsv` — 1.248 righe, 127.596
caratteri — e salvare come `work/mt/dlg1.it.tsv`.

| file | ruolo |
|---|---|
| `work/mt/dlg1.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/dlg1.it.tsv` | **output da produrre** |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.650+ coppie EN→IT |

---

## La cosa più importante: le quattro varianti di tono

Il giocatore sceglie una **personalità** a inizio partita, e ogni battuta esiste
in quattro versioni. Lo vedi dal suffisso della chiave:

| suffisso | personalità | come suona in italiano |
|---|---|---|
| `_HEROIC` | l'eroe tradizionale | diretto, schietto, cavalleresco. Frasi piene, niente ironia |
| `_JOKER` | il burlone | leggero, ironico, colloquiale. Può permettersi battute e understatement |
| `_SCHOLAR` | lo studioso | preciso, curioso, lessico più ricco. Fa domande, cita, spiega |
| `_STOIC` | lo stoico | asciutto, controllato, poche parole. Mai enfasi, mai emozione esplicita |

Le quattro varianti della **stessa** battuta sono **righe adiacenti** nel file,
perché le chiavi sono ordinate. **Traducile sempre insieme, mai separate fra due
blocchi.**

Il punto non è tradurle in modo diverso per forza: è che **la differenza di
registro dell'inglese deve restare percepibile in italiano**. Se le quattro
versioni inglesi si distinguono e le tue quattro versioni italiane suonano
uguali, la scelta del giocatore non conta più niente — ed è l'errore più grave
che si possa fare in questo file.

Le righe `_BASE` sono neutre, senza variante di personalità.

---

## È parlato, non scritto

Questi sono **dialoghi**, non descrizioni. Valgono regole diverse dai giri
precedenti:

- **Italiano parlato e naturale.** Contrazioni, ellissi, ordine delle parole
  colloquiale dove l'inglese è colloquiale.
- **Non tradurre la sintassi inglese.** Una frase che in inglese scorre può
  risultare legnosa in italiano se ricalcata: riscrivila come la direbbe un
  italiano.
- **Il "tu" fra personaggi.** Il "lei" solo se il rapporto lo richiede davvero.
- **Mantieni le interiezioni e le pause.** I puntini, i trattini, le esitazioni
  fanno parte della recitazione.
- **Non appiattire.** Se un personaggio è brusco, resti brusco anche in italiano.

### Le due voci di questo lotto

Myrll e Manga hanno ciascuno un carattere riconoscibile nell'inglese. **Leggi
qualche battuta di ciascuno prima di cominciare**, decidi come suona quella
persona in italiano, e tieni quella voce per tutte le sue righe. La coerenza
interna di un personaggio conta più dell'eleganza della singola frase.

---

## Regole di formato — inderogabili

1. **Una riga di output per ogni riga di input**, stesso numero, stesso ordine.
2. **La prima colonna (la chiave) non si tocca mai.**
3. **Separatore: una tabulazione.** Il testo tradotto non deve contenerne.
4. **Codifica UTF-8.** Accenti veri: `à è é ì ò ù`.
5. **Nessun ritorno a capo dentro una traduzione.** Una riga = un record.
6. Niente intestazioni, commenti, numerazione o blocchi di codice.

### I segnaposto `<x1/>`

Vanno **ricopiati identici**, possono **cambiare posizione** se la sintassi
italiana lo richiede, ma **non possono sparire, duplicarsi né esserne inventati
di nuovi**. Una riga che ne perde uno viene **rifiutata** e resta in inglese.

---

## Terminologia — `reference.tsv` è la legge

Oltre 2.650 coppie, frutto di quattro giri già approvati. Quando un termine del
riferimento compare, usa **esattamente** la resa indicata: il giocatore ha già
quei nomi davanti nell'interfaccia, sulla mappa e nell'inventario.

I **nomi propri di persona degli NPC restano in inglese** (Myrll, Manga, Alaric,
Tamsin…), come hanno fatto i localizzatori ufficiali.

Attenzione particolare qui: i personaggi parlano di luoghi, oggetti e creature
che il giocatore trova altrove tradotti. `Waygate` è **Varco**, `Sanctum` è
**Santuario**, `beacon` è **segnalatore**, `Deed` è **Incarico**, `Stamina` è
**Vigore**.

Se un termine non è nel riferimento, traducilo sensatamente e **annotalo**.

---

## Come procedere

Blocchi di **100-150 righe**, in ordine, senza saltare nulla — ma **non spezzare
mai un gruppo di quattro varianti di tono fra due blocchi**. Se un blocco
finirebbe a metà di un gruppo, allungalo o accorcialo di qualche riga.

Concatena i blocchi in un unico `dlg1.it.tsv` alla fine.

---

## Verifica prima di consegnare

1. Le righe di `dlg1.it.tsv` sono **1.248**, come l'input.
2. Le chiavi sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` dell'input è presente nell'output, uguale.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese.
6. **Le quattro varianti di tono di una stessa battuta si distinguono fra loro.**

---

## In fondo alla consegna, riporta

- come hai caratterizzato **la voce di Myrll e quella di Manga** in italiano, in
  due righe ciascuna: serve a mantenerle uguali negli altri lotti e a chi
  rileggerà;
- i termini nuovi che hai deciso tu;
- le righe su cui hai avuto dubbi di senso, con la chiave;
- le incoerenze notate **nel testo inglese originale**.
