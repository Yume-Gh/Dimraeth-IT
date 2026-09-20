# Incarico: traduzione dei dialoghi — lotto `dlg5`, l'ultimo

Traduzione amatoriale di **Dimraeth** (Mudtek), RPG d'azione fantasy.
Quattordici categorie su sedici erano già complete; i dialoghi sono divisi in
cinque lotti per personaggio. `dlg1`, `dlg2` e `dlg3` sono chiusi e installati,
`dlg4` è in lavorazione.

**Questo è il quinto e ultimo.** Con `dlg4` chiude `NPCDialogues` — ed è stato
verificato che insieme i due lotti coprono **tutte** le righe rimaste, senza
scoperti. Quando rientra, la traduzione del gioco è completa.

---

## Cosa fare

Tradurre la **seconda colonna** di `work/mt/dlg5.tsv` — 787 righe, 96.254
caratteri — e salvare come `work/mt/dlg5.it.tsv`.

| file | ruolo |
|---|---|
| `work/mt/dlg5.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/dlg5.it.tsv` | **output da produrre** |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.736 coppie EN→IT |

**134 quartetti** di tono, 45 righe `_BASE`, 206 righe parlate dagli NPC.

---

## Nove personaggi, non due

È l'unico lotto affollato. Le righe si dividono così:

| personaggio | righe | chi è |
|---|---:|---|
| Corin | 257 | il comandante degli esploratori |
| Saqi | 180 | la quartiermastra di Earlwood |
| Faustas | 90 | il mago, che appare come proiezione |
| Aelwynor | 79 | il Re della Foresta, un cervo titanico |
| Suspicious Trader | 55 | il mercante losco |
| Guard | 50 | la guardia intimidita |
| Lost Boy | 38 | il bambino smarrito |
| Ronny | 37 | il pastore scontroso |
| Basilton's Note | 1 | solo l'etichetta del nome |

Le quattro voci maggiori hanno registri molto diversi fra loro: è quella
distanza a reggere il lotto. Le cinque minori sono brevi ma **caratterizzate**:
non appiattirle in un italiano neutro solo perché hanno poche righe.

---

## Le quattro varianti di tono

Il giocatore sceglie una **personalità** a inizio partita, e ogni sua battuta
esiste in quattro versioni, riconoscibili dal suffisso della chiave:

| suffisso | personalità | come suona in italiano |
|---|---|---|
| `_HEROIC` | l'eroe tradizionale | diretto, schietto, cavalleresco. Frasi piene, niente ironia |
| `_JOKER` | il burlone | leggero, ironico, colloquiale. Battute e understatement |
| `_SCHOLAR` | lo studioso | preciso, curioso, lessico più ricco. Fa domande, cita, spiega |
| `_STOIC` | lo stoico | asciutto, controllato, poche parole. Mai enfasi esplicita |

Le quattro varianti della **stessa** battuta sono **righe adiacenti**.
**Traducile sempre insieme, mai separate fra due blocchi.**

Il punto non è renderle diverse per forza: è che **la differenza di registro
dell'inglese deve restare percepibile in italiano**. Le righe `_BASE` sono
neutre, senza variante di personalità.

---

## Il genere del giocatore

Il gioco fa **scegliere il sesso del personaggio**, e l'inglese lo aggira perché
«you» non ha genere. L'italiano no.

**Convenzione del progetto, applicata in tutti i lotti: il giocatore è al
MASCHILE.** Due regole, in quest'ordine:

1. **Dove puoi, gira la frase e non far comparire il genere.** In `dlg3` ha
   funzionato bene: *you're already worth more* → «vali già più di gran parte di
   chi passa di qui».
2. **Dove il genere è inevitabile, maschile.**

Qui pesa su **Guard** e **Lost Boy**, che riempiono il giocatore di complimenti
(«You were amazing!», «the great adventurer who…»), e su **Saqi**, che è
calorosa e diretta.

Quando è il **giocatore** a parlare a un'NPC donna — Saqi — l'accordo è
**femminile** e va tenuto.

---

## È parlato, non scritto

- **Italiano parlato e naturale.** Contrazioni, ellissi, ordine delle parole
  colloquiale dove l'inglese è colloquiale.
