# Incarico: traduzione in italiano di `Quests.tsv`

Traduzione amatoriale del gioco **Dimraeth** (Mudtek), RPG d'azione fantasy.
Il progetto è già al 47% e questa è la prima categoria di prosa narrativa.

---

## Cosa fare

Tradurre dall'inglese all'italiano la **seconda colonna** di
`work/mt/Quests.tsv` — 1.152 righe, 35.567 caratteri — e salvare il risultato
come `work/mt/Quests.it.tsv`.

## File

| file | ruolo |
|---|---|
| `work/mt/Quests.tsv` | **input**: `chiave <TAB> testo inglese` |
| `work/mt/Quests.it.tsv` | **output da produrre**: `chiave <TAB> testo italiano` |
| `work/mt/reference.tsv` | **terminologia vincolante**, 2.553 coppie EN→IT |

---

## Regole di formato — inderogabili

1. **Una riga di output per ogni riga di input**, stesso numero, stesso ordine.
2. **La prima colonna (la chiave) non si tocca mai.** Va ricopiata identica.
   Le chiavi sono identificatori del gioco, non testo.
3. **Separatore: una tabulazione.** Non virgole, non punti e virgola.
   Il testo tradotto non deve contenere tabulazioni.
4. **Codifica UTF-8.** Gli accenti italiani vanno scritti come tali: `à è é ì ò ù`,
   mai `a'` o `e'`.
5. **Nessun ritorno a capo dentro una traduzione.** Una riga = un record.
6. Non aggiungere righe, intestazioni, commenti, numerazione o blocchi di codice.

### I segnaposto `<x1/>`

36 righe contengono segnaposto tipo `<x1/>`, `<x2/>`. **Sostituiscono elementi
del gioco**: un tag di colore, un numero inserito a runtime, un'interruzione di
riga.

- Vanno **ricopiati identici** nella traduzione, stessa grafia esatta.
- Possono **cambiare posizione** se la sintassi italiana lo richiede.
- **Non possono sparire, duplicarsi, né esserne inventati di nuovi.**

Una riga che perde un segnaposto viene **rifiutata automaticamente** al reimport
e resta in inglese nel gioco. Non c'è recupero silenzioso.

---

## Terminologia — `reference.tsv` è la legge

Contiene i termini e i nomi propri **già tradotti e già visibili in gioco**:
luoghi, oggetti, creature, abilità, set di equipaggiamento, statistiche.

Quando uno di quei termini inglesi compare nel testo, **usa esattamente la resa
indicata**. Non è una preferenza stilistica: se una missione chiama un luogo
"Bosco Selvaggio" mentre la mappa dice "Wildwood", il giocatore non capisce
dove andare.

Esempi di vincoli già fissati:

| inglese | italiano | nota |
|---|---|---|
| Earlwood, Wildwood, Dimraeth | invariati | nomi propri |
| Frostward | Guardia Gelida | set di equipaggiamento |
| Droop Core | Nucleo di Droop | `Droop` resta invariato |
| Waygate | Varco | non "Portale" |
| Sanctum | Santuario | la base del giocatore |
| Shrine | Sacrario | distinto da Santuario |
| Stamina | Vigore | non "Stamina" |
| Deed | Incarico | non "Impresa" |

I nomi propri di persona degli NPC (Alaric, Tamsin, Corin, Myrll…) **restano in
inglese**: è la scelta dei localizzatori ufficiali del gioco.

Se un termine **non** è in `reference.tsv`, traducilo sensatamente e **annotalo**
in fondo alla risposta, così viene aggiunto al glossario.

---

## Registro e stile

- **Dai del "tu" al giocatore.** Il resto dell'interfaccia è già così.
- **Non gonfiare.** L'italiano tende ad allungarsi: le stringhe finiscono in
  riquadri di dimensione fissa. Resta vicino alla lunghezza dell'originale,
  taglia le ridondanze invece di aggiungerne.
- **Registro fantasy sobrio**, non aulico e non gergale. Il gioco non è solenne:
  ha anche battute e sarcasmo. Segui il tono della riga che hai davanti.
- **I nomi delle missioni sono nominali e brevi**, come titoli: "Assalto al
  mulino", non "Devi assaltare il mulino".
- Alcune righe sono **voce in-world** — avvisi affissi a una bacheca, scritti da
  un personaggio. Mantieni quella voce, non appiattirla in italiano burocratico.
- **Non tradurre letteralmente** se l'italiano ha una resa idiomatica: "Hail of
  Arrows" è "Pioggia di frecce", non "Grandine di frecce".

---

## Come procedere

Il file è grosso: lavoralo **a blocchi di 100-150 righe**, in ordine, senza
saltare nulla. Le chiavi sono ordinate alfabeticamente, quindi le righe di una
stessa missione (`_NAME`, `_DESC`, obiettivi) sono vicine: **traducile insieme**,
così nome e descrizione restano coerenti fra loro.

Concatena i blocchi in un unico `Quests.it.tsv` alla fine.

---

## Verifica prima di consegnare

1. Il numero di righe di `Quests.it.tsv` è **uguale** a quello di `Quests.tsv`.
2. Le chiavi della prima colonna sono **identiche e nello stesso ordine**.
3. Ogni `<x…/>` presente nell'input è presente anche nell'output, **uguale**.
4. Nessuna tabulazione dentro il testo tradotto.
5. Nessuna riga rimasta in inglese per dimenticanza.

Non serve che tu esegua altro: al reimport ci sono controlli automatici su
segnaposto, tag e terminologia, e ti verranno segnalate le righe rifiutate.

---

## In fondo alla consegna, riporta

- i termini nuovi che hai dovuto decidere tu (non presenti in `reference.tsv`);
- le righe su cui hai avuto dubbi di senso, con la chiave;
- eventuali incoerenze che hai notato **nel testo inglese originale** (il gioco
  ne ha già alcune documentate: stringhe rimaste in portoghese, segnaposto di
  sviluppo).
