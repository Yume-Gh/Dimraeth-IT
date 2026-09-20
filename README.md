# Dimraeth — traduzione italiana

Traduzione italiana completa e non ufficiale di **[Dimraeth](https://store.steampowered.com/app/2402680/)**
(Mudtek). Tutte e sedici le categorie di testo del gioco: **20.373 stringhe**,
interfaccia, oggetti, abilità, incantesimi, missioni, codex e i **5.202
dialoghi** degli NPC.

## Scaricala

**[→ Ultima versione](../../releases/latest)** — un solo file, niente da installare.

1. Chiudi il gioco.
2. Avvia `Dimraeth-IT-Setup.exe`.
3. La cartella del gioco viene trovata da sola tramite Steam; se non succede,
   indicala con «Sfoglia».
4. Premi **Installa la traduzione**.
5. In gioco: **Impostazioni → Lingua → «Italiano»**.

Per rimuoverla, riapri l'installer e premi **Rimuovi**: i file originali
vengono ripristinati byte per byte.

## Perché la lingua si chiama «Italiano» ma era il russo

Il gioco ha otto lingue decise quando è stato compilato (IL2CPP), e l'italiano
non è fra quelle: non si può aggiungerne una nona senza ricompilare il gioco.
La traduzione occupa quindi lo **slot russo** — l'unico con margine di byte in
tutte e sedici le categorie, perché il cirillico in UTF-8 costa due byte per
carattere — e la voce del menu viene rinominata in «Italiano».

Questo permette una sostituzione **byte-esatta** dentro
`Dimraeth_Data/sharedassets1.assets`: nessun offset del file si sposta e non
serve ricostruire le tabelle di Unity. Finché la traduzione è installata il
russo non è disponibile; le altre sette lingue restano intatte.

## Com'è stata fatta

Traduzione assistita da modelli linguistici, con controlli automatici a ogni
passaggio e rilettura umana della prosa:

- un **glossario di 481 termini** vincolanti, con varianti contestuali
  dichiarate (`Furia` la meccanica, `rabbia` il sostantivo comune);
- verifica di segnaposto, tag, numeri e capienza degli slot su ogni riga;
- **controllo di coerenza terminologica** su tutte le 20.309 righe tradotte,
  che ha scoperto errori reali nel testo già approvato — accordi di numero
  sbagliati, un sostantivo usato come aggettivo, `cooldown refund` reso
  «riduzione» invece di «rimborso»;
- i dialoghi tradotti **un personaggio alla volta**, perché ogni voce restasse
  riconoscibile.

Il gioco fa scegliere una personalità a inizio partita e ogni battuta del
protagonista esiste in quattro versioni — eroica, ironica, analitica, stoica.
La differenza fra le quattro è stata mantenuta: è il motivo per cui quella
scelta esiste.

I brief dati al traduttore e le note di consegna di ogni lotto sono in
[`work/mt/`](work/mt/): documentano le voci dei personaggi, i termini decisi,
i dubbi rimasti e le incoerenze trovate **nell'originale inglese**.

## Per chi vuole guardarci dentro

```
it/           la traduzione: 16 CSV, uno per categoria
tools/        estrazione, dizionari, cornici, validatore, patcher
installer/    sorgenti dell'installer grafico
work/mt/      brief, note di consegna, terminologia
HANDOVER.md   come funziona il progetto, in dettaglio
```

Ricostruire l'installer:

```bash
pip install pyinstaller
python installer/build.py        # -> installer/dist/Dimraeth-IT-Setup.exe
```

Applicare la traduzione senza l'installer grafico:

```bash
python tools/patch.py install --game "<cartella del gioco>" --label
python tools/validate.py --game "<cartella del gioco>"
```

### Cosa non c'è in questo repository

Lo **script originale del gioco** — `source/`, con i testi in inglese, tedesco,
spagnolo, portoghese e russo, e `glossary/names.csv` con le rese ufficiali — non
è pubblicato: è materiale di Mudtek. Si rigenera dalla propria copia del gioco:

```bash
python tools/extract.py --game "<cartella del gioco>"
```

## Segnalazioni

Se trovi un errore, una frase che suona male o un accordo sbagliato, apri una
[issue](../../issues) indicando il testo italiano e, se puoi, dove compare nel
gioco.

## Crediti

Traduzione italiana di **[Yume](https://steamcommunity.com/id/yumexx/)**.

Dimraeth è di [Mudtek](https://store.steampowered.com/app/2402680/). Questa è
una traduzione amatoriale distribuita gratuitamente, senza alcun rapporto con
gli sviluppatori o con l'editore. Il codice degli strumenti è liberamente
riutilizzabile; i testi tradotti sono un'opera derivata dal gioco.