- **Non tradurre la sintassi inglese.** Riscrivi come lo direbbe un italiano.
- **Il "tu" fra personaggi.** Il "lei" solo se il rapporto lo richiede davvero.
- **Mantieni interiezioni e pause.** Puntini, trattini ed esitazioni fanno parte
  della recitazione.
- **Non appiattire.** Se un personaggio è sgradevole, resti sgradevole.

---

## Le voci

### Corin — il comandante degli esploratori (257 righe)

Giovane, capelli neri, intensità trattenuta. Freddo e valutativo: ti squadra
prima di parlarti. Parla per **frasi dichiarative brevi**, da ufficiale, e per
**aforismi duri**: «Luck is what people call discipline after they survive it».
Concede malvolentieri spazio ai sentimenti — le didascalie lo dicono.

**Continuità importante:** in `dlg3` Alaric lo descrive così, ed è già in gioco:

> «Ha un'ombra dura alle spalle. Non cattiveria. Non debolezza. Una ferita che
> ha imparato a portare una lama.»

Quella è la chiave della sua voce. Non ammorbidirlo e non renderlo cinico: è
disciplinato, e la durezza è una cicatrice, non una posa.

### Saqi — la quartiermastra (180 righe)

Energica, calorosa, diretta, **rumorosa**. Si muove con scopo, gesticola più del
necessario, passa dal complimento all'ordine pratico in una frase. Si occupa di
cibo, scorte e riparazioni. Tiene all'ospitalità di Earlwood come a un principio
morale: «nobody gets left outside the door».

