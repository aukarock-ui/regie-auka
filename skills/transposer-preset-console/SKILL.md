---
name: "transposer-preset-console"
description: "Transposer un preset ou une architecture du Guide de Mixage Live (StudioLive 32SC) sur une autre console (SQ6, WING, HD96, M32, DM3, XR18/X-AIR, Ui24R…) à partir de son manuel, fonction par fonction."
---

# Transposer un preset du guide sur une autre console

À utiliser quand Louis mixe sur une console qui n'est pas sa 32SC, ou demande comment un réglage, un bus ou une méthode du guide se fait sur une autre console.

## 0. Identifier la console

1. Modèle exact et, si possible, version du firmware. Une variante (WING Compact / Rack, SQ5 / SQ6 / SQ7, XR18 / XR12) se nomme explicitement.
2. Retrouver le manuel dans les fichiers du projet. S'il n'y est pas, le dire, et proposer de le chercher sur le site du constructeur ou de demander à Louis de le déposer. Sans manuel, aucune fonction ni plage n'est affirmée.
3. Lire dans la Partie 8 du guide ce qui est déjà établi pour cette console et avec quel niveau de confiance. Chercher aussi dans les conversations du projet une discussion sur cette console (cas réel : une discussion entière sur la HD96).

## 1. Transposer fonction par fonction

Suivre l'ordre de la fiche : Micro et placement → Phantom → Gain → HPF → Gate/Expander → Compresseur → EQ → Limiteur → Bus. Pour chaque étape, un des trois statuts, avec la page du manuel :

- **Documenté** : la fonction existe ; donner son nom sur cette console, ses plages et ses crans d'après le manuel.
- **Équivalent partiel** : une fonction proche existe ; dire précisément ce qui diffère (plage, pente, type de détection, position dans la chaîne).
- **Absent ou non documenté** : le dire, et proposer le contournement le plus propre.

Règles :
- Les valeurs ne se transposent pas telles quelles. Les plages, les unités et les crans changent d'une console à l'autre (gain par pas, délais maximum, plages de HPF). Reconvertir chaque valeur et signaler celles qui tombent hors plage.
- Un modèle émulé ne s'identifie pas par son nom commercial. Rapprocher deux émulations (par exemple un 1176 ou un LA-2A sous deux noms) seulement si le manuel le dit.
- L'ordre de traitement par défaut et les points d'insertion diffèrent : les vérifier au manuel avant de proposer une chaîne.
- Si le manuel se contredit (deux plages différentes pour le même filtre, par exemple), le signaler et le placer dans les vérifications à faire.

## 2. Chercher ce que cette console fait mieux

La transposition n'est pas une copie appauvrie. Pour chaque problème que le guide règle par un contournement sur la 32SC, chercher dans le manuel l'outil natif qui le règle à la racine : filtre de sidechain réglable avec écoute, de-esser ou EQ dynamique, mix parallèle intégré, filtre passe-tout, enveloppe de gate en ducker, outils d'édition multi-canaux. Les proposer comme la meilleure option quand le manuel les documente.

## 3. Lire les manuels correctement

- L'extraction en texte casse les tableaux. Pour un tableau décisif (entrées et sorties, plages des processeurs), rendre la page en image et la lire.
- Lire la section entière avant de conclure ; une fonction peut être décrite à deux endroits.
- Distinguer ce que le manuel dit de ce qui se déduit, et marquer la déduction « à vérifier à la console ».

## 4. Livrable

- Pour un preset ou une date : fiche en prose dans l'ordre canonique, avec les noms et les valeurs propres à la console, et en tête les écarts par rapport au preset du guide.
- Pour une console entière : vue de synthèse en tableau (fonction du guide, équivalent sur la console, statut, page), puis les points à vérifier dans les premières minutes devant la console (patch, horloge, sauvegarde et rappel des scènes, solo, compensation de latence).
- Une correspondance nouvelle et sûre est proposée à Louis pour la Partie 8 du guide (skill `maj-guide-mixage`), avec son niveau de confiance.