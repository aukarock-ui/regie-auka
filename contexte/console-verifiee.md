# Comportements console vérifiés et principes de travail

Repris de la mémoire du projet claude.ai « Mix Live » (état au 22 novembre 2026). Certaines lignes datent d'avant la V35 du guide : **le guide prime** ; signaler à Louis tout écart.

## Corrections techniques vérifiées

- Standard Compressor en mode Auto : Attack bloquée à 10 ms et Release à 150 ms, les commandes deviennent inopérantes.
- Tube CB : en mode Fixed, attaque 1 ms et release 50 ms (addendum 3.7) ; utiliser le mode Manual sur les voix.
- FC-670 : l'Input Gain est le moteur principal de la compression, le Threshold un affinage.
- Class-A FET : pas de commande Threshold, piloté par l'Input Gain.
- Alpine EQ-550 : cinq positions de gain par bande, pas de pas fixes de ±2 dB.
- Solar 69 EQ : pas de Level Adjust ; fréquence de la bande haute réglable.
- Comp 160 : les voyants Above/Below existent visuellement mais ne sont pas documentés par PreSonus ; piloter au résultat mesuré.
- Baxandall High Cut : l'addendum duplique par erreur la description du Low Cut ; plage relevée visuellement d'environ 7,5 à 70 kHz.
- Gate/Expander : Range réglable (0 à −∞) en mode Gate, désactivé en mode Expander ; le mode Expander n'a que Threshold, Attack, Release, Key Filter.
- Limiteur (firmware 3.4.0.111374) : UC Surface expose une commande Release en plus du Threshold.
- Gate de kick : Range à −15/−20 dB (pas −∞) pour garder la résonance du micro boundary.
- Réverbes : pas de commande Decay, la durée vient du preset chargé.
- Classic Compressor : pas de commande Attack.
- 16R autonome : fonctionne sans console via UC Surface mais demande un routeur, elle n'émet pas de WiFi.
- Sources ligne TRS symétriques : directement sur les combos de la 16R, sans DI.
- FabFilter Pro-R 2 : zéro latence par conception.
- LiquidSonics Seventh Heaven Pro : 8 cœurs physiques et 32 Go conseillés, risque sur le PC actuel.

## Principes de travail

- Un patch fixe par jour, pas de repatch entre groupes.
- Coordination technique avec les artistes par SMS ; Claude rédige, Louis relit et envoie.
- Matériel emprunté traité comme conditionnel, confirmé date par date.
- Scènes de style par genre plutôt qu'un traitement générique.
- Audits du guide confiés à une autre IA que Claude ; Claude vérifie et applique.
