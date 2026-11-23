# Audit du code et de la méthode par Claude (2026-11-23)

Périmètre : serveur `code/studiolive-mix-assistant` (copie locale, commit annoncé d76fb52), `CLAUDE.md`, skills et flux de publication. Le guide n'est pas relu ici : quatre audits l'ont déjà traité aujourd'hui.

Rappel de l'objectif (`CLAUDE.md`) : un rendu professionnel et musical de haut niveau, sans aucune approximation. Le serveur sert à préparer les concerts (lecture, plans validés par Louis), pas à mixer en direct.

## État vérifié

- Build `tsc --build` : OK. Tests : 48 fichiers, **872 tests passés** (23/11).
- Sans `PRESONUS_WRITE`, aucun outil d'écriture n'est enregistré, et un test le vérifie. Le `.mcp.json` actuel est en lecture seule.
- Le plan de preset est bien verrouillé : clés limitées à `line.ch1–32`, démute refusé, faders seulement à 0 dB, phantom séparé, valeurs bornées à [0, 1].

## Code : constats

| # | Gravité | Constat | Preuve | Correction proposée |
|---|---|---|---|---|
| C-01 | **Important** | `apply_preset_plan` annonce « s'arrête si un mute échoue », mais il ne vérifie pas que les mutes ont pris avant d'écrire les réglages. `applyChange` ne fait qu'envoyer le paquet, donc un mute perdu (réseau, console qui ne renvoie pas d'écho) ne bloque rien. Gain, EQ et HPF sont alors écrits sur un canal ouvert. | `client-manager.ts` l. 531–569 (envoi sans attente d'écho) ; `tools.ts` l. 2179–2191 (l'arrêt ne se produit que sur exception). | Après la phase mute : attendre, relire l'état et refuser la suite si un seul canal n'est pas muté. Ajouter le test correspondant. |
| C-02 | **Important** | `recall_console_preset` contourne le modèle de catégories. Un rappel de projet ou de scène peut changer le master et démuter, avec une simple note libre, sans `allow` et sans vérifier que le fichier existe. | `tools.ts` l. 2063–2085. | Exiger `allow` avec `master` et `unmute` pour un projet ou une scène, et vérifier le nom dans `listConsolePresets` avant l'envoi. |
| C-03 | Moyen | Dans `prepare_settings_plan`, le modèle de comp ou d'EQ est lu sur la console au moment de la préparation. Un plan qui change de modèle (ex. Comp160) et règle ses paramètres en même temps les code pour l'**ancien** modèle, sauf si l'appelant donne `paramList`. Les étapes partent aussi dans l'ordre fourni, sans mettre le changement de modèle en premier. | `tools.ts` l. 1817–1840 ; `ucnet-catalog.ts` l. 147–228 (`modelSource: 'console_state'`). | Si le plan contient un `modelSwitch`, résoudre les paramètres du composant avec le nouveau modèle, ou refuser sans `paramList`. Trier les changements de modèle en tête. |
| C-04 | Moyen | Pas de contrôle de fraîcheur à l'application. Un plan reste valable 30 min, et si Louis a touché la console entre-temps, l'application écrase son geste sans le signaler. | `PRESET_PLAN_TTL_MS`, `apply_settings_plan` l. 2100–2124. | À l'application, comparer les valeurs actuelles à celles de la préparation et signaler (ou refuser) ce qui a bougé. |
| C-05 | Mineur | Le journal d'audit des écritures ne va que sur stderr : il n'est pas conservé. | `tools.ts` l. 2079, 2138, 2207. | Ajouter une ligne JSON dans un fichier (`Regie-Auka/logs/ecritures.jsonl`). |
| C-06 | Mineur | Le dossier `code/studiolive-mix-assistant` n'est pas un dépôt git, et il est exclu de GitHub. Le commit d76fb52 cité dans VERSION.md n'est donc pas vérifiable sur place. `CLAUDE.md` impose `git init` avant toute modification. | `Test-Path .git` → False. | Faire le `git init` + commit « base » maintenant, avant la première correction. |

Rien n'a été modifié dans le code.

## Méthode : constats

