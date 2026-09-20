# Round 3 — note di traduzione

Tradotte **1.173 righe** in `round3.it.tsv`. Blocchi salvati in ordine: 1–136, 137–266, 267–396, 397–528, 529–656, 657–786, 787–917, 918–1045, 1046–1173. Nessuna riga omessa. `reference.tsv` non è stato modificato.

## Lessico dell'ambientazione

Questo lotto contiene soprattutto meccaniche e varianti di incantesimi; le voci narrative autonome sono brevi descrizioni di materiali. Non introduce nuove ere, istituzioni o popoli da nominare. Restano vincolanti le rese già nel riferimento: Aldoria, Mirkea, Earlwood, Wildwood, Droop, Treant e Thaumablossom invariati; Heart Oak → Quercia del Cuore; ley lines → linee di forza; Hoard King → Re del Tesoro. I nomi personali, incluso Basilton, restano invariati.

Le etichette di persone, creature e oggetti non presenti come coppie complete nel riferimento sono comprese nella tabella dei titoli sotto. In particolare: Basilton's Note → Biglietto di Basilton; Lost Boy → Bambino smarrito; Suspicious Trader → Mercante sospetto. Non sono nuovi nomi propri.

## Termini tecnici presenti solo nelle descrizioni

| Inglese | Italiano | Nota / chiave di esempio |
|---|---|---|
| Blizzard | Tormenta | `CODEX_SPELLBLIZZARD_DESC`; base comune alle varianti |
| Inferno | Inferno | `CODEX_SPELLINFERNO_DESC`; nome mantenuto, già italiano |
| Decay Channel | Canalizzazione del Decadimento | `CODEX_TIMEDDECAYCHANNEL_DESC` |
| Temporal Pressure | Pressione temporale | `CODEX_SPELLTIMELESSVOID_DESC` |
| Effect Milestone Modifier | modificatore della tappa Effetto | `CODEX_SPELLFURIOUSSTRIKE_SPLINTERINGSTRIKE_DESC`; «Effetto» interpretato come nome della tappa di progressione |
| Raging Pulverize | Polverizza Furente | Richiamo d'incompatibilità in `CODEX_SPELLPULVERIZE_ENRAGINGPULVERISE_DESC` |
| Enraging Pulverize | Polverizza Infuriante | Richiamo d'incompatibilità in `CODEX_SPELLPULVERIZE_RAGINGPULVERISE_DESC` |
| Raging Vortex | Vortice Furente | Alias presente in `CODEX_SPELLVORTEX_*`; distinto testualmente da Vortex → Vortice |
| Minion Health | Salute dei servitori | `CODEX_STATMINIONS_DESC` |
| Minion Critical Chance | Probabilità di critico dei servitori | `CODEX_STATMINIONS_DESC` |
| Rejuvenation | Ringiovanimento | Variante ortografica di Rejuvination, già nel riferimento |
| Multi-strike | Colpo multiplo | Variante ortografica di Multistrike, già nel riferimento |
| Rupture | lacerazione | Esplosione dello stato Ruptured → Lacerato, vincolante; `CODEX_SPELLSHADOWCONVERGENCE_HARVESTINGCONVERGENCE_DESC` |

Maiuscole adattate alla funzione di titolo o nome di effetto; plurali e accordi adattati alla sintassi. I modificatori nuovi sono documentati come nomi completi, per riutilizzarli nei dialoghi e nei richiami d'incompatibilità.

## Dubbi di senso e incoerenze dell'originale

