---
name: "integrer-retour-terrain"
description: "Intégrer au Guide de Mixage Live ce que Louis a constaté sur la console ou en concert : registre 8.7, passage de « à tester » à « validé », contradictions, nouvelles découvertes."
---

# Intégrer un retour de terrain dans le guide

À utiliser quand Louis rapporte le résultat d'une séance de vérification sur la console (registre 8.7), d'une balance ou d'un concert : une valeur testée, un comportement observé, un réglage qui a marché ou non.

## 0. Recueillir le contexte

Une observation n'a de valeur que dans son contexte. Avant de classer, s'assurer d'avoir (et le demander en une seule question s'il manque l'essentiel) :
- la console et son firmware ;
- pour une écoute : le lieu, le système de diffusion, le style et la source (micro, instrument, musicien) ;
- la date ;
- ce qui a été fait exactement (réglage de départ, geste, résultat).

## 1. Rattacher chaque observation

Pour chaque point rapporté, retrouver dans le guide courant :
- la ligne du registre 8.7 qu'il traite (et la séance : console seule, balance virtuelle, avec musiciens) ;
- toutes les sections où la valeur ou le comportement apparaît (fiches de la Partie 3, bus de la Partie 4, scènes de la Partie 6, Partie 8, annexes).

Une observation qui ne correspond à aucune ligne est une découverte : la traiter à l'étape 2, cas 4.

## 2. Classer

1. **Confirme le guide** : la valeur ou le comportement « à tester » devient « validé », avec la mention de la source (console et firmware, ou concert avec date, lieu et système). La ligne du registre est close.
2. **Contredit le guide** : c'est une correction. Elle prime sur toute inférence, mais elle se propage partout où l'ancienne valeur apparaît, et ce qui en dépendait est relu.
3. **Mesure ou comportement console** (une plage, un cran, une fonction présente ou absente, un affichage) : c'est un fait pour ce firmware ; il vaut pour toutes les dates.
4. **Découverte** : un geste ou un réglage qui a bien marché. Il entre dans le guide comme « validé en concert » dans son contexte (style, source, système), sans être généralisé au-delà.
5. **Impression d'écoute isolée** : elle reste attachée à la date. La noter comme piste, pas comme règle. Une impression devient une règle quand elle se répète dans des contextes différents ou que Louis la pose comme décision.

Ne jamais compléter une observation par une valeur plausible : si Louis dit « plus lent ça marchait mieux » sans chiffre, le guide garde la méthode et le critère d'écoute, pas un chiffre inventé.

## 3. Appliquer

Toutes les modifications passent par le skill `maj-guide-mixage` (script de remplacements comptés, propagation, contrôle des raccords, changelog avant/après, publication). Le changelog cite le retour de terrain comme source.

## 4. Tenir le registre à jour

- Les lignes closes sortent du registre ou passent en « fait », selon la convention du guide.
- Une observation qui ouvre une nouvelle question crée une ligne, formulée comme un geste de trente secondes à deux minutes et rangée dans la bonne séance.
- Proposer à Louis la prochaine séance la plus rentable : celle qui débloque le plus de valeurs « à tester ».

## 5. Compte rendu à Louis

Court : ce qui est maintenant validé, ce qui a été corrigé (avant / après), les découvertes ajoutées et leur contexte, ce qui reste ouvert au registre.