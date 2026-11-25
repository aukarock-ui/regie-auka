# Campagne de tests exhaustive — StudioLive 32SC et 16R (chantier 10)

Console 32SC serial:SD7E24030014 (10.104.31.89), 16R serial:RA1E18040123 en mode Stagebox. Serveur `code/studiolive-mix-assistant`, branche `guide-auka`. Plan validé par Louis le 24/11 (`~/.claude/plans/background-from-the-session-ethereal-hummingbird-…md`).

## Décisions de Louis

- 24/11 : amplis coupés pendant les tests, générateur de signal permis, mesures aux vu-mètres et par relecture.
- 24/11 : toutes les catégories d'écriture sont permises pendant la campagne, sauf `danger`. Chaque clé `danger` est redemandée à part.
- 24/11, en plan mode : pas besoin de garder le preset rock. Pas de scène « Avant tests » ni de restauration en fin de campagne. On enregistre une scène dans la console à chaque fois, et un dossier sur le PC (`sauvegardes-console/`) garde toutes les sauvegardes.

## État de départ (lecture, 24/11)

- Catalogue : 2 106 paramètres. 30 `observed`, 251 `calibrated`, 1 414 `apk_definition`, 370 `probe_required`, 41 non écrits (`ucnetCatalogStats()`).
- Enregistrement de scène : la bibliothèque `@featherbear/presonus-studiolive-api@1.9.1` ne le fait pas. `Plugins/studiolivepanel.dll` d'Universal Control 5.1.1 contient le message `StorePreset`, à côté de `presetFile`, `presetTarget`, `presetTargetSlave`, `presetChannelNames`, `targetSlot`, `CopyPreset` et `ReorderPreset`. Les champs restent à relever par capture réseau.

## Lot 0 — Sauvegardes