- `CODEX_RECIPE*` e `CODEX_BUILDEARLWOODBED_DESC` / `CODEX_BUILDTENT_DESC` / `CODEX_BUILDLARGETENT_DESC`: ricorrono le vecchie risorse **Hunger e Thirst**, mentre `CODEX_STATNOURISHMENT_DESC` descrive **Nourishment** come risorsa unificata. Mantenute Fame, Sete e Nutrimento distinti. «Restores Hunger/Thirst» reso come «Ripristina la barra della Fame/Sete» per chiarire che si riempie la risorsa.
- `CODEX_RECIPENATURESWARDSTEAK_DESC`: «cooled with Treant wood» è probabilmente un refuso per «cooked». Reso «cotta con Legno di Treant», coerente con la ricetta e con il testo già approvato del giro precedente. Corretto anche il refuso grammaticale «Grant's».
- `CODEX_RECIPETHICKBLOODBROTH_DESC`: la prosa promette resistenza al sanguinamento, ma gli effetti indicano **4 Rage** e cariche ricaricabili riposando. Entrambe le informazioni sono conservate; non sono state ricostruite le statistiche dalla versione precedente.
- `CODEX_RECIPETHAUMABLOSSOMTEA_DESC`: rispetto al testo precedente manca il bonus alla Concentrazione al colpo. L'omissione del Codex è conservata.
- `CODEX_RECIPELIGHTBANDAGES*_DESC` e `CODEX_RECIPEPOISONCURE*_DESC`: la frase sulla ricarica delle cariche riposando compare due volte. Conservate entrambe le occorrenze e tutti i segnaposto.
- `CODEX_RECIPELINEN_DESC`: il suffisso letterale «None» è conservato come «Nessuno».
- `CODEX_MONSTERCORRUPTEDHEART1_NAME`: conservato il suffisso **1** in «Cuore corrotto1», verosimilmente un residuo tecnico. Analogamente, conservati **T2** e la struttura dei nomi dei Goblin potenziati.
- `CODEX_RECIPESPELLBOOKCONFLAGURATION_DESC`: «Conflaguration» normalizzato alla resa vincolante **Conflagrazione**. Refusi ordinari come «Presst» e «Vilage» corretti nella prosa italiana.
- `CODEX_CAT_EFFECTS_BLURB`: parla di un indicatore nascosto che deve riempirsi, mentre le singole voci descrivono accumuli applicati direttamente. Informazioni mantenute senza reinterpretare il sistema.
- `CODEX_CAT_OFFENCE_BLURB` e `CODEX_STATCRITICAL_CRITDAMAGE_DESC`: la categoria dice che i critici moltiplicano per Critical Damage; la statistica descrive invece un bonus base di +50%. Formula e definizione sono conservate come nell'originale.
- `CODEX_SPELLBLIZZARD_*`, `CODEX_SPELLFIREBALL_FLASHHEATINGFIREBALL_DESC`, `CODEX_SPELLFROSTGLIDE_FLASHHEATINGGLIDE_DESC`, `CODEX_SPELLFROSTJAVELIN_FLASHHEATINGJAVELIN_DESC`, `CODEX_SPELLINFERNO_*`: l'originale usa talvolta **Chilled** come nome di accumuli, altrove **Chill**. Conservati rispettivamente **Assiderato** e **Gelo**; non equiparati di nascosto.
- `CODEX_SPELLBLADEDANCE_SHREDDINGSTRIKE_DESC`: richiama «Multi-strike» anziché Blade Dance; mantenuto **Colpo multiplo**. Lo stesso criterio vale per gli alias Cleave/Fendente e Raging Vortex/Vortice Furente.
- `CODEX_SPELLCONTAGION_VECTORTRANSFER_DESC`: «refreshes to 50% of its remaining duration» interpretato letteralmente come durata reimpostata al 50% di quella residua, non della durata totale.
- `CODEX_SPELLDRAGONSBREATH_CHANNELEDDRAGON_DESC` / `CODEX_SPELLDRAGONSBREATH_CHANNELLEDDRAGON_DESC`: quasi duplicati; solo il secondo riduce i danni del 25%. Dati conservati separatamente; entrambi i titoli resi Drago Canalizzato.
- `CODEX_SPELLFROSTJAVELIN_CHANNELEDJAVELIN_DESC` / `CODEX_SPELLFROSTJAVELIN_CHANNELLEDJAVELIN_DESC`: indicano rispettivamente **20%** e **25%** dei danni. Conservata la differenza. «50% fewer maximum Chill stacks» reso come riduzione del 50% del numero massimo di accumuli consumabili per colpo; la base non esplicita quel massimo.
- `CODEX_SPELLPULVERIZE_ENRAGINGPULVERISE_DESC` / `CODEX_SPELLPULVERIZE_ENRAGINGPULVERIZE_DESC`: **1** contro **2** accumuli di Furia per nemico. Le varianti RAGINGPULVERISE/RAGINGPULVERIZE differiscono anche per bonus ai danni e riduzione dell'Armatura. Nessuna fusione.
- `CODEX_SPELLHUNTERSTRAP_*`, `CODEX_SPELLWAVESTRIKE_*`, `CODEX_SPELLSTRONGSTRAIGHT_*`: alcune varianti parlano di consumi di Veleno, Sanguinamento o Furia «normali» che le voci base non descrivono. Mantenute le condizioni delle varianti senza aggiungerle alle basi.
- `CODEX_SPELLSHADOWCONVERGENCE_HARVESTINGCONVERGENCE_DESC`: il bonus del 10% per Clone d'ombra «fino al 40%» è mantenuto; il testo non chiarisce se il limite riguardi il bonus o il coefficiente totale dell'esplosione.
- `CODEX_SPELLTIMELESSVOID_DESC`: «Arcane», «Ether» e «Magic» convivono; mantenuti «arcano», «etere» e «magico» nei rispettivi contesti. **Pressure** resta in inglese solo dentro la formula letterale `(M:1.5 + Pressure x 0.05)`; nella prosa è Pressione temporale.
- Le sigle delle formule, compresi **ME/MA**, **MF**, **PT**, **PX** e **AT**, sono state conservate letteralmente. L'originale usa ME sia per elettricità sia per etere e alterna ME/MA per l'etere. Non è compito della traduzione correggerle.
- `CODEX_STATRESISTANCE_DESC`, `CODEX_STATPENETRATION_DESC` e voci specifiche: la resistenza viene descritta sia come statistica generale più resistenza elementale sia come valore separato per elemento; la penetrazione viene descritta sia come sottrazione alla riduzione del danno sia come difesa ignorata. Le formulazioni originali sono conservate senza imporre un modello diverso.

## Titoli ed etichette nuovi rispetto a reference.tsv

Tabella delle coppie complete assenti dal riferimento (anche quando composte da parole già approvate). Non contiene nuove traduzioni dei termini già vincolanti.

