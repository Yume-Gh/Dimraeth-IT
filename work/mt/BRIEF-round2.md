# Incarico: traduzione in italiano di `round2.tsv`

Secondo giro della traduzione amatoriale di **Dimraeth** (Mudtek), RPG d'azione
fantasy. Il progetto è al 53%; `Quests` è già stata tradotta e approvata, e la
sua terminologia è ora vincolante.

---

## Cosa fare

Tradurre dall'inglese all'italiano la **seconda colonna** di
`work/mt/round2.tsv` — 1.237 righe, 102.979 caratteri — e salvare il risultato
come `work/mt/round2.it.tsv`.

## File

| file | ruolo |
|---|---|
| `work/mt/round2.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/round2.it.tsv` | **output da produrre** |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.592 coppie EN→IT |

---

## Regole di formato — inderogabili

1. **Una riga di output per ogni riga di input**, stesso numero, stesso ordine.
2. **La prima colonna (la chiave) non si tocca mai.** Va ricopiata identica.
3. **Separatore: una tabulazione.** Il testo tradotto non deve contenerne.
4. **Codifica UTF-8.** Accenti veri: `à è é ì ò ù`, mai `a'` o `e'`.
5. **Nessun ritorno a capo dentro una traduzione.** Una riga = un record.
6. Niente intestazioni, commenti, numerazione o blocchi di codice.

### I segnaposto `<x1/>`

Sostituiscono elementi del gioco: tag di colore, numeri inseriti a runtime,
interruzioni di riga. Vanno **ricopiati identici**, possono **cambiare
posizione** se la sintassi italiana lo richiede, ma **non possono sparire,
duplicarsi né esserne inventati di nuovi**.

Una riga che perde un segnaposto viene **rifiutata automaticamente** e resta in
inglese. Non c'è recupero silenzioso.

---

## Terminologia — `reference.tsv` è la legge

Contiene i nomi e i termini **già visibili in gioco**. Quando uno di quei termini
inglesi compare nel testo, usa **esattamente** la resa indicata.

Vincoli che è facile sbagliare:

| inglese | italiano | attenzione |
|---|---|---|
| Stamina | Vigore | non "Stamina" |
| Waygate | Varco | non "Portale" |
| beacon | segnalatore | non "faro" |
| Sanctum | Santuario | la base del giocatore |
| Shrine | Sacrario | distinto da Santuario |
| Deed | Incarico | non "Impresa" |
| Piercing | Penetrazione | come statistica |
| Strike | Taglio (danno) / Colpo (attacco) | dipende dal contesto |
| Droop, Treant, Earlwood, Wildwood | invariati | nomi propri |

I nomi propri di persona degli NPC restano in inglese.

Se un termine **non** è in `reference.tsv`, traducilo sensatamente e **annotalo**
in fondo, così viene aggiunto al glossario.

---

## Questo file mescola registri diversi: guarda il prefisso della chiave

| prefisso | contenuto | registro |
|---|---|---|
| `ITEM_`, `EQUIPMENT_`, `ATTR_`, `PASSIVE_` | descrizioni di meccaniche | **preciso e asciutto**: sono numeri e regole, non racconto. Non abbellire |
| `INSCENE_` | testo del mondo di gioco: cartelli, appunti, iscrizioni | voce in-world, mantieni il tono di chi l'ha scritto |
| `CINEMATIC_` | sottotitoli del filmato introduttivo | **narrativo e solenne**: è l'apertura del gioco, frasi brevi e cadenzate |
| `POI_`, `TUTORIAL_` | nomi di luoghi e istruzioni | nominale e diretto |

Le descrizioni di meccaniche sono la maggioranza. Lì la chiarezza vale più
dell'eleganza: se l'inglese dice quanto danno infligge una runa, l'italiano deve
dire la stessa cosa con la stessa precisione, senza aggiungere aggettivi.

---

## Registro generale

- **Dai del "tu" al giocatore.**
- **Non gonfiare.** Le stringhe finiscono in riquadri di dimensione fissa e
  l'italiano tende ad allungarsi. Resta vicino alla lunghezza dell'originale.
- **Non tradurre letteralmente** dove l'italiano ha una resa idiomatica.
- Il gioco non è solenne ovunque: ha battute e sarcasmo. Segui il tono della riga.

---

## Come procedere

Lavora a **blocchi di 100-150 righe**, in ordine, senza saltare nulla. Le chiavi
sono ordinate alfabeticamente, quindi le righe di uno stesso oggetto o di una
stessa passiva (`_NAME`, `_DESC`, `_EFFECT`) cadono vicine: **traducile
insieme**, così nome ed effetto restano coerenti fra loro.

Concatena i blocchi in un unico `round2.it.tsv` alla fine.

---

## Verifica prima di consegnare

1. Le righe di `round2.it.tsv` sono **1.237**, come l'input.
2. Le chiavi sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` dell'input è presente nell'output, uguale.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese per dimenticanza.

---

## In fondo alla consegna, riporta

- i termini nuovi che hai deciso tu (non presenti in `reference.tsv`);
- le righe su cui hai avuto dubbi di senso, con la chiave;
- le incoerenze notate **nel testo inglese originale**.

Il giro precedente ne ha trovate di reali e utili: continua così.
