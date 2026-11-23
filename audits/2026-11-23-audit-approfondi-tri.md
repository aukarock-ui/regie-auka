# Tri de l'« Audit approfondi » du 2026-11-23 (sur la V36)

Version relue par l'auditeur : arbre 8889f9b (guide V36), sans les manuels.
Tri fait par Claude le 2026-11-23 : chaque point a été relu dans le guide, le contexte et le retour PC, et les logiciels ont été vérifiés directement sur le PC de régie (dossier VST3).

Bilan : 10 remarques. 6 sont retenues, 2 retenues en partie, 1 rejetée et 1 concerne une limite déjà connue. Deux des erreurs retenues (A-01 et A-04) sont **de mon fait**, introduites ou laissées en V36.

| # | Remarque | Verdict | Pourquoi |
|---|---|---|---|
| A-01 | 0.2 conclut « 8 microphones personnels » | **Retenu** | Exact. La V36 avait corrigé 0.7 sans propager en 0.2 : ma recherche portait sur « 8 micros » et pas sur « 8 microphones ». Corrigé en V37. |
| A-02 | 13 canaux en 0.7 alors que le calcul en donne 12 | **Rejeté sur le fond, retenu pour la clarté** | L'audit suppose que la DI passive et la Palmer ne servent pas ensemble. 0.5 dit le contraire : « clavier stéréo plus basse plus une source ligne mono tiennent maintenant sans emprunt ». 4 + 1 + 1 + 1 + 2 + 4 = 13. Le calcul est maintenant écrit dans le texte. |
| A-03 | Patch rock/punk « 4 musiciens » avec 4 micros voix | **Retenu en partie** | Ce ne sont pas 7 personnes : 4 micros voix pour 4 musiciens, c'est un micro par musicien. La V37 le dit explicitement. |
| A-04 | Pas de changelog V35 → V36 dans l'historique | **Retenu** | Le bloc existait, mais un caractère invisible (BOM) collé devant « ### » l'empêchait de s'afficher comme titre. Erreur de mon script. Corrigé en V37, avec un contrôle qui refuse tout BOM. |
| A-05 | Retours musicaux non intégrés | **Retenu (déjà prévu)** | C'est voulu : le retour est « hors guide, à valider à l'oreille ». Sa file de décisions reste à faire avec Louis. |
| A-06 | Pas d'index des preuves | **Retenu (déjà ouvert)** | Déjà inscrit dans le bilan V36. `PREUVES.md` reste à construire. |
| A-07 | Registre 8.7 jamais soldé | **Retenu (limite connue)** | Le guide le dit lui-même. Seuls des tests sur la console pourront solder ces lignes. |
| A-08 | Contexte PC périmé (Studio One, Live 12, Pro-R 2, Valhalla, Decapitator, SuperPlate) | **Retenu** | Vérifié sur le PC. Mis à jour dans `contexte/parc-et-systeme.md` et `contexte/console-verifiee.md`, et en 7.10 du guide (V37). En plus de l'audit, il y a des plug-ins installés que le contexte ne mentionnait pas : Pro-DS, Pro-L 2, Pro-G, Timeless 3, R2. |
| A-09 | `skills.zip` absent du dépôt | **Retenu** | Le README précise maintenant que l'archive est sur le Drive et pas sur GitHub. |
| A-10 | Affirmations constructeur non certifiables sans manuels | **Limite connue** | La remarque est juste, mais ce n'est pas une erreur du guide. L'index des preuves (A-06) y répondra. |

## Avis
C'est un bon audit de cohérence. Les deux erreurs certaines qu'il trouve, A-01 et A-04, viennent de la publication V36 elle-même. La leçon pour les prochaines versions : chercher toutes les formes d'une valeur avant de dire qu'elle est propagée, et refuser tout BOM dans les fichiers produits par script.
