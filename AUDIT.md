# Auditer la méthode : mode d'emploi pour un relecteur (humain ou IA)

Tu relis la méthode de mixage live d'un technicien son. Le but est de trouver des erreurs de fait, de raisonnement ou de musicalité, pas de reformuler. Le rendu visé est professionnel et musical : une réponse exacte mais plate, qui laisse de côté une meilleure option documentée, est aussi un défaut à signaler.

## Quoi lire, dans l'ordre

1. `CLAUDE.md` : règles absolues (zéro approximation, distinguer fait vérifié et inférence).
2. `guide/Guide_Mixage_Live_V38.md` : la méthode. Le « Bloc assistant » en tête explique les règles de priorité.
3. `retours/` : propositions pas encore intégrées, en particulier `2026-11-23_approches-par-style.md` (intention musicale et références par style).
4. `contexte/` : parc matériel et comportements console vérifiés.
5. Les manuels cités (StudioLive 32SC/16R parties 1 et 2, addendum Fat Channel, Universal Control) ne sont pas dans le dépôt : demander à Louis un lien vers le dossier Drive `Regie-Auka/manuels`.

## Points où un avis extérieur est le plus utile

- **Les sources des approches par style** (`retours/2026-11-23_approches-par-style.md`) : la source existe-t-elle, et dit-elle bien ce qu'on lui attribue ? Une technique de mix, un ingénieur ou un disque de référence qui manque pour un style ?
- **Les scènes par style** (Partie 6) : l'intention musicale est-elle juste pour le genre ? Les réglages la servent-ils ?
- **Les fiches par source** (Partie 3) et les bus (Partie 4) : cohérence avec le tableau 2.4 (Release du limiteur), la règle du mode Auto (2.1), les plages et crans de la Partie 2, et le tableau 6.1 du manuel (quelle fonction existe sur quel type de canal).
- **Les renvois « voir X.Y »** : disent-ils bien ce qui est annoncé ?
- **Tout chiffre** de réglage ou de spécification qui ne serait pas sourcé.

## Règle de preuve

- Toute remarque qui invoque un manuel cite le passage exact (section, page). Une citation inventée disqualifie la remarque.
- Une valeur proposée a une source. Sans source, propose une méthode et ce qu'il faut entendre, pas un chiffre.
- Une technique attribuée à un ingénieur ou un producteur cite où il l'a dit (livre et page, interview datée, URL).

## Comment laisser tes notes (au choix)

- **Un fichier** : copie `audits/_modele.md` en `audits/AAAA-MM-JJ-<ton-nom-ou-modele-IA>.md`, remplis-le, et propose-le (pull request, ou envoie-le à Louis si tu n'as pas les droits d'écriture).
- **Une issue GitHub** par problème (modèle « Remarque d'audit »).
- **Un commentaire de relecture** sur une pull request, ligne par ligne.

Pour chaque remarque : section du guide et citation exacte, ce qui ne va pas, pourquoi (source, page, calcul), gravité (**bloquant / important / mineur**), type (**incohérence / manque / raisonnement / musical / formulation**), proposition, et « vérifiable sans manuel : oui ou non ». Ne modifie pas le guide toi-même : Louis tranche, puis la correction passe par le projet « Mix Live ».

## Ce qui ne compte pas comme un défaut

- La section `HISTORIQUE — NE PAS CITER` (valeurs volontairement périmées), la table des matières et ce que liste le dernier changelog (sauf si la correction elle-même est fausse).
- Les éléments marqués « à tester » ou listés dans le registre 8.7 : ils attendent un essai sur console. Signale-les seulement si la méthode prévue pour les tester est fausse.
- Les choix de style de Louis (compression forte du Bus Voix en métal, par exemple) : ce sont des décisions, pas des erreurs.

**Points déjà vérifiés : ne pas les signaler de nouveau.**
- La 32SC a 10 sorties FlexMix : 6 XLR et 4 jacks TRS (tableau 3.1.4 du mode d'emploi). Les 4 entrées Aux sont dans le tableau des entrées, pas dans celui des sorties.
- La 32SC n'a pas de sorties physiques de sous-groupe (3.2.2).
- Le guide parle des 32 canaux de mixage, pas du nombre de départs USB.
- Le tableau des Release de 2.4 concerne le limiteur, pas les compresseurs.
- Les retours FX n'ont ni HPF ni gate (tableau 6.1 du mode d'emploi) : pas de ducking ni de filtrage sur un retour FX.
- La Key Source n'existe que sur les canaux d'entrée (6.8.3 / 6.8.4).
- L'ordre par défaut du Fat Channel est Comp > EQ (6.8.4) ; le guide l'inverse volontairement sur les canaux.
- Le FC-670 émule un Fairchild 670 à tube variable-mu, pas un opto.
- Sous Windows, la console se pilote avec Universal Control ; « UC Surface » dans le guide désigne la même surface de contrôle (harmonisation des termes en cours).
