# Retour de séance — 24/11/2026, preset rock alternatif écrit par Claude (32SC, serveur bb4297a)

Faits constatés sur la console (relecture de l'état), pas encore intégrés au guide.

## Envoyé et confirmé

- Preset complet 15 canaux (spec `2026-11-24_preset-rock-alternatif.spec.json`) : 503 pas sur 534 au premier envoi, puis 78 sur 79 au renvoi ciblé. Phantom non envoyé (non tranché par Louis).
- Types d'effet : B Stereo Delay, C Digital XL, D Ping Pong (A était déjà Vintage Plate). EQ du Main en Passive.
- Bus 9 à 16 et Main : Brit release 0,3 s ; Solar 69 bass 100 Hz gain 0, mid 0,7 kHz +2 dB, 10 kHz +2 dB ; FC-670 time constant 3 ; Alpine low 100 Hz 0 dB, mid 1,5 kHz +2 dB, high 7 kHz ; Tube CB mode manual, gain +2 dB ; Vintage EQ low 220 Hz +2, L-mid +1, H-mid +2, high +2 ; Comp 160 output +10 dB ; RC-500 EQ low 0 dB, high 3 kHz +2 dB ; Everest attack et release Fast ; Passive EQ on, high 10 kHz.
- Canaux : Baxandall du kick (low cut 36 Hz, low shelf 84 Hz +1 dB, high shelf 3,4 kHz +1 dB, high cut Off) ; RC-500 de la basse (attack 0,5 ms, release 500 ms, makeup +3 dB).

## Codage observé (nouveau)

- **Type d'effet** (`fx.chN.type`, pas de 1/8) : 0 = Digital XL, 0,125 = PAE-16, 0,375 = Vintage Plate, 0,5 = Mono Delay, 0,625 = Stereo Delay, 0,75 = Ping Pong. Identifié par les paramètres exposés par la console, puis vérifié après écriture. 0,25 (probablement 335), 0,875 et 1 (probablement Chorus, Flanger) : non vérifiés.
- **Modèle d'EQ du Main** : 1/9 = Passive (même ordre que sur les canaux ligne), vérifié par la présence des clés Passive après écriture.
- Entiers (sources) : `(v − min) / (max − min)` (avb_src ch20 = 20/64), mais `adc_src` est normalisé sur 16 sur la 32SC et non sur 32 comme dans le catalogue.

## Deuxième passe (13 h 06 à 13 h 14)

- **Routage corrigé.** LEAD, CHOEUR 1 et CHOEUR 2 partaient encore dans le bus DRUMS (reste d'une ancienne config : la spec n'allumait que le bon bus). Les bus 9 à 16 sont maintenant affectés explicitement, on ou off, sur chaque canal : 287 pas sur 287 confirmés. Relecture des bus 9, 11, 13, 15 et 16 : chaque bus ne reçoit que son groupe. Batterie → 9/10 (et 15 sauf OH), basse, guitares et synthé → 11/12, voix → 13/14. Main L/R off sur les 15 canaux. Départs FX : voix → A et B, caisse claire et toms → C, kick jamais ; niveaux à −∞, à doser à l'oreille.
- **EQ des retours d'effet** (Standard, constaté sur les 4 retours). FX A : plateau grave mis à 300 Hz et 0 dB (il restait 201 Hz à −8,2 dB d'une autre config ; la profondeur se règle à l'oreille, 5.2), Low-Mid 1 kHz −2 dB, Hi-Mid remis à 0 dB, plateau aigu 8 kHz −2 dB. Q laissés à 0,6, le guide ne les chiffre pas. FX C : bande basse passée en plateau, gain 0 dB, à régler à l'oreille (5.4). B et D restent à plat : leurs coupures sont conditionnelles (« si ça siffle encore », « si nécessaire »).
- **Paramètres internes des effets** : maintenant acceptés, une clé à la fois après la stabilisation des types. FX A LPF 8 kHz ; FX B feedback L/R 0,4, LPF 6 kHz, HPF 200 Hz, Fb LPF L/R 5 kHz ; FX C LPF 7 kHz ; FX D feedback 0,3, LPF 5 kHz, HPF 300 Hz, Fb LPF 4 kHz. 12 sur 12 confirmés à la relecture. L'échec précédent suivait de près le changement de type et le plantage du serveur : cause exacte non établie.
- **Passive EQ du Main** : Low Frequency 60 confirmé.

## Troisième passe (13 h 28 à 13 h 41) : 16R en stagebox, contrôle complet

- **Sources d'entrée.** État trouvé : mélange Analog / USB / Network (OH L, OH R et CHOEUR 1 sur USB, CHOEUR 2 en Network). Les canaux 1 à 15 sont passés en **Network** (`line.chN.inputsrc`, brut 1/3). Patch AVB par canal (`line.chN.avb_src`, entier de −1 à 63, brut (v+1)/64) : déjà N → N, sauf le **canal 3, qui recevait l'entrée AVB 2** (la caisse claire), corrigé. 16 sur 16 confirmés. Horloge AVB : Sync. La 16R est en mode Stagebox.
- **Préamplis de la 16R : non pilotés.** Écrire `line.chN.preampgain` et `line.chN.48v` directement sur la 16R (RA1E18040123) est refusé, rien n'est pris (`stageboxsetup.preamp_lock` = on sur la 16R). Écrire le gain sur la 32SC, canal en Network, est refusé aussi : le canal 2 reste à 0 dB. Le 48 V n'est donc pas envoyé. Il est prévu sur les entrées 1 (BD 500 Beta), 3-4 (Lewitt LCT 040) et 8 (DI active), d'après le guide 1.5 et 3.3. Le chemin reste à identifier par un geste dans UC Surface.
- **Bus 15 PARALLEL** : fader à −∞ (guide 4.4, « −∞ par défaut », à monter de 1 dB en 1 dB, plafond −12 à −6 dB ; la spec disait −10 dB, à tort, corrigé), master démuté.
- **Contrôle complet** (`audit.mjs` : valeur brute visée de chaque clé écrite aujourd'hui, comparée à la relecture) : 702 clés, 683 conformes. Écarts : 14 gains et 4 phantom (préamplis 16R ci-dessus), et le couplage OH L/R, trouvé défait après le changement de source puis rétabli. Une deuxième connexion le lit encore à off alors que la session principale le lit à on : à vérifier dans UC Surface.

## Non appliqué, à comprendre

- Master du bus 16 DIVERS : muté, bus inutilisé sur ce preset.
- Feedback des delays : la console l'expose sur 0 à 1 ; 0,4 pour « 40 % » suppose une échelle linéaire, à vérifier à l'écran d'UC Surface.

## Écarts entre le guide et les plages des modèles (catalogue UC Surface 5.1)

- **Class-A FET** : Attack de 0,021 à 0,8 ms, Release de 50 ms à 1,1 s. Les « Attack 3 ms » et « 5 ms » du guide (3.2 caisse claire, guitare rythmique) sont hors plage ; les Release de 150 et 250 ms sont dans la plage. Ligne « Plages du Class-A FET » du registre 8.7.
- **RC-500 EQ** : Mid de 400 à 7 500 Hz. Le « Mid vers 250 Hz, −2 dB » du Bus Parallel (4.4) est hors plage.
- **Alpine EQ-550** : crans de gain à ±2 dB autour de 0 (−2, 0, +2) ; le « High +1 dB » du Bus Instru (4.2) n'existe pas. Crans de fréquence relevés : low 50/100/200/300/400 Hz, mid 0,4/0,8/1,5/3/5 kHz, high 5/7/10/12,5/15 kHz (cinq crans, pas sept).
- **Solar 69** : mid 0,7/1/1,4/2/2,8/3,5/4,5/6 kHz (le « 800 Hz » du 4.1 tombe sur 0,7 kHz) ; aigu fixe à 10 kHz (`10kGain`, crans de 2 dB), contrairement au « fréquence réglable » du 4.1.
- **Brit Comp** : Release cranté 0,1 / 0,3 / 0,6 / 1,2 s / auto, ce qui confirme l'inférence du 4.1.
- **Passive EQ** : Boost et Atten gradués de 0 à 10 (sans unité), pas en dB : le « +1 dB » du 5.1 n'a pas de correspondance directe.

## Encore à régler à la main ou par étalonnage

Seuils Brit (−15 dB) et makeup (+2), seuil FC-670 et Input Gain (au mètre), Tube CB attack/release/ratio/seuil, Comp 160 seuil et compression (au mètre), Everest gain (au mètre), Passive boosts, mode Peak du Solar, FET attack/release, temps des delays (TAP), predelay/reflection/size des reverbs, niveaux des départs FX, plateaux graves des retours A et C.

## Quatrième passe (17 h 50 à 18 h 20) : préamplis de la 16R, plantages du serveur

- **Permissions durables.** Le serveur se présentait à chaque connexion sous un nouvel identifiant (horodaté) : la console le voyait comme un nouveau client et ses droits se perdaient. Corrigé (commit 40edd3d) : identifiant fixe `presonus-mcp-server-<numéro de série>`. Louis lui a donné FOH et Préamplis dans les permissions de l'unité. Erreur de Claude, plus tôt dans la journée : un clic dans UC Surface a touché la case Préamplis du client « AUKA: PC » au lieu de celle du serveur ; Louis a repris la main.
- **Plantages du serveur (trois dans la journée).** Cause trouvée par reproduction : la bibliothèque PreSonus découpait mal les paquets TCP et levait une exception non rattrapée quand un en-tête arrivait coupé en deux (« Header not matching and remaining is zero »). Elle écrivait aussi sur la sortie standard, réservée au dialogue avec Claude Code. Corrigé (commit 8234594 : découpage robuste, sorties parasites redirigées, journal des plantages) ; plus de plantage ensuite.
- **Préamplis de la 16R pilotés depuis la 32SC.** Canal de la 32SC en source Network : le gain et le 48 V écrits sur le canal de la 32SC arrivent sur la 16R (relu sur la 16R). Gains de la spec envoyés, 19 sur 19 confirmés (mutes de sécurité compris). 48 V sur 1, 3, 4 et 8, canaux mutés : 4 sur 4, relu sur la 16R après relecture complète (la première lecture de la 16R était périmée : le serveur ne reçoit pas ses mises à jour en continu, la 16R lui donne la permission de mixage « None » et coupe la liaison toutes les 30 s environ).
- **Ordre EQ → comp** (`swapcompeq`) : non encore réglé sur les canaux ; à faire, test sur un canal d'abord.

## Limites constatées de l'outil (à corriger)

- Retours : le preset n'a pas configuré les FlexMix 1 à 6 (noms et départs d'une ancienne config : « Retours scène », « Dj », « Retour Robot », « Matt »). Le plan de preset ne sait pas encore écrire les mix de retour, leurs GEQ, ni le patch des sorties de la 16R.
- `get_aux_mix` mélange les canaux, les entrées Aux, le talkback et les retours d'effet sous les mêmes numéros ; pré/post toujours « unknown ».
- `get_monitor_mix_layout` voit tous les bus en mono et infère des paires absurdes (1-2, 2-3, 3-4…).
- GEQ : correspondance entre GEQ et mix non documentée (valeur brute seulement). GEQ 3, 4 et 6 portent des coupes d'une ancienne config.
- Pas d'outil pour enregistrer une scène ou un projet sur la console : le preset écrit aujourd'hui n'est sauvegardé nulle part (scène chargée : « 12.Base / 01.Base groupes »). À enregistrer à la main dans UC Surface.
- Détecteur de larsen : `PRESONUS_USB_DEVICE` absent de `.mcp.json`, l'analyseur ne tourne pas.
- Fichier de spec : fader du bus 15 encore à −10 dB (doit être −∞).
