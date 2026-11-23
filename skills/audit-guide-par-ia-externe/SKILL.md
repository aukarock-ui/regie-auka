---
name: "audit-guide-par-ia-externe"
description: "Faire auditer le Guide de Mixage Live par une autre IA (Gemini, Mistral, DeepSeek…) : préparation du prompt, points déjà vérifiés à exclure, découpage en passes, tri des réponses."
---

# Audit du guide par une IA externe

À utiliser quand Louis demande de faire auditer le guide par une autre IA, ou de préparer un prompt d'audit qu'il collera lui-même dans une autre application. Louis préfère que l'audit soit fait par une autre famille d'IA ; l'assistant du projet reste chef d'équipe : il prépare, lance, vérifie et applique. Rien de ce que renvoie l'auditeur n'entre dans le guide sans vérification (skill `maj-guide-mixage`, étape 1).

## 1. Choisir le mode

- **Par API** (clé fournie par Louis) : l'assistant lance l'audit lui-même, en tâche de fond.
- **Par copier-coller** (DeepSeek dans son application, par exemple) : l'assistant rédige le prompt, Louis le colle avec le docx et rapporte la réponse.

Clés d'API : rangées dans un fichier protégé de la session, jamais affichées, jamais écrites dans un message, un script visible ou la mémoire. L'adresse e-mail de Louis n'est jamais envoyée à un service externe. Offres gratuites sans carte bancaire uniquement, sauf décision contraire de Louis. Si la session ne contient plus la clé, la redemander.

## 2. Composer le prompt

Dans cet ordre :

1. **Mission.** Auditer le contenu musical et technique ; ne pas réécrire le guide. Pour chaque remarque : section, citation exacte du guide, problème, gravité (bloquant / important / mineur), type (incohérence / manque / raisonnement / musical / formulation), proposition, et « vérifiable sans manuel : oui ou non ».
2. **Règle de preuve.** Toute remarque qui invoque le manuel doit citer le passage exact. Une citation inventée disqualifie la remarque. Une valeur proposée doit avoir une source ; sinon proposer une méthode, pas un chiffre.
3. **Hors périmètre.** Table des matières, section HISTORIQUE, tout ce que liste le dernier changelog (sauf si la correction elle-même est fausse).
4. **Points déjà vérifiés — ne pas les signaler de nouveau.** Tenir cette liste à jour à chaque audit. Elle contient au moins :
   - La 32SC a 10 sorties FlexMix : 6 XLR et 4 jacks TRS (tableau 3.1.4 du mode d'emploi). Les 4 entrées Aux sont dans le tableau des entrées, pas dans celui des sorties.
   - La 32SC n'a pas de sorties physiques de sous-groupe (3.2.2).
   - Le guide parle des 32 canaux de mixage, pas du nombre de départs USB.
   - Le tableau des Release de 2.4 concerne le limiteur, pas les compresseurs.
   - Les choix de style de Louis (compression forte du Bus Voix en métal, par exemple) sont des décisions, pas des erreurs.
   - Les retours FX n'ont ni HPF ni gate (tableau 6.1 du mode d'emploi) : pas de ducking ni de filtrage sur un retour FX.
   - La Key Source n'existe que sur les canaux d'entrée (6.8.3 / 6.8.4).
   - L'ordre par défaut du Fat Channel est Comp > EQ (6.8.4) ; le guide l'inverse volontairement sur les canaux.
   - Le FC-670 émule un Fairchild 670 à tube variable-mu, pas un opto.
   - La 32SC n'a pas de touches User Function (mode d'emploi, p. 108) : la battue du tempo passe par la touche TAP et Tap Assign (9.1, p. 79).
   - Logiciels du PC de régie : Universal Control 5.1.1 (la surface « UC Surface » y est intégrée sous Windows), pilote « StudioLive Series III ASIO », Ableton Live 11 Suite, FabFilter Pro-R version 1 (pas Pro-R 2).
