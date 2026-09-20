# Round 4 — note di traduzione

Prodotte **1.979 righe** in `round4.it.tsv`, UTF-8 senza intestazione. Elaborazione in ordine in 16 blocchi: 1–126, 127–251, 252–376, 377–502, 503–627, 628–753, 754–878, 879–1004, 1005–1130, 1131–1256, 1257–1382, 1383–1507, 1508–1632, 1633–1757, 1758–1879, 1880–1979.

## Verifica

- Numero di record, chiavi e ordine identici all'input.
- Una sola tabulazione per record; nessuna traduzione vuota o su più righe.
- Segnaposto `<x…/>`, valori numerici, percentuali, segni dei bonus e formule tra parentesi conservati.
- Nessuna riga identica all'inglese; nessun residuo delle statistiche o degli stati inglesi cercati.
- Controllati i nomi di statistiche, tipi di danno, stati e abilità presenti nel riferimento. Le forme grammaticali sono adattate quando necessario; i prefissi di ramo indicati come invarianti mantengono la forma prescritta anche al plurale.
- Le descrizioni ripetute e i relativi modificatori degli incantesimi condividono la stessa traduzione. Le differenze presenti nell'inglese sono conservate.

## Scelte terminologiche e dubbi

- **Hook → Gancio**: `reference.tsv` fissa `Hook → Gancio` e `Power Hook → Gancio potente`, mentre l'esempio del brief propone «Uncino Lacerante». Applicata la priorità esplicitamente attribuita al riferimento: **Gancio Lacerante** (`SKILL_BRAWLER_ES2B10_DESC` e ricorrenze).
- **Effect Milestone Modifier → modificatore della soglia effetto**, reso coerentemente nelle descrizioni. Il riferimento non contiene la locuzione completa (`SKILL_BRAWLER_WS1U3_DESC`, `SKILL_ELF_NS1B1_DESC`, `SKILL_SHADOW_ES3U4_DESC` e relative ricorrenze).
- **Surging / Surged → Montante**: il riferimento assegna la stessa resa ai due prefissi. Conservata anche quando genera nomi uguali per modificatori diversi: Fenditura Montante, Assalto Montante e Vuoto Montante. Le descrizioni distinguono acquisizione e consumo delle cariche (`SPELL_ECHORIFT_MOD_3/4`, `SPELL_LIMITLESSONSLAUGHT_MOD_4/5`, `SPELL_TIMELESSVOID_MOD_6/7`).
- **Piercing → penetrante** nei nomi dei proiettili che attraversano i nemici; **Penetrazione** resta la statistica. Per il tipo di danno `Thrust` resta **Perforante**. Vedi `SPELL_FIREBALL_MOD_3`, `SPELL_FROSTJAVELIN_MOD_1`, `SPELL_SHADOWDAGGERS_MOD_0`.
- **Kindled → Ravvivato**, **Kindling → Innesco**, **Frostbound → Vincolo gelido**: conservate le rese vincolanti, anche nelle espressioni «cariche di Ravvivato». **Inoculating → Inoculante** resta distinto da **Inoculated → inoculato**.
- **Temporal Stacks → cariche temporali**: il testo non specifica Eco o Ondata; non è stata aggiunta una specificazione (`SKILL_ELF_NS2B1_DESC`, `…B2_DESC`, `…B3_DESC`).
- **Cryo Surge → Ondata criogenica**, **afterimage → immagine residua**, **damage-over-time → danno nel tempo**, **cooldown refund → rimborso del tempo di recupero**. Il rimborso indica una riduzione del tempo di recupero, senza attribuirgli una regola ulteriore.
- `SKILL_EARTHSHAKER_KEYSTONENW_DESC`: «up to 10» non precisa l'unità del limite. Conservato «fino a 10», senza trasformarlo in una percentuale.
- `SKILL_SHADOW_WS2U2_DESC` / `SPELL_CONTAGION_MOD_1`: «refreshes to 50% of its remaining duration» reso «si rinnova al 50% della sua durata rimanente». Non reinterpretato come durata base o aumento del 50%.
- `SKILL_ELF_NBL5R7_DESC` usa **Movement** e non **Movement Speed**: conservato **Movimento**. `SKILL_MINOTAUR_SBL2R4_DESC` parla di **concentration regeneration on hit**, reso «rigenerazione della concentrazione al colpo», senza sostituirlo con la diversa statistica «Concentrazione al colpo».

## Incoerenze e imprecisioni nell'originale

- `SKILL_ELF_NS3U7_DESC` / `SPELL_LIMITLESSONSLAUGHT_MOD_6`: il modificatore riduce **Strike Damage**, ma la descrizione base di Assalto illimitato dichiara **Thrust Damage**. Conservati rispettivamente Danno da taglio e Danno perforante.
- `SKILL_ELF_NS2B2_NAME` / `…B3_NAME`, `SKILL_HUMAN_SS2B2_NAME` / `…B3_NAME`, `SKILL_HUMAN_SS3B2_NAME` / `…B3_NAME`: i suffissi delle chiavi B2/B3 corrispondono ai livelli III/II. Numeri romani mantenuti come nel testo originale.
- `SKILL_MAGICIAN_ES2B5_NAME`, `…B7_NAME`, `…B9_NAME`: i nomi indicano un aumento della **cadenza di tiro**, mentre le rispettive descrizioni aumentano il **numero di proiettili** di 1 per punto. Distinzione conservata.
- `SKILL_BRAWLER_WS3U4_NAME` / `…DESC` e `SPELL_PULVERIZE_MOD_3`: **Remote Pulverize** descrive una riduzione del tempo di lancio, senza menzionare il lancio a distanza. Nome conservato come **Polverizza remoto**.
- `SKILL_MAGICIAN_EBL5R7_DESC`: conferisce 2 Spell Haste e 2% Attack Speed per carica, poi indica solo un limite «up to 24%». Limite lasciato nella forma originale, senza inventarne uno per Celerità magica.
- `SKILL_PHASEDUELIST_KEYSTONESE_DESC` parla di **Stun Damage**, mentre `SPELL_TEMPORALRIPPLE_DESC` usa **Stun Build-up**; mantenute le due statistiche distinte.
- Le descrizioni `SKILL_…` e `SPELL_…` di Spina cronale, Fenditura d'eco, Echi di mutilazione, Assalto illimitato, Contagio, Epidemia, Convergenza d'ombra, Pugnali d'ombra, Colpo dissolvente e Sisma del Tiranno non hanno sempre gli stessi dettagli o valori espliciti. Le versioni brevi non sono state completate copiando informazioni dalle versioni lunghe.
- `SKILL_ELF_SS3_DESC` esclude espressamente il danno degli effetti di stato dalla Pressione temporale; `SPELL_TIMELESSVOID_DESC` omette tale esclusione. Omissione conservata.
- `SPELL_ALPHAHOWLPLAYER_DESC` usa Ice/Ether, mentre diverse descrizioni di creature usano Frost senza chiarire se sia sinonimo del tipo Ice. Applicate le rese del riferimento: Ghiaccio/Etere e Gelo, senza uniformare le fonti.
- Refusi grammaticali o di punteggiatura senza effetto sulle meccaniche normalizzati in italiano: «direction.,» (`SKILL_MAGICIAN_WS2_DESC`, `SPELL_FROSTGLIDE_DESC`), «bite and the enemy» (`SPELL_BITE_DESC`), «a nearby Wolves» (`SPELL_EMPOWERWOLF_DESC`). Nell'ultimo caso è stato mantenuto il plurale Wolves: «i Lupi vicini».
- Le sigle grezze `(AT)`, `(MA:…)`, `(MH:…)`, `(ME:…)`, `(PB:…)` sono presenti nell'originale e sono state mantenute integralmente.

