---
name: "preparer-evenement-sono"
description: "Préparer une date ou un festival (projet Mix Live) à partir des fiches techniques : patch, plan micros, retours, besoins en DI, matériel à emprunter, questions aux groupes, fiche d'écarts au guide."
---

# Préparer un événement à partir des fiches techniques

À utiliser quand Louis transmet une fiche technique (rider), un planning de festival ou une liste d'artistes, ou demande un patch, un plan de scène ou une fiche pour une date. Les règles de fond (zéro approximation, format des fiches, statuts validé / à tester) viennent des instructions du projet et du guide : ce skill fixe la méthode.

## 0. Retrouver ce qui existe déjà

1. Chercher dans les conversations du projet une discussion dédiée à cet événement ou à ces groupes (recherche par nom de groupe, de lieu et de festival). Elle peut contenir des décisions, des contacts, des riders ou du matériel confirmé qui ne sont nulle part ailleurs.
2. Lire dans le guide courant le matériel actuel, l'architecture des bus et des retours (FlexMix, sorties de la 16R) et les presets des sources concernées. La fiche d'événement s'appuie dessus et ne le recopie pas.
3. Lire chaque rider en entier (texte et tableaux ; une page en image si l'extraction du tableau est illisible).

## 1. Séparer le confirmé du supposé

- Un rider, un SMS ou une phrase de Louis est une donnée. Une recherche web sur un groupe donne au mieux le style et la composition : l'écrire comme supposition, jamais comme besoin technique.
- Un nom inconnu ou mal orthographié (lieu, prêteur, matériel) se fait confirmer par Louis avant d'être repris. Ne jamais recopier une coquille comme un fait.
- Le matériel emprunté (MJC, amis, autre équipe) n'est compté que s'il est confirmé pour cette date.

## 2. Confronter les besoins au parc réel

Un tableau de synthèse par groupe (les tableaux sont permis pour ces vues) : poste, demandé par le rider, ce que Louis a, statut (équivalent, substitution à valider à l'oreille, manque, emprunt nécessaire).

Points à compter explicitement, avec la marge restante :
- les DI (le poste le plus tendu historiquement) ;
- les micros par modèle, en tenant compte des groupes qui se succèdent sans temps de récupération ;
- les pieds, pinces et alimentations fantômes ;
- les entrées de la console et de la stagebox, et les sorties de retour (sorties Mix de la 16R, FlexMix) ;
- les circuits de retour demandés (in-ear stéréo ou mono, wedges) contre les départs disponibles.

Une substitution de micro (modèle absent de la liste du rider) est signalée comme telle, avec ce qu'elle change, et reste « à valider à l'oreille ».

## 3. Patch, plan de scène et enchaînements

- Patch canal par canal, en reprenant la numérotation et le câblage standard du guide (sous-multipaire batterie sur la 16R, multipaire vers les entrées locales, etc.) sauf raison de faire autrement, dite.
- Un patch fixe par jour quand plusieurs groupes se succèdent, si c'est possible ; sinon lister les changements de patch entre groupes.
- Plan des retours : quel départ pour quel musicien, et quels FlexMix sortent de leur rôle par défaut pour ce set.
- Enchaînements : temps de changement de plateau, balances possibles, chevauchements de matériel entre scènes.
- Si la console du soir n'est pas la 32SC, enchaîner avec le skill `transposer-preset-console`.

## 4. La fiche d'événement

Livrable : un document (type Docs quand il est proposé) qui contient seulement :
- le résumé de la date (horaires, scène, système, console, contacts techniques) ;
- par groupe : le patch, le plan micros et retours, et les écarts au guide (preset modifié, source absente du guide, choix de style propre au groupe), rédigés en fiches en prose dans l'ordre Micro et placement → Phantom → Gain → HPF → Gate/Expander → Compresseur → EQ → Limiteur → Bus ;
- les zones d'incertitude et ce qui les lèvera ;
- la liste du matériel à emprunter ou à acheter, avec la date limite.

Ne jamais redire ce que le guide contient déjà : y renvoyer par numéro de section.

## 5. Questions aux groupes

Rédiger les questions qui manquent sous forme d'un message prêt à envoyer (SMS ou e-mail selon le contact, en français, court) : retours, sorties DI des amplis ou des machines, micros apportés, HF, besoins électriques, timing. Une question par point bloquant, pas de questionnaire générique.

## 6. Mise à jour au fil des réponses

Quand une réponse arrive, mettre à jour le patch et la fiche, dire ce qui change (par exemple « le patch passe de 18 à 21 lignes ») et reporter dans la fiche ce qui reste ouvert. Une découverte technique qui vaut pour tous les concerts est signalée à Louis comme candidate au guide (skill `integrer-retour-terrain`).