5. **Consigne de balayage.** Comparer chaque fiche de la Partie 3 et chaque bus de la Partie 4 : au tableau 2.4 ; à la règle du mode Auto (2.1) ; aux plages et crans de la Partie 2 ; au tableau 6.1 du manuel (quelle fonction existe sur quel type de canal) ; à la scène de style qui la modifie. Vérifier que chaque renvoi « voir X.Y » dit bien ce qui est annoncé.
6. **Documents.** Le guide complet, puis l'addendum Fat Channel, le mode d'emploi StudioLive (parties 1 et 2), et si la place le permet le manuel UC Surface.

## 3. Soigner ce qu'on envoie

- Les tableaux des manuels perdent leur mise en page à l'extraction en texte, et l'auditeur les lit de travers (cas réel : les sorties FlexMix de la 32SC, signalées à tort trois fois). Pour les tableaux importants, joindre la page en image si l'API l'accepte, ou réécrire le tableau proprement dans le prompt en indiquant la page d'origine.
- Vérifier la taille : guide + manuels ≈ 200 000 tokens. Si le modèle ne les accepte pas, découper.

## 4. Découper en passes

Deux passes donnent plus qu'une seule : passe A sur les Parties 0 à 4, passe B sur les Parties 5 à 8 et les annexes, chacune avec les mêmes manuels. Les lancer l'une après l'autre en tâche de fond, avec une pause entre les deux et jusqu'à trois essais en cas d'échec. Enregistrer chaque réponse dans un fichier.

Pendant que l'auditeur tourne, faire sa propre relecture : ne pas attendre.

## 5. Trier les réponses

**Dans Claude Code à la régie**, où les agents de `.claude/agents/` existent : envoyer toutes les remarques en un seul appel à l'agent `verif-manuel`, puis classer à partir de ses verdicts. Sinon : pour chaque remarque, retrouver la citation dans le guide courant, retrouver le passage du manuel invoqué, refaire les calculs. Classer en retenu, retenu en partie, rejeté. Compter et dire à Louis combien de remarques reposaient sur une lecture fausse ou une citation inventée : c'est ce qui permet de juger l'auditeur.

Une remarque rejetée deux fois pour la même raison rejoint la liste « points déjà vérifiés » du prompt suivant.

## 6. Enchaîner

Les remarques retenues s'appliquent avec le skill `maj-guide-mixage`. Compte rendu à Louis : verdict point par point, puis ce qui a changé dans le guide.

## Choix de l'auditeur

- Une IA d'une autre famille que celle qui rédige le guide.
- D'abord les voies gratuites déjà installées sur le PC de régie : le proxy Gemini local (`127.0.0.1:8000`, script `audits/outils/audit_gemini.py`, quatre passes A1, A2, B1, B2 ; quota quotidien remis à zéro vers 9 h, heure de Paris ; « aucune clé disponible » veut dire quota épuisé) et les modèles gratuits d'opencode (`opencode_ask`). Un audit payant seulement sur décision de Louis.
- Les offres gratuites changent : vérifier par une recherche les conditions du moment (carte bancaire, limites par minute, taille de contexte) avant de recommander un service, et dire à Louis ce qui n'a pas pu être vérifié.
- Un modèle rapide et gratuit se trompe plus souvent sur les tableaux et invente parfois des citations : la règle de preuve et la liste des points déjà vérifiés servent à limiter ces défauts, pas à les supprimer.
- Constaté sur l'offre gratuite Gemini : les modèles Pro refusent les requêtes longues (erreur 429), seul le modèle Flash passe avec guide + manuels. Pistes gratuites sans carte déjà repérées, à revérifier avant usage : Mistral (offre gratuite), catalogue NVIDIA (modèles Kimi, DeepSeek). Les API DeepSeek et OpenAI demandent du crédit.
- Quand Louis colle lui-même le prompt dans une application, livrer le prompt dans un fichier texte prêt à copier, avec le format de réponse numéroté et la section « Déjà traité — ne pas répéter ».