| Élément | Statut | Détail |
|---|---|---|
| `snapshot_console_state` (sauvegarde PC) | codé, testé en unitaire | commit `d65189c` (1054 tests). Lecture seule. Relit la console (déconnexion puis reconnexion), puis écrit `sauvegardes-console/AAAA-MM-JJ_HHMM_<sujet>.json` sans jamais écraser un fichier. Dossier fixé par `PRESONUS_SNAPSHOT_DIR` dans `.mcp.json`. Pas encore essayé sur la 32SC : il faut d'abord relancer Claude Code. |
| Projet console de la campagne | créé par Louis | `13.Claude.proj`. Scène `01.Test A.scn` enregistrée puis écrasée dans UC Surface, sans capture. |
| Capture `StorePreset` (pktmon) | écrasement relevé ; création non relevée | `sauvegardes-console/capture-store.pcapng` (20 h 05). Le PC (10.104.31.223) envoie une seule demande à la console : `JM {"id":"StorePreset","url":"presets","presetTarget":"","presetFile":"presets/proj/13.Claude.proj/01.Test A.scn"}`. La console diffuse deux fois `StoredPreset {presetFile, presetName:"Test A", presetType:"scn", url:"presets"}`, puis le PC relit la liste (`FR List`). Les cases vides s'appellent `NN._ Empty Location _.scn`. Aucune trame pour « Test B » dans cette première capture. |
| Capture de la création (20 h 07) | relevée | Même message, la case vide prenant le nom de la nouvelle scène : `JM {"id":"StorePreset","url":"presets","presetTarget":"","presetFile":"presets/proj/13.Claude.proj/02.Test B.scn"}`. Réponses de la console : `StoredPreset {presetFile:"…/02.Test B.scn", presetName:"Test B", presetType:"scn"}`, puis `PS presets/loaded_scene_title = "Test B"` et `PS presets/loaded_scene_name = "proj/13.Claude.proj/02.Test B.scn"` (la scène créée devient la scène chargée), puis `PV presets/diskusage`. Le nom de la scène est donc porté par le nom de fichier `NN.<nom>.scn`, à la place de `NN._ Empty Location _.scn`. |
| `store_console_preset` | codé, testé en unitaire | Commits `3505d91` (modes `overwrite` et `create`, garde-fous, attente de `StoredPreset`, relecture de la liste brute avec les cases vides, journal d'audit) et `bef5277` (JSON compact identique à la capture, 115 octets) : 1069 tests. Nom limité à 32 caractères par le code ; la limite réelle de la console n'est pas relevée. Outil ajouté à la liste `ask` de `.claude/settings.json`. Pas encore essayé sur la console (relance de Claude Code nécessaire). |

### Lot 0, essais réels (25/11, 00 h 15 à 00 h 30, serveur 60bac11, Claude Code relancé par Louis)

- `snapshot_console_state` : **passe.** Le fichier `sauvegardes-console/2026-11-25_0017_debut-lot1.json` fait 22 387 clés et 1,27 Mo. Firmware 3.4.0.111374. Défaut mineur : le champ `clientIdentifier` affiche le `deviceId` (`serial:SD7E24030014`) au lieu de l'identifiant client.
- `store_console_preset`, mode `overwrite`, sur `13.Claude.proj/02.Test B.scn` : **passe.** La console confirme (`StoredPreset` reçu), et la liste relue est correcte.
- `store_console_preset`, mode `create`, case 03 « Test C » : **échoue sans rien envoyer** (« listProjectSlots: timeout »). Cause lue dans la bibliothèque : le collecteur `FD` jette toute réponse dont l'identifiant n'a pas été réservé par son propre générateur `UniqueRandom`, et `sendList` filtre les cases vides. Correction en cours (`dev-serveur`).
- **Les tables de libellés de la console sont perdues.** L'état contient des listes `*.strings`. Certaines sont en clair : `permissions.mix_permissions` = None, FOH, All Auxes, Aux 1/2…, `mastersection.mon_list`, `stageboxsetup.*`. D'autres ne valent qu'un numéro de table partagée : 3 pour `inputsrc`, 5 et 6 pour les modèles d'EQ et de comp, 7 pour `auxpremode`, 8 pour `busmode`, 9 pour `bussrc`, 11 pour `geq.source`, 12 pour `fx.type`. Or la bibliothèque jette la table `shared` (`keyHandlers.shared: null`) et ignore les messages `PL` (ParamStrList), qui portent probablement les listes dynamiques comme `analog_source` (28 entrées). Les garder décoderait la source des GEQ, le type de FX, la source des bus et le patch des sorties. Correction en cours (`dev-serveur`).
- Indice pour le générateur et le GEQ (DLL du simulateur d'UC, à confirmer sur la console) : juste après « Pink Noise, White Noise, Sine » vient une liste « Main L/R, Flex Mix 1/2 … 15/16, Subgroups A/B, C/D, Mono/Center, Flex Mix 17/18 … 31/32, Insert 1-4 ». La DLL contient aussi les chaînes `geqin`, `geqout`, `sourceName` et `AssignGEQSource`.

### Lot 0 terminé ; tables de libellés décodées (25/11, 00 h 30 à 00 h 40, serveur e7f7db6)

- `store_console_preset` en mode `create` (case 03, « Test C ») : **passe** après correction (`e7f7db6` : `sendList` brut, id réservé par la bibliothèque). La console confirme, et la liste relue contient « 03.Test C.scn ».
- `recall_console_preset` de `13.Claude.proj/03.Test C.scn` : **passe.** La comparaison des sauvegardes de 00 h 30 et 00 h 35 (`outils/diff-sauvegardes.py`) ne montre que 2 clés changées, `presets.loaded_scene_name` et `presets.loaded_scene_title` (Test B → Test C). Résultat attendu, puisque la scène contenait l'état courant.
- **Table partagée reçue** (`sharedStrings`, une entrée à la racine) : un tableau indexé à partir de 0. 0 = Main L/R, Flex Mix 1/2…15/16, Subgroups A/B, C/D (référencée par aucune clé lue). 1 = chaîne vide. 2 = Stand-alone, Monitor Mixer, Stagebox. 3 = Analog, Network, USB, SD Card. 4 = None, Ch. 1…32. 5 = Standard, Passive, Vintage, Alpine EQ-550, Baxandall EQ, RC500 EQ, Solar 69, The Tube EQ, Vintage 3-band, VT1 EQ. 6 = Standard, Tube, FET, Brit Comp, Classic Comp, Comp 160, Everest C100A, FC-670, RC500 Comp, The Tube CB, VT1 Comp. 7 = Pre1, Pre2, Post. 8 = Aux, Subgroup, Matrix. 9 = Mixer, Network. 10 = Standard. 11 = None, Main L, Main R, Mix 1…16, Sub A…D. 12 = Digital XL Reverb, PAE-16 Digital Reverb, 335 Digital Reverb, Vintage Plate Reverb, Mono Delay, Stereo Delay, Pingpong Delay, Chorus, Flanger.
- **Règle de décodage prouvée** : indice = valeur × (n − 1). Vérifiée sur cinq paramètres indépendants, contre la spec du preset rock :
  - `line.ch1.inputsrc` = 1, Network ;
  - `line.ch1.opt.compmodel` = 0, Standard ;
  - `line.ch1.opt.eqmodel` = 4, Baxandall EQ ;
  - `fx.ch2.type` = 5, Stereo Delay (FX B delay de la spec) ;
  - `geq.ch1.source` = 3, Mix 1, et `geq.ch3.source` = 5, Mix 3.

  **La correspondance GEQ → mix est décodée.**
- **Liste des permissions** (en clair) : None, FOH, All Auxes, Aux 1/2, Aux 3 … Aux 16. La permission « None » de la 16R correspond à l'indice 0.
- `PL` reçu : seulement `permissions/device_list`, qui contient « AUKA: PC » et « presonus-mcp-server: StudioLive API ». Les listes `analog_source` et `digital_source` (sources du patch de sortie) ne sont pas arrivées : elles restent `probe_required`.
- `swapcompeq` à 1 sur le canal 24 (00 h 24) : confirmé à la relecture. **À contrôler par Louis dans UC Surface** : l'accès de Claude à l'écran a été refusé. Le canal 21 a le 48 V actif sans source nommée, à signaler à Louis.
- Outil de balayage `sweep_parameters` commandé à `dev-serveur`, avec rapport dans un fichier pour ménager le contexte. Il est déjà ajouté à la liste `ask` de `.claude/settings.json`.

### Lecture des retours et des GEQ corrigée (25/11, 05 h, serveur 4e52914, 1132 tests)

Commits `0314e5d` (listes décodées, `observed`), `ea1ab90` (GEQ), `b1e6958` (`get_aux_mix`), `07fa651` (paires stéréo), `96f8fc9` (identifiant client de la sauvegarde) et `4e52914` (`sweep_parameters`). Vérifié sur la console :
- `get_geq_overview` : **passe.** GEQ 1 à 6 sont sur Mix 1 à 6 (Retours scène, Dj, Retour Robot, Matt, Aux 5, Aux 6), GEQ 7 sur Main L et GEQ 8 sur Main R. GEQ 5 est éteint. Coupes héritées d'une ancienne config : GEQ 3 à −4,5 dB à 3,15 kHz ; GEQ 4 à −12 dB à 3,15 kHz, avec des coupes de 4 à 12,5 kHz ; GEQ 6, dix bandes entre 250 Hz et 12,5 kHz. À montrer à Louis, rien n'est effacé.
- `get_monitor_mix_layout` : **passe.** Les paires viennent de `aux.chN.link` et `linkmaster`, recoupés par `panlinkstate` : 1/2, 9/10, 11/12 et 13/14, `observed`. Les modes de bus sont lus : Aux 1-6 et 8 en Aux ; 7 et 9-16 en Subgroup. **À signaler à Louis** : le bus 7 est en Subgroup sans nom, et le bus 12 s'appelle « INSTRUS » alors que le 11 s'appelle « INSTRU ».
- `get_aux_mix 1` : **passe.** Les familles sont séparées : `line` (32), `return` (Aux In 1, Aux In 2, USB), `fxreturn` (4) et `talkback`. Le mode pré/post est lu par mix (`Pre1`) ; aucune clé ne porte le pré/post par départ. Reste : des mix fantômes 17 à 32 dans l'état (`aux1..32` sur chaque canal), et un sens de `assign_auxM` à confirmer (canal muté = « not_assigned »).
- Description d'outil périmée : celle de `get_geq_overview`, affichée par Claude Code, dit encore « mapping not documented ». C'est la liste d'outils qui est restée en mémoire, et une relance de Claude Code la rafraîchira.
- `sweep_parameters` : pas encore visible. Il faut relancer Claude Code pour qu'il apparaisse.

## Lot 1 — Générateur de signal et vu-mètres (24/11, 22 h 55, ancien serveur 8234594)

| Clé | Avant | Écrit | Relu | Statut |
|---|---|---|---|---|
| `signalgen.type` | Pink Noise | Sine (brut 1 = indice 2/2) | Sine | passe (confirmé à la relecture) |
| `signalgen.freq` | 440 Hz (brut 0,4475) | 1000 Hz (brut 0,5663) | 1000 Hz | passe ; codage log vérifié : brut = log₁₀(f/20)/3 |
| `signalgen.level` | −∞ (brut 0) | −40 dB (brut 0,1498), puis retour à −84 dB = −∞ | idem | passe |

- **Pas d'écho** de la console pour les écritures `signalgen` (`confirmedByEcho: 0`) : à la première écriture, le serveur a renvoyé les 3 valeurs, puis les a confirmées à la relecture. À la seconde écriture, une seule valeur, confirmée à la relecture sans renvoi. Le serveur ne reçoit peut-être pas ses propres échos sur ces clés : à comparer avec les autres familles.
- **Routage du générateur** : le catalogue ne contient que `type`, `freq` et `level` (et la page `mainscreen.signalGenPage`). Le manuel français 32SC/16R ne décrit pas le générateur. Les sources de sortie (`analog_source`) sont une liste dynamique fournie par la console. Il faut relever l'état brut (nouvel outil `snapshot_console_state`) pour trouver où le générateur est envoyé. Pas d'écoute possible tant que ce n'est pas trouvé.
- **Vu-mètres** : le résumé des vu-mètres est **vide** (ni silencieux ni actifs), alors que des trames UDP arrivent (300 trames `rtan` en mémoire). Cause soupçonnée, non prouvée : une erreur de décodage `levl` dans la bibliothèque, passée sous silence, ou un groupe absent de `packet[0]`. Diagnostics codés (commit `60bac11`, 1083 tests). Relevé à 00 h 13 avec le serveur rechargé : 401 trames `levl` reçues, **0 erreur de décodage**, taille 225 octets, 93 valeurs, 3 groupes, **numéros 2, 4 et 5, de 31 valeurs chacun** ; aucun groupe 0. Le serveur n'ingère que `packet[0]` (`meterEventsWithLineValues: 0`), d'où le résumé vide. **Cause prouvée.** Ce que mesurent ces groupes reste inconnu : 31 valeurs ne correspondent pas aux 32 canaux d'entrée. À identifier en envoyant un signal connu sur une source connue. La bibliothèque demande aussi `redu` (498 trames) et `rtan` (496 trames).
- **Deux serveurs `studiolive` en même temps** : celui de la session principale (lancé à 19 h 08) et celui de cette session (19 h 31). Ils ont le même identifiant client, et le second ne pouvait pas ouvrir le port du détecteur (`EADDRINUSE 127.0.0.1:53999`). Une coupure de liaison est relevée à 22 h 56 min 08 s, juste après une relecture. Le serveur de la session principale (PID 3896) a été arrêté à 22 h 57. Alerte de doublon ajoutée (`duplicateServerSuspected`, commit `60bac11`). Le serveur de cette session a été relancé à 00 h 12 (arrêt du processus, puis redémarrage automatique au premier appel). Claude Code garde cependant l'ancienne liste de 52 outils : les nouveaux outils n'apparaissent qu'après une vraie reconnexion. **Règle proposée : une seule session à la fois avec le serveur `studiolive`.** Il reste à vérifier si les coupures « toutes les 30 s » relevées plus tôt venaient de ce doublon.

## Lot 2 — Premier balayage `sweep_parameters` sur `line.ch24.` (25/11, 09 h 32, serveur 4e52914)

Rapport : `sauvegardes-console/sweeps/2026-11-25_0932_line-ch24.json`. Paquets de 20, toutes catégories sauf `danger`, `unmute` et `phantom` ; `includeProbeRequired` activé. 224 clés retenues ; arrêt au premier paquet.

| Clé (canal 24) | Résultat | Lecture |
|---|---|---|
| `chnum`, `name`, `username`, `iconid` | passe (écho + relecture) | texte écrit et remis |
| `solo`, `volume`, `pan`, `stereopan`, `dawpostdsp`, `memab`, `rta_active` | relu sans écho | la console n'envoie pas d'écho, la relecture confirme ; remis |
| `panlinkstate`, `link`, `linkmaster` | relu sans écho, remis | **couplage** : pendant le link, les valeurs de test du paquet ont été recopiées sur le canal 23 |
| `select` | remise échouée → arrêt | **sélection exclusive** : écrire 1 désélectionne le canal 1 ; écrire 0 ne désélectionne pas |
| `rta_pre`, `assign_aux1` à `assign_aux4` | écriture ignorée (relecture inchangée) | clés vraisemblablement dérivées, à étudier (inférence, à valider) |

Effets de bord relevés puis remis à la main par plan (09 h 35, 6 clés, toutes confirmées) : `line.ch1.select` 0→1 ; canal 23 : `dawpostdsp`, `memab`, `iconid`, `preampgain` (0,1667→0,4167), `opt.swapcompeq` (1→0). Sauvegarde `2026-11-25_0935_apres-remise-sweep-ch24.json` comparée à `2026-11-25_0035_apres-rappel-test-c.json` : seules diffèrent `global.rta_active` et `line.ch1.rta_active` (1→0, affichage RTA) et l'adresse IP (changement de réseau). État rétabli.

Corrections confiées à `dev-serveur` : clés exclusives et de couplage exclues par défaut et testées une par une à part ; remise automatique des effets de bord ; statut « ignorée par la console » sans arrêt ; seconde tentative avant arrêt.

### Deuxième balayage du canal 24 (25/11, 09 h 51, serveur 2272bfd)

Essai à blanc : 212 clés ; `select`, `solo`, `link*`, `panlinkstate`, `linkoptions.*`, `rta_active` mis de côté (12 clés). Vrai balayage arrêté au premier paquet : 20 clés, 4 passées, 16 relues sans écho, aucune ignorée, aucun échec.
- Collatéral `line.ch24.flexassignflags` 0 → 832 pendant le paquet, remis et confirmé. Cause non attribuée (arrêt avant le rejeu clé par clé) ; probablement lié aux `assign_auxN` (inférence, à valider).
- Collatéral `permissions.device_list.value` 0 → 1, remise non confirmée → arrêt. La liste (`device_list.strings` = « AUKA: PC%ucapp ») suit les clients connectés ; le serveur d'une autre session venait de se déconnecter. Valeur revenue seule à 0 : sauvegarde `2026-11-25_0952_apres-sweep2-ch24.json` identique à celle de 09 h 35 (0 différence).
- **Défaut de garde-fou relevé** : la remise des collatéraux a tenté d'écrire une clé `permissions.*` sans que sa catégorie soit permise. Corrigé par `dev-serveur` (remise soumise aux mêmes catégories, clés volatiles exclues de la détection, rejeu clé par clé avant tout arrêt).

### Troisième balayage du canal 24 (25/11, 09 h 58, serveur 33c85b4)

22 clés testées : 4 passées, 18 relues sans écho, aucun échec ; état final identique à l'état de départ (`residual` vide). Une clé volatile (`permissions.device_list`) notée sans être remise. Arrêt sur un collatéral de sélection (voir plus bas).

**Découverte (observé)** : `line.chN.flexassignflags` est le champ de bits des assignations FlexMix du canal : `assign_auxK` ↔ bit K−1. `assign_aux7` → 64 ; `assign_aux9` → 768 et met aussi `assign_aux10` à 1 (mix 9/10 liés en stéréo, assignés ensemble) ; `assign_aux11` → 3072 (paire 11/12). Le 832 du deuxième essai = 64 + 256 + 512 (mix 7, 9 et 10).

**Sélection** : pendant le rejeu de `assign_aux12`, la sélection est passée du canal 1 au Main (`line.ch1.select` 1→0, `main.ch1.select` 0→1). La cause reste inconnue : la clé testée, ou un geste sur la console ou UC Surface, à vérifier. Resélectionner le canal 1 a tout remis. Le serveur a pourtant arrêté, parce que `main.ch1.select` est de catégorie `master` et qu'il a eu raison de refuser de l'écrire. Correction demandée : traiter les sélections en groupe exclusif, puis relire avant d'arrêter.

### Balayage complet du canal 24 (25/11, 10 h 09, serveur 65db9f6)

Rapport : `sweeps/2026-11-25_1009_line-ch24.json`. **208 clés testées, état final identique à l'état de départ** (`residual` vide, 0 collatéral non remis).
- 200 passent : 4 avec écho, 196 confirmées à la relecture sans écho. Cela couvre noms, fader, pan, départs aux 32 mix et leurs pans, assignations FX, sources, délai, préampli et gain numérique, polarité, HPF, gate, comp, EQ 4 bandes et limiteur.
- 6 échecs, tous dus à des valeurs de test hors grille. Retestés par plan (10 h 35) avec des valeurs sur la grille, puis remis (10 h 37) : 6/6 confirmés.
  - `usb_src`, `sd_src` : 12/17 → 25/34 accepté.
  - `usb_src2`, `sd_src2` : 1/34 → 2/34.
  - `comp.kneewidth` : 0 → 0,5 (0,25 refusé).
  - `eq.eqtype1` : liste à deux valeurs, 0 « Hi Pass », 1 « Parametric » (libellés du catalogue).
- 2 écritures ignorées. `comp.reduction` est un vu-mètre, qu'il faut sauter. `opt.swapcompeq` est ignorée sur le canal 24, alors qu'un plan l'a bien écrite sur le canal 23 ce matin : **à étudier**.
- Effets liés, observés :
  - changer `adc_src` change `preampgain` (le gain suit la source, inférence à valider) ;
  - changer `inputsrc` change `inputsrc_preview`, `diggainactive`, `preampgain` et `digsendsrc` ;
  - assignations FlexMix : `flexassignflags`, bit K−1 = mix K ; les paires 9/10, 11/12 et 13/14 sont liées, les mix 15 et 16 sont seuls.
- 21 clés sautées. Les 12 de sélection, solo et link sont à tester à part (`includeCoupled`). `eqmodel`, `compmodel`, `gatekeysrc` et `compkeysrc` sont des listes que le balayage ne sait pas encore mesurer : correction en cours (tables de libellés). Restent la couleur, le mute, le 48 V, `clip` et `flexassignflags`.

### Balayage du bus 1 (FlexMix 1, lié au bus 2) (25/11, 10 h 44, serveur 65db9f6)

Rapport : `sweeps/2026-11-25_1044_aux-ch1.json`. `busmode` et `bussrc` exclus (tests à part).

**Résultats**
- 140 clés testées, 132 passent (4 avec écho, 128 à la relecture).
- 5 échecs :
  - `usb_src`, `sd_src`, `usb_src2`, `sd_src2` : valeurs hors grille, même cause qu'au canal 24 ;
  - `opt.swapcompeq` : test à 0,25, hors grille.
- 3 écritures ignorées : `monolevel`, `centerdiv`, `adc_src`.

**Effet du link sur le bus 2 (observé)** : tout réglage écrit sur le bus 1 se recopie sur le bus 2. Fader, mute, pan stéréo, assignations, nom d'icône et EQ sont concernés.

**Arrêt et remise en état**
- Le balayage s'est arrêté : l'EQ du bus 2 était revenue aux valeurs par défaut (0 dB, Q 0,6) sur les bandes 1, 2, 4, 5 et 6, et le serveur n'a pas réussi à la remettre. Cause probable : le test du modèle d'EQ ou de `swapcompeq` sur le bus 1, recopié par le link. C'est une inférence, à valider.
- J'ai remis ces 14 clés par un plan à 11 h 15, et la console les a toutes confirmées.
- Comparaison de la sauvegarde `2026-11-25_1115_apres-remise-bus2.json` avec celle de 09 h 52 : une seule différence, `line.ch24.preampgain.range.mid` 0 → 1. C'est une donnée de plage, pas un réglage. Son sens est à vérifier.

**Correctifs suivants (b479be3, 1158 tests)** : valeurs de test prises sur la grille (tables de libellés, puis `range.min/max`, puis dénominateur déduit), nouvel essai sur la grille avant de déclarer un échec, changement de modèle testé seul en attendant la confirmation de la console.

## Arrêt de la séance (25/11, vers 11 h 30) : état à la reprise

Louis a demandé l'arrêt et une publication intermédiaire (« fais un stop, on va continuer ailleurs, mets tout à jour »). La console est restée dans l'état de 11 h 15 (sauvegarde `2026-11-25_1115_apres-remise-bus2.json`), sans scène enregistrée pour ce lot.

Le serveur est en `db4fc4d` (1163 tests ; le balayage exige `unmute` pour remettre un canal démuté) :
- remise des paires liées (canal balayé d'abord, partenaire ensuite) ;
- plan de remise prêt dans le rapport en cas d'arrêt ;
- modèles testés seuls ;
- valeurs de test prises sur la grille.

Aucun de ces correctifs n'a encore été essayé sur la vraie console, en particulier sur un bus lié. Aucune scène n'a été enregistrée pour ce lot, alors que Louis l'avait demandé le 24/11 : la faire à la reprise.

Cause de la remise à zéro de l'EQ du bus 2 (relevée par `dev-serveur` dans le rapport de 10 h 44) : le changement de modèle d'EQ du bus 1 remet l'EQ des deux bus liés aux valeurs par défaut. C'est vu dans le rapport, pas encore validé par un essai isolé. L'EQ du bus 1 n'en garde pas de trace : la comparaison complète des sauvegardes ne montre que `line.ch24.preampgain.range.mid`.

Reste à faire :
1. Rebalayer le bus 1, puis les bus 3 à 16, les sous-groupes, les FX, le Main et le patch.
2. Tester à part `select`, `solo`, `link`, `busmode` et `bussrc`.
3. Étudier `swapcompeq`.
4. Lots 1 (routage du générateur, vu-mètres), 8 (16R), 9, 10 et 11 (détecteur de larsen : brancher l'USB).
5. Enregistrer une scène en fin de lot.
