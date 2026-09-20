# Dimraeth — traduzione italiana: stato e prosecuzione

Documento di passaggio fra sessioni. Aggiornato al 2026-09-20.

**La traduzione è COMPLETA**: 16 categorie su 16, installata e verificata.

**Cartella del progetto:** `E:\Dimraeth-IT`
**Cartella del gioco:** `E:\Games\Steam\steamapps\common\Dimraeth`

Aprire `E:\Dimraeth-IT` come cartella di lavoro: i percorsi relativi di questo
documento e dei brief si risolvono da lì.

---

## Cos'è questo progetto

Traduzione amatoriale di **Dimraeth** (Mudtek, Unity 6 / IL2CPP). Il gioco ha un
sistema di localizzazione a CSV con 16 categorie e 8 lingue, ma **l'italiano non
esiste nell'enum compilato**, quindi la traduzione **occupa lo slot russo**:
è l'unico con margine di byte in tutte le categorie, il che permette una
sostituzione **byte-esatta** dentro `sharedassets1.assets` senza ricostruire le
tabelle di Unity.

In gioco: Impostazioni → Lingua → **Italiano** (l'etichetta è stata rinominata
nel metadata).

---

## Stato attuale

| | |
|---|---:|
| copertura del traducibile | **100%** (20.373 / 20.376) |
| categorie complete | **16 su 16** |
| installato nel gioco | sì, verificato 16/16 |
| validatore | **pulito**: 0 errori, 0 avvisi, 0 incoerenze |

Tutte complete, `NPCDialogues` compresa: 5.202 righe su 5.202.

Le uniche tre righe non tradotte sono **etichette di `Attributes`** —
`% HP`, `{0} HP`, `{0}% HP` — che **sono corrette così**: «HP» è la convenzione
già usata in 23 punti del tradotto, compreso `{0}% Danno vs. <40% HP`, e il
tedesco le lascia identiche all'inglese. Resteranno sempre fra le «pendenti» di
`mt.py status`: è un artefatto del conteggio, non lavoro mancante.

---

## PROSSIMA AZIONE: provare il gioco

Non resta lavoro di traduzione. Quello che resta lo trova solo chi gioca:
accordi di genere a schermo, nomi montati a runtime, registri che stonano.

I cinque lotti hanno lasciato una **lista di punti da verificare in gioco**,
raccolti nelle note di consegna (`work/mt/dlg*.it.note.md`) con la chiave di
ogni riga. I più rilevanti:

| punto | dove |
|---|---|
| pronomi della carovana di Manga, «my smith and my steel» | dlg1 |
| il racconto di JJ: esche e ami non tornano nell'originale | dlg2 |
| `memorial wall` → «muro dei caduti» | dlg2 |
| «heartwood oak» ricondotto a *Quercia del Cuore*; il Re «bound» | dlg3 |
| `Lumen Realm` contro `Numen realm`: incoerenza dell'inglese | dlg4 |
| `Faustas's Rest` contro `Faustas's Tower`, e `AREA_FAUSTASREST` = «Earlwood» | dlg4 |
| i tre oggetti di riassegnazione citati da Rahaner, assenti dal catalogo | dlg4 |

### Se si riprende in mano il testo

```bash
python tools/validate.py --game "E:/Games/Steam/steamapps/common/Dimraeth"
python tools/apply_it.py                  # copertura per categoria
python tools/patch.py install --game "<gioco>" --label
```

Il glossario è a **481 termini**, 457 verificabili automaticamente. Dopo ogni modifica: `mt.py reference`,
`validate.py`, poi installare e confrontare i byte con `it/`.

---

## Sicurezza del lavoro e aggiornamenti del gioco

### Su GitHub

**https://github.com/Yume-Gh/Dimraeth-IT** — pubblico, con le release
scaricabili. L'exe della `v1.0` è stato riscaricato dal link pubblico e il suo
sha256 combacia con quello costruito in locale.