| # | Constat | Proposition |
|---|---|---|
| M-01 | **La validation passe par un texte écrit par l'IA.** `confirmationNote` est rédigé par Claude, donc le code ne peut pas prouver l'accord de Louis. La vraie barrière, c'est la demande d'autorisation de Claude Code. Or aucun fichier `.claude/settings.json` n'existe dans `Regie-Auka` : en mode automatique ou après un « toujours autoriser », les outils d'écriture passeraient sans question. | Créer `Regie-Auka/.claude/settings.json` avec des règles `ask` sur `mcp__studiolive__apply_settings_plan`, `apply_preset_plan` et `recall_console_preset`, pour que la demande d'autorisation apparaisse toujours. |
| M-02 | **Les audits sur papier ne trouvent plus rien.** Quatre audits ont eu lieu aujourd'hui, et le dernier n'a trouvé aucune erreur dans le guide. Le skill `maj-guide-mixage` prévoit d'arrêter dans ce cas. Le registre 8.7, lui, n'a jamais été exécuté. | Figer le guide en V38. L'effort suivant porte sur la console. |
| M-03 | **Certaines lignes du registre peuvent être avancées sans la console.** Le catalogue UC Surface du serveur (définitions du logiciel, pas une observation) montre ceci : les retours FX (`fxreturn.ch1–4`) ont comp et EQ, mais **ni limiteur, ni gate, ni HPF** ; le Key Source (`gatekeysrc`, `compkeysrc`) n'existe que sur `line.ch1–32` et talkback. Cela confirme le « canaux d'entrée uniquement » du guide (2.5) et répond par avance à la question du retour « approches par style » sur les retours FX. | Ajouter cette preuve « catalogue, à confirmer à l'écran » dans les lignes du registre concernées, puis les solder en 30 s sur la console. |
| M-04 | **L'objectif musical est en retard sur la cohérence documentaire.** La journée a servi à la cohérence du guide. Le seul apport musical nouveau, le retour « approches par style » (38 Ko), attend toujours son tri. | Prochaine séance de travail sur le guide : trier ce retour avec Louis, scène par scène (6.1 à 6.9). |
| M-05 | **Quatre copies de la régie : Drive, local, GitHub et projet « Mix Live ».** Elles se synchronisent à la main, sur la foi de VERSION.md et du JOURNAL. Le projet « Mix Live » n'a peut-être pas encore récupéré les V36 à V38 publiées depuis la régie, et je ne peux pas le vérifier d'ici. | À la prochaine ouverture de « Mix Live », lancer l'étape 0 de `maj-guide-mixage` (synchro depuis le Drive) avant toute modification. |
| M-06 | **Le registre est fermé aux trouvailles du serveur.** Le serveur connaît des faits (catalogue, niveaux de confiance) que le guide ignore, et aucun chemin n'existe pour les y faire entrer, sauf à la main comme en M-03. | Plus tard : un outil en lecture seule qui sort, pour chaque ligne du registre, ce que le catalogue en dit. |

## Suite donnée le 23/11 (validée par Louis : « Oui fais tout ça »)

Code : dépôt git local créé (`abb34b3` base, `45acb52` corrections). Build, typecheck et **887 tests** passent, dont 15 nouveaux.

- **C-01 corrigé.** `apply_preset_plan` envoie les mutes, puis attend (jusqu'à `settleMs`) que l'état lu sur la console les montre tous. S'il en manque un seul, il s'arrête et rien d'autre ne part. Tests : aucun écho, un seul canal manquant, écho tardif.
- **C-02 corrigé.** Un rappel de projet ou de scène est refusé sans `allow` contenant `master`, `unmute`, `phantom` et `patch`, et tout fichier absent de `list_console_presets` est refusé, de même quand la liste est illisible. **Reste à confirmer console branchée :** que les noms renvoyés par la console sont bien ceux qu'on passe au rappel. Sinon, le contrôle refusera tout rappel. Ce défaut est sûr, mais il bloque. Pour un preset de tranche, je n'exige aucune catégorie de plus. Je ne sais pas s'il peut toucher le phantom ou le gain, et c'est à vérifier.
- **C-07, nouveau, trouvé pendant l'audit approfondi, corrigé.** `prepare_mute_change_set` + `apply_change_set` démutait n'importe quel canal, Main compris, avec une simple note. `apply_change_set` applique maintenant les mêmes catégories que `apply_settings_plan`, et le dry-run les affiche. Renommage, Sub et assignation Aux restent des écritures normales, comme dans `prepare_settings_plan`.
- **C-06 fait** (dépôt git). **M-01 fait** : `Regie-Auka/.claude/settings.json` (demande d'autorisation sur les 4 outils d'écriture), signalé dans `CLAUDE.md`.
- **Toujours ouverts :** C-03 (changement de modèle dans un plan), C-04 (fraîcheur du plan), C-05 (journal d'écriture sur fichier), M-02 à M-06.
- Les tests utilisent une console simulée. Aucune de ces corrections n'a encore tourné sur la vraie 32SC.

## Ordre proposé

1. M-01 (fichier de permissions) et C-06 (`git init`) : sans risque, quelques minutes.
2. C-01 et C-02, avec leurs tests, avant toute première écriture réelle sur la console.
3. C-03 et C-04 avant d'utiliser `prepare_settings_plan` pour des changements de modèle.
4. Séance console seule : registre 8.7 (M-03 en premier), PRESONUS_SERIAL, nom USB, canaux ASIO.
5. Tri du retour « approches par style » → V39.