Usa forme colloquiali («I'll pay ya back one day»): rendile con un italiano
parlato vero, non con una storpiatura.

**Continuità importante:** in `dlg3` Alaric la difende così, già in gioco:

> «Chi ha appena conosciuto Saqi forse sente solo il volume della voce. Non
> coglie il giudizio che c'è dietro. Parla schiettamente perché le parole
> morbide non sempre sono gentili.»

La schiettezza non è maleducazione: è una scelta. Tienile il calore sotto.

### Faustas — il mago in proiezione (90 righe)

Anziano, cappello storto, appare come **proiezione tremolante** — spesso rivolto
nella direzione sbagliata, e all'inizio deve aggiustare l'immagine. Quel
dettaglio comico convive con una gravità assoluta quando parla di Sylbos.

Registro **alto, cortese e preciso**. Rifiuta gli eufemismi e lo dice:
«A war. Yes. I will not insult you by using a smaller word». Frasi compiute,
niente contrazioni brusche, ritmo lento.

Porta il peso dell'esposizione narrativa — Sylbos, Dolmarok, i Maghi Ogre, il
rituale spezzato. **Tienila leggibile**: sono le righe in cui il giocatore capisce
la trama, e un italiano contorto qui costa più che altrove.

### Aelwynor — il Re della Foresta (79 righe)

Un cervo grande come una fortezza, fasciato di corteccia viva e radici, sotto
l'albero antico. **Non parla: la sua voce preme nella mente del giocatore.**
Le didascalie lo dicono esplicitamente — rendilo, non appiattirlo in un
«dice».

Chiama il giocatore **«mortale»**. Registro **il più alto del gioco**: solenne,
cosmico, senza colloquialismi. Nelle ultime battute è morente e pentito, e la
solennità si incrina: «Mi sono avvolto nella rabbia». Quel passaggio da
maestà a rimorso è il culmine narrativo del lotto — non lo si appiattisce.

**«the Mother»** è Ceres: rendilo **«la Madre»**.

### Le cinque voci minori

- **Suspicious Trader** — mercante losco di Aldoria. Passa da **gratitudine
  teatrale** («Bless you, adventurer. Truly») a **negazione** a **confessione
  amara**: «I lost everything. Goblins took my home». È il rivenditore della
  trama di Tamsin in `dlg2`. Tre registri distinti in poche righe: falli sentire.
- **Guard** — intimidita e deferente davanti al giocatore, balbetta
  («It's… it's you. Uh…»), e nasconde un mucchio di equipaggiamento dietro di sé.
  Ammirazione e imbarazzo insieme.
- **Lost Boy** — bambino entusiasta, occhi sgranati, frasi corte ed esclamative,
  adorazione per l'eroe. **Italiano da bambino vero**, non da adulto in miniatura.
- **Ronny** — il pastore: amaro, lamentoso, sprezzante. «Bah.», «Shoo off.»
  Stanco e risentito, convinto che nessuno lo consideri. Non addolcirlo.
- **Basilton's Note** — una sola riga, solo l'etichetta del nome.

---

## Regole di formato — inderogabili

1. **Una riga di output per ogni riga di input**, stesso numero, stesso ordine.
2. **La prima colonna (la chiave) non si tocca mai.**
3. **Separatore: una tabulazione.** Il testo tradotto non deve contenerne.
4. **Codifica UTF-8**, accenti veri: `à è é ì ò ù`. Scrivi il file direttamente
   con `Path.write_text(..., encoding="utf-8")` — in un lotto precedente un
   passaggio per la pipe ASCII di PowerShell 5.1 ha sostituito tutti i non-ASCII
   e il file è stato da rifare.
5. **Nessun ritorno a capo dentro una traduzione.** Una riga = un record.
6. Niente intestazioni, commenti, numerazione o blocchi di codice.

### I segnaposto `<x1/>`

Vanno **ricopiati identici**, possono **cambiare posizione** se la sintassi
italiana lo richiede, ma **non possono sparire, duplicarsi né esserne inventati
di nuovi**. Una riga che ne perde uno viene **rifiutata** e resta in inglese.

---

## Terminologia — `reference.tsv` è la legge

2.736 coppie, frutto di sette giri già approvati e installati. Quando un termine
del riferimento compare, usa **esattamente** la resa indicata.

I **nomi propri di persona degli NPC restano in inglese**: Corin, Saqi, Faustas,
Aelwynor, Ronny, e tutti quelli dei lotti precedenti.

### Termini che ricorrono in questo lotto

| Inglese | Resa |
|---|---|
| Forest King | **Re della Foresta** — è Aelwynor |
| Wildroot Father | **Padre delle Radici Selvatiche** — suo epiteto |
| the Mother | **la Madre** — è Ceres |
| Goblin King | **Re Goblin** |
| Sylbos, Dolmarok, Aldoria | invariati |
| Ogre Magi | **Maghi Ogre** |
| Old Gods | **Antichi Dei** — distinti da Old Ones → **Antichi** |
| Waygate | **Varco** |
| elder tree | **albero antico** |
| Tenderberry / tender-berries | **Tenderberry** — invariato |
| Treant / Goblin | invariati anche al plurale |
| Corrupted / Corruption | **Corrotto / Corruzione** |
| forest kin | **gente della foresta** |
| Stamina | **Vigore** |

Se un termine non è nel riferimento, traducilo sensatamente e **annotalo**.

---

## Come procedere

Blocchi di **100-150 righe**, in ordine, senza saltare nulla — ma **non spezzare
mai un gruppo di quattro varianti di tono fra due blocchi**.

Concatena i blocchi in un unico `dlg5.it.tsv` alla fine.

**Consiglio per questo lotto:** con nove personaggi il rischio non è la deriva
lungo il file, ma l'**appiattimento reciproco**. Prima di cominciare fissa in una
riga ciascuna le nove voci, e rileggile quando passi da un personaggio all'altro.

---

## Verifica prima di consegnare

1. Le righe di `dlg5.it.tsv` sono **787**, come l'input.
2. Le chiavi sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` dell'input è presente nell'output, uguale.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese.
6. I **134 quartetti** sono interi e le quattro varianti si distinguono.
7. Il file è davvero UTF-8: riapri e controlla che gli accenti siano accenti.
8. Gli accordi riferiti al **giocatore** sono al maschile, o aggirati.
9. Le nove voci restano distinguibili, comprese le cinque brevi.

---

## In fondo alla consegna, riporta

- come hai caratterizzato **le nove voci**, una o due righe ciascuna — con
  particolare cura per Aelwynor, che ha il registro più alto del gioco;
- i termini nuovi che hai deciso tu, in tabella `Inglese | Resa | Nota`;
- **le righe in cui hai dovuto forzare il genere del giocatore**, con la chiave;
- le righe su cui hai avuto dubbi di senso, **con la chiave**;
- le incoerenze notate **nel testo inglese originale**.

Le note dei lotti precedenti sono in `work/mt/dlg1.it.note.md`,
`dlg2.it.note.md` e `dlg3.it.note.md`: stesso formato, ed è stato utile così.
