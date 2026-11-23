# Tri de l'audit Gemini du Drive Regie-Auka (2026-11-23, sur la V38)

Version relue par l'auditeur : le Drive après la publication V38 (commit 5aa69b4).
Tri fait par Claude le 2026-11-23. Chaque fait a été vérifié dans le manuel 32SC, dans le guide V38 et sur le Drive.

L'audit ne trouve aucune erreur dans le guide. Il signale surtout du travail déjà connu et trois points de rangement du Drive.

| # | Remarque | Verdict | Pourquoi |
|---|---|---|---|
| G-01 | Le retour « approches par style » n'est pas intégré au guide | **Retenu (déjà ouvert)** | C'est voulu : le retour attend son tri avec Louis. J'ai vérifié ses trois faits de manuel. (1) Les touches User Function n'existent pas sur la 32SC : le manuel le dit p. 108 (« n'est pas disponible sur les StudioLive 32SC et StudioLive 16 »), et le guide ne les mentionne nulle part. (2) Tap Assign : la touche TAP ne pilote qu'un delay à la fois (manuel 9.1, p. 79), ce que le guide dit déjà (paragraphe « Tap Assign », ligne 1655 de la V38). (3) Pas de phaser ni de pitch shifter : le manuel ne cite aucun des deux, et le guide n'en propose aucun dans le rack. Aucun de ces trois faits ne contredit la V38. Ils entreront en V39 avec le reste du retour. |
| G-02 | Registre 8.7 jamais soldé, tests de la chaîne PC–32SC à faire console branchée | **Retenu (limite connue)** | Seule une séance console peut solder ces lignes : PRESONUS_SERIAL, nom USB, nombre de canaux ASIO, cohabitation avec Studio Pro, latence de Pro-R v1. |
| G-03 | Le registre s'appelle encore V36 | **Retenu en partie** | Ce nom est voulu, car son contenu n'a pas bougé depuis la V36. Le README le dit maintenant, pour éviter qu'on le croie périmé. |
| G-04 | Document « Audit complet — Régie Auka » (V35) à la racine de Mon Drive | **Retenu** | Il existe bien (créé le 23/11 à 1 h 25). Il est hors du dossier Regie-Auka et dépassé. Il ira à la corbeille si Louis le valide. |
| G-05 | Pas de dossier `audits/` sur le Drive | **Retenu** | C'est exact : les tris d'audit ne sont que sur GitHub et en local, alors que le JOURNAL y renvoie. Proposition : créer `audits/` sur le Drive avec les tris, sans `outils/`. |
| G-06 | `StudioLive_III_Audio_Interface_Mode_WDM_Guide.pdf` absent de `manuels/` | **Retenu** | Le PDF est sur le Drive sous son nom d'origine (`OM_2779200201_…pdf`), mais dans « Fichiers son », pas dans `Regie-Auka/manuels`. La copie locale existe. Proposition : le copier dans `manuels/`. |

Hors périmètre : le document « Audit complet — calage-sono » relève de l'autre discussion.
