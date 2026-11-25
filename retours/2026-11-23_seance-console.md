# Séance console — 23 novembre 2026 (premier test du serveur, lecture seule)

Liaison PC ↔ console en Wi-Fi (pas d'USB). Serveur studiolive-mix-assistant, mode `soundcheck_assist`, écriture désactivée pendant tout le test.

## Identités (observed)

| Machine | Série | IP vue | Firmware |
|---|---|---|---|
| StudioLive 32SC | SD7E24030014 | 10.104.31.89 (vue une fois en 169.254.14.248, link-local) | 3.4.0.111374 |
| StudioLive 16R | RA1E18040123 | 10.104.31.134 | non lu |

- La 16R n'apparaît pas toujours à la première découverte.
- AVB : d'abord `connected: false`, puis `connected: true` en fin de séance. Blocs 17-24 = « 16R CKI:Send 1-8 », 25-32 = « 16R CKI:Send 9-16 ».
- Scène chargée : `12.Base.proj` / `01.Base groupes.scn`. Format exact des noms pour `recall_console_preset` : `NN.Titre.proj`, `NN.Titre.scn`.

## Ce qui marche en lecture

Découverte, état complet, capacités, liste projets/scènes/presets de tranche, Fat Channel (32SC et 16R), sous-groupes, noms des aux, 8 GEQ, sources d'entrée, diagnostic de canal, AVB, catalogue `describe_parameters`. `prepare_settings_plan` à blanc (renommage ch29) : plan valide, catégorie `normal`, confiance `observed`.

## Défauts constatés (à corriger dans le serveur)

1. `get_aux_mix` : envois mal numérotés (Facade, Aux In 1, Talkback, Reverb attribués au « canal 1 »…).
2. `get_monitor_mix_layout` : paires stéréo « inférées » entre tous les aux voisins (1-2, 2-3…), sans signification.
3. `validate_stagebox_routing` dit « pas de stagebox » (confiance `guessed`, écrit pour une 32R) alors que `validate_avb_routing` voit la 16R connectée (`observed`).
4. `validate_output_routing` : sources des sorties connues par index seulement.
5. `PRESONUS_SERIAL` et `PRESONUS_ROLE` ne servent qu'avec `PRESONUS_IP` (index.ts) : sans IP fixe, le rôle reste `UNKNOWN`.
6. Analyseur larsen inactif sans USB ; trames RTA de la console reçues mais non décodées.

## À vérifier dans Universal Control

- Quel GEQ est sur quel mix (le serveur ne le sait pas). GEQ 4 : −12 dB à 3,15 kHz ; GEQ 6 : creusé sur une dizaine de bandes.
- Sources d'entrée de la 32SC (`inferred`) : Stage Box sur 14, 16-19, 25-26 ; USB sur 3 et 13 ; le reste en Local, y compris 20-24 et 27-32 alors que l'AVB y envoie la 16R.

## Tests d'écriture (soir du 23/11)

- Renommage d'un canal : visible dans UC Surface sur la tablette de Louis. L'écriture fonctionne.
- Preset rock alternatif de 15 canaux envoyé (`apply_preset_plan` puis 4 renvois par `apply_settings_plan`). État relu en fin de séance :
  - Main Off sur les canaux 1 à 15 ;
  - envois vers les bus de groupe du guide 1.3 (Drums 9/10 + Parallel 15, Instru 11/12, Voix 13/14) ;
  - HPF, gates, comps, EQ, limiteurs et pan conformes à la spec, sauf sur les canaux dont le modèle n'est pas Standard.
- **Pertes en rafale** : sur un envoi de 100 réglages ou plus, un bloc continu de messages se perd (par exemple le routage des canaux 5 à 10, perdu deux fois). Un paquet de 15 à 35 réglages passe.
- **`notConfirmed` peu fiable** : un paquet de 13 réglages a été annoncé « 0 confirmé » alors que la relecture après `refresh_mixer_state` montrait tout appliqué. Il faut toujours relire avant de renvoyer.
- **Deux lectures qui ne concordent pas** :
  - Gain d'EQ du canal 5 : le planificateur lit −3 dB, `get_fat_channel` lit −2,4 dB.
  - Release du limiteur du canal 5 : le planificateur lit 150 ms, `get_fat_channel` lit 86 ms.
  - L'échelle juste est à lire dans UC Surface.
- Pistes de correction du serveur : envoi par paquets avec pause, fenêtre de confirmation plus longue avec relecture, une seule fonction de conversion des valeurs.

## Suite

Écriture activée dans `.mcp.json` (`PRESONUS_WRITE=1`) à la demande de Louis, avec autorisation demandée avant chaque envoi. Premier essai prévu : renommer le canal 29 de la 32SC, contrôle dans Universal Control (chantier 3).
