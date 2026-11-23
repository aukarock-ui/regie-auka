---
name: "fiche-evenement"
description: "Remplir avec Louis la fiche d'un événement son (lieu, piles, public, style, réglementation, positions micro, réseau) avant tout calage, puis en déduire délais, vigilances et plan de mesure."
---

# Fiche événement — préparer un calage

Avant de toucher au processeur, le contexte doit être complet. Modèle : `data/evenements/_modele.yaml` du kit Google Drive « calage-sono ». Sortie : `data/evenements/AAAA-MM-JJ_<lieu>.yaml`. Dans une conversation (hors Claude Code), produire la fiche remplie en YAML, au format du modèle, pour que Louis la dépose dans ce dossier.

## Champs à couvrir
- Événement : nom, date, horaires, organisateur, contact technique.
- Style : principal (punk, métal, hip-hop, reggae-dub, techno, tekno, noise…), secondaires, source live/DJ/mixte, niveau visé à la régie, demandes particulières.
- Réglementation : limites, enregistrement/affichage, contraintes de voisinage, activité destinée aux enfants de 6 ans ou moins.
- Lieu : extérieur/intérieur/chapiteau, dimensions, sol, surfaces réfléchissantes, météo (température, humidité, vent), alimentation électrique.
- Public : jauge, profondeur et largeur de la zone, distance du premier rang, debout/assis.
- Régie : distance à la scène, hauteur, console.
- Système : config utilisée, disposition, position (x, y) et orientation de chaque pile, empilement, hauteur, angle des têtes, configuration des subs (empilés, ligne, cardioïde…), front fills, retours.
- Mesure : logiciel (Open Sound Meter par défaut), micro et calibration, interface, positions micro (≥ 3 pour l'EQ, 1 sur l'axe de sommation pour l'alignement), temps disponible.
- Réseau : IP du Venu360, de la PA2, du PC, de l'hôte OSM.

## Déroulé
1. Vérifier si une fiche existe déjà pour cette date et ce lieu.
2. Poser les questions par blocs courts (3 à 5 questions par message), dans l'ordre : événement et style → réglementation → lieu et météo → public et régie → disposition du système → mesure et réseau. Choix multiples quand c'est possible.
3. Ne jamais remplir un champ par supposition : `null` + question. Distances mesurées ; si Louis estime, noter « estimé » et le signaler à re-mesurer sur site.
4. Ne pas redemander ce qui est déjà dans la base matériel ou la config système.

## Ce qu'on en déduit (à présenter à la fin)
- Délais physiques pile → positions micro et pile → régie : délai (ms) = d / c × 1000 avec c = 331,3 + 0,606·T(°C), température de la fiche. Écarts de trajet entre piles → zones de filtrage en peigne à surveiller.
- Subs en ligne ou cardioïdes : espacements et délais calculés à partir des distances, marqués « à valider par mesure ».
- Réglementation France (décret 2017-1244, art. R.1336-1 du code de la santé publique) : LAeq 15 min ≤ 102 dB(A) et LCeq 15 min ≤ 118 dB(C) partout où le public a accès ; 94 dB(A) / 104 dB(C) si l'activité est destinée aux enfants jusqu'à 6 ans révolus. Festivals et lieux de plus de 300 places : enregistrement et affichage dB(A)/dB(C), conservation 6 mois. En tekno et dub, le dB(C) est souvent la limite bloquante : prévoir la mesure LCeq à la régie.
- Style : courbe cible correspondante (skill methode-calage) et niveau visé.
- Plan de mesure : chaque voie seule → paires autour de chaque coupure → système complet ; positions micro ; temps estimé comparé au temps disponible.
- Liste des manques : champs encore vides qui bloquent une étape du calage.

## Règles
- La fiche contient les faits du jour ; les choix de réglage vont dans le journal `journal/ETAT.md`.
- Fin de préparation : ajouter une ligne dans le journal (« Fiche <date> <lieu> prête, manques : … »).