Il repository **non contiene lo script originale del gioco**: `.gitignore`
esclude `source/` e `glossary/`, e tratta `work/` per **allowlist** — quello che
non è esplicitamente ammesso resta fuori, così una dimenticanza non finisce
online. Ammessi solo i `.md`, la terminologia e i `.it.tsv`. Prima di
pubblicare, il contenuto del commit è stato passato al setaccio cercando
frasi inglesi di gioco: le uniche trovate sono coppie brevi d'interfaccia
dentro `reference.tsv`, cioè il glossario.

`.gitattributes` imposta `* -text`: **nessuna conversione di fine riga**, in
nessuna direzione. I CSV vengono spliciati byte per byte nel file del gioco, e
una normalizzazione li romperebbe silenziosamente.

Per una versione nuova:

```bash
python installer/build.py
gh release create v1.1 installer/release/*/Dimraeth-IT-Setup.exe --notes-file <note>
```

### Dov'è il lavoro, e cosa lo minaccia

Il progetto vive in `E:\Dimraeth-IT`, **fuori dalla cartella del gioco**: un
aggiornamento Steam non lo tocca. Sono 20,8 MB, 240 file.

**Copie di sicurezza:** GitHub (tutto tranne `source/` e `glossary/`) e
`D:- Games\Dimraeth-IT-backup6-09-20\` (tutto, compresi gli originali)
verificata con SHA256 file per file, zero differenze. È su un **disco fisico
diverso** (D: è il SATA da 4 TB, E: un NVMe), quindi regge anche a un guasto
del disco di lavoro. Rifarla dopo ogni sessione di modifiche, con la data nuova.

**Non protetto:** il backup dell'originale del gioco,
`sharedassets1.assets.dimraeth-it.bak` (283 MB), sta **dentro la cartella
Steam**. «Verifica integrità dei file» lo può rendere inutile. Serve solo per
tornare al gioco non tradotto senza riscaricarlo: se conta, va spostato fuori.

### Cosa succede se il gioco viene aggiornato

La traduzione in gioco **si perde** — Steam riscrive `sharedassets1.assets` —
ma il lavoro no. Il punto delicato è la *reinstallazione*.

`patch.py` ora **si rifiuta di lavorare su un backup obsoleto**. Prima non lo
faceva, ed era il rischio peggiore del progetto: `resolve_slots` considerava il
backup la fonte di verità sempre, quindi dopo un aggiornamento avrebbe applicato
**offset vecchi a un file nuovo**, corrompendolo invece di tradurlo. Lo splice
conserva la lunghezza, quindi nemmeno l'`assert` se ne sarebbe accorto. E
`status` diceva «PATCHATO» anche a traduzione sparita.

La guardia è `backup_stale()` e verifica due cose, entrambe a buon mercato:

1. il backup ha la **stessa dimensione** del file attuale — la sostituzione è
   byte-esatta, quindi un backup buono non può differire in lunghezza;
2. gli offset dei suoi slot cadono ancora su **payload che iniziano col BOM**,
   come fanno sia i CSV russi sia quelli italiani.

Se una delle due salta, `install` e `uninstall` si fermano e stampano la
procedura. `uninstall` è il caso più distruttivo — ricopierebbe il gioco vecchio
sopra quello nuovo — e richiede `--force` per insistere.

Nel manifest ora c'è anche `base_sha`: lo sha del file **prima** della patch,
non solo del risultato.

### Procedura dopo un aggiornamento

```bash
python tools/patch.py status --game "<gioco>"     # dira' se il backup e' obsoleto
# se lo e':
#   1. spostare altrove il .bak vecchio, senza cancellarlo
#   2. python tools/extract.py --game "<gioco>"
#   3. confrontare i nuovi source/English con la copia in D:\...\Dimraeth-IT-backup
```

Se il testo inglese è **invariato**, basta reinstallare: il nuovo backup viene
creato da solo e gli slot si risolvono sul file nuovo. Se è **cambiato**,
`validate.py` elenca le chiavi mancanti o in più, e quelle nuove vanno tradotte
prima di installare.

---

## L'installer distribuibile

`installer/` produce **un solo .exe da 9,2 MB** che chi lo riceve avvia e basta:
niente Python, niente cartelle da copiare a mano.

| file | a cosa serve |
|---|---|
| `installer/core.py` | motore: trova il gioco, installa, rimuove, riferisce lo stato |
| `installer/gui.py` | la finestra (tkinter); `--selftest` scrive una diagnosi |
| `installer/build.py` | raccoglie i CSV e lancia PyInstaller |
| `installer/LEGGIMI.txt` | istruzioni per chi installa |

```bash
pip install pyinstaller          # una volta sola
python installer/build.py        # -> installer/dist/Dimraeth-IT-Setup.exe
```

`build.py` copia in `installer/payload/` i sedici CSV da `it/` e `unityfile.py`
da `tools/`: **il pacchetto si costruisce sempre dallo stato attuale di `it/`**,
non da una copia che invecchia. Rilanciarlo dopo ogni modifica al testo.

### Cosa fa l'installer che patch.py non faceva

- **Trova il gioco da solo**: legge `SteamPath` dal registro, poi
  `libraryfolders.vdf` per tutte le librerie, poi `appmanifest_2402680.acf`
  (l'appid di Dimraeth) per l'`installdir`. Se fallisce, c'è «Sfoglia», che
  perdona anche chi indica `Dimraeth_Data` o la cartella di Steam.
- **Parla a chi non legge i traceback**: ogni errore è una frase che dice cosa
  fare — gioco aperto, permessi mancanti, versione incompatibile.
- **Non si fida di una build diversa**: se i CSV italiani non entrano negli
  slot, si ferma e dice che serve una versione nuova della traduzione, invece
  di scrivere comunque.
- Porta la stessa guardia sul backup obsoleto di `patch.py`.
- **Rifiuta una cartella che non sia quella del gioco**: `is_game_folder()`
  pretende `Dimraeth_Data/sharedassets1.assets` e `global-metadata.dat`. Il
  pulsante resta disabilitato e `install()` si ferma prima di toccare nulla.
- **Si chiude da solo** dopo l'OK della conferma di installazione.
- Titolo con l'**icona Steam** che apre la pagina del gioco, piede con
  «traduzione di **Yume**» che apre il profilo. Entrambi in `core.py`
  (`AUTORE`, `AUTORE_URL`, `GIOCO_URL`): si cambiano in un punto solo.
  L'icona e' disegnata su un Canvas, non impacchettata: niente PNG da
  portarsi dietro e resta nitida a qualsiasi scalatura dello schermo.

**Bug corretto dopo la prima prova a schermo:** la conferma diceva
«Impostazioni -> Lingua -> Русский» invece di «Italiano». La causa: `install()`
considerava riuscita la rinomina solo se trovava **una** occorrenza di
«Русский» da sostituire, ma a una seconda installazione l'etichetta era gia'
«Italiano», quindi zero occorrenze, quindi fallimento. Ora vale anche il caso
«gia' rinominata», che e' comunque il risultato voluto.

### Verifica fatta sul pacchetto

Provato l'exe **definitivo**, dalla cartella di distribuzione:

- `--selftest` dentro l'exe: 16/16 CSV raggiungibili via `_MEIPASS`, gioco
  rilevato via Steam, stato corretto;
- **rimozione**: il gioco è tornato a `sha 46344449d8a8adcd`, identico
  all'originale, backup cancellato, etichetta di nuovo «Русский»;
- **installazione da zero**, senza backup preesistente — il percorso di un
  utente nuovo: 16/16 categorie byte-esatte, dimensione invariata, backup
  creato, etichetta «Italiano».

Il pacchetto pronto è `installer/release/Dimraeth-Traduzione-Italiana-1.0.zip`
(8,5 MB): l'exe più `LEGGIMI.txt`.

---

## Com'è andata: i cinque lotti di dialogo

| lotto | personaggi | righe | esito |
|---|---|---:|---|
| dlg1 | Myrll, Manga | 1.248 | 0 rifiutate, 17 segnalazioni tutte legittime |
| dlg2 | Tamsin, Basilton | 914 | 0 rifiutate, 1 segnalazione |
| dlg3 | Eldorian, Alaric | 954 | 0 rifiutate, 2 segnalazioni |
| dlg4 | Heimen, Befr, Rahaner | 1.279 | 0 rifiutate, 2 segnalazioni |
| dlg5 | Corin, Saqi, Faustas, Aelwynor e 5 minori | 787 | 0 rifiutate, 4 segnalazioni |

**Nessuna riga è mai stata rifiutata dall'import**: 5.182 righe, segnaposto
tutti intatti. Le segnalazioni di glossario sono state in tutto 26, e **tutte**
erano varianti contestuali legittime o incoerenze vere del testo già installato.

### Cosa ha funzionato, e vale per lavori simili

**Misurare prima di credere.** L'arretrato dei 651 termini era dato per
prioritario: misurato, zero di essi ricorreva nei dialoghi. La regola sul genere
del giocatore è nata da un controllo, non da un'intuizione. Le voci dei
personaggi sono state descritte nei brief a partire da campioni estratti dal
TSV, non da impressioni.

**Il brief cresce a ogni lotto.** `dlg1` non aveva la regola sul genere;
`dlg3` sì, perché nel frattempo era emersa. `dlg4` ha aggiunto la misura di
quanto pesino le battute del giocatore. `dlg5` ha citato la caratterizzazione
già installata, così le voci nascevano coerenti.

**Le segnalazioni di glossario sono uno strumento di scoperta**, non un
controllo da zittire: hanno trovato «Pugnali Lacerante», «Taglio Contundente»,
`cooldown refund` reso «riduzione», l'oscillazione `Colpo`/`Taglio` e il
femminile mancante di `dwarf` per Saqi.

---

## 64 righe corrette in Codex, Skills, Spells, Passives e Quests

L'esame dell'arretrato (sotto) ha fatto emergere difetti reali nel testo già
installato. Tutti corretti e reinstallati; il validatore ora è pulito.

| difetto | righe | natura |
|---|---:|---|
| `Piercing X` → «X Penetrazione» | 6 | sostantivo usato come aggettivo: «Palla di fuoco Penetrazione» |
| `Decay Piercing` → «Penetrazione Decadimento» | 4 | manca la preposizione del modello «Penetrazione da decadimento» |
| `Blunt Strike` → «Taglio Contundente» | 2 | contraddizione: taglio e contundente si escludono |
| `cooldown refund` → «riduzione» | 4 | è un **rimborso**; Skills e Spells dicevano già «rimborso» |
| accordo di numero | 14 | «Pugnali Lacerante», «Frammenti Purgante» |
| `X Strike` fra «Colpo» e «Taglio» | 32 | oscillava dentro la stessa famiglia |
| `Clear the Forest Near the Road` | 2 | decisione chiusa: «Ripulisci la foresta lungo la strada» |

Sul penultimo: il glossario **documentava già** la regola giusta — «tipo di danno
Taglio; nei nomi di attacco Colpo» — ma il testo non la seguiva. Ora «Colpo» è
usato in tutti i nomi d'attacco derivati da `Strike`, e «Taglio» resta al tipo
di danno (`Danno da taglio`, `Armatura da taglio`, `Penetrazione da taglio`).

**Non toccare** «Taglio Tossico» e «Taglio Settico»: vengono da *Toxic **Slice***
e *Septic **Aftercut***, dove «taglio» è corretto. La rinomina ha usato una
guardia sull'inglese proprio per questo.

---

## L'ARRETRATO DEI 651 TERMINI: non serve ai dialoghi — misurato

`work/mt/round4.newterms.tsv` contiene 651 coppie EN→IT mai promosse a
glossario. Questo documento le dava per prioritarie «perché vincolino i dialoghi
rimanenti». **Il presupposto è falso, ed è stato verificato:**

- 650 delle 651 sono termini nuovi (1 era già a glossario), senza duplicati,
  senza conflitti di resa e senza rese troppo corte: la lista è pulita;
- ma compaiono **tutte** in `Skills` (650), `Codex` (287) e `Spells` (287),
  categorie **già complete al 100%**;
- **zero** di esse compare in `NPCDialogues`, né nelle righe tradotte né in
  quelle ancora da tradurre.

Promuoverle non vincolerebbe nessuna riga di `dlg2`–`dlg5`. Aggiungerebbe 650
voci all'indice del validatore, che segnalerebbe 69 righe di testo già
approvato: di queste solo ~30 erano difetti veri — quelli della tabella sopra,
già corretti — e le altre erano sinonimi equivalenti («Danza Dilaniatrice» vs
«Danza dilaniante») che non vale la pena inseguire.

**Quindi: non promuoverle.** Il valore che avevano è già stato estratto. Il file
resta come documentazione della terminologia di combattimento, utile se un
giorno si rimetterà mano a `Skills`/`Codex`/`Spells`.

Resta vero il principio generale: **se si aggiungono termini, farlo prima dei
lotti di dialogo, non dopo.**

---

## Come sono stati divisi i dialoghi — e perché

I dialoghi sono stati divisi **per personaggio**, non per dimensione: le chiavi
sono `NPC_<NOME>_..._<TONO>` e ordinandole alfabeticamente le quattro varianti
di tono di ogni battuta finiscono adiacenti. Dividere per personaggio le tiene
insieme e mantiene coerente la voce — che è la ragione per cui i cinque lotti
hanno prodotto voci riconoscibili invece di un impasto uniforme.

Comandi usati, se servisse riesportare:

```bash
python tools/mt.py export --cat NPCDialogues --name dlg2 --match "^NPC_(TAMSIN|BASILTON)_"
python tools/mt.py export --cat NPCDialogues --name dlg3 --match "^NPC_(ELDORIAN|ALARIC)_"
python tools/mt.py export --cat NPCDialogues --name dlg4 --match "^NPC_(HEIMENTHALDRIK|BEFR|RAHANER)_"
python tools/mt.py export --cat NPCDialogues --name dlg5 --match "^NPC_(CORIN|SAQI|AELWYNOR|FAUSTAS|SUSPICIOUSTRADER|GUARD|RONNY|LOSTBOY|BASILTONSNOTE)_"
python tools/mt.py reference     # rigenerare DOPO ogni promozione di termini
```

I brief sono in `work/mt/BRIEF-dlg*.md`. `BRIEF-dlg4.md` e `BRIEF-dlg5.md` sono
i più completi e restano il modello per un lavoro simile: oltre a voci, genere
del giocatore, terminologia e UTF-8, contengono la **misura** di quanto pesino
le battute del giocatore nel lotto, la soluzione per il **dialetto di Heimen**,
e le **citazioni della caratterizzazione già installata**.

---

## Il flusso di lavoro, per ogni lotto

1. `python tools/mt.py export --cat ... --name ... --match ...`
2. `python tools/mt.py reference` — rigenera la terminologia vincolante
3. Passare a un traduttore (finora GPT che lavora nel repo) il brief + il TSV
4. **Verificare la struttura prima di importare**: righe, chiavi in ordine,
   segnaposto `<x…/>` intatti, niente tabulazioni nel testo, numeri identici
5. `python tools/mt.py import --cat <nome> --file <...>.it.tsv`
6. `python tools/validate.py --game "<gioco>"` ed esaminare le segnalazioni
7. Promuovere i termini nuovi delle note in `tools/it_terms.py`
8. Installare (gioco chiuso): `python tools/patch.py install --game "<gioco>" --label`
9. Verificare l'installazione confrontando i byte con `it/`

---

## Decisioni chiuse

- **`Clear the Forest Near the Road`** → «Ripulisci la foresta lungo la strada».
  Recupera il riferimento alla foresta che «Bonifica lungo la strada» perdeva.
- **`Praesidiism`** → «Presidiismo», la dottrina di Manga. Era `REVIEW` con la
  nota «'Praesidiismo' se si adatta agli altri nomi di dottrina»: la condizione
  era vuota, perché è l'unico `-ism` del gioco. Ora è `OK` a glossario.
- **`Strike` nei nomi d'attacco** → «Colpo», come il glossario già prescriveva.
- **`Treant`** → invariato anche al plurale («i Treant»), come Goblin. Era
  `REVIEW` con «Ent» come alternativa; «Treant» era già in uso in 141 righe.
- **`Dwarf` / `Dwarves`** → «Nano» / «Nani». La resa era già in `Attributes`
  (selezione della razza) ma non a glossario; `dlg4` usa il plurale.
- **Dieci righe erano contate come tradotte ma erano ancora in inglese.**
  `pending()` esclude le righe che dizionari e cornici *saprebbero* rendere
  (`mt.py:51-54`), e il contatore di copertura le dà per fatte — ma il
  generatore scrive solo le righe di cornice, quindi quelle risolte per
  dizionario non finivano mai in `it/`. Erano 7 nomi di statistica del Codex
  («Healing Power», «Minion Health», «Recovery Up»…) e **3 nomi di NPC visibili
  a schermo**: `Guard`, `Lost Boy`, `Suspicious Trader`. Ora scritte.
  **Il controllo da rifare a fine progetto**: per ogni riga con `IT == EN`,
  provare `apply_it.lookup` e poi le cornici; se producono qualcosa di diverso
  dall'inglese, è una riga persa.
- **Il dialetto di Heimenthaldrik** (dlg4): l'inglese lo marca foneticamente
  — `walkin'`, `aye`, `ye`, `o'` — in **92 delle sue 115 battute**. In italiano
  non esiste un marcatore fonetico che non sia **regionale**, e un nano che
  parla una parlata reale lo colloca su una mappa vera. La marca va spostata
  dalla fonetica alla **sintassi e al lessico**: infiniti troncati («parlar
  chiaro»), paratassi, sentenze, lessico di cava e bottega. Il brief di dlg4 lo
  spiega per esteso. Vale per chiunque altro parli così nei lotti futuri.

Nessuna decisione aperta.

---

## Trappole già incontrate — non ripeterle

**Il compositore usa sempre la PRIMA variante.** `"Strike": ("Taglio|colpo")`
porta la nota «nei nomi di attacco Colpo», ma `frames.term_it` prende `alts[0]`
e ha prodotto «Taglio Lacerante» per 32 righe. La nota nel glossario non vincola
il generatore: se il senso dipende dal contesto, o si mette il termine lungo
(`Rending Strike`) fra le voci esplicite, o si corregge a mano dopo.

**Le desinenze in -ante/-ente sono invarianti per GENERE, non per NUMERO.**
Le cornici accordano il genere con `{g0}` ma non il numero, e con una testa
plurale escono «Pugnali Lacerante» e «Frammenti Purgante». Quattordici righe.
Cercarle con: testa plurale + aggettivo che finisce in `-ante/-ente/-ato/-ito`.

**`it/*.csv` è uno store sicuro.** Il generatore per modelli salta le righe già
tradotte (`if r[1] != v: continue`), quindi le correzioni scritte a mano in
`it/` non vengono sovrascritte da `apply_it.py`.

**La console di Windows è cp1252** e va in `UnicodeEncodeError` quando
`patch.py status` stampa l'etichetta cirillica. Non è un guasto della patch:
basta `PYTHONIOENCODING=utf-8`.

**`\n` nei CSV sono DUE caratteri** (barra + n), non un ritorno a capo.
Scriverli come newline reale fa fallire le corrispondenze **in silenzio**: è
costato sette cornici che non agganciavano mai.

**Gli heredoc di bash collassano i backslash.** Le patch ai file Python fatte con
`python - <<'EOF'` hanno rotto stringhe più volte. Usare gli strumenti di
edit esatti, oppure costruire i backslash con `chr(92)`.

**Validare la sintassi PRIMA di scrivere**, non dopo: `ast.parse(s)` e poi
`open(...).write(s)`. L'ordine inverso ha lasciato un file rotto su disco.

**Le corrispondenze a cavallo di confine.** In "Wave Strike Damage Increase" la
lettura giusta è `[Wave Strike][Damage Increase]`, ma `Strike Damage` è più
lungo e aggancia in mezzo. Il controllo usa un'unica alternanza leftmost-longest
per allinearsi al generatore. Quando succede lo stesso con un termine nuovo, la
soluzione è **registrare il termine più lungo** (es. `Earlwood Wall Banner`).

**Le varianti troppo corte spariscono in silenzio.** Una resa sotto le 4 lettere
produce zero radici e viene scartata. `glossary_check.DROPPED` ora le registra:
`Echo`→"Eco" e `King`→"Re" non sono mai stati verificati.

**I sostituti globali sono pericolosi.** Un regex su "recupero" ha rovinato due
righe corrette: *in recupero* è uno stato, *tempo di recupero* è una durata.
Stampare sempre prima/dopo e rileggere.

**Il filtro `translatable()` scarta i valori fatti di soli segnaposto**, e così
`EQUIP_NAME_FORMAT` (`{0} {1} {2}`) era invisibile — proprio la stringa che
riordina il nome degli oggetti. Le chiavi in `it_bykey.BY_KEY` forzano il filtro.
Audit fatto: non ce ne sono altre.

**Il gioco non blocca sempre il file.** Unity rilascia `sharedassets1.assets`
dopo il caricamento, quindi la scrittura può riuscire a gioco aperto — ma i dati
in memoria restano vecchi. `patch.py` ricontrolla prima dello scambio.

---

## Gli strumenti

| file | a cosa serve |
|---|---|
| `unityfile.py` | trova e sostituisce i TextAsset in `sharedassets1.assets`, byte-esatto con padding |
| `patch.py` | install / uninstall / status, backup automatico, guardia sul gioco in esecuzione **e sul backup obsoleto** |
| `extract.py` | estrae i CSV dal gioco (sola lettura) |
| `validate.py` | **il controllo principale**: chiavi, placeholder, tag TMP, glossario, capienza slot |
| `glossary_check.py` | confronto per radice, varianti con `\|`, tokenizzazione leftmost-longest |
| `it_terms.py` | **il glossario**: ~290 termini con varianti contestuali |
| `apply_it.py` | applica dizionari, cornici e risolutore composizionale; mostra la copertura |
| `frames.py` + `morph.py` | traduzione per modelli con accordo grammaticale italiano |
| `mt.py` + `mt_mask.py` | adattatore per traduttori esterni: export/import, mascheratura segnaposto |
| `it_*.py` | i dizionari: UI, oggetti, luoghi, equipaggiamento, incantesimi, sistema |

Comandi utili:

```bash
python tools/apply_it.py                  # copertura per categoria
python tools/mt.py status                 # cosa resta da tradurre
python tools/validate.py --game "<gioco>" # il controllo completo
```

---

## Principi da mantenere

**Niente esce dalla macchina senza che l'utente lo chieda.** `mt.py` esporta su
file; l'invio a servizi esterni è una sua decisione.

**Installare a ogni fine lotto, non alla fine.** Gli errori veri — accordi di
genere, nomi assemblati a runtime, registri sbagliati — li trova il gioco, non il
validatore. Il caso più istruttivo: l'utente ha notato dallo schermo che i nomi
delle rune erano montati nell'ordine inglese, e la causa era una stringa di
formato che nessun controllo poteva segnalare.

**Sulla prosa il validatore non basta.** Verifica struttura e terminologia; che
una frase suoni italiana e che i quattro toni si distinguano lo vede solo chi
legge.
