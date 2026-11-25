---
name: "charger-preset-console"
description: "Charger sur la StudioLive 32SC, par le serveur MCP studiolive, un preset complet tiré d'une fiche technique et d'un style : patch et ordre des canaux, couleurs, Fat Channel de chaque canal, bus 9-16, master, FX A-D, retours d'effet, vue. Chaque valeur vient du guide."
---

# Charger un preset complet sur la console

À utiliser quand Louis donne une fiche technique (ou une liste d'instruments) et un style, et demande de préparer la console. Les règles de fond (zéro approximation, écriture seulement après son OK, démute seulement avec `unmute` nommé par Louis, phantom sur ordre explicite) viennent de `CLAUDE.md`. Ce skill fixe la méthode. Le format de la spec est décrit dans `code/studiolive-mix-assistant/docs/preset-plan.md`.

## 1. Lire avant de décider

1. Lire la fiche technique en entier, puis le style. S'il manque une information qui change un réglage (micro, DI, clavier mono ou stéréo, nombre de voix), poser **une** question.
2. Dans le guide, lire **seulement** les sections utiles (chercher, puis lire la section) :
   - BLOC ASSISTANT (contenu d'un preset complet, règle de priorité) ;
   - Partie 3, une fois par source ;
   - Partie 4 (bus) ;
   - 5.1 (master) ;
   - 5.2 à 5.5 (FX) ;
   - la scène du style en Partie 6 ;
   - 5.6 si l'événement est en extérieur ;
   - Annexe B (patch type).
3. Lire la console : `refresh_mixer_state`, `get_routing_graph` (sortie à analyser hors contexte), modèles chargés.

## 2. Construire le patch

- **Ordre voulu par Louis :**
  1. batterie (kick, caisse claire, overheads, toms) ;
  2. basse ;
  3. guitares ;
  4. autres instruments (claviers, synthé, cuivres, machines) ;
  5. voix, en commençant par le lead, puis les chœurs.
- Les paires stéréo (overheads, clavier stéréo, DJ) vont sur des canaux impair-pair.
- Annoncer à Louis les écarts à l'Annexe B. Sa consigne prime.
- **Couleurs, une par bus** (préférence de Louis, hors guide). Les canaux prennent la couleur de leur bus, et les retours d'effet sont en violet.

  | Bus | Couleur |
  |---|---|
  | Drums | rouge |
  | Parallel | orange |
  | Instru | bleu |
  | Voix | jaune |
  | Divers | gris |

## 3. Construire la spec complète, chaque valeur citée

Règle de priorité du guide : Partie 2 < Parties 3, 4 et 5 < 3.2 (emprunt) < Partie 6 (scène) < 5.6 et 7.3 < fiche du jour et consignes de Louis.

**Canaux (Partie 3)**, dans l'ordre de la fiche :
1. micro et phantom (prévu, mais envoyé seulement sur ordre) ;
2. gain de préampli (bas de la plage du guide) ;
3. HPF ;
4. gate ;
5. compresseur (modèle et paramètres) ;
6. EQ (modèle et bandes) ;
7. ordre EQ/comp (1.6) ;
8. limiteur (2.4) ;
9. pan ;
10. Main **Off** ;
11. envois vers le bus de groupe, et seulement lui ;
12. envois FX (5.2 à 5.5 : jamais de reverb sur le kick) ;
13. nom ;
14. couleur.

**Bus 9-16 (Partie 4 et scène du style) :**
- mode Subgroup, nom, couleur, link des paires, sortie vers le Main ;
- comp → EQ (ordre par défaut des bus) avec les modèles du guide ;
- limiteur (Instru : ON dès qu'une source électronique est sur le bus) ;
- fader : Parallel à −∞ par défaut, ou à la valeur de la scène.

**Master (5.1 et Partie 6) :** Everest C100A, Passive Program EQ, limiteur au seuil du style, release 250-300 ms.

**FX A à D (5.2 à 5.5 et Partie 6) :** type, réglages, affectation des retours (A et B vers Voix, C vers Drums, D vers le Main à −∞), fader des retours.

**Vue :** user layer dans l'ordre du patch, puis les bus (format des chemins lu dans l'état).

**Qualificatifs du guide.** « Modéré », « assez haut » ou « le cran le plus proche » ne deviennent un nombre que si le paramètre est étalonné (`calibrations.json`) ou à crans connus. Sinon, ils vont dans les **gestes manuels**, avec la méthode du guide (5.1bis).

**Trous du guide.** Appliquer « Quand le guide ne couvre pas » (`CLAUDE.md`) : méthode et critère d'écoute, jamais de chiffre inventé.

## 4. Préparer et présenter

- `prepare_preset_plan` n'envoie rien. Présenter à Louis :
  - ce qui sera écrit, section par section ;
  - les catégories requises (`modelSwitch`, `patch`, `busMaster`, `master`, `unmute`, `forced`, `unknown`) ;
  - les démutes et faders demandés (canaux, bus, Main) : ils ne partent qu'avec `unmute` (et `master` pour le Main), en dernière phase, après confirmation de tout le reste ;
  - les pas de la section `extra` (toute clé de la console, `describe_parameters` pour la trouver), chacun avec sa catégorie ;
  - les gestes manuels (paramètres non étalonnés, type de FX, ordre EQ/comp) ;
  - les écarts au guide.
- Pour `master` et `danger`, faire confirmer nommément.
- Un paramètre `probe_required` important pour le résultat se règle par une séance d'étalonnage (`prepare_calibration`, puis `record_calibration`) plutôt qu'à la main, si Louis est devant UC Surface.

## 5. Appliquer et vérifier

- `apply_preset_plan` avec exactement les catégories que Louis a acceptées. Le serveur :
  - envoie par paquets ;
  - relit toute la console ;
  - renvoie de lui-même ce qui manque.
- Lire le rapport (`confirmedByEcho`, `confirmedOnReread`, `notApplied`). Pour chaque pas `notApplied`, refaire un plan ciblé après `refresh_mixer_state`.
- Faire contrôler par Louis dans UC Surface :
  - couleurs et ordre ;
  - un modèle de bus ;
  - une valeur d'EQ ;
  - le limiteur du master.
- Rappeler ce qui reste à faire : démute (s'il n'a pas été autorisé, ou s'il a été retenu par le serveur), phantom sur ordre, gains au soundcheck (7.1).

## 6. Tracer

- Ce que Louis valide ou corrige à l'écoute va dans un retour de séance, `retours/AAAA-MM-JJ_lieu.md`.
- Un défaut du serveur va dans ce même retour et dans `TACHES.md`.
