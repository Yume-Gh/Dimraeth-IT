# Incarico: traduzione in italiano di `round3.tsv` — il Codex

Terzo giro della traduzione amatoriale di **Dimraeth** (Mudtek), RPG d'azione
fantasy. Il progetto è al 59% e undici categorie su sedici sono già complete.
`Quests` e il lotto precedente sono stati approvati, e la loro terminologia è
ora vincolante.

---

## Cosa fare

Tradurre dall'inglese all'italiano la **seconda colonna** di
`work/mt/round3.tsv` — 1.173 righe, 122.456 caratteri — e salvare il risultato
come `work/mt/round3.it.tsv`.

## File

| file | ruolo |
|---|---|
| `work/mt/round3.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/round3.it.tsv` | **output da produrre** |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.631 coppie EN→IT |

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

2.631 coppie, comprese tutte quelle dei due giri precedenti. Quando un termine
inglese del riferimento compare nel testo, usa **esattamente** la resa indicata.

Vincoli che è facile sbagliare:

| inglese | italiano | attenzione |
|---|---|---|
| Stamina | Vigore | non "Stamina" |
| Waygate | Varco | non "Portale" |
| beacon | segnalatore | non "faro" |
| Sanctum | Santuario | la base del giocatore |
| Shrine | Sacrario | distinto da Santuario |
| Piercing | Penetrazione | come statistica |
| Strike | Taglio (danno) / Colpo (attacco) | dipende dal contesto |
| Droop, Treant, Earlwood, Wildwood | invariati | nomi propri |

I nomi propri di persona degli NPC restano in inglese.

Se un termine **non** è in `reference.tsv`, traducilo sensatamente e **annotalo**
in fondo. I due giri precedenti hanno prodotto così un'ottantina di voci nuove,
tutte poi entrate nel glossario.

---

## Cos'è questo file

Il Codex è il **compendio in gioco**: non è solo ambientazione. Guardando le
chiavi, le voci più numerose riguardano gli **incantesimi**
(`CODEX_SPELLFROSTJAVELIN_*`, `CODEX_SPELLINFERNO_*`…), poi creature, luoghi,
oggetti e costruzioni.

Le righe vanno da poche parole a **979 caratteri**: ci sono etichette secche e
voci lunghe di approfondimento.

| tipo di voce | registro |
|---|---|
| voci su incantesimi e meccaniche | **preciso e asciutto**: numeri, condizioni, tipi di danno. Non abbellire |
| voci su creature, luoghi, storia | **narrativo**: è il libro che il giocatore consulta per capire il mondo. Prosa scorrevole, non didascalica |
| titoli e categorie (`_NAME`, `CAT_`) | nominali e brevi |

Il Codex è il testo che **definisce il lessico dell'ambientazione**: nomi di
popoli, ere, istituzioni, fenomeni. Le tue scelte qui vincoleranno i dialoghi
degli NPC, che sono il blocco successivo e il più grande del progetto. Sceglile
con quell'uso in mente, e annotale tutte.

---

## Registro generale

- **Dai del "tu" al giocatore** dove il testo si rivolge a lui.
- **Non gonfiare.** Le stringhe finiscono in riquadri di dimensione fissa.
- **Non tradurre letteralmente** dove l'italiano ha una resa idiomatica.
- Registro fantasy sobrio: né aulico né gergale.

---

## Come procedere

Lavora a **blocchi di 100-150 righe**, in ordine, senza saltare nulla. Le chiavi
sono ordinate alfabeticamente: le righe di una stessa voce (`_NAME`, `_DESC`,
`_BLURB`) cadono vicine, **traducile insieme** così restano coerenti.

Concatena i blocchi in un unico `round3.it.tsv` alla fine.

---

## Verifica prima di consegnare

1. Le righe di `round3.it.tsv` sono **1.173**, come l'input.
2. Le chiavi sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` dell'input è presente nell'output, uguale.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese per dimenticanza.

---

## In fondo alla consegna, riporta

- i termini nuovi che hai deciso tu, **soprattutto quelli di ambientazione**:
  popoli, luoghi, ere, istituzioni, titoli. Serviranno ai dialoghi;
- le righe su cui hai avuto dubbi di senso, con la chiave;
- le incoerenze notate **nel testo inglese originale**.