| Inglese | Italiano | Chiave |
|---|---|---|
| Heartwood Door | Porta in Durame | `CODEX_BUILDHEARTWOODDOOR_NAME` |
| Building | Costruzioni | `CODEX_CAT_BUILDING_NAME` |
| Damage Types | Tipi di danno | `CODEX_CAT_DAMAGETYPES_NAME` |
| Stacking Effects | Effetti ad accumulo | `CODEX_CAT_EFFECTS_NAME` |
| Empowered Monsters | Mostri potenziati | `CODEX_CAT_EMPOWERMENTS_NAME` |
| Monsters | Mostri | `CODEX_CAT_MONSTERS_NAME` |
| People | Persone | `CODEX_CAT_NPCS_NAME` |
| Effects | Effetti | `CODEX_CAT_TIMEDEFFECTS_NAME` |
| Arcane Shielded | Scudo Arcano | `CODEX_EMPOWERMENTARCANESHIELDED_NAME` |
| Blighted | Infetto | `CODEX_EMPOWERMENTBLIGHTED_NAME` |
| Flamecaller | Evocafiamme | `CODEX_EMPOWERMENTFLAMECALLER_NAME` |
| Mortar | Mortaio | `CODEX_EMPOWERMENTMORTAR_NAME` |
| Spiteful | Rancoroso | `CODEX_EMPOWERMENTSPITEFUL_NAME` |
| Storm Aura | Aura Tempestosa | `CODEX_EMPOWERMENTSTORMAURA_NAME` |
| Unyielding | Inflessibile | `CODEX_EMPOWERMENTUNYIELDING_NAME` |
| Venomous | Velenoso | `CODEX_EMPOWERMENTVENOMOUS_NAME` |
| Cast Time | Tempo di lancio | `CODEX_FACT_CASTTIME` |
| Crafted at | Creato presso | `CODEX_FACT_CRAFTEDAT` |
| Damage Type | Tipo di danno | `CODEX_FACT_DAMAGETYPE` |
| Danger | Pericolo | `CODEX_FACT_DANGER` |
| Element | Elemento | `CODEX_FACT_ELEMENT` |
| Health Cost | Costo in Salute | `CODEX_FACT_HEALTHCOST` |
| Kind | Genere | `CODEX_FACT_KIND` |
| Max Stacks | Accumuli massimi | `CODEX_FACT_MAXSTACKS` |
| Parent | Voce principale | `CODEX_FACT_PARENT` |
| Range | Portata | `CODEX_FACT_RANGE` |
| Stack | Accumulo | `CODEX_FACT_STACK` |
| Storage Slots | Slot di deposito | `CODEX_FACT_STORAGESLOTS` |
| Tags | Etichette | `CODEX_FACT_TAGS` |
| Targets | Bersagli | `CODEX_FACT_TARGETS` |
| Zones | Zone | `CODEX_FACT_ZONES` |
| Brush Flax | Lino Selvatico | `CODEX_ITEMBRUSHFLAX_NAME` |
| Definition  › | Definizione  › | `CODEX_META_DEFINITION` |
| <x1/> sub-entries  › | <x1/> sottovoci  › | `CODEX_META_SUBENTRIES` |
| <x1/> sub-entry  › | <x1/> sottovoce  › | `CODEX_META_SUBENTRY` |
| Corrupted Heart1 | Cuore corrotto1 | `CODEX_MONSTERCORRUPTEDHEART1_NAME` |
| Goblin Flaskrat T2 Empowered | Goblin Flaskrat T2 potenziato | `CODEX_MONSTERGOBLINFLASKRATT2EMPOWERED_NAME` |
| Goblin Ripper T2 Empowered | Goblin Squartatore T2 potenziato | `CODEX_MONSTERGOBLINRIPPERT2EMPOWERED_NAME` |
| Basilton's Note | Biglietto di Basilton | `CODEX_NPCBASILTONSNOTE_NAME` |
| Guard | Guardia | `CODEX_NPCGUARD_NAME` |
| Lost Boy | Bambino smarrito | `CODEX_NPCLOSTBOY_NAME` |
| Suspicious Trader | Mercante sospetto | `CODEX_NPCSUSPICIOUSTRADER_NAME` |
| Spellbook Poison Mist | Libro degli incantesimi: Nebbia velenosa | `CODEX_RECIPESPELLBOOKPOISONSPORES_NAME` |
| Broadhead Shot | Tiro a Punta Larga | `CODEX_SPELLAIMEDSHOT_BROADHEADSHOT_NAME` |
| Corrupting Arrow | Freccia Corrompente | `CODEX_SPELLAIMEDSHOT_CORRUPTINGARROW_NAME` |
| Envenoming Arrow | Freccia Avvelenante | `CODEX_SPELLAIMEDSHOT_ENVENOMINGARROW_NAME` |
| Inoculating Arrow | Freccia Inoculante | `CODEX_SPELLAIMEDSHOT_INOCULATINGARROW_NAME` |
| Long Shot | Tiro Lungo | `CODEX_SPELLAIMEDSHOT_LONGSHOT_NAME` |
| Poison Laced Arrow | Freccia Intrisa di Veleno | `CODEX_SPELLAIMEDSHOT_POISONLACEDARROW_NAME` |
| Purging Arrow | Freccia Purgante | `CODEX_SPELLAIMEDSHOT_PURGINGARROW_NAME` |
| Rending Arrow | Freccia Lacerante | `CODEX_SPELLAIMEDSHOT_RENDINGARROW_NAME` |
| Serrated Arrow | Freccia Seghettata | `CODEX_SPELLAIMEDSHOT_SERRATEDARROW_NAME` |
| Surprising Shot | Tiro a Sorpresa | `CODEX_SPELLAIMEDSHOT_SURPRISINGSHOT_NAME` |
| Crippling Backstep | Passo indietro Storpiante | `CODEX_SPELLBACKSTEPSTRIKE_CRIPPLINGBACKSTEP_NAME` |
| Executing Backstep | Passo indietro Esecutore | `CODEX_SPELLBACKSTEPSTRIKE_EXECUTINGBACKSTEP_NAME` |
| Executing Strike | Colpo Esecutore | `CODEX_SPELLBACKSTEPSTRIKE_EXECUTINGSTRIKE_NAME` |
| Pursuing Backstep | Passo indietro Inseguitore | `CODEX_SPELLBACKSTEPSTRIKE_PURSUINGBACKSTEP_NAME` |
| Pursuing Strike | Colpo Inseguitore | `CODEX_SPELLBACKSTEPSTRIKE_PURSUINGSTRIKE_NAME` |
| Extra Strikes | Colpi Extra | `CODEX_SPELLBLADEDANCE_EXTRASTRIKES_NAME` |
| Rebounding Dance | Danza Rimbalzante | `CODEX_SPELLBLADEDANCE_REBOUNDINGDANCE_NAME` |
| Shredding Dance | Danza Dilaniatrice | `CODEX_SPELLBLADEDANCE_SHREDDINGDANCE_NAME` |
| Shredding Strike | Colpo Dilaniatore | `CODEX_SPELLBLADEDANCE_SHREDDINGSTRIKE_NAME` |
| Sweeping Dance | Danza a Spazzata | `CODEX_SPELLBLADEDANCE_SWEEPINGDANCE_NAME` |
| Thrusting Dance | Danza Perforante | `CODEX_SPELLBLADEDANCE_THRUSTINGDANCE_NAME` |
| Centered Blizzard | Tormenta Centrata | `CODEX_SPELLBLIZZARD_CENTEREDBLIZZARD_NAME` |
| Frostbinding Blizzard | Tormenta del Vincolo Gelido | `CODEX_SPELLBLIZZARD_FROSTBINDINGBLIZZARD_NAME` |
| Frost Bite Blizzard | Tormenta Mordigelo | `CODEX_SPELLBLIZZARD_FROSTBITEBLIZZARD_NAME` |
| Icy Fortification | Fortificazione Gelida | `CODEX_SPELLBLIZZARD_ICYFORTIFICATION_NAME` |
| Pursuing Blizzard | Tormenta Inseguitrice | `CODEX_SPELLBLIZZARD_PURSUINGBLIZZARD_NAME` |
| Soft Blizzard | Tormenta Lieve | `CODEX_SPELLBLIZZARD_SOFTBLIZZARD_NAME` |
| Steady Blizzard | Tormenta Costante | `CODEX_SPELLBLIZZARD_STEADYBLIZZARD_NAME` |
| Boulder Slam | Schianto del Masso | `CODEX_SPELLBOULDERTOSS_BOULDERSLAM_NAME` |
| Enraging Boulder | Masso Infuriante | `CODEX_SPELLBOULDERTOSS_ENRAGINGBOULDER_NAME` |
| Oil Boulder | Masso d'Olio | `CODEX_SPELLBOULDERTOSS_OILBOULDER_NAME` |
| Raging Boulder | Masso Furente | `CODEX_SPELLBOULDERTOSS_RAGINGBOULDER_NAME` |
| Sharp Shrapnel | Schegge Affilate | `CODEX_SPELLBOULDERTOSS_SHARPSHRAPNEL_NAME` |
| Shattering Boulder | Masso Frantumante | `CODEX_SPELLBOULDERTOSS_SHATTERINGBOULDER_NAME` |
| Crippling Spike | Spina Storpiante | `CODEX_SPELLCHRONOSPIKE_CRIPPLINGSPIKE_NAME` |
| Reversing Spike | Spina Invertente | `CODEX_SPELLCHRONOSPIKE_REVERSINGSPIKE_NAME` |
| Splitting Spike | Spina Scindente | `CODEX_SPELLCHRONOSPIKE_SPLITTINGSPIKE_NAME` |
| Bursting Contagion | Contagio Esplosivo | `CODEX_SPELLCONTAGION_BURSTINGCONTAGION_NAME` |
| Lingering Contagion | Contagio Persistente | `CODEX_SPELLCONTAGION_LINGERINGCONTAGION_NAME` |
| Pandemic Cloud | Nube Pandemica | `CODEX_SPELLCONTAGION_PANDEMICCLOUD_NAME` |
| Vector Transfer | Trasferimento del Vettore | `CODEX_SPELLCONTAGION_VECTORTRANSFER_NAME` |
| Bloodscent Charge | Carica all'Odore di Sangue | `CODEX_SPELLCORNUCHARGE_BLOODSCENTCHARGE_NAME` |
| Charge Stun Amplification | Carica Potenziata contro Storditi | `CODEX_SPELLCORNUCHARGE_CHARGESTUNAMPLIFICATION_NAME` |
| Cornu Shockwave | Onda di Shock di Cornu | `CODEX_SPELLCORNUCHARGE_CORNUSHOCKWAVE_NAME` |
| Enraging Charge | Carica Infuriante | `CODEX_SPELLCORNUCHARGE_ENRAGINGCHARGE_NAME` |
| Harvesting Charge | Carica Mietente | `CODEX_SPELLCORNUCHARGE_HARVESTINGCHARGE_NAME` |
| Raging Charge | Carica Furente | `CODEX_SPELLCORNUCHARGE_RAGINGCHARGE_NAME` |
| Rending Charge | Carica Lacerante | `CODEX_SPELLCORNUCHARGE_RENDINGCHARGE_NAME` |
| Stun Amp | Bonus contro Storditi | `CODEX_SPELLCORNUCHARGE_STUNAMP_NAME` |
| Channeled Dragon | Drago Canalizzato | `CODEX_SPELLDRAGONSBREATH_CHANNELEDDRAGON_NAME` |
| Channelled Dragon | Drago Canalizzato | `CODEX_SPELLDRAGONSBREATH_CHANNELLEDDRAGON_NAME` |
| Combusting Dragon | Drago Combustivo | `CODEX_SPELLDRAGONSBREATH_COMBUSTINGDRAGON_NAME` |
| Concentrated Dragon | Drago Concentrato | `CODEX_SPELLDRAGONSBREATH_CONCENTRATEDDRAGON_NAME` |
| Living Dragon | Drago Vivente | `CODEX_SPELLDRAGONSBREATH_LIVINGDRAGON_NAME` |
| Remote Dragon | Drago Remoto | `CODEX_SPELLDRAGONSBREATH_REMOTEDRAGON_NAME` |
| Wildfire Dragon | Drago dell'Incendio Selvaggio | `CODEX_SPELLDRAGONSBREATH_WILDFIREDRAGON_NAME` |
| Expansive Mutilation | Mutilazione Estesa | `CODEX_SPELLECHOESOFMUTILATION_EXPANSIVEMUTILATION_NAME` |
| Pursuing Mutilation | Mutilazione Inseguitrice | `CODEX_SPELLECHOESOFMUTILATION_PURSUINGMUTILATION_NAME` |
| Retreating Mutilation | Mutilazione in Ritirata | `CODEX_SPELLECHOESOFMUTILATION_RETREATINGMUTILATION_NAME` |
| Fractured Rift | Fenditura Fratturata | `CODEX_SPELLECHORIFT_FRACTUREDRIFT_NAME` |
| Receding Rift | Fenditura Retrocedente | `CODEX_SPELLECHORIFT_RECEDINGRIFT_NAME` |
| Charged Fireball | Palla di Fuoco Caricata | `CODEX_SPELLFIREBALL_CHARGEDFIREBALL_NAME` |
| Combusting Fireball | Palla di Fuoco Combustiva | `CODEX_SPELLFIREBALL_COMBUSTINGFIREBALL_NAME` |
| Explosive Impact | Impatto Esplosivo | `CODEX_SPELLFIREBALL_EXPLOSIVEIMPACT_NAME` |
| Igniting Fireball | Palla di Fuoco Incendiaria | `CODEX_SPELLFIREBALL_IGNITINGFIREBALL_NAME` |
| Nearcast Detonation | Detonazione Ravvicinata | `CODEX_SPELLFIREBALL_NEARCASTDETONATION_NAME` |
| Rapid Embers | Braci Rapide | `CODEX_SPELLFIREBALL_RAPIDEMBERS_NAME` |
| Battle Resolve | Determinazione in Battaglia | `CODEX_SPELLFRENZY_BATTLERESOLVE_NAME` |
| Bloodrush Frenzy | Frenesia del Sangue | `CODEX_SPELLFRENZY_BLOODRUSHFRENZY_NAME` |
| Extended Frenzy | Frenesia Prolungata | `CODEX_SPELLFRENZY_EXTENDEDFRENZY_NAME` |
| Lingering Frenzy | Frenesia Persistente | `CODEX_SPELLFRENZY_LINGERINGFRENZY_NAME` |
| Anchored Glide | Scivolata Ancorata | `CODEX_SPELLFROSTGLIDE_ANCHOREDGLIDE_NAME` |
| Cryo Surge | Ondata Criogenica | `CODEX_SPELLFROSTGLIDE_CRYOSURGE_NAME` |
| Frost Armor | Armatura Gelida | `CODEX_SPELLFROSTGLIDE_FROSTARMOR_NAME` |
| Frostbinding Glide | Scivolata del Vincolo Gelido | `CODEX_SPELLFROSTGLIDE_FROSTBINDINGGLIDE_NAME` |
| Frost Glide Extra Charge | Carica Extra di Scivolata Gelida | `CODEX_SPELLFROSTGLIDE_FROSTGLIDEEXTRACHARGE_NAME` |
| Glacial Glide | Scivolata Glaciale | `CODEX_SPELLFROSTGLIDE_GLACIALGLIDE_NAME` |
| Refreezing Glide | Scivolata Rigelante | `CODEX_SPELLFROSTGLIDE_REFREEZINGGLIDE_NAME` |
| Shattering Step | Passo Frantumante | `CODEX_SPELLFROSTGLIDE_SHATTERINGSTEP_NAME` |
| Channeled Javelin | Giavellotto Canalizzato | `CODEX_SPELLFROSTJAVELIN_CHANNELEDJAVELIN_NAME` |
| Channelled Javelin | Giavellotto Canalizzato | `CODEX_SPELLFROSTJAVELIN_CHANNELLEDJAVELIN_NAME` |
| Frostfire Javelin | Giavellotto di Fuocogelo | `CODEX_SPELLFROSTJAVELIN_FROSTFIREJAVELIN_NAME` |
| Frost Ward | Protezione Gelida | `CODEX_SPELLFROSTJAVELIN_FROSTWARD_NAME` |
| Heavy Javelin | Giavellotto Pesante | `CODEX_SPELLFROSTJAVELIN_HEAVYJAVELIN_NAME` |
| Icy Shockwave | Onda di Shock Gelida | `CODEX_SPELLFROSTJAVELIN_ICYSHOCKWAVE_NAME` |
| Shatter | Frantumazione | `CODEX_SPELLFROSTJAVELIN_SHATTER_NAME` |
| Splintering Javelin | Giavellotto a Schegge | `CODEX_SPELLFROSTJAVELIN_SPLINTERINGJAVELIN_NAME` |
| Splitting Javelin | Giavellotto Scindente | `CODEX_SPELLFROSTJAVELIN_SPLITTINGJAVELIN_NAME` |
| Steady Javelin | Giavellotto Stabile | `CODEX_SPELLFROSTJAVELIN_STEADYJAVELIN_NAME` |
| Reset on Kill | Azzeramento all'Uccisione | `CODEX_SPELLFURIOUSSTRIKE_RESETONKILL_NAME` |
| Splintering Strike | Colpo a Schegge | `CODEX_SPELLFURIOUSSTRIKE_SPLINTERINGSTRIKE_NAME` |
| Barrage of Arrows | Raffica di Frecce | `CODEX_SPELLHAILOFARROWS_BARRAGEOFARROWS_NAME` |
| Pinning Hail | Pioggia Inchiodante | `CODEX_SPELLHAILOFARROWS_PINNINGHAIL_NAME` |
| Poison Tips | Punte Velenose | `CODEX_SPELLHAILOFARROWS_POISONTIPS_NAME` |
| Chain Trap | Trappola a Catena | `CODEX_SPELLHUNTERSTRAP_CHAINTRAP_NAME` |
| Explosive Trap | Trappola Esplosiva | `CODEX_SPELLHUNTERSTRAP_EXPLOSIVETRAP_NAME` |
| Freezing Trap | Trappola Congelante | `CODEX_SPELLHUNTERSTRAP_FREEZINGTRAP_NAME` |
| Hand-placed Trap | Trappola Manuale | `CODEX_SPELLHUNTERSTRAP_HANDPLACEDTRAP_NAME` |
| Quick Trap | Trappola Rapida | `CODEX_SPELLHUNTERSTRAP_QUICKTRAP_NAME` |
| Scatter Trap | Trappola Dispersa | `CODEX_SPELLHUNTERSTRAP_SCATTERTRAP_NAME` |
| Venom Burst Trap | Trappola a Esplosione Velenosa | `CODEX_SPELLHUNTERSTRAP_VENOMBURSTTRAP_NAME` |
| Cascading Inferno | Inferno a Cascata | `CODEX_SPELLINFERNO_CASCADINGINFERNO_NAME` |
| Cinderbank Inferno | Inferno Accumulabraci | `CODEX_SPELLINFERNO_CINDERBANKINFERNO_NAME` |
| Combusting Inferno | Inferno Combustivo | `CODEX_SPELLINFERNO_COMBUSTINGINFERNO_NAME` |
| Firepit Inferno | Inferno delle Fosse Ardenti | `CODEX_SPELLINFERNO_FIREPITINFERNO_NAME` |
| Firestorm | Tempesta di Fuoco | `CODEX_SPELLINFERNO_FIRESTORM_NAME` |
| Shielding Inferno | Inferno Protettivo | `CODEX_SPELLINFERNO_SHIELDINGINFERNO_NAME` |
| Soft Flames | Fiamme Lievi | `CODEX_SPELLINFERNO_SOFTFLAMES_NAME` |
| Soft Inferno | Inferno Lieve | `CODEX_SPELLINFERNO_SOFTINFERNO_NAME` |
| Scattering Onslaught | Assalto Dispersivo | `CODEX_SPELLLIMITLESSONSLAUGHT_SCATTERINGONSLAUGHT_NAME` |
| Focused Eruption | Eruzione Focalizzata | `CODEX_SPELLOUTBREAK_FOCUSEDERUPTION_NAME` |
| Lingering Rupture | Frattura Persistente | `CODEX_SPELLOUTBREAK_LINGERINGRUPTURE_NAME` |
| Plague Vector | Vettore della Peste | `CODEX_SPELLOUTBREAK_PLAGUEVECTOR_NAME` |
| Ravenous Cascade | Cascata Vorace | `CODEX_SPELLOUTBREAK_RAVENOUSCASCADE_NAME` |
| Terminal Bloom | Fioritura Terminale | `CODEX_SPELLOUTBREAK_TERMINALBLOOM_NAME` |
| Slicing Counter | Contrattacco Tagliente | `CODEX_SPELLPARRY_SLICINGCOUNTER_NAME` |
| Channeled Shards | Frammenti Canalizzati | `CODEX_SPELLPLAGUESHARDS_CHANNELEDSHARDS_NAME` |
| Lingering Shards | Frammenti Persistenti | `CODEX_SPELLPLAGUESHARDS_LINGERINGSHARDS_NAME` |
| Splintering Shards | Frammenti Scheggiati | `CODEX_SPELLPLAGUESHARDS_SPLINTERINGSHARDS_NAME` |
| Striking Hook | Gancio Tagliente | `CODEX_SPELLPOWERHOOK_STRIKINGHOOK_NAME` |
| Sweeping Hook | Gancio a Spazzata | `CODEX_SPELLPOWERHOOK_SWEEPINGHOOK_NAME` |
| Executing Pulverize | Polverizza Esecutore | `CODEX_SPELLPULVERIZE_EXECUTINGPULVERIZE_NAME` |
| Projected Pulverize | Polverizza Proiettato | `CODEX_SPELLPULVERIZE_PROJECTEDPULVERIZE_NAME` |
| Remote Pulverize | Polverizza Remoto | `CODEX_SPELLPULVERIZE_REMOTEPULVERIZE_NAME` |
| Shredding Pulverize | Polverizza Dilaniatore | `CODEX_SPELLPULVERIZE_SHREDDINGPULVERISE_NAME` |
| Steady Pulverize | Polverizza Stabile | `CODEX_SPELLPULVERIZE_STEADYPULVERIZE_NAME` |
| Striking Pulverize | Polverizza Tagliente | `CODEX_SPELLPULVERIZE_STRIKINGPULVERIZE_NAME` |
| Cycling Strikes | Colpi Ciclici | `CODEX_SPELLQUICKJAB_CYCLINGSTRIKES_NAME` |
| Enraging Jab | Jab Infuriante | `CODEX_SPELLQUICKJAB_ENRAGINGJAB_NAME` |
| Quick Strikes | Colpi Rapidi | `CODEX_SPELLQUICKJAB_QUICKSTRIKES_NAME` |
| Raging Jab | Jab Furente | `CODEX_SPELLQUICKJAB_RAGINGJAB_NAME` |
| Recovering Strike | Colpo Ristoratore | `CODEX_SPELLQUICKJAB_RECOVERINGSTRIKE_NAME` |
| Root Strike | Colpo di Radice | `CODEX_SPELLROOTSTRIKESPIKE_NAME` |
| Dazing Stampede | Carica Travolgente Frastornante | `CODEX_SPELLSEISMICSTAMPEDE_DAZINGSTAMPEDE_NAME` |
| Expansive Stampede | Carica Travolgente Estesa | `CODEX_SPELLSEISMICSTAMPEDE_EXPANSIVESTAMPEDE_NAME` |
| Remote Stampede | Carica Travolgente Remota | `CODEX_SPELLSEISMICSTAMPEDE_REMOTESTAMPEDE_NAME` |
| Anchored Convergence | Convergenza Ancorata | `CODEX_SPELLSHADOWCONVERGENCE_ANCHOREDCONVERGENCE_NAME` |
| Manyfold Convergence | Convergenza Molteplice | `CODEX_SPELLSHADOWCONVERGENCE_MANYFOLDCONVERGENCE_NAME` |
| Numbing Convergence | Convergenza Intorpidente | `CODEX_SPELLSHADOWCONVERGENCE_NUMBINGCONVERGENCE_NAME` |
| Phasing Convergence | Convergenza Sfasata | `CODEX_SPELLSHADOWCONVERGENCE_PHASINGCONVERGENCE_NAME` |
| Relentless Convergence | Convergenza Implacabile | `CODEX_SPELLSHADOWCONVERGENCE_RELENTLESSCONVERGENCE_NAME` |
| Severing Convergence | Convergenza Recidente | `CODEX_SPELLSHADOWCONVERGENCE_SEVERINGCONVERGENCE_NAME` |
| Converging Daggers | Pugnali Convergenti | `CODEX_SPELLSHADOWDAGGERS_CONVERGINGDAGGERS_NAME` |
| Fan of Daggers | Ventaglio di Pugnali | `CODEX_SPELLSHADOWDAGGERS_FANOFDAGGERS_NAME` |
| Momentous Return | Ritorno Impetuoso | `CODEX_SPELLSHADOWDAGGERS_MOMENTOUSRETURN_NAME` |
| Auto Strike | Colpo Automatico | `CODEX_SPELLSTRONGSTRAIGHT_AUTOSTRIKE_NAME` |
| Punishing Straight | Diretto Punitivo | `CODEX_SPELLSTRONGSTRAIGHT_PUNISHINGSTRAIGHT_NAME` |
| Steady Straight | Diretto Stabile | `CODEX_SPELLSTRONGSTRAIGHT_STEADYSTRAIGHT_NAME` |
| Straight Lunge | Diretto in Affondo | `CODEX_SPELLSTRONGSTRAIGHT_STRAIGHTLUNGE_NAME` |
| Stun Shatter | Frantumazione da Stordimento | `CODEX_SPELLSTUNSHATTERBURST_NAME` |
| Sealed Void | Vuoto Sigillato | `CODEX_SPELLTIMELESSVOID_SEALEDVOID_NAME` |
| Warding Void | Vuoto Protettivo | `CODEX_SPELLTIMELESSVOID_WARDINGVOID_NAME` |
| Concussive Quake | Sisma Concussivo | `CODEX_SPELLTYRANTQUAKE_CONCUSSIVEQUAKE_NAME` |
| Rapid Quake | Sisma Rapido | `CODEX_SPELLTYRANTQUAKE_RAPIDQUAKE_NAME` |
| Reverse Quake | Sisma Inverso | `CODEX_SPELLTYRANTQUAKE_REVERSEQUAKE_NAME` |
| Ambush Volley | Raffica d'Imboscata | `CODEX_SPELLVANISHINGSTRIKE_AMBUSHVOLLEY_NAME` |
| Dazing Ambush | Imboscata Frastornante | `CODEX_SPELLVANISHINGSTRIKE_DAZINGAMBUSH_NAME` |
| Flickering Vanish | Dissolvenza Intermittente | `CODEX_SPELLVANISHINGSTRIKE_FLICKERINGVANISH_NAME` |
| Vanishing Roll | Rotolata Dissolvente | `CODEX_SPELLVANISHINGSTRIKE_VANISHINGROLL_NAME` |
| Bloody Cleave | Fendente Sanguinoso | `CODEX_SPELLVEHEMENTCLEAVE_BLOODYCLEAVE_NAME` |
| Crippling Cleave | Fendente Storpiante | `CODEX_SPELLVEHEMENTCLEAVE_CRIPPLINGCLEAVE_NAME` |
| Executing Cleave | Fendente Esecutore | `CODEX_SPELLVEHEMENTCLEAVE_EXECUTINGCLEAVE_NAME` |
| Bloody Vortex | Vortice Sanguinoso | `CODEX_SPELLVORTEX_BLOODYVORTEX_NAME` |
| Concentrated Vortex | Vortice Concentrato | `CODEX_SPELLVORTEX_CONCENTRATEDVORTEX_NAME` |
| Stable Vortex | Vortice Stabile | `CODEX_SPELLVORTEX_STABLEVORTEX_NAME` |
| Twister | Tornado | `CODEX_SPELLVORTEX_TWISTER_NAME` |
| Commander's War Banner | Stendardo di Guerra del Comandante | `CODEX_SPELLWARBANNERCOMMANDER_NAME` |
| Bloody Execute | Esecuzione Sanguinosa | `CODEX_SPELLWAVESTRIKE_BLOODYEXECUTE_NAME` |
| Continuous Wave | Onda Continua | `CODEX_SPELLWAVESTRIKE_CONTINUOUSWAVE_NAME` |
| Follow Up | Colpo Successivo | `CODEX_SPELLWAVESTRIKE_FOLLOWUP_NAME` |
| Returning Wave | Onda di Ritorno | `CODEX_SPELLWAVESTRIKE_RETURNINGWAVE_NAME` |
| Splitting Wave | Onda Scindente | `CODEX_SPELLWAVESTRIKE_SPLITTINGWAVE_NAME` |
| Blade Discipline | Disciplina della Lama | `CODEX_SPELLWEAPONSWAP_BLADEDISCIPLINE_NAME` |
| Crossbow Discipline | Disciplina della Balestra | `CODEX_SPELLWEAPONSWAP_CROSSBOWDISCIPLINE_NAME` |
| Fan Of Bolts | Ventaglio di Dardi | `CODEX_SPELLWEAPONSWAP_FANOFBOLTS_NAME` |
| Hero's Turn | Giravolta dell'Eroe | `CODEX_SPELLWEAPONSWAP_HEROSTURN_NAME` |
| Support Versatility | Versatilità di Supporto | `CODEX_SPELLWEAPONSWAP_SUPPORTVERSATILITY_NAME` |
| Critical | Critico | `CODEX_STATCRITICAL_NAME` |
| Minion Damage | Danno dei servitori | `CODEX_STATMINIONS_MINIONDAMAGE_NAME` |
| Minions | Servitori | `CODEX_STATMINIONS_NAME` |
| Penetration | Penetrazione | `CODEX_STATPENETRATION_NAME` |
| Buff | Bonus | `CODEX_TAG_BUFF` |
| Buildable | Costruibile | `CODEX_TAG_BUILDABLE` |
| Debuff | Malus | `CODEX_TAG_DEBUFF` |
| Empowerment | Potenziamento | `CODEX_TAG_EMPOWERMENT` |
| Equipment Set | Set di equipaggiamento | `CODEX_TAG_EQUIPMENTSET` |
| Reference | Riferimento | `CODEX_TAG_REFERENCE` |
| Stat | Statistica | `CODEX_TAG_STAT` |
| Vital | Risorsa vitale | `CODEX_TAG_VITAL` |
| Concentration On Hit Up | Bonus alla Concentrazione al colpo | `CODEX_TIMEDCONCENTRATIONONHITUP_NAME` |
| Speed Down | Velocità ridotta | `CODEX_TIMEDSPEEDDOWN_NAME` |

## Verifica finale

- 1.173 record UTF-8 non vuoti, ciascuno con esattamente una tabulazione.
- Chiavi identiche all'input e nello stesso ordine.
- Segnaposto `<xN/>` identici per contenuto e molteplicità in ogni riga.
- Valori numerici conservati; virgola decimale italiana nella prosa, notazione originale nelle formule.
- Formule tra parentesi conservate letteralmente.
- Nessuna riga interamente lasciata in inglese; nomi propri e identificatori tecnici preservati dove richiesto.
- Stesse stringhe inglesi ripetute rese allo stesso modo.
- Controllo del glossario sui nomi completi e sui termini delle descrizioni; verifiche manuali per plurali, accordi e parole comuni con significati diversi.
- Non è stata effettuata una prova dei riquadri nell'interfaccia del gioco.
