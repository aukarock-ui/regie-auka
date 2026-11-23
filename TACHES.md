# Tâches de la régie

Tableau de bord partagé entre les sessions. Une session lit ce fichier en arrivant, prend **un** chantier, et le met à jour en partant. Ce qui est fait part dans `JOURNAL.md` et sort d'ici. Modifier seulement la ligne du chantier concerné (plusieurs sessions écrivent ce fichier).

État : `à faire`, `en cours (date)`, `attend Louis`, `attend la console`.

## Chantiers

| # | Chantier | État | Qui | Prochain geste |
|---|---|---|---|---|
| 1 | **Séance console seule** (console branchée) : PRESONUS_SERIAL, nom USB et `PRESONUS_USB_DEVICE`, canaux ASIO vus, cohabitation avec Studio Pro, latence Pro-R v1 (clap-test) | attend la console | session principale + Louis | Voir « Séance console » ci-dessous |
| 2 | **Registre 8.7** : solder les lignes, en commençant par celles que le catalogue éclaire déjà (retours FX sans limiteur, gate ni HPF ; Key Source sur les entrées seulement) | attend la console | session principale + Louis ; `verif-manuel` pour préparer les preuves | Préparer la liste des gestes, puis les faire pendant la séance 1 |
| 3 | **Premier essai d'écriture réelle** du serveur, avec `PRESONUS_WRITE=1` : un seul canal, plan de preset, contrôle dans Universal Control. Vérifier aussi que les noms de `list_console_presets` sont acceptés par `recall_console_preset` | attend la console | session principale + Louis | Après la séance 1 |
| 4 | **V39 du guide** : trier avec Louis `retours/2026-11-23_approches-par-style.md`, scène par scène (6.1 à 6.9), avec ses trois faits de manuel déjà vérifiés | attend Louis | nouvelle session, skill `maj-guide-mixage` ; `verif-manuel` pour les sources ; `relecteur` avant publication | Ouvrir une session dédiée |
| 5 | **`PREUVES.md`** : index des affirmations du guide et de leur source | à faire | nouvelle session ; `verif-manuel` en lots | Après la V39 |
| 6 | **Projet claude.ai « Mix Live »** : récupérer V36 à V38, les skills modifiés et ce journal (étape 0 de `maj-guide-mixage`) | attend Louis | Louis, dans claude.ai | Recopier les skills modifiés (voir `skills/LISEZMOI.md`) |
| 7 | Méthode : un outil du serveur qui sort, pour chaque ligne du registre 8.7, ce que le catalogue en dit (M-06) | à faire | `dev-serveur` | Après la séance 1 |

## Séance console (chantier 1), dans l'ordre

1. Console et PC sur le même réseau, USB branché. Relancer Claude Code dans `Regie-Auka`.
2. `discover_mixers` → noter IP et numéro de série ; les mettre dans `.mcp.json` (`PRESONUS_SERIAL`).
3. `python code\studiolive-mix-assistant\tools\detecteur-larsen\usb_spectra.py --list` → nom du périphérique → `PRESONUS_USB_DEVICE` dans `.mcp.json` ; compter les canaux ASIO vus (32 attendus).
4. Relancer, `get_feedback_alerts` : l'analyseur doit tourner.
5. Lecture seule : `refresh_mixer_state`, `get_geq_overview`, `list_console_presets` (noter le format exact des noms).
6. Registre 8.7 : les gestes préparés au chantier 2.
7. Studio Pro en enregistrement ASIO en même temps que l'analyseur : conflit ou pas.
8. Consigner tout dans `retours/AAAA-MM-JJ_seance-console.md` (et le Drive).
