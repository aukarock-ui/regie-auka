# Tri de l'audit externe du 2026-11-23 (« Audit technique approfondi »)

Version relue par l'auditeur : commit 2db60ea (guide V35).
Périmètre annoncé : revue statique du dépôt. L'auditeur n'avait pas les manuels.
Tri fait par Claude le 2026-11-23, en relisant chaque passage cité dans `guide/Guide_Mixage_Live_V35.md` et `retours/`.
Rien n'est encore corrigé dans le guide. Les corrections passent par Louis, puis par le skill maj-guide-mixage.

Bilan : 12 remarques. 5 sont retenues, 4 retenues en partie et 3 rejetées.

| # | Remarque | Section | Verdict | Pourquoi |
|---|---|---|---|---|
| 1 | Le parc compte 9 micros, pas 8 | 0.2, 0.7 | **Retenu** | Les comptes de 0.2 donnent 1 + 1 + 2 + 1 + 2 + 2 = 9. Pourtant, 0.7 écrit « Avec les 8 micros personnels » (ligne 390). |
| 2 | 13 canaux annoncés alors que le décompte en donne 12 | 0.7 | **Rejeté** | L'auditeur a sauté la ligne « Clavier mono ou source ligne — DI passive, 1 canal ». Le compte est 4 + 1 + 1 + 1 + 2 + 4 = 13, donc le total est juste. |
| 3 | Les seuils de sommation (4 dB, 10 dB) sont trop optimistes | 2.9 | **Retenu en partie** | Le calcul se refait facilement. À 4 dB d'écart, le haut du peigne monte à +4,3 dB et le creux descend à −8,7 dB. L'écart crête-creux vaut 12,9 dB, soit environ ±6,5 dB autour du milieu, ce qui rend « ±6 dB » défendable à condition de dire de quelle référence on parle. À 10 dB, on obtient +2,4 dB et −3,3 dB, soit 5,7 dB crête-creux : on ne peut pas appeler ça « négligeable ». Il faut corriger le mot « négligeable » et la phrase « à 10 dB d'écart, l'interaction ne mérite plus qu'on s'en occupe ». Il faut aussi préciser la référence de l'ondulation. |
| 4 | Contradiction entre « ±3 dB maximum » et « Larsen −3 à −6 dB » | 7.3 | **Retenu** | Le tableau autorise −6 dB alors que la règle d'or en limite l'exception au seul boost de +1 dB. Il faut soit nommer une deuxième exception (l'encoche larsen, en disant d'où vient la valeur), soit ramener la ligne à −3 dB. |
| 5 | Le montage USB n'est pas « mécaniquement » protégé de toute boucle | 7.10 | **Retenu en partie** | Le sélecteur exclusif de source empêche bien la boucle sur un même canal, et le raisonnement du guide est juste là-dessus. En revanche, il ne couvre pas une erreur dans le logiciel hôte (monitoring d'entrée, sortie renvoyée sur le mauvais canal USB) ni un départ USB du canal B. La phrase « rend la boucle structurellement impossible » est trop forte. Il vaut mieux écrire « empêche la boucle sur un même canal », puis ajouter au registre 8.7 un premier essai à bas niveau avec le routage hôte vérifié. |
| 6 | La justification du release à 150 ms du limiteur est trop simplifiée | 2.4 | **Rejeté** | Le guide décrit bien la courbe de réduction de gain : quand elle est trop rapide, elle suit la période et module le signal, ce qui produit de la distorsion harmonique. C'est l'explication habituelle. L'auditeur ne propose ni source contraire ni erreur précise. |
| 7 | Le diagnostic de distorsion du BD 500 est trop catégorique | 3.1 kick | **Retenu en partie** | « À gain modéré, une distorsion vient du micro lui-même » est trop affirmatif. Le geste proposé (reculer le micro) reste bon. Il suffit de transformer la phrase en hypothèse à vérifier : reculer le micro, puis changer de câble ou de micro. Gravité : mineure. |
| 8 | McCarthy est cité sans pages | 2.9 | **Retenu** | Le livre est nommé, mais ni l'édition ni les pages ne sont données, et les valeurs de McCarthy ne sont pas séparées des calculs propres au guide. Le projet exige ce niveau de précision ailleurs. |
| 9 | Les manuels sont absents du dépôt | 1.x, 2.x, 7.x, 8 | **Retenu en partie** | Leur absence est voulue (droits d'auteur), et AUDIT.md l'indique. L'idée d'un index des preuves (manuel, version, page, citation courte) est en revanche utile pour rendre les audits reproductibles. |
| 10 | La source techno live est jugée « Suffisant ? Oui » | retour approches par style | **Rejeté** | C'est inexact. La ligne 258 du retour dit au contraire : « Deux sources, aucune de techno au sens strict ». |
| 11 | Les attributions doivent pouvoir s'auditer phrase par phrase (Pooch) | retour approches par style | **Retenu** | Chaque source a son lien, mais pas le passage précis qui soutient les gestes chiffrés (par exemple les 3 à 6 dB de Pooch sur le Main). Ce passage est à ajouter avant l'intégration au guide. |
| 12 | Le registre 8.7 est daté du 10 novembre | 8.7 | **Retenu** | C'est mineur. Le 23/11, aucun test n'a non plus été fait (retour PC), mais la date de dernière revue mérite d'être mise à jour lors de la prochaine version. |

## À corriger dans la prochaine version du guide (proposition à valider par Louis)
1. 0.7 : remplacer « 8 micros » par « 9 micros ».
2. 2.9 : réécrire la zone Isolation et la phrase qui suit le tableau à partir du calcul ci-dessus, et ajouter l'édition et les pages de McCarthy.
3. 7.3 : rendre la règle d'or cohérente avec la ligne Larsen.
4. 7.10 : remplacer « structurellement impossible » par une formulation limitée au même canal, et ajouter au registre 8.7 un essai à bas niveau du routage dans le logiciel hôte.
5. 3.1 kick : formuler la cause de la distorsion comme une hypothèse.
6. 8.7 : mettre à jour la date de dernière revue.

## Avis général
L'audit est sérieux et honnête sur ses limites. Ses trois meilleurs apports sont l'erreur de comptage des micros, la contradiction de 7.3 et le calcul de 2.9. Deux de ses remarques reposent sur une lecture incomplète (les 13 canaux, la source techno). Aucune citation de manuel n'a été inventée, puisque l'auditeur n'en cite aucune.