## Termini nuovi

L'elenco completo delle nuove rese di nomi e modificatori, incluse le composizioni con termini già fissati, è riportato di seguito ed è disponibile anche in `round4.newterms.tsv`. Non modifica `reference.tsv`.

| Inglese | Italiano |
|---|---|
| Accelerated Hemorrhage | Emorragia accelerata |
| Adaptive Swiftness | Rapidità adattiva |
| Adept of Time | Adepto del tempo |
| afterimage | immagine residua |
| Ambidextrous Precision | Precisione ambidestra |
| Ambush Volley | Salva d'imboscata |
| Anchored Convergence | Convergenza ancorata |
| Anchored Glide | Scivolata ancorata |
| Arcane Momentum | Slancio arcano |
| Arcane Skirmisher | Schermagliatore arcano |
| Auto Strike | Colpo automatico |
| Barrage of Arrows | Sbarramento di frecce |
| Berserker Blood | Sangue del berserker |
| Bestial Force | Forza bestiale |
| Blackblood Adept | Adepto del sangue nero |
| Blade Dance Extra Strikes I | Colpi extra di Danza delle lame I |
| Blade Dance Extra Strikes II | Colpi extra di Danza delle lame II |
| Blade Dance Extra Strikes III | Colpi extra di Danza delle lame III |
| Blade Discipline | Disciplina della Lama |
| Blightfire Quiver | Faretra del fuoco infetto |
| Blood Borne | Nato dal sangue |
| Blood Fury | Furia sanguinaria |
| Blood-lusted Brawler | Rissoso assetato di sangue |
| Bloodkindled Focus | Concentrazione ravvivata dal sangue |
| Bloodrush Frenzy | Frenesia del sangue impetuoso |
| Bloodscent Charge | Carica dell'odore del sangue |
| Bloodscent Hunter | Cacciatore dell'odore del sangue |
| Bludgeon and Bleed | Percuoti e dissangua |
| Blunt Cleave | Fendente Contundente |
| Blunt Strike | Colpo Contundente |
| Blurred Guard | Guardia sfocata |
| Bonebreaker | Spaccaossa |
| Boulder Slam | Schianto di masso |
| Bovine Fervour | Fervore bovino |
| Brawler's Might | Possanza del Rissoso |
| Breathless Passage | Passaggio senza respiro |
| Broadhead Shot | Tiro a punta larga |
| Bursting Contagion | Contagio esplosivo |
| Butcher's Reward | Ricompensa del macellaio |
| Cascading Inferno | Inferno a cascata |
| Centered Blizzard | Tormenta centrata |
| Chain Trap | Trappola a catena |
| Channeled Shards | Frammenti canalizzati |
| Channelled Dragon | Drago canalizzato |
| Channelled Javelin | Giavellotto canalizzato |
| Charge Stun Amplification | Amplificazione della carica contro storditi |
| Charged Fireball | Palla di fuoco carica |
| Child of Blood And Stone | Figlio del sangue e della pietra |
| Child of the Bloodhorn | Figlio del Corno Sanguinario |
| Chillbinder | Vincolagelo |
| Chilling Blizzard | Tormenta Agghiacciante |
| Chilling Dragon | Drago Agghiacciante |
| Chilling Glide | Scivolata Agghiacciante |
| Chilling Inferno | Inferno Agghiacciante |
| Chilling Javelin | Giavellotto Agghiacciante |
| Chrono Spike Stack Consumption Increase I | Aumento consumo cariche di Spina cronale I |
| Chrono Spike Stack Consumption Increase II | Aumento consumo cariche di Spina cronale II |
| Chrono Spike Stack Consumption Increase III | Aumento consumo cariche di Spina cronale III |
| Cinder Weaver | Tessitore di brace |
| Cinder-Gored Strikes | Colpi di brace cruenta |
| Cinderbank Inferno | Inferno accumulabraci |
| Cinderbank Inferno Increase I | Aumento Inferno accumulabraci I |
| Cinderbank Inferno Increase II | Aumento Inferno accumulabraci II |
| Cinderbank Inferno Increase III | Aumento Inferno accumulabraci III |
| Cinderstorm Flurry | Raffica di tempesta di brace |
| Closing Window | Opportunità in chiusura |
| Coagulating Contagion | Contagio Coagulante |
| Coagulating Dance | Danza Coagulante |
| Coagulating Outbreak | Epidemia Coagulante |
| Combusting Dragon | Drago comburente |
| Combusting Dragon Increase I | Aumento Drago comburente I |
| Combusting Dragon Increase II | Aumento Drago comburente II |
| Combusting Dragon Increase III | Aumento Drago comburente III |
| Combusting Fireball | Palla di fuoco comburente |
| Combusting Fireball Increase I | Aumento Palla di fuoco comburente I |
| Combusting Fireball Increase II | Aumento Palla di fuoco comburente II |
| Combusting Fireball Increase III | Aumento Palla di fuoco comburente III |
| Combusting Inferno | Inferno comburente |
| Combusting Inferno Increase I | Aumento Inferno comburente I |
| Combusting Inferno Increase II | Aumento Inferno comburente II |
| Combusting Inferno Increase III | Aumento Inferno comburente III |
| Concentrated Dragon | Drago concentrato |
| Concussive Quake | Sisma concussivo |
| Conditioned Exploitation | Sfruttamento degli stati |
| Contagion Radius Increase I | Aumento raggio di Contagio I |
| Contagion Radius Increase II | Aumento raggio di Contagio II |
| Contagion Radius Increase III | Aumento raggio di Contagio III |
| Continuous Wave | Onda continua |
| Converging Daggers | Pugnali convergenti |
| cooldown refund | rimborso del tempo di recupero |
| Cornu Charge Range Increase I | Aumento portata di Carica di Cornu I |
| Cornu Charge Range Increase II | Aumento portata di Carica di Cornu II |
| Cornu Charge Range Increase III | Aumento portata di Carica di Cornu III |
| Cornu Shockwave | Onda di Shock di Cornu |
| Cornu Shockwave Size Increase I | Aumento dimensioni di Onda di Shock di Cornu I |
| Cornu Shockwave Size Increase II | Aumento dimensioni di Onda di Shock di Cornu II |
| Cornu Shockwave Size Increase III | Aumento dimensioni di Onda di Shock di Cornu III |
| Corrupting Arrow | Freccia Corrompente |
| Corrupting Convergence | Convergenza Corrompente |
| Corrupting Daggers | Pugnali Corrompente |
| Corrupting Hail | Grandine Corrompente |
| Corrupting Trap | Trappola Corrompente |
| Corrupting Vanish | Dissolvenza Corrompente |
| Corrupting Wave | Onda Corrompente |
| Crimson Reaper | Mietitore cremisi |
| Crippling Backstep | Passo indietro storpiante |
| Crippling Spike | Spina storpiante |
| Crippling Spike Increase I | Aumento Spina storpiante I |
| Crippling Spike Increase II | Aumento Spina storpiante II |
| Crippling Spike Increase III | Aumento Spina storpiante III |
| Critical Chance vs below 40% Health | Probabilità di critico contro bersagli sotto il 40% di Salute |
| Critical Chance vs. below 40% Health | Probabilità di critico contro bersagli sotto il 40% di Salute |
| Critical Chance vs. Low Health | Probabilità di critico vs. salute bassa |
| Crossbow Discipline | Disciplina della Balestra |
| Cryo Surge | Ondata criogenica |
| Culling Whisper | Sussurro abbattente |
| Cycling Strikes | Colpi ciclici |
| Damage % vs below 40% Health | Danno % contro bersagli sotto il 40% di Salute |
| Damage vs. Low Health | Danno vs. salute bassa |
| damage-over-time | danno nel tempo |
| Dazing Ambush | Imboscata frastornante |
| Dazing Stampede | Carica travolgente frastornante |
| Decayed Quarry | Preda decomposta |
| Dragon's Breath Cooldown Reduction I | Riduzione recupero di Soffio del Drago I |
| Dragon's Breath Cooldown Reduction II | Riduzione recupero di Soffio del Drago II |
| Dragon's Breath Cooldown Reduction III | Riduzione recupero di Soffio del Drago III |
| Dragon's Breath Damage Increase I | Aumento danno di Soffio del Drago I |
| Dragon's Breath Damage Increase II | Aumento danno di Soffio del Drago II |
| Dragon's Breath Damage Increase III | Aumento danno di Soffio del Drago III |
| Dragon's Breath Rate Of Fire Increase I | Aumento cadenza di tiro di Soffio del Drago I |
| Dragon's Breath Rate Of Fire Increase II | Aumento cadenza di tiro di Soffio del Drago II |
| Dragon's Breath Rate Of Fire Increase III | Aumento cadenza di tiro di Soffio del Drago III |
| Dread Momentum | Slancio terrificante |
| Dreadhorn Charge | Carica del Cornispavento |
| Dreadhorn's Edge | Filo del Cornispavento |
| Duelist of the Gloam | Duellante del crepuscolo |
| Earth Shattering Might | Possanza spaccaterra |
| Earth Speaker's Voice | Voce dell'oratore della terra |
| Earthshaker’s Followthrough | Slancio dello Scuotiterra |
| Earthspeaker's Shadow | Ombra dell'oratore della terra |
| Echo Rift Refresh Increase I | Aumento rimborso recupero di Fenditura d'eco I |
| Echo Rift Refresh Increase II | Aumento rimborso recupero di Fenditura d'eco II |
| Echo Rift Refresh Increase III | Aumento rimborso recupero di Fenditura d'eco III |
| Echoed Backstep | Passo indietro Riecheggiato |
| Echoed Mutilation | Mutilazione Riecheggiata |
| Echoed Onslaught | Assalto Riecheggiato |
| Echoed Rift | Fenditura Riecheggiata |
| Echoed Void | Vuoto Riecheggiato |
| Echoes of Mutilation Hit Increase I | Aumento colpi di Echi di mutilazione I |
| Echoes of Mutilation Hit Increase II | Aumento colpi di Echi di mutilazione II |
| Echoes of Mutilation Hit Increase III | Aumento colpi di Echi di mutilazione III |
| Echoes of Mutilation Max Stacks Converted Increase I | Aumento cariche massime convertite di Echi di mutilazione I |
| Echoes of Mutilation Max Stacks Converted Increase II | Aumento cariche massime convertite di Echi di mutilazione II |
| Echoes of Mutilation Max Stacks Converted Increase III | Aumento cariche massime convertite di Echi di mutilazione III |
| Echoing Backstep | Passo indietro Echeggiante |
| Echoing Mutilation | Mutilazione Echeggiante |
| Echoing Onslaught | Assalto Echeggiante |
| Echoing Rift | Fenditura Echeggiante |
| Echoing Spike | Spina Echeggiante |
| Echoing Void | Vuoto Echeggiante |
| Effect Milestone Modifier | modificatore della soglia effetto |
| Elven Form | Forma elfica |
| Elven Martial Flow | Flusso marziale elfico |
| Emberborne Adept | Adepto nato dalla brace |
| Emberecho | Eco di brace |
| Emberhorn Frenzy | Frenesia del corno di brace |
| Enraging Boulder | Masso Infuriante |
| Enraging Boulder Increase I | Aumento Masso Infuriante I |
| Enraging Boulder Increase II | Aumento Masso Infuriante II |
| Enraging Boulder Increase III | Aumento Masso Infuriante III |
| Enraging Charge | Carica Infuriante |
| Enraging Charge Increase I | Aumento Carica Infuriante I |
| Enraging Charge Increase II | Aumento Carica Infuriante II |
| Enraging Charge Increase III | Aumento Carica Infuriante III |
| Enraging Cleave | Fendente Infuriante |
| Enraging Frenzy | Frenesia Infuriante |
| Enraging Hook | Gancio Infuriante |
| Enraging Jab | Jab Infuriante |
| Enraging Jab Increase I | Aumento Jab Infuriante I |
| Enraging Jab Increase II | Aumento Jab Infuriante II |
| Enraging Jab Increase III | Aumento Jab Infuriante III |
| Enraging Pulverize | Polverizza Infuriante |
| Enraging Quake | Sisma Infuriante |
| Enraging Retaliation | Rappresaglia Infuriante |
| Enraging Stampede | Carica travolgente Infuriante |
| Enraging Straight | Diretto Infuriante |
| Enraging Strike | Colpo Infuriante |
| Enraging Vortex | Vortice Infuriante |
| Envenomed Aim | Mira avvelenata |
| Envenoming Arrow | Freccia Avvelenante |
| Envenoming Contagion | Contagio Avvelenante |
| Envenoming Dance | Danza Avvelenante |
| Envenoming Outbreak | Epidemia Avvelenante |
| Envenoming Shards | Frammenti Avvelenante |
| Envenoming Swap | Cambio Avvelenante |
| Etherbound Whisper | Sussurro vincolato all'etere |
| Ethereal Weaver | Tessitore etereo |
| Etherstride | Falcata d'etere |
| Executing Backstep | Passo indietro esecutore |
| Executing Cleave | Fendente esecutore |
| Executing Pulverize | Polverizza esecutore |
| Expansive Mutilation | Mutilazione espansiva |
| Expansive Stampede | Carica travolgente espansiva |
| Explosive Impact | Impatto esplosivo |
| Fan Of Bolts | Ventaglio di dardi |
| Fan of Daggers | Ventaglio di pugnali |
| Fell Precision | Precisione funesta |
| Fighting Fervour | Fervore combattivo |
| Finesse of the Graced | Finezza dei favoriti |
| Fire Apprentice | Apprendista del Fuoco |
| Firepit Inferno | Inferno delle fosse ardenti |
| Firestorm | Tempesta di fuoco |
| Fist of the Stonebreakers | Pugno degli Spaccapietre |
| Flaring Dragon | Drago Fiammeggiante |
| Flaring Fireball | Palla di fuoco Fiammeggiante |
| Flaring Inferno | Inferno Fiammeggiante |
| Flashheating Fireball | Palla di fuoco Incandescente |
| Flashheating Fireball Conversion Increase I | Aumento conversione di Palla di fuoco Incandescente I |
| Flashheating Fireball Conversion Increase II | Aumento conversione di Palla di fuoco Incandescente II |
| Flashheating Fireball Conversion Increase III | Aumento conversione di Palla di fuoco Incandescente III |
| Flashheating Glide | Scivolata Incandescente |
| Flashheating Inferno | Inferno Incandescente |
| Flashheating Javelin | Giavellotto Incandescente |
| Flickering Vanish | Dissolvenza intermittente |
| Focused Contagion | Contagio Focalizzato |
| Focused Eruption | Eruzione Focalizzata |
| Focused Hook | Gancio Focalizzato |
| Focused Onslaught | Assalto Focalizzato |
| Focused Quake | Sisma Focalizzato |
| Focused Rift | Fenditura Focalizzata |
| Focused Stampede | Carica travolgente Focalizzata |
| Focused Void | Vuoto Focalizzato |
| Follow Up | Colpo successivo |
| Fracture Point | Punto di frattura |
| Fractured Rift | Fenditura fratturata |
| Fracturing Blizzard | Tormenta Fratturante |
| Fracturing Javelin | Giavellotto Fratturante |
| Fracturing Surge | Ondata Fratturante |
| Frenzy Rage Gain Increase I | Aumento Furia ottenuta con Frenesia I |
| Frenzy Rage Gain Increase II | Aumento Furia ottenuta con Frenesia II |
| Frenzy Rage Gain Increase III | Aumento Furia ottenuta con Frenesia III |
| Frost Acolyte | Accolito del Gelo |
| Frost Focused Precision | Precisione focalizzata sul gelo |
| Frost Focused Pursuer | Inseguitore focalizzato sul gelo |
| Frost Glide Extra Charge | Carica extra di Scivolata gelida |
| Frost Glide Speed Increase I | Aumento velocità di Scivolata gelida I |
| Frost Glide Speed Increase II | Aumento velocità di Scivolata gelida II |
| Frost Glide Speed Increase III | Aumento velocità di Scivolata gelida III |
| Frost Javelin Max Consume Increase I | Aumento consumo massimo di Giavellotto gelido I |
| Frost Javelin Max Consume Increase II | Aumento consumo massimo di Giavellotto gelido II |
| Frost Javelin Max Consume Increase III | Aumento consumo massimo di Giavellotto gelido III |
| Frost Javelin Stun Build-up Increase I | Aumento Accumulo di stordimento di Giavellotto gelido I |
| Frost Javelin Stun Build-up Increase II | Aumento Accumulo di stordimento di Giavellotto gelido II |
| Frost Javelin Stun Build-up Increase III | Aumento Accumulo di stordimento di Giavellotto gelido III |
| Frost Ranger's Determination | Determinazione del ranger del gelo |
| Frost-armored Hide | Pelle corazzata di gelo |
| Frostbinder | Vincolatore del gelo |
| Frostbinding Blizzard | Tormenta del vincolo gelido |
| Frostbinding Blizzard Increase I | Aumento Tormenta del vincolo gelido I |
| Frostbinding Blizzard Increase II | Aumento Tormenta del vincolo gelido II |
| Frostbinding Blizzard Increase III | Aumento Tormenta del vincolo gelido III |
| Frostbinding Glide | Scivolata del vincolo gelido |
| Frostbinding Glide Increase I | Aumento Scivolata del vincolo gelido I |
| Frostbinding Glide Increase II | Aumento Scivolata del vincolo gelido II |
| Frostbinding Glide Increase III | Aumento Scivolata del vincolo gelido III |
| Frostdraw | Tiro gelido |
| Frostfire Javelin | Giavellotto di fuoco gelido |
| Frostfire Javelin Increase I | Aumento Giavellotto di fuoco gelido I |
| Frostfire Javelin Increase II | Aumento Giavellotto di fuoco gelido II |
| Frostfire Javelin Increase III | Aumento Giavellotto di fuoco gelido III |
| Frostforged Might | Possanza Forgiata dal Gelo |
| Furious Strike Health Cost Reduction I | Riduzione costo in Salute di Colpo furioso I |
| Furious Strike Health Cost Reduction II | Riduzione costo in Salute di Colpo furioso II |
| Furious Strike Health Cost Reduction III | Riduzione costo in Salute di Colpo furioso III |
| Furnaceheart | Cuore di fornace |
| Glacial Glide | Scivolata glaciale |
| Glacial Weave | Trama glaciale |
| Gloomquick Draw | Estrazione rapida d'ombra |
| Gorespreader | Spargisangue |
| Goring Frenzy | Frenesia delle incornate |
| Grinding Stoneblood | Sangue di pietra abrasivo |
| Hail Of Arrows Damage Increase I | Aumento danno di Pioggia di Frecce I |
| Hail Of Arrows Damage Increase II | Aumento danno di Pioggia di Frecce II |
| Hail Of Arrows Damage Increase III | Aumento danno di Pioggia di Frecce III |
| Hail Of Arrows Rate Of Fire Increase I | Aumento cadenza di tiro di Pioggia di Frecce I |
| Hail Of Arrows Rate Of Fire Increase II | Aumento cadenza di tiro di Pioggia di Frecce II |
| Hail Of Arrows Rate Of Fire Increase III | Aumento cadenza di tiro di Pioggia di Frecce III |
| Hail Of Arrows Status Increase I | Aumento stato di Pioggia di Frecce I |
| Hail Of Arrows Status Increase II | Aumento stato di Pioggia di Frecce II |
| Hail Of Arrows Status Increase III | Aumento stato di Pioggia di Frecce III |
| Hand-placed Trap | Trappola piazzata a mano |
| Harvesting Charge | Carica Mietente |
| Harvesting Charge Increase I | Aumento Carica Mietente I |
| Harvesting Charge Increase II | Aumento Carica Mietente II |
| Harvesting Charge Increase III | Aumento Carica Mietente III |
| Harvesting Cleave | Fendente Mietente |
| Harvesting Convergence | Convergenza Mietente |
| Harvesting Daggers | Pugnali Mietente |
| Harvesting Dance | Danza Mietente |
| Harvesting Dance Damage Increase I | Aumento danno di Danza Mietente I |
| Harvesting Dance Damage Increase II | Aumento danno di Danza Mietente II |
| Harvesting Dance Damage Increase III | Aumento danno di Danza Mietente III |
| Harvesting Frenzy | Frenesia Mietente |
| Harvesting Mutilation | Mutilazione Mietente |
| Harvesting Onslaught | Assalto Mietente |
| Harvesting Outbreak | Epidemia Mietente |
| Harvesting Pulverize | Polverizza Mietente |
| Harvesting Quake | Sisma Mietente |
| Harvesting Stampede | Carica travolgente Mietente |
| Harvesting Straight | Diretto Mietente |
| Harvesting Strike | Colpo Mietente |
| Harvesting Swap | Cambio Mietente |
| Harvesting Trap | Trappola Mietente |
| Harvesting Vanish | Dissolvenza Mietente |
| Harvesting Vortex | Vortice Mietente |
| Harvesting Wave | Onda Mietente |
| Heat Vision Sight | Mira termica |
| Heavy Javelin | Giavellotto pesante |
| Hero's Turn | Giravolta dell'eroe |
| Hot-blooded Hunter | Cacciatore dal sangue caldo |
| Human Endurance | Resistenza umana |
| Hunter's Trap Cooldown Reduction I | Riduzione recupero di Trappola del Cacciatore I |
| Hunter's Trap Cooldown Reduction II | Riduzione recupero di Trappola del Cacciatore II |
| Hunter's Trap Cooldown Reduction III | Riduzione recupero di Trappola del Cacciatore III |
| Hunter's Trap Damage Increase I | Aumento danno di Trappola del Cacciatore I |
| Hunter's Trap Damage Increase II | Aumento danno di Trappola del Cacciatore II |
| Hunter's Trap Damage Increase III | Aumento danno di Trappola del Cacciatore III |
| Hunter's Trap Stun Build-up I | Accumulo di stordimento di Trappola del Cacciatore I |
| Hunter's Trap Stun Build-up II | Accumulo di stordimento di Trappola del Cacciatore II |
| Hunter's Trap Stun Build-up III | Accumulo di stordimento di Trappola del Cacciatore III |
| Igniting Fireball | Palla di fuoco incendiaria |
| Igniting Fireball Increase I | Aumento Palla di fuoco incendiaria I |
| Igniting Fireball Increase II | Aumento Palla di fuoco incendiaria II |
| Igniting Fireball Increase III | Aumento Palla di fuoco incendiaria III |
| Inferno | Inferno |
| Inferno Max Consume Increase I | Aumento consumo massimo di Inferno I |
| Inferno Max Consume Increase II | Aumento consumo massimo di Inferno II |
| Inferno Max Consume Increase III | Aumento consumo massimo di Inferno III |
| Inoculated Contagion | Contagio inoculato |
| Inoculated Hail | Grandine inoculata |
| Inoculated Hide | Pelle inoculata |
| Inoculated Outbreak | Epidemia inoculata |
| Inoculated Shards | Frammenti inoculati |
| Inoculated Trap | Trappola inoculata |
| Inoculated Wave | Onda inoculata |
| Inoculating Arrow | Freccia Inoculante |
| Inoculating Contagion | Contagio Inoculante |
| Inoculating Dance | Danza Inoculante |
| Inoculating Hail | Grandine Inoculante |
| Inoculating Outbreak | Epidemia Inoculante |
| Inoculating Shards | Frammenti Inoculante |
| Inoculating Wave | Onda Inoculante |
| Inverting Retaliation | Rappresaglia invertente |
| Ironhorn Soldier | Soldato dal corno di ferro |
| Kindling Fireball | Palla di fuoco d'Innesco |
| Limitless Onslaught Cost Decrease I | Riduzione costo di Assalto illimitato I |
| Limitless Onslaught Cost Decrease II | Riduzione costo di Assalto illimitato II |
| Lingering Blade | Lama persistente |
| Lingering Contagion | Contagio persistente |
| Lingering Frenzy | Frenesia persistente |
| Lingering Rupture | Lacerazione persistente |
| Lingering Shards | Frammenti persistenti |
| Long Shot | Tiro lungo |
| Lord of Cinders | Signore delle braci |
| Magma Cadence | Cadenza magmatica |
| Many-Cut Phantom | Fantasma dai Molti Tagli |
| Manyfold Convergence | Convergenza molteplice |
| Marked in Silence | Marchiato nel silenzio |
| Master of Afflictions | Maestro delle afflizioni |
| Master of Ice | Maestro del Ghiaccio |
| Master of the Temporal Domain | Maestro del dominio temporale |
| Mastery | Maestria |
| Max Inoculation | Inoculazione max |
| Max Shadow Clone Count | Numero massimo di Cloni d'ombra |
| Minotaur Blood | Sangue di Minotauro |
| Momentous Return | Ritorno impetuoso |
| Momentum Kill | Uccisione di slancio |
| Nightveil Toxins | Tossine del velo notturno |
| Numbing Convergence | Convergenza intorpidente |
| Numbing Convergence Increase I | Aumento Convergenza intorpidente I |
| Numbing Convergence Increase II | Aumento Convergenza intorpidente II |
| Numbing Convergence Increase III | Aumento Convergenza intorpidente III |
| Oil Boulder | Masso d'olio |
| Opened Vein | Vena aperta |
| Outbreak Poison Consumption Increase I | Aumento consumo Veleno di Epidemia I |
| Outbreak Poison Consumption Increase II | Aumento consumo Veleno di Epidemia II |
| Outbreak Poison Consumption Increase III | Aumento consumo Veleno di Epidemia III |
| Outbreak Radius Increase I | Aumento raggio di Epidemia I |
| Outbreak Radius Increase II | Aumento raggio di Epidemia II |
| Outbreak Radius Increase III | Aumento raggio di Epidemia III |
| Palm of the Stonebreakers | Palmo degli Spaccapietre |
| Pandemic Cloud | Nube pandemica |
| Percussive Rush | Impeto percussivo |
| Pestilent Precision | Precisione pestilenziale |
| Phantom Sharpshooter | Tiratore scelto fantasma |
| Phasing Convergence | Convergenza Sfasata |
| Piercing Daggers | Pugnali penetranti |
| Piercing Fireball | Palla di fuoco penetrante |
| Piercing Javelin | Giavellotto penetrante |
| Pinning Hail | Grandine bloccante |
| Plague Initiate | Iniziato della peste |
| Plague Shards Range Increase I | Aumento portata di Frammenti di peste I |
| Plague Shards Range Increase II | Aumento portata di Frammenti di peste II |
| Plague Shards Range Increase III | Aumento portata di Frammenti di peste III |
| Plague Shards Subsequent Hit Damage Increase I | Aumento danno colpi successivi di Frammenti di peste I |
| Plague Shards Subsequent Hit Damage Increase II | Aumento danno colpi successivi di Frammenti di peste II |
| Plague Shards Subsequent Hit Damage Increase III | Aumento danno colpi successivi di Frammenti di peste III |
| Plague Vector | Vettore della peste |
| Plaguebringer | Portatore di peste |
| Poison Tipped Ranger | Ranger dalle punte avvelenate |
| Power Hook Stun Build-up Increase I | Aumento Accumulo di stordimento di Gancio potente I |
| Power Hook Stun Build-up Increase II | Aumento Accumulo di stordimento di Gancio potente II |
| Power Hook Stun Build-up Increase III | Aumento Accumulo di stordimento di Gancio potente III |
| Precision | Precisione |
| Prizefighter | Pugile professionista |
| Projected Pulverize | Polverizza proiettato |
| Pulverize Cost Decrease I | Riduzione costo di Polverizza I |
| Pulverize Rage Capacity Increase I | Aumento capacità di Furia di Polverizza I |
| Pulverize Rage Capacity Increase II | Aumento capacità di Furia di Polverizza II |
| Pulverize Rage Efficiency I | Efficienza della Furia di Polverizza I |
| Pulverize Rage Efficiency II | Efficienza della Furia di Polverizza II |
| Punishing Straight | Diretto punitivo |
| Purging Arrow | Freccia Purgante |
| Purging Contagion | Contagio Purgante |
| Purging Hail | Grandine Purgante |
| Purging Outbreak | Epidemia Purgante |
| Purging Shards | Frammenti Purgante |
| Purging Trap | Trappola Purgante |
| Purging Vanish | Dissolvenza Purgante |
| Purging Wave | Onda Purgante |
| Pursuing Backstep | Passo indietro inseguitore |
| Pursuing Blizzard | Tormenta inseguitrice |
| Pursuing Mutilation | Mutilazione inseguitrice |
| Quaking Shade | Ombra sismica |
| Quick Jab Increase Charges I | Aumento cariche di Jab rapido I |
| Quick Jab Increase Charges II | Aumento cariche di Jab rapido II |
| Quick Jab Physical Boost Increase I | Aumento bonus fisico di Jab rapido I |
| Quick Jab Physical Boost Increase II | Aumento bonus fisico di Jab rapido II |
| Quick Jab Physical Boost Increase III | Aumento bonus fisico di Jab rapido III |
| Quick Strikes | Colpi rapidi |
| Quick Trap | Trappola rapida |
| Quickened Shadow | Ombra accelerata |
| Rage-bound Fighter | Combattente vincolato alla furia |
| Raging Boulder | Masso Furente |
| Raging Boulder Increase I | Aumento Masso Furente I |
| Raging Boulder Increase II | Aumento Masso Furente II |
| Raging Boulder Increase III | Aumento Masso Furente III |
| Raging Bull | Toro Furente |
| Raging Charge | Carica Furente |
| Raging Charge Increase I | Aumento Carica Furente I |
| Raging Charge Increase II | Aumento Carica Furente II |
| Raging Charge Increase III | Aumento Carica Furente III |
| Raging Cleave | Fendente Furente |
| Raging Frenzy | Frenesia Furente |
| Raging Hook | Gancio Furente |
| Raging Jab | Jab Furente |
| Raging Jab Increase I | Aumento Jab Furente I |
| Raging Jab Increase II | Aumento Jab Furente II |
| Raging Jab Increase III | Aumento Jab Furente III |
| Raging Pulverize | Polverizza Furente |
| Raging Quake | Sisma Furente |
| Raging Stampede | Carica travolgente Furente |
| Raging Straight | Diretto Furente |
| Raging Vortex | Vortice Furente |
| Rapid Embers | Braci rapide |
| Rapid Quake | Sisma rapido |
| Ravenous Cascade | Cascata vorace |
| Rebounding Dance | Danza rimbalzante |
| Receding Rift | Fenditura recedente |
| Recovering Strike | Colpo ristoratore |
| Refreezing Glide | Scivolata ricongelante |
| Relentless Convergence | Convergenza implacabile |
| Remote Dragon | Drago remoto |
| Remote Pulverize | Polverizza remoto |
| Remote Stampede | Carica travolgente remota |
| Rending Arrow | Freccia Lacerante |
| Rending Backstep | Passo indietro Lacerante |
| Rending Charge | Carica Lacerante |
| Rending Charge Increase I | Aumento Carica Lacerante I |
| Rending Charge Increase II | Aumento Carica Lacerante II |
| Rending Charge Increase III | Aumento Carica Lacerante III |
| Rending Cleave | Fendente Lacerante |
| Rending Convergence | Convergenza Lacerante |
| Rending Daggers | Pugnali Lacerante |
| Rending Frenzy | Frenesia Lacerante |
| Rending Hail | Grandine Lacerante |
| Rending Hook | Gancio Lacerante |
| Rending Mutilation | Mutilazione Lacerante |
| Rending Onslaught | Assalto Lacerante |
| Rending Pulverize | Polverizza Lacerante |
| Rending Quake | Sisma Lacerante |
| Rending Spike | Spina Lacerante |
| Rending Strike | Colpo Lacerante |
| Rending Swap | Cambio Lacerante |
| Rending Time | Tempo Lacerante |
| Rending Trap | Trappola Lacerante |
| Rending Vanish | Dissolvenza Lacerante |
| Rending Void | Vuoto Lacerante |
| Rending Wave | Onda Lacerante |
| Renowned Hunter | Cacciatore rinomato |
| Repeating Backstep | Passo indietro ripetuto |
| Repeating Cleave | Fendente ripetuto |
| Repeating Mutilation | Mutilazione ripetuta |
| Repeating Strike | Colpo ripetuto |
| Repeating Vortex | Vortice ripetuto |
| Resonance Seeker | Cercatore di risonanza |
| Retreating Mutilation | Mutilazione in ritirata |
| Returning Wave | Onda di ritorno |
| Reverse Quake | Sisma inverso |
| Reversing Spike | Spina invertente |
| Reversing Spike Increase I | Aumento Spina invertente I |
| Reversing Spike Increase II | Aumento Spina invertente II |
| Reversing Spike Increase III | Aumento Spina invertente III |
| Rimebound Stride | Falcata vincolata alla brina |
| Rimehold Precision | Precisione della presa di brina |
| Rot of Ages | Marciume delle ere |
| Rotseeker's Eye | Occhio del cercatore di marciume |
| Scatter Trap | Trappola dispersiva |
| Scattering Onslaught | Assalto dispersivo |
| Scorched Earth Hunter | Cacciatore della terra bruciata |
| Sealed Void | Vuoto sigillato |
| Seismic Stampede Stun Build-up Increase I | Aumento Accumulo di stordimento di Carica sismica I |
| Seismic Stampede Stun Build-up Increase II | Aumento Accumulo di stordimento di Carica sismica II |
| Seismic Stampede Stun Build-up Increase III | Aumento Accumulo di stordimento di Carica sismica III |
| Septic Duelist | Duellante settico |
| Serrated Volley | Salva seghettata |
| Severing Convergence | Convergenza recidente |
| Shade of Echoes | Ombra degli echi |
| Shadow Convergence Clone Damage Increase I | Aumento danno cloni di Convergenza d'ombra I |
| Shadow Convergence Clone Damage Increase II | Aumento danno cloni di Convergenza d'ombra II |
| Shadow Convergence Clone Damage Increase III | Aumento danno cloni di Convergenza d'ombra III |
| Shadow Daggers Cost Decrease I | Riduzione costo di Pugnali d'ombra I |
| Shadow Daggers Linger Increase I | Aumento permanenza di Pugnali d'ombra I |
| Shadow Daggers Linger Increase II | Aumento permanenza di Pugnali d'ombra II |
| Shadow Daggers Linger Increase III | Aumento permanenza di Pugnali d'ombra III |
| Shadow Initiate | Iniziato dell'Ombra |
| Shatter Dancer | Danzatore della frantumazione |
| Shattering Blizzard | Tormenta Frantumante |
| Shattering Boulder | Masso Frantumante |
| Shattering Glide | Scivolata Frantumante |
| Shattering Javelin | Giavellotto Frantumante |
| Shielding Inferno | Inferno schermante |
| Shredding Dance | Danza dilaniante |
| Sight of the Bloodbull | Vista del Toro Sanguinario |
| Silent Alacrity | Alacrità silenziosa |
| Skullbreaker's Toll | Rintocco dello Spaccacrani |
| Slicing Counter | Contrattacco Tagliente |
| Slipstream Cantor | Cantore della scia |
| Soft Inferno | Inferno attenuato |
| Splintering Javelin | Giavellotto scheggiante |
| Splintering Javelin Increase I | Aumento Giavellotto scheggiante I |
| Splintering Javelin Increase II | Aumento Giavellotto scheggiante II |
| Splintering Javelin Increase III | Aumento Giavellotto scheggiante III |
| Splintering Shards | Frammenti scheggianti |
| Splintering Strike | Colpo scheggiante |
| Splitting Javelin | Giavellotto Scindente |
| Splitting Spike | Spina Scindente |
| Splitting Wave | Onda Scindente |
| Stable Vortex | Vortice stabile |
| Steady Blizzard | Tormenta costante |
| Steady Javelin | Giavellotto costante |
| Steady Pulverize | Polverizza costante |
| Steady Straight | Diretto costante |
| Straight Lunge | Affondo diretto |
| Strider's Cadence | Cadenza del viandante |
| Striking Hook | Gancio tagliente |
| Striking Pulverize | Polverizza tagliente |
| Strong Straight Charge Speed Increase I | Aumento velocità di carica di Diretto potente I |
| Strong Straight Charge Speed Increase II | Aumento velocità di carica di Diretto potente II |
| Support Versatility | Versatilità di supporto |
| Surged Backstep | Passo indietro Montante |
| Surged Onslaught | Assalto Montante |
| Surged Rift | Fenditura Montante |
| Surged Void | Vuoto Montante |
| Surging Onslaught | Assalto Montante |
| Surging Rift | Fenditura Montante |
| Surging Spike | Spina Montante |
| Surging Void | Vuoto Montante |
| Surprising Shot | Tiro a sorpresa |
| Sweeping Dance | Danza spazzante |
| Sweeping Hook | Gancio spazzante |
| Swiftblade Stalker | Cacciatore dalla lama rapida |
| Swiftcaster | Incantatore rapido |
| Tactical Precision | Precisione tattica |
| Temporal Echo Power | Potenza dell'Eco temporale |
| Temporal Force | Forza temporale |
| Temporal Novice | Novizio temporale |
| Temporal Stacks | cariche temporali |
| Terminal Bloom | Fioritura terminale |
| Thousand Cuts | Mille tagli |
| Thrusting Dance | Danza delle stoccate |
| Time-focused Sight | Mira focalizzata sul tempo |
| Timebound Palms | Palmi vincolati al tempo |
| Timedrifted Hemorrhage | Emorragia alla deriva temporale |
| Timeless Butcher | Macellaio senza tempo |
| Timeless Capacity | Capacità senza tempo |
| Timeless Void Capacity Increase I | Aumento capacità di Vuoto eterno I |
| Timeless Void Capacity Increase II | Aumento capacità di Vuoto eterno II |
| Timeless Void Capacity Increase III | Aumento capacità di Vuoto eterno III |
| Timeless Void Retention Increase I | Aumento ritenzione di Vuoto eterno I |
| Timeless Void Retention Increase II | Aumento ritenzione di Vuoto eterno II |
| Timeless Void Retention Increase III | Aumento ritenzione di Vuoto eterno III |
| Toxin-Tipped Bolts | Dardi dalla punta tossica |
| Tremor Chant | Canto del tremore |
| Tremorbound Pestilence | Pestilenza vincolata al tremore |
| Twinned Strikes | Colpi gemelli |
| Twister | Tornado |
| Twister Duration Increase I | Aumento durata di Tornado I |
| Twister Duration Increase II | Aumento durata di Tornado II |
| Twister Duration Increase III | Aumento durata di Tornado III |
| Tyrant Quake Damage Increase IV | Aumento danno di Sisma del Tiranno IV |
| Unbroken Advance | Avanzata ininterrotta |
| Vanishing Cut | Taglio dissolvente |
| Vanishing Roll | Rotolata dissolvente |
| Vanishing Strike Backstab Damage Increase I | Aumento danno alle spalle di Colpo dissolvente I |
| Vanishing Strike Backstab Damage Increase II | Aumento danno alle spalle di Colpo dissolvente II |
| Vanishing Strike Backstab Damage Increase III | Aumento danno alle spalle di Colpo dissolvente III |
| Vanishing Strike Clone Duration Increase I | Aumento durata cloni di Colpo dissolvente I |
| Vanishing Strike Stealth Duration Increase I | Aumento durata Furtività di Colpo dissolvente I |
| Vanishing Strike Stealth Duration Increase II | Aumento durata Furtività di Colpo dissolvente II |
| Vanishing Strike Stealth Duration Increase III | Aumento durata Furtività di Colpo dissolvente III |
| Vector Transfer | Trasferimento vettoriale |
| Vehement Cleave Charge Speed Increase I | Aumento velocità di carica di Fendente veemente I |
| Vehement Cleave Charge Speed Increase II | Aumento velocità di carica di Fendente veemente II |
| Vehement Cleave Charge Speed Increase III | Aumento velocità di carica di Fendente veemente III |
| Venom Burst Trap | Trappola a scarica velenosa |
| Venom of the Labyrinth | Veleno del labirinto |
| Versatile Warrior Duration Increase I | Aumento durata di Guerriero Versatile I |
| Versatile Warrior Duration Increase II | Aumento durata di Guerriero Versatile II |
| Versatile Warrior Duration Increase III | Aumento durata di Guerriero Versatile III |
| Vortex Range Increase I | Aumento portata di Vortice I |
| Vortex Range Increase II | Aumento portata di Vortice II |
| Vortex Range Increase III | Aumento portata di Vortice III |
| Wandering Brawler | Rissoso errante |
| Wandering Ranger | Ranger errante |
| Waning Thread | Filo calante |
| Warcaller's Timing | Tempismo dell'araldo di guerra |
| Warding Void | Vuoto protettivo |
| Wave Strike Charge Speed I | Velocità di carica di Colpo d'onda I |
| Wave Strike Charge Speed II | Velocità di carica di Colpo d'onda II |
| Wave Strike Charge Speed III | Velocità di carica di Colpo d'onda III |
| Whispering Blades | Lame sussurranti |
| Wild-fire Ranger | Ranger dell'Incendio Selvaggio |
| Wildfire Dragon | Drago dell'Incendio Selvaggio |
| Wildfire Dragon Increase I | Aumento Drago dell'Incendio Selvaggio I |
| Wildfire Dragon Increase II | Aumento Drago dell'Incendio Selvaggio II |
| Wildfire Dragon Increase III | Aumento Drago dell'Incendio Selvaggio III |
| Wintercrack Smash | Schianto spaccagelo |
| Wraithhorn Ambusher | Assalitore dal corno spettrale |
| Xwin's Fist | Pugno di Xwin |
| Xwin's Might | Possanza di Xwin |
