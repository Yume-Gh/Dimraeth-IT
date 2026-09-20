# Incarico: traduzione in italiano di `round4.tsv` — Skills e Spells

Quarto giro della traduzione amatoriale di **Dimraeth** (Mudtek), RPG d'azione
fantasy. Il progetto è al 64,8%: dodici categorie su sedici sono complete, e i
tre giri precedenti sono stati approvati. La loro terminologia è vincolante.

---

## Cosa fare

Tradurre dall'inglese all'italiano la **seconda colonna** di
`work/mt/round4.tsv` — 1.979 righe, 168.879 caratteri — e salvare il risultato
come `work/mt/round4.it.tsv`.

## File

| file | ruolo |
|---|---|
| `work/mt/round4.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/round4.it.tsv` | **output da produrre** |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.650 coppie EN→IT |

---

## Regole di formato — inderogabili

1. **Una riga di output per ogni riga di input**, stesso numero, stesso ordine.
2. **La prima colonna (la chiave) non si tocca mai.**
3. **Separatore: una tabulazione.** Il testo tradotto non deve contenerne.
4. **Codifica UTF-8.** Accenti veri: `à è é ì ò ù`, mai `a'` o `e'`.
5. **Nessun ritorno a capo dentro una traduzione.** Una riga = un record.
6. Niente intestazioni, commenti, numerazione o blocchi di codice.

### I segnaposto `<x1/>`

Vanno **ricopiati identici**, possono **cambiare posizione** se la sintassi
italiana lo richiede, ma **non possono sparire, duplicarsi né esserne inventati
di nuovi**. Una riga che ne perde uno viene **rifiutata** e resta in inglese.

---

## Terminologia — `reference.tsv` è la legge

2.650 coppie, comprese tutte quelle dei tre giri precedenti. Quando un termine
inglese del riferimento compare nel testo, usa **esattamente** la resa indicata.

Questo lotto è **il più esposto agli errori terminologici di tutto il progetto**:
sono descrizioni di meccaniche, fitte di nomi di statistiche, stati alterati,
tipi di danno e abilità, tutti già fissati. Un termine reso a orecchio qui
contraddice quello che il giocatore legge nella scheda del personaggio.

Vincoli che è facile sbagliare:

| inglese | italiano | attenzione |
|---|---|---|
| Stamina | Vigore | non "Stamina" |
| Concentration | Concentrazione | |
| Piercing | Penetrazione | come statistica |
| Strike | Taglio (tipo di danno) / Colpo (nome d'attacco) | dipende dal contesto |
| Thrust | Perforante (danno) / Stoccata (attacco) | dipende dal contesto |
| Blunt | Contundente | |
| Chill | Gelo · Chilled | Assiderato |
| Burning | Ustione · bersagli | ustionati |
| Bleeding | Sanguinamento · bersagli | sanguinanti |
| Blizzard | Tormenta | non "Bufera" |
| Rupture | lacerazione | legato allo stato Lacerato |
| Stun Build-up | Accumulo di stordimento | |
| Waygate | Varco · beacon | segnalatore |

I prefissi dei rami dell'albero delle abilità sono aggettivi **invarianti**, e
in italiano seguono il nome: `Rending Hook` → "Uncino Lacerante", non
"Lacerante Uncino". Valgono per tutti: Lacerante, Infuriante, Furente,
Echeggiante, Agghiacciante, Corrompente, Purgante, Mietente, Montante,
Coagulante, Inoculante, Incandescente, Avvelenante, Fiammeggiante, Frantumante,
Fratturante.

Se un termine **non** è in `reference.tsv`, traducilo sensatamente e **annotalo**
in fondo.

---

## Cos'è questo file

| suffisso chiave | righe | contenuto |
|---|---:|---|
| `_DESC` | 1.145 | descrizioni di abilità e incantesimi |
| `_NAME` | 521 | nomi di nodi, abilità, incantesimi |
| `_0`, `_1`, `_2`… | ~310 | righe di effetto, spesso con valori numerici |

Righe brevi: **85 caratteri di media**, massimo 464.

**Registro: preciso e asciutto.** Sono regole di gioco, non racconto. Se
l'inglese dice quanto danno infligge un'abilità e a quali condizioni, l'italiano
deve dire la stessa cosa con la stessa precisione. Non aggiungere aggettivi, non
rendere più "epico" il testo, non variare la formulazione per evitare
ripetizioni: qui la ripetizione è una caratteristica, non un difetto — descrive
meccaniche che si assomigliano davvero.

Numeri, percentuali, durate in secondi e condizioni vanno riprodotti esatti.

---

## Registro generale

- **Dai del "tu" al giocatore.**
- **Non gonfiare.** Le stringhe finiscono in riquadri di dimensione fissa e
  l'italiano tende ad allungarsi.
- I nomi di abilità sono **nominali e brevi**, come titoli.

---

## Come procedere

Lavora a **blocchi di 100-150 righe**, in ordine, senza saltare nulla. Le chiavi
sono ordinate alfabeticamente: `_NAME` e `_DESC` della stessa abilità cadono
vicine, **traducile insieme** così restano coerenti.

Concatena i blocchi in un unico `round4.it.tsv` alla fine.

---

## Verifica prima di consegnare

1. Le righe di `round4.it.tsv` sono **1.979**, come l'input.
2. Le chiavi sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` dell'input è presente nell'output, uguale.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese per dimenticanza.
6. **Numeri e percentuali identici all'originale.**

---

## In fondo alla consegna, riporta

- i termini nuovi che hai deciso tu;
- le righe su cui hai avuto dubbi di senso, con la chiave;
- le incoerenze notate **nel testo inglese originale**.

Nei giri precedenti questa sezione ha fatto emergere problemi reali: continua così.
