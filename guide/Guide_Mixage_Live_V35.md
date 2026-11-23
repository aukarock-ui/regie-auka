**GUIDE DE MIXAGE LIVE — V35**

ÉDITION AUTONOMIE — PreSonus StudioLive 32SC + 16R

*Firmware 3.4.0.111374 · UC Surface · Écosystème Milan AVB*

*Punk · Rock · Métal · Hip-Hop · Reggae · Dub · Techno Live*

*Parc micro personnel complet · Kit batterie 4 micros autonome · Presets calés sur le matériel réel*

*L’historique des modifications est en toute fin de document, sous le titre « HISTORIQUE — NE PAS CITER ». Les valeurs qui y figurent comme « avant » sont périmées.*

## BLOC ASSISTANT — mode d’emploi pour l’IA

*Lecteur humain : cette section ne te concerne pas, passe à la Table des matières.*

**Les instructions de projet priment et ne sont pas répétées ici** : zéro approximation, modes de défaillance déjà constatés, format des livrables, et l’objectif de qualité musicale et professionnelle visé — tout ça s’applique à chaque réponse sans repasser dessus dans ce document. Ce qui suit est spécifique à ce guide-ci.

**Statut de ce document.** Version canonique unique. Si un fragment d’une version antérieure remonte dans une recherche — une ancienne version pas encore supprimée du projet — ce document-ci tranche toujours. Un fragment absent d’ici ne doit pas être cité comme actuel.

**Trois statuts, à distinguer sur tout contenu de ce guide :** *validé* (vérifié au manuel ou éprouvé en concert), *à tester* (piste argumentée, jamais essayée — voir le registre en 8.7), *emprunté* (matériel non garanti, à confirmer date par date). Le matériel personnel et le matériel d’emprunt ne se mélangent jamais sur une fiche technique.

**Sur une console autre que la StudioLive, ne jamais supposer** — voir Partie 8 pour les niveaux de confiance par machine, et le protocole en 8.3 pour une console qui n’y figure pas encore.

**Quand Louis demande un preset : récupérer les valeurs dans ce document plutôt que de les reconstruire** de mémoire ou d’une conversation précédente.

**Ne jamais citer la section « HISTORIQUE — NE PAS CITER »** en fin de document comme source d’une valeur : elle contient volontairement les anciennes valeurs, pour la traçabilité. Une valeur ne fait foi que dans le corps du guide.

**Renvois.** Un numéro seul (« voir 4.4 ») renvoie à ce guide. **Dans les Parties 0 à 7, « le manuel » sans autre précision désigne la documentation PreSonus** — mode d’emploi StudioLive III et addendum des plug-ins Fat Channel ; le troisième document PreSonus, le manuel de référence UC Surface, est toujours cité par son nom (« manuel UC Surface 3.3 ») — puisque ces parties ne traitent que de cette console ; un numéro qui suit (« le manuel (12.3.2) ») est un numéro de ce manuel, pas du guide. **Tout autre document est toujours nommé** (« manuel du Venu360 », « manuel HD96 »), et en Partie 8, où plusieurs consoles se côtoient, le nom est toujours écrit.

**Règle de priorité quand deux sections parlent du même paramètre.** Dans cet ordre, la ligne du bas l’emporte sur celles du dessus, **et seulement pour le paramètre qu’elle cite** :

1. **Partie 2** — ce qu’une commande *peut* faire (plages, crans, commandes existantes). Ce n’est pas une prescription, c’est la limite physique : une valeur prescrite ailleurs qui sort de ce que la Partie 2 documente est une contradiction à **signaler**, pas à arrondir.
2. **Partie 3 (canaux), Partie 4 (bus), Partie 5 (effets)** — la base. 3.1 pour le kit personnel.
3. **3.2 (matériel d’emprunt)** — remplace 3.1 pour le paramètre concerné, uniquement si l’emprunt est confirmé pour la date.
4. **Partie 6 (scène de style)** — ne modifie que ce qu’elle cite, sur un canal, un bus ou un effet. Tout le reste demeure celui des Parties 3, 4 et 5.
5. **5.6 et 7.3 (lieu : extérieur, chapiteau, salle)** — adaptent les effets et le GEQ après le choix de la scène.
6. **La fiche groupe du jour (Annexe D) et toute consigne donnée par Louis dans la conversation** — priment sur tout le guide.

Une contradiction que cette règle ne résout pas — deux sections de même rang, ou une valeur impossible selon la Partie 2 — **se signale à Louis, elle ne se tranche pas en silence.**

**Valeur prescrite mais non vérifiée — règle unique.** Plusieurs réglages du guide dépendent d’une vérification console qui n’a pas encore été faite (registre 8.7). Qu’ils soient notés « à vérifier », « à relever », « inférence » ou « sous réserve », la conduite est la même : **la valeur du guide est produite telle quelle, suivie de la mention « valeur de départ, à vérifier sur la console (8.7) »**. L’IA ne lui substitue pas une autre valeur de sa propre initiative. Si la console n’offre pas la valeur, la règle de repli est : **la valeur disponible la plus proche ; si deux valeurs l’encadrent, la plus lente pour un temps, la plus basse pour un gain** — et l’écart se consigne.

**Qualificatifs sans chiffre.** « Fast », « Medium », « Slow » sont définis par modèle en 2.1. « Bas », « modéré », « haut » sur les effets sont définis en 5.1bis, avec la méthode de réglage. Un qualificatif n’est jamais converti en millisecondes ou en décibels inventés.

**Construire un preset complet.** Quand Louis demande « le preset » d’une date ou d’un groupe sans autre précision, le livrable est **autonome** : quelqu’un qui n’a que lui doit pouvoir régler la console. Il comprend, dans cet ordre :

1. *En-tête.* Date, lieu (intérieur, extérieur ou chapiteau), style et scène de la Partie 6, console. Matériel compté : personnel d’un côté, emprunt **confirmé** de l’autre.
2. *Patch* — tableau de synthèse : canal, source, micro ou DI, fantôme, bus de destination, statut (personnel ou emprunt).
3. *Une fiche par canal, en prose*, dans l’ordre de 1.6 : Micro et placement → Phantom → Gain → HPF → Gate/Expander → Compresseur → EQ → Limiteur → Bus, puis départs d’effets. **Toutes les lignes figurent, même quand la réponse est « OFF », « flat » ou « sans objet »** : une ligne absente se lit comme un oubli.
4. *Les bus utilisés* (Partie 4, modifiés par la scène) : compresseur, EQ, limiteur, fader. Bus Parallel toujours mentionné, même à -∞.
5. *Le Master* (5.1).
6. *Les quatre effets* (5.2 à 5.5, adaptés par la scène et par le lieu) : type, réglages, EQ et routage du retour.
7. *Les retours* : un FlexMix par musicien, point de départ Pre1 ou Pre2 (7.11).
8. *Socle et emprunt.* Le preset tient avec le seul matériel personnel ; ce qui dépend d’un emprunt vient dans un bloc séparé, clairement titré, qui peut tomber sans rien réécrire.
9. *À vérifier et à régler à l’oreille* : la liste, extraite du preset, des valeurs portant la mention « à vérifier (8.7) » et de celles données par une méthode plutôt que par un chiffre.

*Peuvent être omis :* les justifications (elles sont dans le guide), les bus non utilisés ce jour-là (Bus Divers, Bus Basse), le GEQ (il se règle sur place, 7.3 et 7.11), la chaîne USB de 7.10 sauf demande, la Partie 8 si la console est la StudioLive. *Format :* fiches en prose, tableaux réservés au patch et aux vues d’ensemble (instructions de projet). **Une « fiche groupe » est un autre livrable** (Annexe D) : elle ne contient que le patch, les écarts au guide et les risques. Sans précision, « preset » veut dire preset complet ; « fiche » veut dire Annexe D.

**Ce que ce guide ne couvre pas**, pour qu’on ne le croie pas exhaustif : l’enregistrement de concert en tant que tel (seule la balance virtuelle est traitée, 7.12), la diffusion en direct, la sécurité électrique (hors la question de terre en 7.9), le calage du système de diffusion (processeurs, mesure, alignement des enceintes), et l’organisation avec une production ou un régisseur.

### TABLE DES MATIÈRES

*Construite à partir des titres du document. Les sous-blocs en italique sont les fiches et consoles à l’intérieur d’une section.*

**PARTIE 0 — MON MATÉRIEL**

0.1 Consoles et infrastructure

0.2 Mon parc microphone

0.3 Spécifications qui changent les réglages

0.4 Pieds et accessoires — la logistique un pied

0.5 Boîtiers DI

0.6 Matériel d’emprunt — MJC et amis

0.7 Mon autonomie réelle

0.8 Angles morts restants

0.9 Feuille de route

**PARTIE 1 — PHILOSOPHIE & ARCHITECTURE**

1.1 Nettoyage → Coloration → Glue

1.2 Gain Staging global

1.3 Architecture FlexMix — 16 bus

1.4 Stagebox 16R

1.5 Gestion de l’alimentation fantôme

1.6 Comment lire une fiche preset

**PARTIE 2 — RÉFÉRENTIEL FAT CHANNEL**

2.1 Compresseurs

2.2 Gate / Expander

2.3 Égaliseurs

2.4 Limiteur — valeurs de Release par source

2.5 Sidechain inter-canal — Key Source

2.6 Errata de la documentation PreSonus

2.7 Plages de réglage chiffrées

2.8 Les machines derrière les émulations — et les gestes qui vont avec

2.9 Sommation, phase et filtrage en peigne — le socle

**PARTIE 3 — PRESETS PAR SOURCE**

3.1 Batterie — le kit 4 micros

3.2 Batterie — extensions en emprunt

3.3 Basses

*— BASSE DI*

*— BASSE AMPLI*

*— CONTREBASSE*

3.4 Guitares

*— GUITARE ACOUSTIQUE*

3.5 Claviers

*— SYNTHÉTISEUR*

*— ORGUE / RHODES*

3.6 Cuivres & Bois

*— TROMPETTE / TROMBONE*

*— SAXOPHONE*

*— FLÛTE*

3.7 Voix

*— CHŒURS / BACKING*

3.8 Sources ligne, DJ et Techno Live

*— TABLE DE MIXAGE DJ*

*— PLATINES VINYLE*

*— PC / PLAYBACK*

**PARTIE 4 — BUS DE GROUPE**

4.1 Bus Drums — FlexMix 9+10 (stéréo)

4.2 Bus Instru — FlexMix 11+12 (stéréo)

4.3 Bus Voix — FlexMix 13+14 (stéréo)

4.4 Bus Parallel — FlexMix 15 (mono)

4.5 Bus Divers — FlexMix 16

4.6 Bus Basse — option sur sous-groupe fixe

**PARTIE 5 — MASTER & FX**

5.1 Traitement Master

5.1bis Le rack d’effets — ce que la console propose réellement

5.2 FX A — Reverb Voix

5.3 FX B — Stereo Delay

5.4 FX C — Reverb Drums

5.5 FX D — Ping Pong Delay

5.6 Adaptation extérieur / chapiteau

5.7 Chorus et Flanger

**PARTIE 6 — SCÈNES PAR STYLE**

6.1 PUNK

6.2 ROCK

6.3 MÉTAL

6.4 HIP-HOP

6.5 REGGAE

6.6 DUB

6.7 TECHNO LIVE

**PARTIE 7 — WORKFLOW & OPÉRATIONS**

7.1 Soundcheck — 60 minutes

7.2 Plateau multi-groupes / changements rapides

7.3 GEQ — correction salle

7.4 Monitoring & Solo

7.5 Troubleshooting

7.6 Backup & sauvegarde

7.7 Retard d’entrée — aligner deux micros sur une même source

7.8 Retard de sortie — aligner la façade sur la scène

7.9 Réseau AVB — état du système et diagnostic

7.10 Insert externe — matériel ou ordinateur

7.11 Retours de scène — GEQ par FlexMix et AFS

7.12 Balance virtuelle — régler sans le groupe

**PARTIE 8 — TRANSFÉRER LA MÉTHODE SUR UNE AUTRE CONSOLE**

8.1 Niveaux de confiance par console

8.2 La méthode exprimée en fonctions, pas en noms de plug-ins

8.3 Protocole — arriver sur une console inconnue

8.4 Deux principes transversaux, à lire avant les fiches

8.5 Tableau comparatif des gates — sept consoles

8.6 Fiches par console

*— Allen & Heath SQ (SQ-5 / SQ-6 / SQ-7)*

*— Behringer WING / WING COMPACT / WING RACK*

*— Midas HD96-24*

*— Midas M32*

*— Yamaha DM3*

*— Behringer X-AIR (XR12 / XR16 / XR18)*

*— Soundcraft Ui24R*

8.7 Registre des tests en attente

**ANNEXE A — RÉCAPITULATIF PLUGINS**

**ANNEXE B — PATCHS TYPES PAR FORMATION**

**ANNEXE C — VÉRIFICATION AUTHENTICITÉ BETA58**

**ANNEXE D — MODÈLE DE FICHE GROUPE**

**HISTORIQUE — NE PAS CITER**

# PARTIE 0 — MON MATÉRIEL

## 0.1 Consoles et infrastructure

**PreSonus StudioLive 32SC**, firmware 3.4.0.111374, console principale. **Stagebox 16R**, même firmware, en liaison AVB. Les deux s’utilisent séparément ou ensemble : la 16R seule sur les petites configurations, en stagebox déportée sur les plateaux complets.

Contrôle via **UC Surface** sur tablette ou laptop. Le **Release du limiteur** n’a pas d’encodeur physique sur la 32SC : il se règle à l’écran tactile ou dans UC Surface (voir 2.4).

**Processeurs de diffusion** : **DBX DriveRack Venu360** (processeur du système de façade personnel, ses six sorties y sont utilisées) et **DBX DriveRack PA2**. Les deux embarquent l’algorithme **AFS** de suppression de larsen — voir 7.11. Leurs manuels ont été retirés du projet le 10 novembre 2026 : les garder sur l’ordinateur pour vérifier sur la machine.

Sur certaines dates, des ingénieurs invités arrivent en **Wing** ou **Wing Rack**. Prévoir la passation, ne pas compter sur ses scènes.

## 0.2 Mon parc microphone

Matériel personnel, propriété pleine :

- 1 × **the t.bone BD 500 Beta** — grosse caisse (condensateur boundary, **48 V requis**)

- 1 × **Audix i5** — caisse claire (dynamique)

- 2 × **Lewitt LCT 040 MATCH** — paire appairée overheads (condensateurs, **48 V requis**)

- 1 × **Shure SM57** — polyvalent

- 2 × **Shure SM58** — voix

- 2 × **Shure Beta58** — voix, **authenticité douteuse** (voir Annexe C)

**Total : 8 microphones personnels.** Trois d’entre eux exigent une alimentation fantôme.

## 0.3 Spécifications qui changent les réglages

Ces données viennent des fiches constructeur et changent concrètement la façon de régler la console. Elles ne sont pas là pour décorer.

***the t.bone BD 500 Beta*** *(article Thomann 436138)*

Condensateur électret à zone de pression, capsule **demi-cardioïde**, alimentation **P48 obligatoire**, réponse annoncée de 20 ou 30 Hz à 20 kHz selon la source, SPL maximal **140 dB à 1 % de THD**, impédance 600 Ω, boîtier métal, filetage 3/8” et pieds caoutchouc antidérapants.

*Ce que ça implique.* C’est un micro **à poser**, pas à pointer. Plus la surface sur laquelle il repose est grande et rigide, plus la réponse descend bas — à l’intérieur d’une grosse caisse, la coque joue le rôle de baffle infini et le grave remonte tout seul. Il capte aussi les médiums et les aigus, donc il donne un son complet sans chercher la position parfaite.

*L’interrupteur d’EQ.* Sous le boîtier se trouve un commutateur qui change la réponse : une position pensée grosse caisse (creusement des médiums), une position pensée piano ou voix. **Le régler sur la position grosse caisse avant toute chose** — et surtout, ne pas recreuser encore les médiums à la console par-dessus, sinon le kick devient creux et sans corps.

*Sensibilité.* Les sources Thomann divergent (-53 dB en fiche produit, -73 dB/1 V en datasheet). **Ne pas chercher une valeur théorique : caler le gain au vumètre**, cible -12 à -6 dBFS en crête.

*Limite.* 140 dB de SPL maximum, c’est confortable mais pas infini dans une caisse frappée fort. Si le signal distord à gain modéré, c’est le micro qui sature, pas le préampli — reculer le micro dans la caisse.

***Audix i5*** *(article 178792) + D-Vice Rimclamp* *(article 160143)*

*Pourquoi l’i5 plutôt qu’un SM57, au-delà du son.* Des retours d’usage d’ingénieurs vont dans le même sens : **l’i5 capterait moins de repisse que le SM57** à placement équivalent. **C’est un retour d’usage, pas une mesure** — ni Audix ni Shure ne publient de comparaison, et la fiche de l’i5 au projet ne chiffre pas cette réjection. Sur un kit 4 micros où la repisse est le problème central, c’est une raison de plus de le garder en poste caisse claire ; à confirmer à l’oreille en écoutant les deux micros sur la même caisse.

Dynamique cardioïde, pas d’alimentation, très haute tenue en SPL. La pince D-Vice se fixe **au cerclage de la caisse claire** avec un col de cygne : plus de pied, plus d’encombrement au sol.

*Ce que ça implique.* Gain de temps considérable en changement rapide, et le micro reste solidaire de la caisse même si le batteur la déplace. En contrepartie, une fixation au cerclage transmet davantage de vibrations de fût et se déplace si le batteur tape le cercle — vérifier le serrage entre deux groupes.

***Lewitt LCT 040 MATCH*** *(article 467013)*

Paire appairée à ± 0,5 dB, condensateurs statiques petite membrane, capsule 17 mm, **cardioïde**, réponse 20 Hz à 20 kHz, **sensibilité 18,8 mV/Pa (-34,5 dBV/Pa)**, bruit propre 20 dB(A), **SPL maximal 135 dB à 0,5 % de THD**, alimentation **48 V ± 4 V, consommation 7,2 mA par micro**, corps aluminium de 44 g. Livrés avec pinces, bonnettes mousse et sacoche deux compartiments.

*Ce que ça implique — trois points concrets.*

**Sensibilité élevée → gain bas.** 18,8 mV/Pa, c’est beaucoup. Au-dessus d’une batterie qui joue fort, le signal arrive déjà costaud. Prévoir un gain préampli **faible**, de l’ordre de +5 à +20 dB, à caler au vumètre. C’est l’inverse du réflexe habituel sur des overheads.

**Aucun atténuateur, aucun filtre sur le micro.** Le LCT 040 n’a aucun commutateur. Si le préampli sature déjà au gain minimum, la solution n’est pas électronique : **éloigner ou remonter les micros**.

**Voicing brillant.** La courbe monte à partir de 4 kHz et culmine vers 15 kHz. Ces micros donnent déjà de l’aigu et du shimmer sans intervention. **Ne pas ajouter de boost d’aigus par réflexe** — au contraire, prévoir un léger cut si ça devient dur en salle réverbérante.

**Consommation notable.** 7,2 mA par micro, 14,4 mA pour la paire. Une alimentation fantôme faible peut générer du souffle sur ce modèle. La StudioLive fournit un 48 V correct, mais si un souffle inhabituel apparaît sur les overheads, vérifier l’alimentation avant d’accuser le micro.

**Bonnettes fournies.** Les monter systématiquement en extérieur, sous chapiteau ou en guinguette. Un condensateur nu prend le moindre souffle d’air.

**Fragilité.** Ce sont les seuls micros fragiles du parc. Sacoche obligatoire au transport, et jamais laissés montés sur le pied pendant un déplacement de plateau.

## 0.4 Pieds et accessoires — la logistique un pied

- 1 × **K&M 210/9** — pied perche noir, grande hauteur

- 1 × **K&M 23550** — barre stéréo pour couple de micros

*Le point important.* Avec le kick posé dans la caisse, la caisse claire pincée au cerclage et les overheads sur barre stéréo, **la batterie complète ne demande qu’un seul pied**. Sur un plateau à cinq ou six groupes qui s’enchaînent, c’est probablement l’avantage pratique le plus fort du parc : montage et démontage en moins de deux minutes, aucun encombrement au sol autour du batteur.

*Ce que la barre stéréo autorise.* Un couple **coïncident (XY)** ou **quasi coïncident type ORTF** selon l’écartement permis par la barre. Elle n’autorise pas un couple espacé large (AB), qui demanderait un second pied — ni une configuration Glyn Johns, pour la même raison. Voir 3.1 pour le choix entre XY et ORTF.

## 0.5 Boîtiers DI

- 1 × **DI passive** (perso)

- 1 × **DI active** (perso)

- 1 × **Palmer River Elde** — DI **stéréo**, deux canaux (perso, acquise à l’automne 2026)

**Total : 4 canaux de DI en propre.** La DI active pour les sources faibles ou passives — basse passive, guitare électro-acoustique à pile fatiguée. La DI passive pour les sorties ligne déjà fortes — clavier, pédalier, sortie symétrisée d’ampli. La Palmer pour toute source stéréo : clavier, contrôleur DJ, machine, loopstation.

*Ce que la Palmer change.* Un clavier stéréo ne mobilise plus les deux DI mono : clavier stéréo **plus** basse **plus** une source ligne mono tiennent maintenant sans emprunt. La contrainte ne disparaît pas, elle recule : deux sources stéréo simultanées (deux loopstations, clavier stéréo et machine stéréo) ramènent à l’emprunt.

*Non vérifié ici.* La notice de la Palmer River Elde n’est pas au projet : type (passive ou active), atténuateur, ground lift et niveau d’entrée admissible ne sont pas documentés dans ce guide. À relever sur le boîtier ou la notice avant de l’inscrire sur une fiche technique avec des valeurs.

*Rappel utile.* Une source ligne **symétrique en jack TRS** entre directement sur les combos de la 16R, sans DI (constat d’usage de Louis ; le manuel de la 16R n’est pas au projet). Sur la 32SC, seules les 8 entrées mixtes l’acceptent — voir 1.4.

## 0.6 Matériel d’emprunt — MJC et amis

Rien de ce qui suit n’est garanti : à confirmer date par date, et à ne jamais inscrire sur une fiche technique comme acquis.

*Côté MJC :* 2 × **Sennheiser e604** avec pinces (toms), 1 × **Shure PGA52** (grosse caisse), 2 × SM57, 2 × SM58, 5 grands pieds et 1 petit. **La MJC n’a ni système HF ni boîtier DI** — les versions précédentes du guide en listaient, c’était faux. Backline : batterie **Pearl**, ampli guitare **Blackstar**, clavier **Yamaha**.

*Côté amis :* selon disponibilité, à confirmer date par date.

*Ce que ce prêt autorise.* Avec les deux e604 et le PGA52, un kit à deux toms micés et un kick à deux micros (BD 500 Beta dedans, PGA52 dans la caisse près de la batte ou devant la peau de résonance) devient possible — voir 3.2. Dès que les toms sont micés, le HPF des overheads change de logique (3.1).

*Règle de travail.* Construire chaque fiche groupe sur le parc personnel, puis ajouter l’emprunt en couche supplémentaire clairement identifiée. Si l’emprunt tombe, la date tient quand même.

## 0.7 Mon autonomie réelle

Avec les 8 micros personnels et les 4 canaux de DI, sans aucun emprunt :

*Batterie complète en 4 canaux* — kick (BD 500 Beta), caisse claire (i5), overheads stéréo (paire Lewitt). Les toms et les cymbales sont portés par les overheads. C’est une configuration professionnelle standard, pas un compromis.

*Basse* — DI active, 1 canal.

*Guitare* — SM57 sur l’ampli, 1 canal.

*Clavier mono ou source ligne* — DI passive, 1 canal.

*Clavier stéréo, contrôleur DJ ou machine* — Palmer River Elde, 2 canaux.

*Voix* — jusqu’à 4 canaux (2 Beta58 + 2 SM58).

**Total : 13 canaux, un groupe de rock complet avec clavier stéréo couvert seul.** C’était l’objectif de la démarche d’achat, il est atteint.

## 0.8 Angles morts restants

*Toms micés individuellement.* Portés par les overheads, ce qui marche bien en configuration 4 micros et impose le réglage de HPF décrit en 3.1. Sur un kit à quatre toms en métal, un micro de tom dédié manquerait.

*Seconde guitare.* Un seul SM57. Deux amplis simultanés imposent l’emprunt, ou un SM58 sur le second — compromis acceptable.

*Peau de résonance non percée.* Le BD 500 Beta étant un boundary, il doit pouvoir entrer dans la caisse. Sur une peau pleine, il faut le poser contre la peau de frappe côté extérieur, ce qui dégrade le résultat. C’est le cas d’usage qui justifie l’Audix D6 en feuille de route.

*Capacité DI.* Quatre canaux depuis l’arrivée de la Palmer. Le clavier stéréo n’est plus bloquant ; les dates électroniques à plusieurs sources stéréo le restent.

*Système HF.* Aucun en propre, aucun à la MJC. Sur les dates qui en demandent, il vient du lieu ou des artistes.

*Cuivres et bois.* Le SM57 dépanne sur une trompette. Sur un sax ou une flûte, on reste en dépannage.

*Authenticité des Beta58.* Deux des quatre micros voix sont incertains. Test à faire (Annexe C).

## 0.9 Feuille de route

Les trois premières priorités de l’ancienne feuille de route sont acquises. Reste, par ordre d’utilité :

- **Audix D6** — repasse en tête : ferme la vulnérabilité de la peau non percée, que le PGA52 de la MJC ne couvre qu’en prêt.

- **Capacité DI** — première tranche acquise (Palmer River Elde, stéréo). Une seconde DI stéréo ne se justifie que si les dates à machines multiples se répètent.

- **Micros de toms** (e604 ou équivalent, 2 à 3) — la MJC en prête deux ; l’achat ne devient utile que pour ne plus dépendre du prêt. À noter : dès qu’ils sont en poste, le HPF des overheads change de logique (voir 3.1).

- **Sennheiser e609** — seconde guitare, et libère le SM57. *⚠️ À nuancer : la réputation de l’e609 est nettement plus partagée que celle de l’e604.* Les retours sont mitigés sur guitare face au SM57, plus favorables sur kick. Ce sera probablement l’acquisition la moins décisive de la liste — la garder pour le gain de temps en changement rapide (il se pose contre la grille, sans pied) plutôt qu’en attendant un meilleur son que le SM57 déjà en poste. *Pourquoi il a quand même été choisi plutôt qu’un e906 :* son pic naturel 5–7 kHz sied bien au punk/métal, et le e906 mise sur un switch de présence passif — redondant dès qu’on est sur une console numérique à EQ paramétrique complet, ce qui est toujours le cas ici.

- **Remplacement des Beta58** si le test d’authenticité est négatif.

- **Second pied perche** — pour les toms ou une seconde guitare.

*Règle d’achat.* Revendeur agréé uniquement, Thomann ou SonoVente. Sur l’occasion, vérifier avant de payer et évaluer la valeur nette après revente des éléments inutiles.

# PARTIE 1 — PHILOSOPHIE & ARCHITECTURE

**L’objectif, avant toute technique : un rendu professionnel et musical de haut niveau — pas seulement un rendu qui n’est pas faux.** Tout ce qui suit dans ce guide n’a de sens qu’au service de ça. La rigueur (sourcer chaque valeur, distinguer un fait d’une inférence, ne rien inventer) n’est pas une fin en soi : c’est ce qui permet de distinguer une technique qui marche vraiment d’une technique qui semble seulement plausible, et donc de choisir la meilleure plutôt que la plus prudente.

Concrètement, ça veut dire mobiliser **toute technique réelle et documentée** qui s’applique à un problème donné — un geste historique propre à la machine identifiée (2.8), une fonction native d’une autre console que le Fat Channel n’a pas (Partie 8), un outil qui règle le problème à la racine plutôt qu’un montage de contournement — plutôt que de se rabattre par réflexe sur la solution la plus générique. Une réponse exacte mais mixologiquement plate n’est pas un objectif atteint.

Ce niveau se juge à l’esthétique propre de chaque style couvert — agressif et dense en punk/métal, spacieux et dynamique en dub, présent et large en hip-hop, jamais un traitement identique appliqué partout — et s’obtient en exploitant au maximum le matériel **réellement possédé pour la date**, pas un matériel idéal imaginé. C’est le fil qui relie l’identification des machines de référence en 2.8, les gestes historiques qui en découlent, et le choix conscient de colorer ou non un canal en 1.1 ci-dessous.

## 1.1 Nettoyage → Coloration → Glue

**Sur les canaux : NETTOYAGE par défaut, coloration si la source le justifie.** EQ soustractif, coupes chirurgicales, compresseur transparent : c’est le point de départ sur la majorité des canaux. Mais ce n’est pas une interdiction — et le guide lui-même ne l’a jamais respectée à la lettre. La caisse claire tourne sur un Class-A FET (coloré, c’est le but), la contrebasse et l’acoustique sur un Classic Compressor (coloré), le saxophone sur un Tube Leveling Amplifier (coloré). Ces choix sont bons. La vraie règle : **on colore au canal quand la source le demande et qu’on sait pourquoi, pas par réflexe**. Un canal coloré sans raison, c’est une couleur qu’on ne pourra plus retirer au bus.

**Sur les bus : COLORATION.** Compresseur vintage pour coller le groupe, puis EQ pour le caractère. Ordre inversé par rapport aux canaux.

*Pourquoi Compresseur → EQ sur les bus : trois raisons distinctes, pas une règle plate.* Sur **Drums et Instru**, le compresseur doit réagir au mélange brut ; si l’EQ passait avant, un boost sur une bande changerait le niveau que le compresseur voit sur cette bande précise, et on perdrait le contrôle de ce qui déclenche réellement la compression. Sur le **Bus Voix**, l’effet serait carrément pervers : booster les 4,8 kHz agressifs *avant* le Tube CB ferait que cette bande, désormais plus forte, déclencherait *plus* de réduction de gain sur elle-même — on annulerait une partie du boost qu’on vient de faire. Sur le **Bus Parallel**, l’EQ sert explicitement à remettre en forme *après* l’écrasement : l’ordre inverse n’aurait aucun sens. Les quatre bus tombent sur le même ordre, mais pour trois raisons différentes selon leur fonction.

**Sur le Master : GLUE FINALE.** Everest C100A à 1–2 dB maximum, EQ à ±1–2 dB maximum. Si le compresseur Master travaille plus de 2–3 dB, le problème vient des bus.

## 1.2 Gain Staging global

Ce sont des **zones de travail**, pas des cibles à atteindre. Un bus qui tourne à -10 dBFS n’a rien d’anormal : ce qui compte, c’est d’avoir de la marge partout et de savoir pourquoi on est là.

| **Étape** | **Zone de travail** | **Indicateur** |
| --- | --- | --- |
| Preamp canaux | Peak -12 à -6 dBFS | LED verte/jaune, jamais rouge |
| Faders canaux | Position U (Unity) | Repère U sur la tranche |
| Bus de groupe | Peak -6 à -3 dBFS | Mètre bus confortable |
| Master avant limiteur | Peak -3 à -1 dBFS | RMS indicatif, voir 5.1 |
| Master après limiteur | **Peak -1 dBFS maximum** | LED qui ne clignote presque jamais |

*Pourquoi le niveau des bus compte vraiment.* Ce n’est pas qu’une question de marge. Deux des compresseurs utilisés sur les bus n’ont **pas de Threshold indépendant du niveau d’entrée** : sur le **Class-A FET**, c’est l’Input Gain qui pilote seul le déclenchement, et sur le **FC-670**, c’est l’Input Gain qui est le moteur principal. Sur ces modèles, changer le niveau qui entre dans le bus change la façon dont le compresseur travaille. Un bus 6 dB plus bas ne donne pas le même son 6 dB plus bas : il donne un son moins compressé. C’est la vraie raison de fixer une zone et de s’y tenir d’une date à l’autre.

*Pourquoi -1 dBFS et pas -0,1 dBFS au Master.* Les crêtes reconstruites à la conversion peuvent dépasser la valeur affichée par les mètres, qui ne lisent que les échantillons. Coller le Master à -0,1 dBFS ne laisse aucune marge pour ça, et n’apporte **aucun volume utile** : le niveau en salle se règle aux amplis et au processeur de diffusion, pas en poussant la console contre son plafond numérique. Une console qui sort à -1 dBFS et un système correctement calé sonneront toujours plus fort et plus propre qu’une console écrasée contre zéro.

## 1.3 Architecture FlexMix — 16 bus

Les canaux s’assignent uniquement à leur sous-groupe. Seules les sources ligne vont directement au Main.

| **FlexMix** | **Mode** | **Nom** | **Rôle** |
| --- | --- | --- | --- |
| 1 | Aux | Retour 1 | Sortie Mix 1 → 16R |
| 2 | Aux | Retour 2 | Sortie Mix 2 → 16R |
| 3 | Aux | Retour 3 | Sortie Mix 3 → 16R |
| 4 | Aux | Retour 4 | Sortie Mix 4 → 16R |
| 5 | Aux | Retour 5 | Batteur ou side-fill |
| 6 | Aux | Retour 6 | Second side-fill ou invité |
| 7 | Aux | Cue / Talkback | Écoute isolée, envoi régie |
| 8 | Aux | Réserve | Console invitée, enregistrement, secours |
| 9 + 10 | Subgroup stéréo | Bus Drums | Batterie complète, kick inclus |
| 11 + 12 | Subgroup stéréo | Bus Instru | Basse, guitares, claviers, cuivres |
| 13 + 14 | Subgroup stéréo | Bus Voix | Toutes les voix |
| 15 | Subgroup MONO | Bus Parallel | Compression parallèle, fader -∞ par défaut |
| 16 | Subgroup **MONO** | Bus Divers | Imprévus, effets externes |

**Pourquoi cette répartition.** Le kick est dans le Bus Drums pour la cohésion rythmique — le Brit Comp colle l’ensemble de la frappe d’un seul geste, et avec des overheads qui portent tout le kit, ce regroupement prend encore plus de sens. La basse est dans le Bus Instru pour la cohésion harmonique, liée aux guitares et claviers par le FC-670.

**Conséquence.** Kick et basse ne partagent plus de bus mais se somment au Master : le cut à 60 Hz sur la basse reste indispensable.

**Bus Divers, mono par défaut.** Les 16 FlexMix sont tous alloués, donc Bus Divers ne dispose que d’un seul FlexMix — mono. Pour l’écrasante majorité des cas (un instrument imprévu, un effet externe ponctuel), c’est suffisant. Si une date précise amène une source stéréo imprévue (un clavier d’invité, par exemple), emprunter temporairement le FlexMix 8 (Réserve) pour former une paire stéréo 8+16 le temps du set, à condition qu’il ne serve pas déjà à un enregistrement ou une console invitée ce soir-là.

**Les quatre sous-groupes fixes — la réserve qu’on oublie.** En plus des 16 FlexMix, le manuel documente que **tous les modèles StudioLive à 32 canaux disposent de quatre sous-groupes dédiés**, distincts des FlexMix. Ils offrent le même traitement Fat Channel qu’un sous-groupe FlexMix (compresseur, EQ, limiteur — le gate est annoncé en 5.3.2 mais absent du tableau 6.1, voir 2.6), se couplent en stéréo et s’assignent au Main.

*Cette architecture ne les utilise pas*, et c’est un choix : les bus du guide restent sur les FlexMix, où ils sont éprouvés, documentés et rappelés correctement par les scènes. Mais il faut savoir qu’ils existent, parce que ça change la réponse à deux questions récurrentes :

- **« Je n’ai plus de FlexMix pour un besoin ponctuel. »** Faux, en réalité : quatre bus de groupe complets restent libres. Un sous-groupe de cuivres, un groupe de chœurs, un bus d’effets externes sur une grosse date — tout ça peut vivre sur un sous-groupe fixe sans toucher aux FlexMix ni à l’architecture.

- **« Un renfort retardé mange un retour. »** Pas forcément — voir 7.8, le manuel indique que les sous-groupes de la 32SC peuvent être envoyés sur le réseau AVB.

*Limite à connaître — et sa vraie portée.* Sur la 32SC, les sous-groupes fixes **n’ont pas de sortie analogique dédiée** (contrairement aux 32S, 32SX et 32). Mais « pas de sortie dédiée » ne veut pas dire « pas de sortie » : le manuel (12.3.2, Analog Sends) liste les **sous-groupes A–D parmi les mixages qu’on peut envoyer aux sorties Mix physiques** par le patch numérique, au même titre que les FlexMix, les départs d’effets, le Main et le bus Solo. Ils figurent aussi dans les sources envoyables en USB (12.3.4). Le coût : la sortie Mix utilisée n’est plus disponible pour le FlexMix qui l’occupait par défaut. *Jamais essayé ici — voir 8.7.*

*Premier usage prévu de cette réserve :* le **Bus Basse** optionnel, décrit en 4.6.

## 1.4 Stagebox 16R

Liaison CAT5e ou CAT6 entre les ports AVB. *La latence propre du lien AVB n’est pas chiffrée par le manuel, qui ne donne que la latence totale en routage local (1,9 ms, entrée analogique vers sortie analogique) ; le « moins de 1 ms » des versions précédentes n’avait pas de source.* Les 16 préamplis apparaissent comme canaux supplémentaires, gain et fantôme pilotables depuis la surface ou UC Surface. FlexMix 1 à 6 routés vers les sorties analogiques mono de la 16R.

**⚠️ Les entrées/sorties réelles de la 32SC — plus larges que ce que le guide supposait.** Vérification faite dans le manuel (3.1.4) :

- **Sorties FlexMix : 10 physiques**, soit 6 XLR mâles **plus** 4 jacks TRS. Le guide a longtemps raisonné comme si la limite était de 6. Elle ne l’est pas. Et le manuel précise que **n’importe quel FlexMix peut être acheminé vers n’importe quelle sortie** — l’ordre par défaut (FlexMix 1 → sortie Mix 1, etc.) n’est qu’un défaut, pas une contrainte. Concrètement : un plateau qui demande 7 ou 8 circuits de retour n’est pas hors capacité, contrairement à ce que l’allocation FM 1–6 laissait croire.

- **Seize bus, mais pas seize sorties à prévoir.** Les FlexMix 9 à 16 sont en mode sous-groupe et vont au Main : ils n’occupent aucune sortie physique. Seuls les FlexMix 1 à 8 (retours, cue, réserve) et les éventuels renforts en ont besoin. Dans le câblage de ce guide, FlexMix 1 à 6 sortent sur la 16R ; les 10 sorties FlexMix de la 32SC restent alors disponibles pour le cue, la réserve, un renfort (7.8) ou des retours supplémentaires — n’importe quel FlexMix vers n’importe quelle sortie, par le patch numérique. *Le nombre exact de sorties de la 16R n’est pas documenté au projet (son manuel n’y est pas) : ne pas en déduire de capacité au-delà des six utilisées.*

- **Sous-groupes dédiés : aucune sortie analogique** sur la 32SC (les 32S, 32SX et 32 en ont 4). Sans conséquence tant qu’ils vont au Main.

- **Entrées analogiques locales : 16**, soit 8 mixtes micro/ligne **plus 8 XLR micro uniquement**. La 32SC seule plafonne donc à 16 canaux analogiques ; au-delà, la 16R est obligatoire.

- **⚠️ Les 8 entrées « micro uniquement » n’acceptent une source ligne que via un boîtier DI** — c’est écrit noir sur blanc dans le manuel. Ça resserre encore le goulot d’étranglement des DI déjà identifié en 0.5 : un synthé ou une machine branché sur l’une de ces 8 entrées consomme une DI *en plus* de celles déjà comptées pour la basse et les claviers.

**16R en autonome, sans console physique — cas réel (formation Crystal Distortion).** Les racks StudioLive III sont conçus pour fonctionner **pilotés uniquement par UC Surface** (Mac/Windows/iPad), sans 32SC connectée — pertinent pour prêter la 16R seule sur une session encadrée par quelqu’un d’autre. **⚠️ Un routeur physique est obligatoire dans la chaîne** : la 16R n’émet pas son propre WiFi. Filaire ou sans fil, le chemin passe toujours par un routeur relié au port Control de la 16R. UC Surface et QMix-UC acceptent plusieurs appareils connectés simultanément (ordinateur du formateur + tablette de secours), avec gestion des permissions par appareil.

## 1.5 Gestion de l’alimentation fantôme

Nouveau point de vigilance : **trois micros du parc et la DI active exigent du 48 V**, alors qu’aucun n’en demandait avant. La Palmer River Elde reste à vérifier : son type (passive ou active) n’est pas documenté au projet (0.5).

*Micros à fantôme :* BD 500 Beta (kick), les deux Lewitt LCT 040 (overheads). Plus la DI active selon la source.

*Dépannage à connaître :* le **SM57 et le SM58 reposent sur la même cartouche** ; la différence principale est la grille (FAQ Shure). Conséquences citées par Shure : la grille du SM57 place la capsule plus près de la source, d’où un **effet de proximité plus marqué**, et un **niveau légèrement plus élevé au-dessus de 5 kHz**. La boule du SM58 intègre un filtre anti-pop. En cas de casse en pleine date, un SM57 peut réellement dépanner en voix (et l’inverse sur un ampli), sans que ce soit un pis-aller sonore.

*Micros sans fantôme :* Audix i5, SM57, SM58, Beta58. Ne pas leur envoyer de 48 V par facilité — un dynamique symétrique ne craint rien en théorie, mais un câble légèrement défectueux plus du 48 V donne des bruits difficiles à diagnostiquer en pleine date.

*Procédure.* Fantôme **coupé** au branchement et au débranchement, canal **muté** pendant l’opération. Activer après, canal par canal. Le claquement d’un condensateur qui s’alimente dans une diffusion à niveau peut endommager un moteur d’aigu.

*Diagnostic.* Un souffle inhabituel sur les overheads oriente vers l’alimentation, pas vers le micro — les LCT 040 tirent 7,2 mA chacun.

*Sur la 16R.* Le fantôme se gère par canal depuis la 32SC ou UC Surface. Vérifier au line check que les trois canaux concernés sont bien alimentés : un kick muet en début de set, c’est presque toujours ça.

## 1.6 Comment lire une fiche preset

Chaque fiche suit **l’ordre des commandes du Fat Channel** :

**Micro et placement → Phantom → Gain → HPF → Gate/Expander → Compresseur → EQ → Limiteur → Bus.**

*L’ordre des commandes n’est pas l’ordre du signal.* **Par défaut, la console fait passer le signal dans le compresseur, puis dans l’EQ** (manuel 6.8.4, bouton **Comp>EQ** de l’écran du compresseur). **Ce guide veut l’EQ avant le compresseur sur les canaux** — le conseil du manuel lui-même : « placer l’égaliseur avant le compresseur […] donne une réponse plus naturelle » — et garde l’ordre par défaut sur les bus (1.1). *Conséquence pratique :* sur chaque canal d’entrée, **inverser l’ordre avec ce bouton**, puis l’enregistrer dans les presets de Fat Channel et les scènes de style. Les versions précédentes affirmaient que l’EQ passait avant le compresseur par défaut : c’était faux. *Registre 8.7 :* vérifier sur un canal neuf, et que le réglage est bien rappelé avec la scène.

*Les valeurs sont des points de départ.* Les fréquences de coupe se trouvent à l’oreille sur le kit du jour. Les valeurs indiquées sont la zone où chercher, pas une vérité.

# PARTIE 2 — RÉFÉRENTIEL FAT CHANNEL

Cette partie documente le comportement **réel** des plugins tel que constaté sur le firmware 3.4.0.111374, y compris là où il s’écarte de ce qu’on attendrait d’un équivalent studio.

## 2.1 Compresseurs

**Standard Compressor** *(inclus d’origine)*

Transparent, numérique, sans coloration. Commandes : Threshold, Ratio, Attack, Release, Gain, Soft Knee, Auto, Key Filter, Key Source.

C’est le scalpel : aucune opinion sonore. Sur les canaux, il fait le ménage avant que le bus ajoute la couleur.

⚠️ **Le mode Auto ne concerne pas que le Release. Le manuel est formel : quand Auto est actif, les commandes d’attaque et de retour sont toutes les deux inopérantes, et la console impose Attack 10 ms / Release 150 ms. Écrire « Attack 3 ms, Release Auto » n’a donc aucun sens : l’attaque de 3 ms ne sera jamais appliquée. Les versions du guide antérieures à la V15 commettaient cette erreur sur trois presets.** *Règle : dès qu’une attaque autre que 10 ms est voulue, le Release doit être réglé manuellement. Le mode Auto reste utile quand 10/150 convient et qu’on manque de temps — c’est le cas sur beaucoup de sources.*

**Tube Leveling Amplifier** *(inclus d’origine)*

Opto-électronique à lampes, attaque et release adoucies naturellement. Commandes : Gain (entrée — pilote indirectement la compression), Peak Reduction, **sélecteur Lim/Cmp**, Key Filter, Key Source.

*⚠️ Le sélecteur compresseur/limiteur était absent des versions précédentes du guide.* En mode **compresseur**, le ratio est variable de 1:1 à 10:1. En mode **limiteur**, de 10:1 à 20:1, ce qui écrête les crêtes bien plus agressivement. Vérifier sa position : un Tube Leveling qui semble trop dur est souvent simplement resté en mode limiteur.

Le compresseur invisible : il lisse sans qu’on l’entende travailler. Moins de contrôle fin que le Standard, plus musical sur les sources continues — orgue, sax, Rhodes.

**Class-A FET Compressor** *(inclus d’origine)*

FET agressif et percutant. Commandes : Input Gain, Output Gain, Attack, Release, Ratio (4 / 8 / 12 / 20 / All), Key Filter. *Le manuel (6.5.3) n’affiche que les valeurs par défaut — Attack 0,10 ms, Release 250 ms — sans chiffrer les plages.* Les plages « 0,1–60 ms » et « 250 ms–3 s » des versions précédentes n’avaient pas de source. **À relever sur la console** : si 250 ms est la butée basse du Release, le Release de 150 ms prescrit sur la caisse claire (3.1) n’existe pas, et la valeur la plus courte disponible s’impose (registre 8.7). **La même réserve vaut pour toutes les valeurs d’Attack de ce modèle dans le guide** (3 ms sur la caisse claire et la trompette, 5 ms sur la guitare rythmique et la variante hip-hop) : si la plage réelle ne les contient pas, appliquer la règle de repli du Bloc assistant — valeur disponible la plus proche, et la plus lente si deux valeurs encadrent — et la consigner.

*⚠️ Pas de commande Threshold sur ce modèle. C’est l’Input Gain qui pilote seul le déclenchement : augmenter l’Input Gain revient à baisser le seuil effectif. Régler l’Input Gain en surveillant la réduction de gain, puis compenser à l’Output Gain.*

À 20:1 ou en position All, il devient un limiteur dur. Son mordant est exactement ce qu’on cherche sur une caisse claire punk ou une guitare rythmique en palm mute.

**Brit Comp** *(Classic Studio Bundle)*

Double VCA britannique, punch marqué, légère saturation sur les transitoires. Commandes : Threshold, Attack, Ratio, Release, Makeup, Key Filter, Sidechain.

La référence pour le Bus Drums. Il transforme des sources séparées en un groupe cohérent qui claque — kick compris depuis la nouvelle architecture.

**Classic Compressor** *(Vintage Channel Strips Bundle)*

Doux et polyvalent. Commandes : Threshold, Gain, Recovery, Ratio, Key Filter.

*⚠️ Pas de commande Attack. Seul le Recovery (release) est réglable. C’est ce qui le rend imprécis sur les percussions et très musical sur les instruments à dynamique large et lente — contrebasse, guitare acoustique, accordéon.*

**Comp 160** *(Modern Classics Bundle)*

VCA extrême, graduation Compression non linéaire (de 0 à ∞, ce n’est pas un ratio numérique). Commandes : Threshold, Compression, Output Gain, Key Listen, Key Filter, Sidechain.

*⚠️ Le panneau porte deux inscriptions lumineuses, BELOW et ABOVE (deux LED), que l’addendum PreSonus ne mentionne nulle part : il ne décrit qu’un Threshold continu (addendum 3.3) — contrairement à d’autres bascules (Peak/Trough du Solar 69, Fixed/Manual du Tube CB) qui sont, elles, expliquées. Le guide parlait jusqu’ici d’une « position BELOW » à tenir ; tant que la vérification ci-dessous n’est pas faite, **piloter le Threshold à l’oreille et au mètre de réduction de gain**, sans chercher à régler BELOW ou ABOVE.*

*Ce que fait l’original — inférence à vérifier.* Sur le dbx 160 d’origine, dont le Comp 160 est très probablement l’émulation (2.8), le manuel de l’émulation Universal Audio décrit **Below** et **Above** comme deux **voyants d’état** : Below allumé, aucune compression ; Above allumé, le signal dépasse le seuil, avec une luminosité qui croît avec le dépassement. Si PreSonus a reproduit ce comportement, ce ne sont pas des positions à choisir, et sur un bus qui compresse de 8 à 12 dB (4.4), c’est Above qui doit s’allumer. **Vérification console :** sur le Bus Parallel en balance, observer lequel des deux s’allume quand le mètre de réduction de gain bouge, et si l’un des deux réagit au toucher. *Registre 8.7.*

Réservé au Bus Parallel. Sa violence est un outil : le signal original reste intact ailleurs, on mélange l’écrasé en appoint.

**Everest C100A** *(Modern Classics Bundle)*

Réduction douce et naturelle. Commandes : Attack (Fast/Medium/Slow), Release (Fast/Medium/Slow), Gain, Gain Reduction, Key Filter, Sidechain.

Conçu pour ne pas s’entendre. Sur le Master : 1–2 dB maximum. Ses commandes en Fast/Medium/Slow forcent des choix musicaux plutôt que techniques. *Échelle :* l’addendum (3.4) nomme trois positions — Fast, Medium, Slow — sans chiffrer aucun temps. *Méthode :* même démarche que le Tube CB ci-dessous, mais par positions : une position plus lente en Attack si les attaques s’aplatissent, une position plus lente en Release si le niveau pompe ; au mètre, ne jamais dépasser la réduction prescrite.

**FC-670** *(Classic Studio Bundle)*

Compresseur/limiteur des années 1950 (addendum), modèle du **Fairchild 670** (2.8) — un compresseur **à lampes à pente variable (« variable-mu »)**, pas un optique. Commandes : Input Gain, Threshold, Time Constant (1–6, pilote Attack et Release ensemble), Key Filter, Sidechain.

*⚠️ Modèle non conventionnel. L’Input Gain est le moteur principal : c’est lui qui détermine la profondeur de compression. Le Threshold n’intervient qu’en second pour affiner le point de déclenchement. Toujours régler l’Input Gain en premier, contrairement au réflexe habituel.*

*Time Constant — ce qui est documenté et ce qui ne l’est pas.* L’addendum dit seulement que la commande « règle les temps d’attaque et de release fixes », sans les chiffrer. Sur le Fairchild 670 d’origine — et sur l’émulation HD 670 de la Midas HD96, dont le manuel au projet donne le tableau — les positions **1 à 4 sont des temps fixes de plus en plus lents** (release d’environ 0,3 s en 1 jusqu’à 5 s en 4 ; **2 s en position 3**), et les positions **5 et 6 ont un release dépendant du programme**. Que le FC-670 suive exactement cette échelle est une **inférence**, à confirmer à l’oreille. **Position de référence de ce guide : 3**, lente et fixe, pour le Bus Instru (4.2) et le reggae (6.5) : les graves ont le temps de passer avant que la compression intervienne. C’est le compresseur du Bus Instru.

**RC-500 Compressor** *(PreSonus Bundle — gratuit)*

FET rapide, **ratio fixe 3:1 non modifiable**. Commandes : Threshold, Attack (**0,5 ms en butée Fast à 10 ms en butée Slow**), Release (**40 ms en butée Fast à 500 ms en butée Slow**), Makeup, Key Filter, Sidechain (addendum 3.6). « Attack Fast, Release Slow » dans ce guide = les deux butées.

Son ratio fixe est polyvalent sur la majorité des sources. Rapidité FET là où un opto serait trop lent. Premier choix sur la basse DI.

**Tube CB** *(Vintage Channel Strips Bundle)*

Opto-lampe, ultra-musical, préserve la clarté même en compression appuyée. Commandes : Gain, Attack, Threshold, Release, Ratio, Mode Fixed/Manual, Key Filter, Sidechain.

*⚠️ Sur les voix, toujours en mode Manual. Le mode Fixed verrouille Attack à 1 ms et Release à 50 ms sans aucun réglage possible — trop rigide dès qu’un chanteur ou un MC sort du cadre. En Manual : Fast/Fast pour les styles rapides et agressifs, Slow/Slow pour laisser respirer la dynamique.*

*Ce que « Fast », « Medium » et « Slow » veulent dire ici.* Sur le panneau du Tube CB (addendum 3.7), Attack et Release sont des **boutons rotatifs continus**, marqués « fast » à une extrémité et « slow » à l’autre. Dans tout ce guide, « Fast » et « Slow » désignent donc les **butées** du bouton, et « Medium » sa **mi-course** — pas des positions crantées. L’addendum ne chiffre pas les temps correspondants (contrairement au VT-1, documenté de 0,5 à 10 ms en attaque et de 40 à 500 ms en release) : régler à l’oreille, en partant de ces repères.

*Méthode de convergence (une minute, voix seule en balance).* **Attack d’abord** : partir de la position prescrite ; si les consonnes d’attaque s’émoussent, tourner vers Slow jusqu’à ce qu’elles repassent ; si les crêtes passent sans être tenues, tourner vers Fast. **Release ensuite** : si le souffle et la salle remontent entre les mots (pompage), tourner vers Slow ; si la voix reste écrasée après une note forte, tourner vers Fast. **Terminer au mètre** : la réduction lue doit être celle que prescrit la fiche ou la scène ; sinon corriger le Threshold, pas les temps.

**VT-1 Compressor** *(PreSonus Bundle — gratuit)*

FET-lampe, raffiné. Commandes : Threshold, Attack (0,5–10 ms), Release (40–500 ms), Ratio variable, Gain, Key Filter, Sidechain.

Rapide comme un FET, chaud comme une lampe. Le compresseur de finesse pour une voix lead qui joue avec sa dynamique — typiquement le MC hip-hop.

## 2.2 Gate / Expander

**Pourquoi un gate en live, la vraie raison.** Ce n’est pas d’abord une question de propreté. Le *Yamaha Sound Reinforcement Handbook* documente le principe **NOM** (Number of Open Mics) : **chaque doublement du nombre de micros ouverts simultanément coûte 3 dB de gain avant larsen sur tout le système.** Passer de 4 à 8 micros ouverts, c’est 3 dB de marge perdue avant que ça siffle — sur la totalité de la façade et des retours, pas seulement sur les micros concernés. Sur un kit 4 micros plus charley, voix et cuivres, ce n’est pas une abstraction, c’est du gain que tu payes cash.

Un gate qui referme un micro inutilisé le retire temporairement du compte NOM. **C’est la justification première du gate en concert**, avant même la question de la repisse — et c’est ce qui le rend plus utile en live qu’en studio.

*Confirmation externe du choix du Range modéré.* Le même ouvrage distingue explicitement les gates « tout ou rien », dont l’ouverture s’entend, de ceux qui réduisent le niveau d’une quantité finie pour éviter un changement brutal du bruit de fond. C’est exactement le raisonnement derrière les Range modérés prescrits plus loin sur le kick et les cuivres — une source indépendante confirme la direction.

Deux modes distincts, avec des commandes différentes — c’est le point que la V12 avait mal transcrit et qu’il faut corriger.

**Mode Gate** — Threshold, **Range**, Attack, Release, Key Listen, Key Filter. Le Range est un vrai réglage continu : il fixe l’ampleur de l’atténuation appliquée sous le seuil, de quasi rien jusqu’à -∞. **Ce n’est pas tout ou rien.** Un Range à -20 dB laisse un fond de signal audible et discret sous le seuil ; un Range à -∞ coupe totalement. C’est cette commande qui permet de doser une réduction douce plutôt qu’une coupure nette.

**Mode Expander** — Threshold, Attack, Release, Key Filter. Ici, et seulement ici, **le Range disparaît** : le comportement est celui d’un expander à pente fixe, plus doux et plus progressif qu’un gate, mais sans réglage d’ampleur.

*Conséquence pratique :* sur une source où on veut une atténuation partielle et dosée (un cuivre entre deux phrases, par exemple), le mode **Gate avec un Range modéré** (-15 à -25 dB) est l’outil adapté — pas l’Expander, qui n’offre pas ce dosage, et pas le Gate en Range -∞, qui coupe tout. Sur une source où le silence total entre les coups est recherché (caisse claire, toms), Gate avec Range -∞ reste le bon choix.

Sur les sources percussives, régler le Threshold avec prudence quand ça change vite : un seuil mal calé coupe des attaques au lieu d’atténuer du bruit de fond. En cas de doute en live, mieux vaut un gate ouvert (ou un Range moins profond) qu’un gate qui mange les frappes faibles.

**Le Key Filter contre la repisse — ce qu’il fait vraiment**

C’est l’outil le plus sous-utilisé du bloc Gate, et le manuel PreSonus en donne l’exemple exact de ton problème : un gate posé sur une caisse claire risque de capter assez de grosse caisse pour s’ouvrir à chaque coup de kick ; régler le filtre de gate pour supprimer certaines basses fréquences empêche le kick de déclencher l’ouverture.

**Le Key Filter n’agit que sur ce que le gate *écoute*, jamais sur ce qui passe dans le son.** Le canal reste intact, seule la décision d’ouvrir change.

*Valeurs de départ, à caler au Key Listen :*

- **Caisse claire (top et bottom) — Key Filter 100 à 150 Hz.** Retire la fondamentale du kick de la détection. Le gain le plus net du lot : c’est le cas d’école du manuel.

- **Toms — Key Filter 80 à 100 Hz**, selon le tom. Attention à ne pas monter trop haut : la fondamentale d’un floor tom descend vers 60–80 Hz et on couperait la détection du tom lui-même.

- **Charley — Key Filter 150 Hz.** Le HPF du canal est déjà à 400 Hz, mais le Key Filter travaille sur une chaîne séparée : il faut le régler aussi.

*⚠️ Ce que le Key Filter ne peut pas faire : la cymbale.* Le filtre ne retire **que les basses fréquences** de la détection — il n’existe aucun passe-bas côté sidechain sur ce Gate. Une cymbale qui repisse dans un micro de tom ou de kick est le problème inverse (source voulue grave, repisse aiguë), et **aucun réglage de Key Filter n’y changera quoi que ce soit**. Contre la cymbale, les vrais leviers sont le Threshold bien calé, les temps ajustés, et surtout le placement physique du micro — directivité, distance, angle. Ne pas perdre de temps à chercher un réglage qui n’existe pas.

*Validation croisée.* Le schéma de traitement d’un système de renfort réel publié dans le Yamaha Handbook (fig. 17-3) attribue : overheads = compression seule, aucun gate ; toms = gate seul ; charley = aucun traitement ; caisse claire = gate + EQ + limiteur. C’est exactement l’architecture minimaliste déjà en place dans ce guide — bon signe que l’approche n’est pas une préférence personnelle mais la pratique documentée.

*Technique avancée, à connaître sans la prescrire.* Le même ouvrage décrit le câblage du gate de caisse claire pour qu’il se déclenche sur le signal du **kick** plutôt que sur le sien, forçant une resynchronisation rythmique. Sur StudioLive, c’est le **Key Source** (voir 2.5) appliqué à un gate. Outil correctif de dernier recours, pas une réponse à la repisse.

## 2.3 Égaliseurs

**Standard EQ** *(inclus)* — Entièrement paramétrique, transparent. **4 bandes sur les canaux (Low, L-Mid, H-Mid, High), 6 bandes quand un bus est sélectionné** — confirmé par le manuel — plus le HPF. Chaque bande a gain, fréquence et Q réglables. **Les bandes Low et High passent en plateau** (boutons Low Shelf et High Shelf, manuel UC Surface 3.3, points 8 et 10 ; le mode d’emploi de la console ne les mentionne pas — les activer depuis UC Surface). En plateau, la fréquence règle le point du plateau (même source) ; **ce que fait alors le Q n’est pas documenté** — les bandes médium restent des cloches à Q réglable. Le couteau suisse pour la chirurgie sur canal.

**Passive Program EQ** *(inclus)* — Lampe passif, Low et High avec Boost et Atténuation séparés et interactifs. Courbes toujours musicales même poussées. Poste : Master.

**Vintage 1970s EQ** *(inclus)* — 4 bandes (manuel 6.6.3). **Low en plateau, fréquence réglable (60 Hz par défaut)** ; **L-Mid et H-Mid à fréquence réglable** (700 Hz et 4,8 kHz par défaut) ; **High : gain seul**, sa fréquence n’est pas réglable et le manuel ne la chiffre pas. *Correction V33 :* les versions précédentes décrivaient quatre fréquences fixes, dont un Low « vers 200 Hz » et un High « vers 12 kHz » — aucune de ces deux valeurs n’est dans le manuel. **Conséquence sur le Bus Voix :** le Low reste à 60 Hz tant qu’on ne le déplace pas ; un +2 dB à 60 Hz sur des voix ne remonte que du bruit de scène. **Régler Low Freq vers 200 Hz avant de toucher son gain.** Le +3 dB sur le H-Mid donne cette présence agressive caractéristique. Poste : Bus Voix sur les styles agressifs.

**Alpine EQ-550** *(Classic Studio Bundle)* — 3 bandes qui se recouvrent, **7 points de fréquence fixes par bande, cinq crans de boost ou d’atténuation**, Peak ou Shelf commutable sur les bandes haute et basse, plus un **filtre passe-bande commutable de 50 Hz à 15 kHz**. Les fréquences fixes forcent des choix musicaux plutôt que techniques. Poste : Bus Instru, et Bus Voix sur les styles chauds.

*⚠️ La V14 annonçait « paliers de ±2 dB ». L’addendum ne dit pas ça : il parle de cinq crans par bande, sans en chiffrer la valeur en décibels. Régler à l’oreille en comptant les crans, pas en supposant une valeur.*

**Baxandall EQ** *(Modern Classics Bundle)* — Plateaux glissants très larges, Low Cut et High Cut à 12 dB/oct. Commandes : Low Cut (12–54 Hz), Low Shelf (74–361 Hz), High Shelf (1,6–18 kHz), High Cut (≈7,5–70 kHz).

*⚠️ L’addendum PreSonus contient lui-même une coquille sur le High Cut : le texte officiel recopie mot pour mot la description du Low Cut (« 54 à 12 Hz »), ce qui est impossible pour un filtre coupe-haut. Lecture directe du panneau : la zone du knob est clairement libellée en kHz (même zone « HIGH kHz » que le High Shelf), avec des graduations visibles de 7,5 à 70 kHz environ. Dans la pratique, ce contrôle n’est pas utilisé dans ce guide — le laisser OFF partout.*

*⚠️ Libellés trompeurs sur ce modèle.* Le potentiomètre marqué **« Low Shelf » règle la fréquence** du plateau grave (74 à 361 Hz), tandis que celui marqué **« Low Frequency » règle le gain**. Même inversion côté aigu : « High Shelf » = fréquence (1,6 à 18 kHz), « High Frequency » = gain. Le savoir évite de tourner le mauvais bouton dans le noir.

*Poste attribué :* **canal Kick.** Ses plateaux larges asseoient les graves du kick sans créer de résonance, là où le Standard EQ demande de la chirurgie. Le Low Cut sert de HPF musical. C’est le seul endroit du guide où il est utilisé par défaut — ailleurs, en retouche exceptionnelle sur le Master.

**RC-500 EQ** *(gratuit)* — 3 bandes semi-paramétriques, Peak/Shelf commutable, Q optimisé par bande. Propre, sans artefact. Poste : Bus Parallel, pour remettre en forme après l’écrasement du Comp 160.

**Solar 69 EQ** *(Classic Studio Bundle)* — Britannique classique. Low (fréquence + gain), Mid (fréquence + gain) avec mode Peak/Trough, High (fréquence + gain), **plus un inverseur de polarité intégré** et le bypass.

⚠️ **Pas de Level Adjust sur ce modèle** — l’inscription visible sur le panneau est le libellé du High Band Gain, pas une commande séparée. Et **la bande High est à fréquence réglable** — elle n’est pas fixée à 10 kHz.

Le mode Trough transforme le Mid en notch précis pour éliminer une résonance. La bande High réglable permet de viser la zone de shimmer propre au kit du jour, généralement entre 8 et 10 kHz. Poste : Bus Drums.

**Tube EQ** *(Vintage Channel Strips Bundle)* — Passif lampe, **médiums uniquement — et c’est littéralement vrai** : lecture directe du panneau, les trois bandes sont graduées en kHz et couvrent **200 Hz à 5 kHz**, pas un hertz en dehors. Sa limitation est sa force : impossible de se tromper dans les graves ou les aigus, ils sont hors de portée.

*Architecture réelle, à connaître avant de s’en servir :* **Low PEAK (300 Hz – 1 kHz), Mid DIP (200 Hz – 5 kHz), High PEAK (1,5 – 5 kHz)**. Les bandes grave et aiguë **boostent**, la bande médium **creuse** — c’est imprimé sur le panneau. On ne choisit donc pas librement ; le geste que l’appareil propose est de remonter les bas-médiums et les haut-médiums en creusant entre les deux. C’est le fameux sourire dans les médiums, et c’est exactement pour ça que ce modèle existe.

Poste : chaleur subtile sur une voix. Option à tester sur le **Bus Voix Dub** (voir Partie 6), où sa portée limitée devient une protection : il ne peut pas entrer en conflit avec la chaîne de delay/reverb qui occupe déjà les extrêmes.

**Vintage 3-Band EQ** *(Vintage Channel Strips Bundle)* — Actif 3 bandes, Low et High en plateau, caractère mordant prononcé. Commandes complètes : Low freq/gain, Mid freq/gain, **commutateur Hi Q** (Q large ou étroit — l’addendum ne dit pas sur quelle bande ; il est numéroté entre Mid et High), High freq/gain, **filtre passe-haut intégré à fréquence réglable**, bypass, **inverseur de phase**. Poste : canal guitare ou voix qui manque de présence. À utiliser avec modération sur les bus.

**VT-1 EQ** *(gratuit)* — 4 bandes semi-paramétriques, Q optimisé par bande. Très musical, difficile d’en tirer quelque chose de laid. Poste : voix demandant finesse et transparence.

## 2.4 Limiteur — valeurs de Release par source

*💡 Le firmware 3.4.0.111374 expose une commande Release en plus du Threshold sur le limiteur du Fat Channel, accessible dans UC Surface. Sur une console au firmware antérieur, ce paramètre peut ne pas apparaître — vérifier la version installée avant de le chercher.*

*Deux précisions du manuel.* Le **taux du limiteur est de ∞:1** : c’est un mur, pas une compression forte — d’où des seuils réglés très haut (-1 à -3 dB) dans tout ce guide, le limiteur n’étant là que pour la protection. Et la page d’encodeurs qui contient Limiteur, départ mono et Delay **n’existe pas dans le Fat Channel physique des 32SX et 32SC** : sur cette console, ces trois paramètres se règlent à l’écran tactile ou dans UC Surface. Ce n’est donc pas une bizarrerie de firmware mais une caractéristique du modèle.

**⚠️ Ce que le limiteur est, et ce qu’il n’est pas.** Ce guide place un limiteur à -1 dB sur la plupart des canaux. C’est un **filet de sécurité, pas un étage de traitement** — et la distinction est essentielle, parce qu’un ratio ∞:1 n’a rien de musical.

Sur un canal correctement gainé (crête -12 à -6 dBFS) et correctement compressé, **un limiteur à -1 dB ne travaille jamais**. Il ne fait rien, il ne colore rien, il ne coûte rien. Il est là pour l’accident : le chanteur qui hurle dans le micro, le guitariste qui enclenche sa pédale de boost, le clavier dont on ouvre le filtre. C’est un airbag.

*La règle qui en découle :* **si le limiteur d’un canal travaille de façon visible et répétée, ce n’est pas un réglage à ajuster, c’est un symptôme.** Le gain est trop haut, ou le compresseur ne fait pas son travail. Corriger en amont, pas au limiteur. Un limiteur qui écrête régulièrement devient un élément sonore — et sur les sources graves, un élément sonore franchement laid.

*Où il est vraiment utile :* voix (surtout HF et chanteurs très dynamiques), sources électroniques et machines, canaux susceptibles de recevoir un niveau anormal. *Où il est le plus dispensable :* sources acoustiques stables déjà compressées, où il ne servira jamais. Le laisser ne coûte rien ; savoir qu’il ne sert à rien évite de croire qu’il fait partie du son.

| **Type de source** | **Release de départ** | **Pourquoi** |
| --- | --- | --- |
| Cymbales / Overheads | 50 ms | Laisse respirer les transitoires métalliques |
| Snare / Toms / Percussion | 70 ms | Équilibre contrôle et naturel |
| Kick / Basse | 150 ms | Voir l’encadré ci-dessous — ne pas raccourcir sans raison |
| Trompette / Sorties monitor | 100 ms | Réactivité sans pompage |
| Voix | 150–200 ms | Préserve la musicalité |
| Bus / Master | 250–300 ms | Glue finale, transparence |
| Guitares, cuivres, bois | 100 ms | Fondamentales au-dessus de 80 Hz : à 100 ms, le release couvre plusieurs périodes (encadré ci-dessous) |
| Claviers, synthé, orgue, Rhodes | 150 ms | Même règle que la basse : le registre grave peut descendre aussi bas qu’elle |
| Sources déjà mixées (table DJ, vinyle, playback) | 250–300 ms | Un mix complet se traite comme un bus |

*Ces valeurs sont des points de départ.* Le bon release dépend aussi de la profondeur de réduction, de la répétition des crêtes et du tempo. Le critère final est l’absence d’artefact audible, pas le chiffre.

*Les trois dernières lignes du tableau sont une extension de la règle par son propre mécanisme (ci-dessous), pas des valeurs éprouvées en concert.*

**Pourquoi 150 ms sur le kick et la basse — le mécanisme.** Ce n’est pas une superstition, et ça mérite d’être compris plutôt que récité. Une fondamentale de grosse caisse ou de basse tourne autour de 50 à 80 Hz, soit une période de **12 à 20 ms**. Si le release du limiteur descend vers quelques dizaines de millisecondes, la courbe de réduction de gain devient assez rapide pour suivre la forme d’onde elle-même, période par période, au lieu de suivre l’enveloppe de la note. Le limiteur se met alors à moduler la forme d’onde : c’est de la **distorsion harmonique**, pas de la limitation. Elle ne s’entend pas comme une saturation franche — on entend juste un bas qui devient sale et sans définition, sans savoir pourquoi. D’où la valeur longue. Plus haut en fréquence, le problème disparaît : une cymbale à 8 kHz a une période de 0,125 ms, aucun release réaliste ne peut la suivre.

*⚠️ Sur un canal individuel, prendre la ligne correspondant à la nature de la source. Sur un bus, prendre la ligne Bus/Master — sauf deux exceptions : le **Bus Parallel** (4.4 : il reçoit le kick, et le mécanisme de l’encadré ci-dessus s’applique dès qu’une fondamentale grave traverse le bus) et le **Bus Voix** (4.3), qui ne contient que des voix et suit donc la ligne Voix.*

## 2.5 Sidechain inter-canal — Key Source

Sur les **canaux d’entrée uniquement**, le compresseur et le gate peuvent être déclenchés par le niveau d’un **autre canal**. Le paramètre s’appelle **Key Source** et se trouve dans l’écran tactile du Fat Channel, à côté du Key Filter. Réglé sur « None », le processeur travaille normalement sur son propre signal.

Ne pas confondre les deux commandes voisines. Le **Key Filter** dit *à quelle fréquence* le processeur se déclenche, sur son propre signal. Le **Key Source** dit *quel autre canal* le déclenche. Les deux se combinent : on peut déclencher le gate de la basse depuis le kick, en ne retenant du kick que sa fondamentale grave.

**Usage 1 — mise en valeur du kick dans la basse (compresseur).** C’est le cas d’usage qui concerne le plus directement l’architecture de ce guide. Depuis la V12, kick et basse ne partagent plus de bus : ils ne se rencontrent qu’au Master, et la seule arme du guide était le cut à 60 Hz sur le canal de basse. Le sidechain en ajoute une seconde, dynamique plutôt que statique : compresseur sur le canal de basse, **Key Source = canal kick**, Threshold bas, ratio élevé, attaque rapide. La basse recule de un ou deux décibels à chaque frappe de kick et reprend sa place entre les coups.

*Réglage de départ, à valider à l’oreille.* Standard Compressor sur la basse — **à la place** du RC-500 de la fiche 3.3, un canal n’ayant qu’un compresseur (conséquences et issues en 3.3) —, Key Source = kick, Ratio 4:1, Attack 3 ms, Release 150 ms, Threshold descendu jusqu’à voir **1 à 3 dB de réduction sur les frappes de kick seulement**. Au-delà, ça s’entend et ça pompe. C’est un effet qu’on doit sentir sans l’identifier ; si on l’entend, c’est qu’il est trop fort.

*⚠️ Le release dépend du tempo — le 150 ms n’est pas universel.* Pour que la basse ait le temps de revenir entre deux frappes, **le release doit rester nettement plus court que l’intervalle entre deux kicks**. À 120 BPM, une noire dure 500 ms : 150 ms laisse largement le temps de remonter. À 170 BPM en punk rapide avec un kick sur chaque croche, l’intervalle tombe autour de 175 ms — un release de 150 ms n’a plus le temps de relâcher et la basse reste écrasée en permanence, ce qui produit exactement l’inverse de l’effet recherché : elle disparaît au lieu de laisser passer le kick.

*Règle de calcul rapide.* Intervalle entre deux kicks en millisecondes = 60 000 / BPM (pour un kick à la noire), ou la moitié pour un kick à la croche. Viser un release autour du **tiers à la moitié** de cet intervalle. En pratique : 150 ms convient de 90 à 140 BPM environ ; monter vers 200 ms sur du reggae lent, descendre vers 60–80 ms sur du punk rapide ou de la techno à kick continu — et sur un kick vraiment continu à la croche, renoncer au sidechain plutôt que de le régler trop court.

*Quand s’en servir.* Sur un plateau où le kick disparaît malgré un bon EQ, en métal et en techno live surtout. Inutile en reggae et en dub, où la basse doit rester continue et pleine — la faire reculer à chaque kick y détruit précisément ce qu’on cherche.

**Usage 2 — resserrer une section rythmique (gate).** Gate d’une source rythmique, Key Source = kick, attaque et retour rapides : la source ne s’ouvre qu’au moment du kick. *Méthode, dans l’ordre.* **Threshold** : le descendre jusqu’à ce que le gate s’ouvre sur chaque frappe de kick, puis s’arrêter — plus bas, il s’ouvrirait sur la repisse du canal kick. **Attack** : en butée rapide. **Release** : partir de la valeur par défaut (700 ms, 2.7) et raccourcir jusqu’à entendre la source pulser avec le kick ; elle doit se refermer avant la frappe suivante (à 120 BPM, moins de 500 ms). **Range** : c’est lui qui règle la profondeur de l’effet — commencer par une fermeture partielle et creuser à l’oreille plutôt que de fermer complètement. Le manuel le décrit pour la basse ; ça vaut aussi pour une nappe ou un pad tenu qu’on veut faire pulser.

*Avertissement du manuel, à prendre au sérieux.* Cette technique **n’améliore pas un groupe qui ne joue pas ensemble, elle aggrave le problème.** Un batteur et un bassiste légèrement décalés deviennent, une fois le gate synchronisé, franchement décalés. À réserver aux sections rythmiques qui sont déjà en place.

**Usage 3 — ducking (compresseur).** Une source recule automatiquement quand une autre parle. Threshold bas, ratio élevé, attaque rapide, retour long. *Méthode, dans l’ordre (Standard Compressor, mode Auto désactivé).* **Attack** : en butée rapide, pour que le recul précède la première syllabe. **Threshold** : le descendre pendant que la source de commande parle à niveau normal, jusqu’à ce que le mètre de réduction réagisse à chaque mot et reste immobile sur les respirations et la repisse. **Ratio** : partir de 4:1 (la valeur de l’usage 1) et monter tant que la musique gêne encore la parole — c’est lui qui règle la profondeur. **Release** : l’allonger jusqu’à ce que la musique ne remonte plus entre deux mots, sans dépasser le temps d’une respiration. **Consigner la réduction lue au mètre** : c’est la valeur qui manque au guide (registre 8.7). Il s’applique à **n’importe quel canal d’entrée** — par exemple faire reculer un playback quand un MC prend la parole — mais **pas à un retour d’effet** : pas de Key Source sur ce type de canal (5.2).

**Limite à connaître.** Key Source n’existe **pas sur les bus**, seulement sur les canaux d’entrée. Toute idée de sidechainer un bus par un autre est hors de portée de cette console.

## 2.6 Errata de la documentation PreSonus

Trois erreurs, une lacune et une divergence de nommage constatées dans la documentation officielle. Elles sont consignées ici pour éviter qu’une relecture future du manuel ne les réintroduise dans le guide.

**Baxandall EQ, High Cut.** L’addendum recopie la description du Low Cut (« 54 à 12 Hz »), impossible pour un coupe-haut. Lecture du panneau : zone libellée en kHz, environ 7,5 à 70 kHz. Contrôle laissé OFF dans tout le guide.

**Reverbs, Low Pass et LPF Freq.** Le manuel français indique pour les quatre reverbs : « Utilisez cette commande pour atténuer les basses fréquences qui peuvent brouiller une réverbération. » Un filtre passe-bas atténue les **hautes** fréquences, pas les basses. L’intention est claire — assombrir une queue de reverb trop brillante — mais la phrase dit le contraire de ce que fait la commande. Le guide utilise le Low Pass pour ce qu’il fait réellement.

**Comp 160, inscriptions BELOW et ABOVE.** Deux inscriptions lumineuses sur le panneau, aucune explication fonctionnelle nulle part, contrairement aux autres bascules (Peak/Trough du Solar 69, Fixed/Manual du Tube CB) qui sont, elles, documentées. Ne pas inventer d’explication : piloter au mètre de réduction de gain. Sur le dbx 160 d’origine, ce sont des voyants d’état du seuil (2.1) ; que le Comp 160 fasse de même reste à vérifier.

**Deux modèles, deux noms selon le document.** Le manuel français de la console appelle **« Tube P1B Compressor »** et **« Tube Midrange EQ »** ce que l’addendum des plug-ins — et ce guide — appellent **Tube CB** et **Tube EQ**. Les descriptions correspondent : compresseur optique tout lampe pour le premier, égaliseur passif de médiums pour le second. Ce ne sont pas des modèles supplémentaires. À savoir avant de chercher sur la console un « P1B » qui n’apparaîtrait pas sous ce nom, ou de conclure à l’inverse qu’un modèle manque.

**Gate sur les bus — le manuel se contredit.** Le tableau 6.1 ne donne de gate qu’aux canaux d’entrée ; la section 5.3.2 dit que les sous-groupes, fixes comme FlexMix, reçoivent « les noise gate, limiteur, compresseur et égaliseur du Fat Channel ». Sans conséquence pour ce guide, qui ne pose aucun gate sur un bus.

**Tube CB, numérotation des commandes.** Le texte de l’addendum (3.7, point 7) renvoie aux commandes « Attack (#2) and Release (#4) » ; sur l’illustration et dans la liste elle-même, Attack porte le n° 3 et Release le n° 5 (le n° 2 est Gain, le n° 4 Threshold). Sans conséquence sur le réglage, mais à savoir avant de suivre l’addendum au numéro.

## 2.7 Plages de réglage chiffrées

Les butées réelles, telles que le manuel les documente. Utile pour savoir quand une valeur du guide est proche d’une limite physique.

| **Paramètre** | **Plage** | **Remarque** |
| --- | --- | --- |
| Gate Threshold | 0 à -84 dB | En butée basse, le gate est désactivé (toujours ouvert) |
| Gate Range | jusqu’à -84 dB affiché | C’est ce que le guide appelle « -∞ » ; désactivé en mode Expandeur |
| Gate Attack / Release | valeurs par défaut 5 ms / 700 ms | Plages non chiffrées par le manuel |
| Compresseur Threshold | -56 à 0 dB | Vaut pour le Standard Compressor du Fat Channel |
| Standard Comp par défaut | -0 dB · 2,0:1 · 20 ms · 150 ms | État à l’ouverture d’un canal neuf |
| Mode Auto | Attack 10 ms / Release 150 ms imposés | Les deux commandes deviennent inopérantes |
| HPF | 24 Hz à 1 kHz, pente -12 dB/oct | Désactivé quand réglé au minimum |
| Limiteur | Threshold seul, ratio ∞:1 | Release exposé par le firmware dans UC Surface |
| Retard d’entrée | 0 à 85 ms, pas de 0,1 ms | Par canal — voir 7.7 |
| Class-A FET Ratio | 4:1 · 8:1 · 12:1 · 20:1 · All | Pas de Threshold sur ce modèle |
| Tube Leveling ratio | 1:1–10:1 (Comp) · 10:1–20:1 (Lim) | Selon le sélecteur Lim/Cmp |
| RC-500 Comp | ratio fixe 3:1 · Attack 0,5–10 ms · Release 40–500 ms | Ratio non modifiable |
| VT-1 Comp | Attack 0,5–10 ms · Release 40–500 ms | Ratio variable |
| Tube CB mode Fixed | Attack 1 ms / Release 50 ms | Non réglables en Fixed |
| Tube CB mode Manual | boutons continus Fast ↔ Slow | Temps non chiffrés par l’addendum — convention et méthode en 2.1 |
| Everest C100A | trois positions : Fast · Medium · Slow | Temps non chiffrés par l’addendum |
| Brit Comp Attack | crans 0,1 · 0,3 · 1 · 3 · 10 · 30 ms | Lus sur le panneau (2.8) ; crans du Release à relever |
| Class-A FET Attack / Release | défauts 0,10 ms / 250 ms | Plages non chiffrées par le manuel — à relever |
| Effets : Reflection, Size, Diffusion, Spread, Width | non chiffrés | Convention et méthode en 5.1bis — à relever |

## 2.8 Les machines derrière les émulations — et les gestes qui vont avec

PreSonus ne nomme jamais le matériel copié : marques déposées. Mais les commandes, les valeurs imprimées sur les panneaux et les descriptions permettent d’identifier la plupart des modèles. **Le niveau de confiance est indiqué à chaque fois, et il ne faut pas le confondre avec une certitude.** L’intérêt n’est pas la culture générale : une fois la machine identifiée, des décennies de technique documentée deviennent applicables.

| Plugin | Machine d’origine probable | Confiance |
| --- | --- | --- |
| FC-670 | Fairchild 670 | Quasi-certain (nom explicite) |
| Comp 160 | dbx 160 | Quasi-certain (nom + face avant BELOW/ABOVE) |
| Class-A FET | UREI 1176 | Quasi-certain (ratios 4/8/12/20/All) |
| Tube Leveling Amplifier | Teletronix LA-2A | Quasi-certain (nom de catégorie historique) |
| Passive Program EQ | Pultec EQP-1A | Quasi-certain (Boost/Atten interactifs) |
| **Tube EQ** | **Pultec MEQ-5** | **Quasi-certain (voir ci-dessous)** |
| Vintage 1970s EQ | Neve 1073 | Très probable |
| Brit Comp | SSL G-Series Bus Compressor | Très probable (voir ci-dessous) |
| VT-1 Comp + VT-1 EQ | Avalon VT-737SP | Très probable |
| Alpine EQ-550 | API 550A/550B | Probable (le « 550 » du nom) |
| Everest C100A | Compresseur lampe américain classique | Catégorie confirmée, modèle non identifié |
| Tube CB | Famille opto tout-lampe | Faible |
| Solar 69 EQ | EQ britannique classique | Faible |
| Vintage 3-Band EQ | Non identifié | Faible |
| RC-500 Comp + EQ | Matériel PreSonus historique | Confirmé par le manuel |
| Classic Compressor | Générique assumé | Aucun calque revendiqué |
| Baxandall EQ | Topologie Baxandall (circuit, pas une marque) | — |

*Sur le design :* comparaison faite des 21 panneaux de l’addendum — **aucun ne reproduit l’esthétique de sa machine de référence.** PreSonus dessine des façades originales, avec un code couleur interne de gamme (rouge pour la famille lampe, bleu marine pour VT-1, teal pour Brit Comp). Le visuel n’est donc pas un indice ; **ce sont les valeurs imprimées sur les boutons qui trahissent la filiation.**

**Tube EQ = Pultec MEQ-5.** Les graduations du panneau sont décisives : Low PEAK 0,3–1 kHz, Mid DIP 0,2–5 kHz, High PEAK 1,5–5 kHz. La bande haute du vrai MEQ-5 est exactement 1,5/2/3/4/5 kHz — identique. C’est le seul EQ du pack qui ne peut pas toucher les graves ni les aigus, et c’est voulu.

**Brit Comp = SSL G-Series Bus Compressor.** La séquence d’Attack imprimée sur le panneau — 0,1 / 0,3 / 1 / 3 / 10 / 30 ms — est identique à celle publiée pour le bus compressor SSL, et le « double VCA » du descriptif PreSonus correspond aux deux cellules VCA du modèle stéréo. Une coïncidence peu probable sur six valeurs.

**Les gestes historiques applicables tels quels**

- **Class-A FET, position « All » = le « All Buttons In » du 1176.** Sur le vrai 1176, enfoncer tous les boutons de ratio ensemble donne un ratio instable, une attaque et un relâchement qui se déforment, un son explosif et saturé — surnommé *British Mode*. Usage universellement documenté : **jamais en direct sur un canal, uniquement en parallèle.** Ton Bus Parallel (FM 15) est exactement l’endroit pour ça, et il n’a jamais été testé avec autre chose que le Comp 160. À essayer.

- **Passive Program EQ : le tour de passe-passe Pultec dans les graves.** Booster et atténuer la *même* fréquence simultanément. Sur ce circuit passif, les deux ne s’annulent pas : le boost est un pic large, l’atténuation un plateau qui démarre juste en dessous. Résultat : un renflement propre à la fréquence visée et un nettoyage du sub en dessous, d’un seul geste. Le panneau PreSonus partage le même sélecteur de fréquence entre Low Boost et Low Atten, exactement comme le vrai appareil — le geste est reproductible à l’identique. **Au Master, à tester : Low Boost +1 à +2 dB ET Low Atten +1 à +2 dB, tous les deux à 60 Hz.**

- **Alpine EQ-550 : le Q proportionnel de l’API.** Le Q se resserre automatiquement quand le gain monte. Un petit boost (2–4 dB) reste large et musical ; un gros boost (9–12 dB) devient chirurgical tout seul, sans rien régler. Conséquence pratique : **on peut pousser plus fort qu’avec un EQ classique** sur un problème ponctuel, la bande se resserre d’elle-même. Deux essais documentés et directement transposables : plateau aigu sur les overheads, et boost vers 1,5 kHz pour le crack de caisse claire.

- **Neve ou API — lequel quand.** Retours d’ingénieurs convergents : le Neve (Vintage 1970s) pousse vers un son épais, dense, presque saturé — le choix quand on veut que *ça pousse*. L’API (Alpine) reste plus plat, plus retenu, avec une légère compression rien qu’en le traversant — le choix pour de la cohésion sans écraser. Ça valide la répartition actuelle : **Neve sur Bus Voix agressif, API sur Bus Instru.**

- **FC-670 et Tube Leveling Amplifier : rien à changer.** Ces deux compresseurs à lampes — variable-mu pour le premier, optique pour le second — sont réputés « disparaître » à faible réduction (2–4 dB) — exactement ce que ce guide prescrit déjà sur Bus Instru, cuivres et claviers. Confirmation, pas correction.

## 2.9 Sommation, phase et filtrage en peigne — le socle

Le guide décrit depuis longtemps des *procédures* de phase correctes (touche Ø, retards d’entrée, centrage du couple) sans jamais dire **quand elles comptent vraiment**. Les travaux de Bob McCarthy (*Sound Systems: Design and Optimization*) donnent les critères chiffrés qui manquaient.

**Les quatre zones de sommation.** Quand deux signaux corrélés se somment, le résultat dépend de leur écart de phase et de leur écart de niveau :

| Zone | Condition | Conséquence |
| --- | --- | --- |
| **Couplage** | Phase dans ±120° (±⅓ de longueur d’onde) | Addition seule, 0 à +6 dB |
| **Combing** | Au-delà de ±120° **et moins de 4 dB d’écart de niveau** | Zone à fuir : pertes potentiellement totales |
| **Combining** | **4 à 10 dB d’écart de niveau** | Interaction bornée, ondulation limitée à ±6 dB |
| **Isolation** | **10 dB ou plus d’écart de niveau** | Interaction négligeable |

**⚠️ Ce qu’il faut en retenir avant tout : l’écart de niveau est lui-même un outil de phase.** Deux micros sur la même source à moins de 4 dB l’un de l’autre dans le mix sont en zone de combing — il *faut* traiter (polarité, retard, placement). À 10 dB d’écart, l’interaction ne mérite plus qu’on s’en occupe. C’est ce qui transforme « vérifier la phase » en geste ciblé plutôt qu’en rituel : **la question n’est pas seulement *sont-ils en phase*, c’est *à quel écart de niveau sont-ils*.**

**Le critère du ⅓ de longueur d’onde — ce qui tranche XY contre ORTF.** Le couplage exige une différence de trajet inférieure à ⅓ de longueur d’onde. En **XY coïncident**, cette différence est proche de zéro : couplage sur tout le spectre. C’est la raison physique de la compatibilité mono, pas une affirmation de principe. En **ORTF à 17 cm**, pour une source franchement latérale, la différence de trajet atteint 17 cm — soit ⅓ de longueur d’onde autour de **670 Hz** : au-dessus, on sort du couplage. Et ça explique enfin pourquoi le guide demande de mesurer à la ficelle pour centrer la caisse claire : distance égale = différence de trajet nulle = couplage à toutes les fréquences **pour cette source-là**.

**La largeur des dents du peigne, et ce que l’EQ peut corriger.** Un décalage d’une longueur d’onde crée un pic large d’une octave ; deux longueurs d’onde, une demi-octave. Or la **bande critique de l’oreille tourne autour de 1/6 d’octave dans le médium et l’aigu** (au-dessus d’environ 1 kHz) ; **elle s’élargit nettement dans le grave**, où elle atteint environ une demi-octave vers 100 Hz (bandes ERB, Glasberg et Moore : ERB = 24,7 × (4,37 f/1000 + 1), soit ≈ 35 Hz à 100 Hz). *Correction V33 : l’ancien texte disait « dépasse l’octave ».* Plus étroit qu’elle n’est plus perçu comme une couleur mais comme un effet spatial — ce qui veut dire que dans le grave, même des dents de peigne larges s’entendent surtout comme une perte de corps. Trois règles en découlent, directement applicables au GEQ (7.3) :

- **N’égaliser que les pics larges.** Les pics et creux étroits ne se corrigent pas utilement.

- **Un creux d’annulation ne se rattrape jamais en boostant.** Baisser les pics empêche qu’ils ressortent ; ça ne restitue pas ce que l’annulation a retiré.

- Le GEQ en 1/3 d’octave est **plus large que la bande critique** : bon outil pour la couleur, mauvais outil pour un notch fin.

**Le seuil d’écho n’est pas 60 ms.** Le chiffre universellement cité vient d’études sur la voix, autour de 400 Hz. Le seuil réel glisse avec la fréquence : de l’ordre de **2 ms à 12 kHz et 240 ms à 100 Hz**. D’où la règle de décision qui manquait en 7.7 et 7.8 : **en deçà du seuil, l’EQ est une option ; au-delà, seul le retard fonctionne.** Ça explique aussi pourquoi quelques dixièmes de milliseconde sur un retard d’entrée s’entendent nettement — à 10 kHz, 0,1 ms représente déjà une longueur d’onde entière.

**Les effets secondaires du stéréo en salle.** Les auditeurs décentrés subissent du filtrage en peigne, ceux placés sur les côtés des échos francs, et les dégâts sont proportionnels au recouvrement de niveau là où les décalages temporels sont trop grands. Le choix du XY par défaut en live n’est donc pas une prudence excessive : c’est la réponse à un problème mesurable.

# PARTIE 3 — PRESETS PAR SOURCE

Chaque fiche suit l’ordre des commandes du Fat Channel. Les micros indiqués sont **ceux du parc personnel** ; le matériel d’emprunt est traité séparément en 3.2 et signalé partout ailleurs.

*⚠️ Ne jamais assigner un canal directement au Main L/R — uniquement vers son bus de groupe. Seules les sources ligne de la section 3.8 font exception.*

## 3.1 Batterie — le kit 4 micros

C’est la configuration de référence, entièrement autonome : **kick BD 500 Beta, caisse claire i5 sur D-Vice, overheads Lewitt en couple sur barre stéréo**. Quatre canaux, un seul pied.

Dans cette configuration, **les overheads ne sont pas des micros de cymbales : ils portent tout le kit** — toms, cymbales, ambiance générale. Toute la logique de réglage découle de là, en particulier le HPF.

**Ordre de montage recommandé**

Poser le kick en premier (il faut accéder à l’intérieur de la caisse avant que le batteur s’installe), pincer la caisse claire ensuite, monter les overheads en dernier. Au démontage, l’ordre inverse — récupérer les Lewitt en premier et les remettre en sacoche immédiatement.

**KICK — t.bone BD 500 Beta**

*Micro et placement.* C’est un micro à zone de pression : il se **pose à plat**, il ne se pointe pas. Le poser à l’intérieur de la caisse, sur la coque inférieure, en passant par le trou de la peau de résonance. Plus la surface porteuse est rigide et étendue, plus la réponse descend — la coque de la caisse joue naturellement ce rôle.

*Position et son.* Vers la peau de frappe, on gagne en attaque et en clic ; reculé vers le centre ou vers la peau de résonance, on gagne en rondeur et en grave. Un boundary est peu sensible à la position exacte, c’est justement son intérêt en changement rapide.

*Attention au coussin.* Si un coussin ou une couverture occupe la caisse, **ne pas poser le micro dessus** : une surface molle annule l’effet de zone de pression et le micro perd son grave. Le poser sur la coque elle-même, ou sur une petite plaque rigide calée sur le coussin.

*Peau non percée.* Le micro ne peut pas entrer. Le poser au sol contre la peau de frappe, sur une surface dure — le résultat est nettement moins bon. C’est le scénario qui justifie l’Audix D6.

*Interrupteur d’EQ.* **À régler sur la position grosse caisse avant de poser le micro** — il devient inaccessible une fois dans la caisse. Cette position creuse déjà les médiums.

*Phantom.* **ON 48 V — obligatoire.** Sans fantôme, aucun signal.

*Gain.* +25 à +40 dB, **à caler au vumètre**, cible -12 à -6 dBFS en crête. Les spécifications constructeur divergent sur la sensibilité : ne pas chercher de valeur théorique.

*HPF.* 30 Hz. La position boundary dans la caisse remonte déjà le sub — ce filtre protège les enceintes sans rien enlever d’utile.

*Gate/Expander.* Optionnel, et si utilisé : **Gate avec Range modéré plutôt que Range -∞.** Un micro boundary posé dans la caisse capte la résonance complète de la coque, pas juste l’attaque du batteur — c’est justement ce qui lui donne son grain plein. Un Range à -∞ tranche cette résonance net à chaque silence et peut rendre le kick sec et artificiel. Threshold vers -35 dB, **Range vers -15 à -20 dB** (laisse un fond de résonance naturel plutôt qu’un silence total), Attack minimum, Release 200 ms. Vérifier que les frappes douces passent encore. En cas de doute, laisser ouvert : l’isolation naturelle de la coque suffit souvent sans aucun gate.

*Compresseur.* Standard Compressor. Threshold -15 dB, Ratio 4:1, Attack 10 ms, Release Auto. Réduction visée 3–5 dB, makeup +2 dB. L’attaque à 10 ms laisse passer le clic de batte avant de serrer le sustain. *(Ici le mode Auto tombe juste : il impose précisément 10 ms d’attaque et 150 ms de retour. Même chose partout où ce guide écrit « Attack 10 ms, Release Auto » (overheads, toms, charley, synthé, Bus Divers) : les deux sont compatibles. Avec toute autre attaque, régler le Release à la main — voir 2.1.)*

*EQ — point critique.* **L’interrupteur du micro creuse déjà les médiums. Ne pas recreuser 400 Hz à la console par réflexe** — le kick deviendrait creux et sans corps. Commencer avec un Baxandall EQ quasi flat : Low Cut vers 30–40 Hz, plateau grave vers 80–100 Hz à +1 ou +2 dB, plateau aigu vers 3–4 kHz à +1 ou +2 dB pour le clic. *Sur ce modèle, le bouton « Low Shelf » règle la fréquence et « Low Frequency » le gain ; même inversion côté aigu (2.3).* High Cut : OFF (voir 2.3, le contrôle n’est pas calibré de façon fiable dans la doc). Écouter avant d’ajouter quoi que ce soit. Si le carton persiste malgré l’interrupteur, alors seulement passer en Standard EQ et couper -2 à -3 dB dans la zone 300–500 Hz.

*Limiteur.* Threshold -1 dB, **Release 150 ms**. Jamais plus court : sur une source aussi grave, un release rapide produit une distorsion qu’on n’identifie pas comme telle mais qui salit tout le bas du mix.

*Bus.* Bus Drums (FM 9+10) + Bus Parallel (FM 15).

*Si ça distord.* À gain modéré, une distorsion vient du micro lui-même (140 dB SPL maximum à 1 % de THD), pas du préampli. Reculer le micro dans la caisse plutôt que baisser le gain.

**CAISSE CLAIRE — Audix i5 sur D-Vice**

*Micro et placement.* Pince D-Vice au cerclage, col de cygne orienté vers le centre de la peau, capsule à 3–5 cm, inclinée pour éviter la trajectoire de la baguette. Aucun pied nécessaire.

*Réglage du col de cygne.* Plus la capsule vise le centre, plus le son est plein et sourd ; plus elle vise le bord, plus il est claquant et riche en timbre. Point de départ : à mi-chemin, à 45°.

*Vérification entre deux groupes.* Contrôler le serrage de la pince — un batteur qui tape les cercles la déplace. C’est le seul point de fragilité de cette solution.

*Phantom.* OFF — dynamique.

*Gain.* +30 à +40 dB.

*HPF.* 80 Hz.

*Gate/Expander.* Threshold vers -30 dB si la repisse de charley gêne, **Range -∞** (silence net souhaité entre les coups, la caisse claire doit claquer), Attack minimum, Release 100 ms. En punk et métal, souvent inutile : ça joue en continu. **Attention en configuration 4 micros** : un gate serré sur la caisse claire coupe aussi de l’ambiance utile qu’on ne retrouve que dans les overheads.

*Compresseur.* Class-A FET. **Pas de Threshold sur ce modèle** : monter l’Input Gain depuis sa valeur par défaut (-24 dB, affichée au manuel 6.5.3) jusqu’à lire 4–6 dB de réduction au mètre. Aucune valeur cible n’est documentée : c’est le mètre qui décide, pas le chiffre. Ratio 4:1, Attack 3 ms, Release 150 ms *(les deux sous réserve des plages réelles — voir 2.1, Class-A FET)*, compenser à l’Output Gain.

*Variante hip-hop ou reggae.* Même ratio que la base (4:1 est le plus bas de ce modèle, 2.1) ; ce qui change : Attack 5 ms et réduction limitée à 2–3 dB, pour un rendu plus naturel.

*EQ — recalée sur la courbe réelle de l’i5.* La courbe constructeur de l’i5 montre deux bosses naturelles : **+5 dB vers 150 Hz** (bass hump) et **+9 dB vers 5,5 kHz** (présence, plateau large de 3 à 8 kHz). Ce n’est pas un micro plat comme un SM57 — il colore déjà dans les deux zones où on cherche justement à booster.

Cut -4 dB à 300 Hz, Q 1.5, pour le carton — ça reste nécessaire, indépendant de la courbe du micro. **Zone du « ping » (800 Hz – 1,5 kHz) : jamais exploitée jusqu’ici.** C’est la résonance métallique du fût, distincte du corps (180–250 Hz) et de l’attaque (2–7 kHz). Sur une caisse claire qui sonne correcte mais sans caractère, un boost léger (+1 à +2 dB, Q 1.5) dans cette fenêtre lui rend son timbre propre sans toucher ni au corps ni au claquement. **Corps (200 Hz) : commencer FLAT.** Le hump naturel à 150 Hz de l’i5 fait probablement déjà le travail ; ajouter +2 dB par-dessus risque d’empâter. Écouter d’abord après compression, booster seulement si le corps manque encore. **Claque (3 kHz) : viser +1 à +2 dB, pas +3–4 dB**, et si possible décaler légèrement vers 4–4,5 kHz plutôt que 3 kHz pour travailler dans le sens du plateau naturel du micro (qui culmine à 5,5 kHz) plutôt que contre lui. Le micro apporte déjà l’essentiel de la présence ; la console vient juste peaufiner.

*Limiteur.* Threshold -1 dB, **Release 70 ms**.

*Bus.* Bus Drums (FM 9+10) + Bus Parallel (FM 15).

**OVERHEADS — couple Lewitt LCT 040 MATCH**

C’est le canal le plus important du kit dans cette configuration : il porte les toms, les cymbales et toute l’ambiance.

*Choix du couple : XY ou ORTF.*

**XY coïncident** — les deux capsules aussi proches que possible, angle de 90 à 135°. Compatibilité mono excellente et **aucune différence de temps d’arrivée entre les deux capsules**, image stéréo plus resserrée. *Formulation exacte : le XY supprime le décalage temporel entre L et R, il ne supprime pas toute interaction de phase — le couple continue d’interagir avec le micro de kick, celui de caisse claire et l’acoustique du lieu.* **C’est le choix par défaut en live** : la majorité du public n’est pas dans l’axe stéréo, et beaucoup de diffusions se comportent en mono dans la salle.

**ORTF ou quasi coïncident** — capsules écartées d’environ 17 cm, angle de 110°. **Vérifié sur la fiche K&M : la 23550 s’écarte de 60 à 172 mm entre les deux points de fixation.** **Mais les 17 cm se mesurent entre les capsules, pas entre les fixations — et en ORTF les capsules sont plus écartées que les fixations.** Chaque micro est tourné de 55° vers l’extérieur, capsule en avant de sa pince : si L est la distance entre le point de fixation et la capsule, chaque capsule gagne L × sin 55° ≈ 0,82 L vers l’extérieur. *Calcul :* écartement des capsules ≈ écartement des fixations + 1,64 L. Il faut donc **rapprocher les fixations** sous 17 cm, d’autant plus que la capsule dépasse loin de la pince — la course de la 23550 n’est pas la limite. L dépend de la position du micro dans sa pince et n’est pas documenté : **régler les fixations, puis mesurer à la ficelle entre les deux capsules** jusqu’à 17 cm, à chaque montage. Image plus large et plus flatteuse au casque, compatibilité mono encore correcte. À réserver aux salles où la diffusion est réellement stéréo et le public relativement centré.

*Placement.* Barre stéréo sur le K&M 210/9, positionné derrière ou sur le côté du batteur. Hauteur : environ 1,0 à 1,3 m au-dessus des cymbales, centré sur l’ensemble du kit. **Ne pas monter trop haut** : en configuration 4 micros, les overheads doivent capter le corps des toms, pas seulement les cymbales. Trop de hauteur donne un kit sans toms et beaucoup de salle.

*Centrer la caisse claire.* Mesurer avec une ficelle ou un câble la distance de chaque capsule au centre de la caisse claire : les deux doivent être égales. C’est ce qui place la caisse claire au centre de l’image et évite qu’elle « tire » d’un côté. En XY coïncident, c’est quasi automatique ; en ORTF, ça demande d’orienter la barre.

*Phantom.* **ON 48 V sur les deux canaux.**

*Gain — attention, contre-intuitif.* Ces micros sont très sensibles (18,8 mV/Pa). Sur une batterie qui joue fort, prévoir **+5 à +20 dB seulement**, à caler au vumètre. Si le préampli sature au gain minimum, **remonter ou éloigner les micros** : il n’y a pas d’atténuateur sur le LCT 040.

*Coupler les deux canaux.* Utiliser le link stéréo de la console pour que gain, EQ et compression restent rigoureusement identiques sur les deux canaux L et R. Un écart de gain entre les deux détruit l’image stéréo et la compatibilité mono.

*HPF — le réglage décisif.* **80 Hz** en configuration 4 micros, comme point de départ. Les overheads portent les toms, et un floor tom a sa fondamentale autour de 60 à 80 Hz. *Ce que ça implique :* avec une pente de 12 dB/octave, un HPF à 80 Hz atténue déjà le bas de cette zone — de l’ordre de 6 dB à 60 Hz pour un filtre de type Butterworth (**estimation** : PreSonus documente la pente, pas le type de filtre). **Si le floor tom manque de corps, descendre vers 60–70 Hz** ; monter vers 100 ou 120 Hz **seulement** si la repisse de kick empâte le mix. Le bon réglage se trouve entre ces deux défauts, sur le kit du jour.

*⚠️ Le réglage 300–400 Hz ne s’applique qu’à des overheads dédiés uniquement aux cymbales, avec tous les toms micés par ailleurs. L’appliquer ici viderait la batterie de sa substance. Ce réglage deviendra pertinent le jour où les micros de toms arriveront (voir 3.2).*

*Gate/Expander.* **OFF. Jamais de gate sur des overheads** — ça détruit les queues de cymbales et fait respirer le mix de façon audible.

*Compresseur.* Standard Compressor, très léger. Threshold -20 dB, Ratio 3:1, Attack 10 ms, Release Auto. **Réduction 2–3 dB maximum.** Au-delà, on écrase les transitoires de cymbales et l’image stéréo se referme.

*EQ — attention au voicing du micro.* Le LCT 040 monte déjà à partir de 4 kHz avec un sommet vers 15 kHz : **il apporte le shimmer tout seul.** Ne pas reproduire le boost d’aigus classique.

Point de départ : Cut -2 dB à 400 Hz, Q 1.5, pour le mud commun. Aigus **flat**. Si l’ensemble sonne dur ou agressif en salle réverbérante, **couper** -1 à -2 dB vers 6–8 kHz plutôt qu’ajouter ailleurs. Si et seulement si le haut manque vraiment, +1 dB à 12 kHz maximum.

*Limiteur.* Threshold -1 dB, **Release 50 ms** — catégorie cymbales/overheads.

*Bus.* Bus Drums (FM 9+10). **Pas dans le Bus Parallel** : la compression extrême du Comp 160 sur des overheads produit un effet de pompage très audible sur les cymbales.

**PHASE ET COMPATIBILITÉ MONO — à faire à chaque soundcheck**

Avec trois sources qui captent la même batterie, la phase devient un vrai sujet. Cinq minutes bien employées font plus pour le son que n’importe quel EQ.

*1. Kick contre overheads.* Monter le kick et les overheads seuls. Appuyer sur la touche Ø du kick, puis relâcher. **Garder la position qui donne le plus de grave et de corps.** Une annulation se reconnaît à un kick qui devient mince dès qu’on monte les overheads.

*2. Caisse claire contre overheads.* Même opération sur le canal caisse claire. Garder la position la plus pleine. Sur une pince D-Vice au cerclage, la capsule est proche de la peau : l’inversion est souvent bénéfique, mais ça se vérifie, ça ne se décrète pas.

*3. Somme mono.* Passer la sortie en mono et écouter. **Rien ne doit disparaître** — si la caisse claire recule ou si les cymbales s’éteignent, le couple overhead est mal aligné : resserrer vers du XY strict.

*4. Vérifier l’image.* Revenir en stéréo, caisse claire au centre, charley et ride répartis naturellement. Si la caisse claire tire à gauche ou à droite, réajuster la barre stéréo, pas le panoramique.

*Panoramique.* Overheads en L/R francs. Kick et caisse claire au centre. Ne pas paner les close mics pour « élargir » : ça casse la cohérence avec les overheads.

*Si l’inversion de polarité ne suffit pas.* La touche Ø ne propose que deux états ; quand aucun des deux ne donne un résultat franchement meilleur, c’est que le problème est un décalage temporel et non une opposition de phase. Passer alors au **retard d’entrée (7.7)** : quelques dixièmes de milliseconde sur le micro le plus proche font ce que la polarité ne peut pas faire.

## 3.2 Batterie — extensions en emprunt

**TOMS — e604 ou équivalent emprunté**

Dès que des micros de toms s’ajoutent, **le rôle des overheads change** et leur réglage aussi.

*Micro et placement.* Pince au cerclage, capsule à 3–5 cm de la peau, pointée vers le centre.

*Phantom.* OFF sur les e604 — dynamiques.

*Gain.* +25 à +35 dB.

*HPF.* Tom aigu 60 Hz, médium 60 Hz, grave 50 Hz, floor 50 Hz.

*Gate/Expander.* Utile ici : un tom résonne et capte tout. Threshold vers -30 dB, **Range -∞** (isolation nette recherchée entre les passages), Attack minimum, Release 150–200 ms. Vérifier que les frappes légères passent.

*Compresseur.* Standard Compressor. Threshold -15 dB, Ratio 4:1, Attack 10 ms, Release Auto. Réduction 3–4 dB.

*EQ.* Cut commun -3 dB à 400 Hz, Q 1.5. Fondamentale : tom aigu +3 dB à 100 Hz, médium +3 dB à 90 Hz, grave +3 dB à 80 Hz, floor +2 dB à 70 Hz. Attaque : +2 dB à 3 kHz / 2,5 kHz / 2 kHz / 1,5 kHz selon la taille.

*Limiteur.* Threshold -1 dB, **Release 70 ms**.

*Bus.* Bus Drums (FM 9+10) + Bus Parallel (FM 15).

⚠️ **Conséquence sur les overheads. Avec tous les toms micés, les overheads redeviennent des micros de cymbales : remonter leur HPF à 300–400 Hz**, ce qui nettoie considérablement le bas du bus batterie. Avec seulement un ou deux toms micés sur un kit qui en compte davantage, rester à 80–120 Hz : les overheads portent encore les toms non repris.

**KICK, SECOND MICRO — Shure PGA52 de la MJC**

Le BD 500 Beta reste le micro principal (3.1). Le PGA52 s’ajoute quand le prêt de la MJC le permet, pour séparer deux couleurs de kick et les doser l’une contre l’autre.

*Micro et placement — ce que Shure documente.* Micro dynamique cardioïde, réponse annoncée **50 Hz – 12 kHz**. Le guide de l’utilisateur ne décrit que des positions **par rapport à la peau de frappe** : à **5–7,5 cm**, légèrement décalé du centre de la batte, pour une attaque nette, le maximum de grave et le niveau le plus élevé ; à **20–30 cm**, dans l’axe de la batte, pour une attaque moyenne et un son équilibré. Sur une peau de résonance percée, Shure conseille de passer **à l’intérieur** pour mieux rejeter le reste du kit. Avec le BD 500 posé sur la coque, la répartition qui découle de ces indications : **PGA52 près de la peau de frappe pour l’attaque, BD 500 en retrait vers la résonance pour la rondeur** (3.1, *Position et son*).

*Placement devant la peau de résonance — usage courant, non documenté par Shure.* C’est le « kick out » des fiches techniques, qui capte le corps de la caisse et l’air devant elle. Distance et hauteur à l’oreille, et sur une scène bruyante, s’attendre à plus de repisse qu’en position intérieure.

*Phase.* Les deux micros captent la même frappe à des distances différentes : appliquer 7.7 (usage 1) — mesurer l’écart entre les deux capsules, retarder le micro le plus proche de la batte de la valeur calculée, puis comparer les deux positions de la touche Ø en écoutant les deux canaux ensemble. Garder celle qui donne le plus de grave.

*Phantom.* OFF — dynamique.

*Gain.* À caler au vumètre, cible -12 à -6 dBFS en crête comme sur le kick principal. Près de la batte, la source est très chaude : partir bas.

*HPF.* 40 Hz. Le micro est annoncé à partir de 50 Hz : ce filtre ne retire rien d’utile, il protège le système.

*Gate/Expander.* OFF par défaut. Si la repisse oblige à le poser, mêmes réglages que le kick principal (3.1), Range modéré.

*Compresseur.* Standard Compressor, mêmes valeurs de départ que le kick principal : Threshold -15 dB, Ratio 4:1, Attack 10 ms, Release Auto. Réduction 3–5 dB.

*EQ.* Chaque micro garde son rôle, l’EQ ne doit pas les rendre identiques. Le guide de fréquences du manuel (13.4.1) donne pour la grosse caisse : graves de 60 à 125 Hz, confusion vers 400 Hz, attaque de 2 à 5 kHz. **Micro à l’attaque** (PGA52 près de la batte) : cut vers 400 Hz si le son devient confus, plateau ou cloche vers 2–5 kHz si le clic manque — gain à l’oreille. **Micro au corps** (PGA52 devant, ou BD 500 en retrait) : travailler la zone 60–125 Hz, laisser l’aigu tranquille. Commencer à ±2 dB maximum.

*Limiteur.* Threshold -1 dB, **Release 150 ms** (kick, 2.4).

*Bus.* Comme le kick principal : Bus Drums (FM 9+10) + Bus Parallel (FM 15). L’équilibre entre les deux micros reste ainsi le même dans les deux bus.

**CAISSE CLAIRE DESSOUS — SM57 emprunté**

*Placement.* Sous la caisse, orienté vers le timbre, à 5 cm.

*Phase.* **Inverser systématiquement** (touche Ø) — la peau du dessus et celle du dessous bougent en opposition. Vérifier ensuite à l’oreille en montant les deux canaux.

*Gain.* +35 à +45 dB. *HPF.* 100 Hz.

*Compresseur.* Standard Compressor. Threshold -15 dB, Ratio 4:1, Attack 5 ms, Release 150 ms. Réduction 3–4 dB.

*EQ.* Cut -3 dB à 300 Hz, Q 1.5. Boost +3 dB à 1,5 kHz pour le timbre, +4 dB à 5 kHz pour le croustillant.

*Limiteur.* Threshold -1 dB, Release 70 ms. *Bus.* Bus Drums.

**HI-HAT — SM57 emprunté, seulement si la fiche technique le demande**

*Quand ne pas le poser.* En kit 4 micros, les overheads Lewitt captent le charley avec leur voicing brillant, et un micro de plus n’apporte que de la repisse et un problème de phase supplémentaire. **Par défaut, pas de micro de charley.**

*Quand le poser quand même.* Quand un groupe le demande nommément sur sa fiche technique, ou quand le charley porte un motif rythmique central qu’on veut pouvoir doser indépendamment des cymbales — cas fréquent en techno live jouée sur batterie acoustique et en transe. La bonne réponse est alors de le poser, pas d’expliquer au groupe qu’il a tort.

*Micro et placement.* SM57 (ou statique petite membrane si emprunté), capsule **5 à 10 cm au-dessus du bord de la cymbale supérieure**, vers l’extérieur du kit, **dos du micro tourné vers la caisse claire** — c’est l’arrière du cardioïde qui rejette la repisse la plus gênante. **Jamais dans l’espace entre les deux cymbales** : le souffle d’air produit à la fermeture donne un pop de pression que ni le HPF ni le gate ne rattrapent.

*Phase.* Tester la touche Ø contre les overheads et garder la position où le charley reste net et centré.

*Phantom.* OFF sur un SM57.

*Gain.* +20 à +30 dB. Un charley joué fort à 5 cm est une source très chaude : ne pas monter par habitude.

*HPF.* **300 Hz.** Rien d’utile en dessous, et c’est ce qui retire l’essentiel de la repisse de caisse claire et de kick.

*Gate/Expander.* **OFF — jamais de gate sur une cymbale.**

*Compresseur.* OFF, ou Standard Compressor très léger si l’alternance ouvert/fermé varie trop : Threshold -20 dB, Ratio 2:1, Attack 10 ms, Release Auto, réduction 1–2 dB.

*EQ.* Flat au départ. Cut -3 dB vers 1 kHz, Q 2.0, contre le « clang » de boîte de conserve. Cut -2 dB vers 6–8 kHz si ça pique — les Lewitt apportent déjà le shimmer, ce canal ne sert qu’à la définition du motif.

*Limiteur.* Threshold -1 dB, **Release 50 ms** (catégorie cymbales).

*Bus.* Bus Drums (FM 9+10) uniquement, **jamais le Bus Parallel**. Pan légèrement du côté où le charley apparaît dans l’image des overheads, jamais à l’opposé.

## 3.3 Basses

### BASSE DI

*Source.* DI active personnelle. Sur une basse passive, toujours une DI active.

*Phantom.* ON 48 V si DI active.

*Gain.* +10 à +20 dB.

*HPF.* 40 Hz.

*Gate/Expander.* OFF.

*Compresseur.* RC-500. Ratio fixe 3:1, Threshold -18 dB, Attack Fast, Release Slow, Makeup +3 dB. Réduction 3–4 dB. Le Fast attrape les pics, le Slow évite le pompage entre les notes.

*EQ.* Standard EQ. **Cut -3 dB à 60 Hz, Q 1.0** — critique pour laisser la place au kick, qui est désormais sur un autre bus mais se somme au même Master. Boost +2 dB à 100 Hz, Q 1.0, pour la fondamentale. Boost +2 dB à 800 Hz, Q 1.5, pour la définition des cordes.

*Limiteur.* Threshold -1 dB, **Release 150 ms**. Même règle que le kick.

*Sidechain optionnel.* Si le kick disparaît malgré le cut à 60 Hz, activer le sidechain du compresseur avec **Key Source = canal kick** (voir 2.5). **⚠️ Un canal n’a qu’un compresseur** : dès que Key Source pointe sur le kick, le RC-500 ne compresse plus la basse sur son propre niveau, il ne fait plus que la faire reculer à chaque frappe. Trois issues : accepter de perdre la compression de la basse (souvent acceptable sur une DI régulière) ; passer ce compresseur en Standard Compressor aux réglages de 2.5 ; ou confier la compression de la basse au **Bus Basse (4.6)**, ce qui libère le compresseur du canal pour le seul ducking. Viser 1 à 3 dB de réduction sur les frappes de kick seulement. À éviter en reggae et en dub, où la basse doit rester continue.

*Bus.* Bus Instru (FM 11+12). La couleur vient du FC-670 du bus, qui lie la basse aux guitares et claviers.

### BASSE AMPLI

*Micro et placement.* SM57 sur le haut-parleur, légèrement décentré, à 5–10 cm.

*Phase.* Si la DI tourne en parallèle, tester l’inversion de phase (touche Ø) et garder la position qui donne le plus de grave.

*DI et ampli ensemble — ne pas cumuler les EQ.* Les deux fiches portent chacune un cut de -3 dB à 60 Hz : sommés au Master, les deux canaux le cumulent. Garder ce cut **sur un seul des deux canaux** (ou sur le Bus Basse, 4.6), puis juger au Master que le bas n’est ni creux ni baveux. Même vigilance sur les boosts voisins (100 et 120 Hz).

*Gain.* +25 à +35 dB.

*HPF.* 50 Hz.

*Compresseur.* RC-500, mêmes réglages que la DI.

*EQ.* Cut -3 dB à 60 Hz, Q 1.0. Boost +3 dB à 120 Hz, Q 1.0, pour le punch de l’ampli. Boost +2 dB à 1,5 kHz, Q 2.0, pour le grain.

*Limiteur.* Threshold -1 dB, **Release 150 ms**.

*Bus.* Bus Instru (FM 11+12).

### CONTREBASSE

*Source.* Pickup via DI, ou à défaut SM57 à 20–30 cm de l’ouïe. Sans condensateur, la prise micro reste approximative — privilégier le pickup.

*Gain.* +35 à +40 dB.

*HPF.* 40 Hz.

*Compresseur.* Classic Compressor. **Pas de commande Attack** sur ce modèle : Threshold -20 dB, Ratio 4:1, Recovery à mi-course *(l’addendum ne chiffre pas cette commande ; tourner vers un retour plus lent si le niveau pompe entre les notes, plus rapide si une note forte étouffe la suivante)*, Gain +4 dB. Réduction 6–8 dB — l’écart pizzicato/archet atteint facilement 18 dB, et l’absence d’Attack est ici un avantage : ça gère l’écart sans pompage.

*EQ.* Cut -2 dB à 60 Hz. Boost +3 dB à 100 Hz pour le corps, +2 dB à 1,5 kHz pour la définition de l’archet.

*Limiteur.* Threshold -1 dB, **Release 150 ms**.

*Bus.* Bus Instru (FM 11+12).

## 3.4 Guitares

**GUITARE ÉLECTRIQUE — ampli (Blackstar MJC ou ampli du groupe)**

*Micro et placement.* SM57 décalé du centre du cône, à 2–3 cm de la grille. Plus on approche du centre, plus c’est brillant et agressif ; plus on s’écarte vers le bord, plus c’est rond. *(Variante Sennheiser e609 : se pose à plat contre la grille, gain de temps en changement rapide, et l’écart avec un e906 se corrige à l’EQ numérique.)*

*Phantom.* OFF.

*Gain.* +25 à +35 dB.

*HPF.* 80 Hz en lead, 100 Hz en rythmique — plus agressif pour libérer les graves à la basse.

*Gate/Expander.* Utile sur les gros gains saturés en métal, pour couper le souffle et le buzz de l’ampli entre les riffs. Threshold vers -35 dB, **Range -∞** (le silence net entre riffs fait partie du son métal moderne), Attack minimum, Release 100 ms.

*Compresseur — lead.* Standard Compressor léger. Threshold -15 dB, Ratio 3:1, **Attack 5 ms, Release 150 ms en manuel — pas en Auto** (le mode Auto imposerait 10 ms d’attaque et annulerait le réglage). Réduction 2–3 dB : l’ampli compresse déjà naturellement.

*Compresseur — rythmique.* Class-A FET. **Pas de Threshold** : Input Gain monté depuis sa valeur par défaut (-24 dB, manuel 6.5.3) jusqu’à lire 3–4 dB de réduction au mètre, Ratio 4:1, Attack 5 ms, Release 250 ms *(sous réserve des plages réelles, 2.1)*. Le FET réagit vite et ajoute le mordant qu’on cherche sur les palm mutes.

*EQ — lead.* Cut -3 dB à 250 Hz, Q 1.5, pour la boue de proximité. Boost +2 dB à 2 kHz, Q 2.0, pour la présence. Cut optionnel -2 dB à 3,5 kHz, Q 3.0, si l’ampli est agressif. **Deuxième fenêtre de présence à essayer : 800 Hz – 1,5 kHz**, plus bas que le 2 kHz habituel. Selon l’ampli et le micro, c’est parfois là que le solo ressort du mur de guitares rythmiques sans devenir criard — à comparer en A/B avec le 2 kHz plutôt qu’à cumuler.

*Si le cut à 3,5 kHz ne suffit pas :* essayer le **Vintage 3-Band EQ** — le manuel le décrit par sa « brillance » et son « mordant », avec des plateaux grave et aigu ; l’addendum ajoute un HPF intégré à fréquence réglable et un inverseur de phase. Son usage sur une guitare qui manque de présence est le choix de ce guide, pas une indication du constructeur. Le guide l’envisage aussi sur les retours d’effet (5.2, 5.4). À tester avant de s’acharner sur le Standard EQ. *Point de départ et méthode (aucune valeur n’est documentée ni éprouvée) :* tous les gains à zéro et HPF au minimum, comparer avec le bypass pour entendre la couleur du modèle seul ; puis bande Mid en atténuation, balayer sa fréquence jusqu’à la zone dure, resserrer avec Hi Q si elle est étroite ; ne toucher aux plateaux Low et High qu’en dernier.

*EQ — rythmique.* Cut -4 dB à 200 Hz, Q 1.5, pour laisser la place à la basse. Boost +1 dB à 800 Hz pour le corps. Boost +2 dB à 3 kHz, Q 2.0, pour l’attaque des palm mutes. **Le poids du palm mute vit vers 100 Hz**, pas à 3 kHz — le 3 kHz donne le claquement du médiator, le 100 Hz donne la masse du riff. Sur un mur de guitares métal qui claque sans peser, tenter +1 dB à 100 Hz, Q 1.0 — **mais uniquement si la basse ne tient pas déjà cette zone**, sinon les deux se battent et le bas devient confus.

*Limiteur.* Threshold -1 dB, Release 100 ms.

*Bus.* Bus Instru (FM 11+12).

### GUITARE ACOUSTIQUE

*Source.* Pickup via DI — sans condensateur, c’est la seule option propre. Une prise au SM58 devant la rosace dépanne mais reste médiocre.

*Gain.* +20 à +35 dB via DI.

*HPF.* 80 Hz.

*Compresseur.* Classic Compressor. Threshold -18 dB, Ratio 5:1, Recovery à mi-course (même méthode que la contrebasse, 3.3), Gain +3 dB. Réduction 5–7 dB pour gérer l’écart entre strumming et fingerpicking.

*EQ.* Cut -2 dB à 200 Hz, Q 1.5, contre la boue du pickup rosace. Boost +3 dB à 3 kHz pour la définition, +2 dB à 10 kHz pour l’air.

*Limiteur.* Threshold -1 dB, Release 100 ms.

*Bus.* Bus Instru (FM 11+12).

## 3.5 Claviers

**CLAVIER / PIANO NUMÉRIQUE (Yamaha MJC ou clavier du groupe)**

*Source.* Sortie ligne en DI. En stéréo, la Palmer River Elde (0.5) ; à défaut, les deux DI mono.

*Gain.* +0 à +15 dB. Signal ligne : ne pas forcer.

*HPF.* 40 Hz.

*Compresseur.* Everest C100A. Attack Medium, Release Medium, Gain +1 dB. Réduction 2–3 dB pour préserver le dynamisme du jeu.

*EQ.* Flat par défaut. Si le clavier masque la basse, cut -2 dB à 200 Hz.

*Limiteur.* Threshold -1 dB, **Release 150 ms** — même règle que la basse (2.4). La main gauche d’un piano joue toute une octave et demie sous 80 Hz (jusqu’au la grave, 27,5 Hz). *Pas de contradiction avec le HPF à 40 Hz :* à -12 dB/octave (manuel, 6.3), il atténue l’octave la plus grave du clavier sans la retirer, et l’atténuation devient faible au-dessus. *Calcul, en supposant un filtre de Butterworth (le manuel ne donne que la pente) :* -3 dB à 40 Hz, environ -0,8 dB à 60 Hz, -0,3 dB à 80 Hz. C’est ce registre de 40 à 80 Hz qui impose les 150 ms.

*Bus.* Bus Instru (FM 11+12).

### SYNTHÉTISEUR

*Gain.* +0 à +15 dB.

*HPF.* 40 Hz, à descendre sur les patches de basse.

*Compresseur.* Standard Compressor. Threshold -18 dB, Ratio 3:1, Attack 10 ms, Release Auto. Réduction 2–3 dB.

*EQ.* Variable selon le patch — à évaluer à l’oreille en préparation. Un patch de nappe et un patch de lead n’ont rien en commun.

*Limiteur.* Threshold -1 dB, **Release 150 ms** — un patch peut descendre aussi bas qu’une basse (2.4). C’est aussi la sécurité contre le filtre qu’on ouvre en montée.

*Bus.* Bus Instru (FM 11+12).

### ORGUE / RHODES

*Source.* DI ligne, ou SM57 sur l’ampli.

*Gain.* +10 à +25 dB.

*HPF.* 60 Hz.

*Compresseur.* Tube Leveling Amplifier. Gain +5 dB, Peak Reduction autour de 30 %. Réduction 3–4 dB. L’opto gère les swells expressifs avec la douceur qui convient à ces instruments.

*EQ.* Cut -2 dB à 150 Hz contre la boue de bas-médiums. Boost +2 dB à 2 kHz pour la présence, +1 dB à 8 kHz pour le shimmer.

*Limiteur.* Threshold -1 dB, **Release 150 ms** — orgue et Rhodes ont un registre grave (2.4).

*Bus.* Bus Instru (FM 11+12).

## 3.6 Cuivres & Bois

*⚠️ Sans condensateur, cette famille est le point faible du parc. Le SM57 fait un travail honnête sur une trompette, correct sur un trombone, médiocre sur un sax et franchement limite sur une flûte. Ajuster les attentes et prévenir le musicien.*

### TROMPETTE / TROMBONE

*Micro et placement.* SM57 à 30–50 cm du pavillon, légèrement décentré. Ne pas coller : les niveaux en forte sont extrêmes.

*Gain.* +30 à +45 dB.

*HPF.* 100 Hz.

*Gate/Expander.* Absent du guide jusqu’ici — à ajouter dès qu’il y a du backline fort à proximité (cas fréquent en punk/rock/métal avec cuivres). **Gate, Threshold vers -32 dB, Range -20 à -25 dB** (pas -∞ : un cuivre a un timbre de fin de note et une réverbération naturelle du pavillon qu’un silence total tranche de façon disgracieuse), Attack minimum, Release 300–400 ms pour laisser la résonance du pavillon se dissiper. Si la scène est calme, laisser ouvert.

*Compresseur.* Class-A FET. **Pas de Threshold** : Input Gain monté depuis sa valeur par défaut (-24 dB, manuel 6.5.3) jusqu’à lire 5–7 dB de réduction au mètre, Ratio 4:1, Attack 3 ms, Release 250 ms *(sous réserve des plages réelles, 2.1)*, Output Gain +3 dB. L’attaque rapide attrape les pics avant qu’ils saturent la chaîne.

*EQ.* Cut -3 dB à 500 Hz, Q 2.0, pour le nasal du métal. Boost +2 dB à 2 kHz pour la brillance. Cut optionnel -2 dB à 4 kHz, Q 3.0, si ça pique en forte.

*Limiteur.* Threshold -1 dB, **Release 100 ms**.

*Bus.* Bus Instru (FM 11+12).

### SAXOPHONE

*Micro.* SM57 à 20–30 cm du pavillon, décentré vers les clés pour capter aussi le corps de l’instrument.

*Gain.* +25 à +40 dB.

*HPF.* 80 Hz.

*Gate/Expander.* Même logique que la trompette : **Gate, Threshold vers -32 dB, Range -20 à -25 dB**, Attack minimum, Release 300–400 ms. Le sax a un souffle de clétage et un decay de corps qu’un Range -∞ couperait trop sec.

*Compresseur.* Tube Leveling Amplifier. Gain +5 dB, Peak Reduction autour de 40 %. Réduction 4–5 dB.

*EQ.* Cut -2 dB à 400 Hz. Boost +3 dB à 2,5 kHz pour l’expressivité.

*Limiteur.* Threshold -1 dB, Release 100 ms (catégorie Guitares, cuivres, bois — 2.4).

*Bus.* Bus Instru (FM 11+12).

### FLÛTE

*Micro.* SM58 en dépannage, au plus près sans toucher — un dynamique sur une flûte reste un compromis assumé.

*Gain.* +45 à +50 dB, soit le maximum utile du préampli.

*HPF.* 200 Hz — critique pour éliminer le souffle d’embouchure.

*Gate/Expander.* **Gate, Threshold -30 dB, Range -30 à -35 dB** (plus profond que sur les autres cuivres/bois : à +45–50 dB de gain préampli, le bruit de fond amplifié est nettement plus présent, donc un Range plus marqué se justifie ici — mais on reste volontairement sous -∞ pour ne pas trancher la fin de souffle de chaque phrase). C’est un des rares cas où le gate est franchement utile malgré ses limites.

*Compresseur.* Everest C100A. Attack Medium, **Release Medium**, Gain +2 dB. Réduction 3–4 dB. *Pourquoi pas Fast :* à +45–50 dB de gain, un retour rapide remonte le bruit de fond entre les notes et fait respirer les phrases liées. Les temps de l’Everest ne sont pas chiffrés (addendum 3.4) : juger à l’oreille.

*EQ.* Cut -2 dB à 400 Hz. Boost +3 dB à 4 kHz pour la définition, +2 dB à 8 kHz pour la brillance.

*Limiteur.* Threshold -1 dB, Release 100 ms (catégorie Guitares, cuivres, bois — 2.4).

*Bus.* Bus Instru (FM 11+12).

## 3.7 Voix

C’est le point fort du parc : jusqu’à 8 canaux voix simultanés avec l’appoint MJC. Les fiches ci-dessous couvrent les micros réellement disponibles.

**VOIX LEAD — Beta58 ou SM58**

Le Beta58 (supercardioïde, plus de présence dans le haut) convient mieux aux voix qui doivent percer : punk, métal, rap agressif. Le SM58 (cardioïde, plus neutre) convient aux voix chantées et aux plateaux où la maîtrise du larsen prime.

*Phantom.* OFF — dynamiques.

*Gain.* **+35 à +45 dB.** C’est plus haut que ce qu’on lit habituellement pour une voix lead, parce que les fiches de référence supposent souvent un condensateur. Avec un SM58 ou un Beta58, il faut monter.

*HPF.* 100 Hz en punk, métal et rock — le chanteur mange le micro et l’effet de proximité charge le bas. 80 Hz en hip-hop, reggae et sur les voix posées.

*Gate/Expander.* Généralement OFF sur une voix lead. Sur un plateau très bruyant, Threshold vers -40 dB maximum, en surveillant que les fins de phrase ne se coupent pas.

*Compresseur — styles agressifs (punk, métal, rock).* Standard Compressor. Threshold -15 dB, Ratio 4:1, **Attack 3 ms, Release 150 ms en manuel — surtout pas en Auto.** Réduction 3–4 dB, Gain +2 dB. L’attaque à 3 ms attrape les consonnes dures, et c’est justement elle que le mode Auto écraserait en la ramenant à 10 ms. *(Erreur corrigée en V15 : les versions précédentes prescrivaient Release Auto tout en justifiant le son par une attaque de 3 ms qui n’était jamais appliquée.)*

*Compresseur — hip-hop, reggae, voix expressives.* VT-1 Compressor. Le VT-1 est gradué en millisecondes (addendum 3.8) : **Attack 1 ms** (près de la butée rapide, 0,5–10 ms), **Release 200 ms** (plage 40–500 ms), **Ratio 4:1**, Gain +2 dB. Ces trois valeurs remplacent les « Fast / Medium / medium » des versions précédentes, qui ne désignaient rien de précis sur un réglage continu ; points de départ, à l’oreille. Réduction 4–5 dB. Rapide sur les pics, chaud dans la couleur — le bon outil pour un MC qui joue de sa dynamique.

*EQ.* **Soustractif uniquement** — la coloration vient du Bus Voix. Cut -3 dB à 250 Hz, Q 1.5, contre la boue de proximité (-2 dB à 200 Hz suffit sur les voix posées). Cut optionnel -2 dB à 3 kHz, Q 3.0, si la voix est nasillarde.

*⚠️ Sibilance — la zone que le guide n’adressait pas.* Les « sss » vivent entre **4 et 8 kHz**, nettement plus haut que le 3 kHz du nasillard. Et il y a un piège structurel : **le Bus Voix des styles agressifs booste +3 dB à 4,8 kHz** (Vintage 1970s EQ) — en plein dans cette zone. Une voix déjà sifflante au micro ressort donc *amplifiée* après le bus. Deux réponses possibles, dans cet ordre :

- **Au canal, gratuit et immédiat** — un cut étroit (-2 à -3 dB, Q 3.0 ou plus) entre 5 et 7 kHz, calé à l’oreille sur la fréquence qui siffle le plus chez ce chanteur-là. Grossier mais efficace, et ça ne coûte rien.

- **Un vrai de-esser**, voir 7.10. **Toujours au canal, jamais sur le Bus Voix** : sur le bus, il devrait rattraper une sibilance déjà renforcée par le boost 4,8 kHz, et il agirait sur toutes les voix indifféremment.

*Option EQ à tester sur les voix de finesse.* Sur une voix hip-hop ou reggae déjà confiée au **VT-1 Compressor**, le **VT-1 EQ** est son jumeau du même châssis (probable Avalon VT-737SP, voir 2.8) — même caractère, décrit comme difficile à rendre laid. Marier un compresseur de caractère à un EQ neutre est un choix par défaut, pas une décision : à comparer en A/B avec le Standard EQ.

*Limiteur.* Threshold -2 dB, **Release 150–200 ms**. *-2 dB plutôt que -1 :* choix de ce guide, pas une valeur documentée — la voix est la source la plus exposée aux crêtes accidentelles (2.4, « Où il est vraiment utile »).

*Bus.* Bus Voix (FM 13+14).

**VOIX — micro HF (fourni par le lieu ou l’artiste — la MJC n’en a pas, 0.6)**

Mêmes réglages que ci-dessus, avec trois précautions.

*Gain.* Le niveau de sortie du récepteur diffère du niveau d’un micro filaire : refaire le gain staging spécifiquement, ne pas copier le preset d’un canal filaire sans vérifier.

*HPF.* Remonter à 120 Hz : un micro HF circule, capte les manipulations et les bruits de main.

*Surveillance.* Vérifier le niveau de batterie avant chaque set. Un HF qui faiblit produit des décrochages qu’on prend d’abord pour un problème de console.

### CHŒURS / BACKING

*Micro.* SM58.

*Gain.* +35 à +45 dB.

*HPF.* 120 Hz — plus agressif que le lead, les chœurs n’ont pas besoin de grave.

*Compresseur.* Standard Compressor. Threshold -18 dB, Ratio 4:1, **Attack 5 ms, Release 150 ms en manuel** (pas Auto, qui imposerait 10 ms). Réduction 4–5 dB.

*EQ.* Cut -3 dB à 250 Hz, Q 1.5. Cut optionnel -2 dB à 3 kHz, Q 3.0.

*Limiteur.* Threshold -2 dB, **Release 150–200 ms**. *-2 dB plutôt que -1 :* choix de ce guide, pas une valeur documentée — la voix est la source la plus exposée aux crêtes accidentelles (2.4, « Où il est vraiment utile »).

*Bus.* Bus Voix (FM 13+14).

**PLUSIEURS MC — configuration rap**

Sur un plateau rap à deux, trois ou quatre MC, tous les canaux voix reçoivent le **même preset de base**, puis on ajuste uniquement le gain par voix. Ne pas chercher à égaliser chaque MC différemment en live : c’est du temps perdu et ça déséquilibre le groupe.

Le vrai réglage se fait au Bus Voix (voir 4.3), qui traite l’ensemble.

*Point de vigilance :* avec quatre micros ouverts simultanément, le gain avant larsen baisse d’environ 6 dB par rapport à un seul micro. Muter les canaux inutilisés est le geste le plus efficace du set.

## 3.8 Sources ligne, DJ et Techno Live

Ces sources arrivent déjà traitées ou masterisées. Elles vont **directement au Main L/R**, sans bus de groupe : un compresseur vintage de bus réagissant à un signal déjà compressé produit du pompage et des comportements imprévisibles.

**⚠️ Sur quelles entrées les brancher.** Les fiches ci-dessous prescrivent HPF, gate et limiteur : ces étages n’existent que sur les **canaux d’entrée**. Les **entrées Aux (jacks TRS) et Tape (RCA)** n’ont ni HPF, ni gate, ni limiteur, ni panoramique — seulement compresseur et EQ 4 bandes (tableau 6.1). Brancher table DJ, platines et ordinateur sur des canaux d’entrée (combos micro/ligne de la 32SC ou entrées de la 16R) ; sur une entrée Aux ou Tape, sauter les lignes HPF, Gate et Limiteur, et savoir qu’on perd la sécurité du limiteur.

### TABLE DE MIXAGE DJ

*Source.* Sortie master de la table, en XLR symétrique si possible, RCA sinon via DI.

*Gain.* +0 à +5 dB.

*HPF.* 30 Hz — le DJ gère son sub sur sa table.

*Gate/Expander.* OFF.

*Compresseur.* Everest C100A. Attack Fast, Release Fast. Réduction 1–2 dB maximum : c’est une sécurité, pas un traitement.

*EQ.* **Flat.** Le DJ égalise déjà sur sa table. Intervenir seulement sur un problème identifié.

*Limiteur.* Threshold -1 dB, Release 250–300 ms — catégorie Sources déjà mixées (2.4) : la sortie d’une table est un mix complet, pas une source isolée.

*Destination.* Main L/R direct, en stéréo.

*💡 Sur un plateau à plusieurs DJ qui s’enchaînent, réserver deux paires stéréo de canaux. Le DJ suivant se branche et vérifie son niveau sur la paire inactive pendant que le set en cours tourne sur l’autre. L’enchaînement se réduit alors à un fader qui monte et un qui descend.*

### PLATINES VINYLE

*Source.* Sortie ligne après préampli phono.

*Gain.* +10 à +20 dB selon le préampli.

*HPF.* 30 Hz — clics et bruits de surface se logent dans le sub.

*Gate/Expander.* OFF.

*Compresseur.* RC-500, ratio fixe 3:1. Threshold -18 dB, Attack Fast, Release Slow. Réduction 2–3 dB.

*EQ.* Léger cut à 6–8 kHz si les craquements dominent.

*Limiteur.* Threshold -1 dB, Release 250–300 ms (catégorie Sources déjà mixées — 2.4).

*Destination.* Main L/R direct, en stéréo.

### PC / PLAYBACK

*Gain.* +0 à +5 dB.

*HPF.* 40 Hz.

*Gate/Expander.* OFF.

*Compresseur.* Standard Compressor en protection seule. Threshold -15 dB, Ratio 2:1, **Auto** (10 ms / 150 ms imposés, 2.1), réduction 1–2 dB maximum.

*EQ.* Flat — le signal est déjà masterisé.

*Limiteur.* Threshold -1 dB, Release 250–300 ms (catégorie Sources déjà mixées — 2.4). Sécurité contre un fichier mal normalisé ou un volume poussé côté ordinateur.

*Destination.* Main L/R direct, en stéréo.

**TECHNO LIVE — machines et boîtes à rythmes**

Un set techno live n’est pas un DJ set : les sources sortent séparément et demandent un vrai traitement. Structure typique.

*Sorties séparées (idéal).* Kick sur un canal, basse/sub sur un autre, percussions et synthés sur les autres. Chaque source suit le preset correspondant de ce guide — le kick machine se traite comme un kick, avec un HPF plus bas (25–30 Hz) et **Release limiteur 150 ms**.

*Sortie master unique (fréquent).* Traiter comme une table DJ : Everest C100A léger, EQ flat, direct au Main. Ne pas essayer de récupérer un mix mal équilibré à l’EQ — demander à l’artiste d’ajuster sur sa machine.

*Assignation bus.* Si les sources sortent séparément, kick machine et percussions vers Bus Drums, basses et synthés vers Bus Instru. On retrouve la logique du guide, et les bus font leur travail de glue.

*⚠️ Contrainte matérielle actuelle : un set techno live à sorties séparées en stéréo dépasse très vite les quatre canaux de DI personnels (0.5) — une source stéréo sur la Palmer, les suivantes sur les DI mono ou en emprunt. Privilégier les sorties symétriques directes quand la machine en dispose.*

# PARTIE 4 — BUS DE GROUPE

Tous les bus : mode Subgroup, sortie vers Main L/R. **Ordre du signal sur les bus : Compresseur → EQ** — l’ordre par défaut de la console (1.6), l’inverse de ce que ce guide règle sur les canaux. On colle d’abord, on colore ensuite.

## 4.1 Bus Drums — FlexMix 9+10 (stéréo)

*Contenu.* Toute la batterie, kick compris : kick, caisse claire, overheads, et les toms lorsqu’ils sont micés en emprunt.

*Compresseur.* Brit Comp. Threshold -15 dB, **Attack 10 ms** (ou 30 ms pour plus d’attaque), Ratio 4:1, Release : le cran le plus proche de 200–300 ms, Makeup +2 dB. *Les crans d’Attack imprimés sur le panneau sont 0,1 / 0,3 / 1 / 3 / 10 / 30 ms (2.8) : les « 10–20 ms » des versions précédentes n’existaient pas. Si le Release est lui aussi cranté comme sur le bus compressor SSL (0,1 / 0,3 / 0,6 / 1,2 s / Auto — inférence), prendre 0,3 s.* Réduction visée 3–5 dB. L’attaque relativement lente laisse passer les premiers transitoires puis colle le sustain — c’est ce qui donne le punch de groupe.

*EQ.* Solar 69. Bande Low vers 100 Hz, gain flat : laisser respirer la fondamentale du kick et de la caisse claire, elles sont déjà traitées au canal. Bande Mid vers 800 Hz, +2 dB, mode Peak, pour le corps de l’ensemble. Bande High — **fréquence réglable, pas fixée à 10 kHz** — à placer entre 8 et 10 kHz selon le kit. Gain : **+1 à +2 dB avec les overheads Lewitt du kit de référence** (paragraphe suivant) ; jusqu’à +3 dB seulement avec des overheads plus neutres.

*Avec les overheads Lewitt.* Ces micros apportent déjà beaucoup d’aigu par leur voicing. La bande High du Solar 69 se règle donc plus bas qu’on ne le ferait avec des overheads neutres : **+1 à +2 dB suffisent généralement**, et il n’est pas absurde de la laisser flat. Si le bus sonne dur, c’est cette bande qu’il faut baisser en premier.

*Limiteur.* Threshold -1 dB, **Release 250–300 ms** (catégorie Bus/Master).

*Fader.* -3 à 0 dB vers Main L/R.

*Piste à tester — saturation ou mise en forme des transitoires par l’ordinateur.* Le Fat Channel n’a ni saturateur dédié ni « transient shaper » : le grain du Bus Drums vient du Brit Comp. Pour aller plus loin, un FlexMix peut partir en USB (manuel 12.3.4 : « Mixages Flex », sans distinction entre mode Aux et mode sous-groupe) vers un plugin (Decapitator, déjà utilisé en 7.10, ou un transient shaper) et revenir sur un canal. **Deux pièges** : le retour arrive en retard de la latence de l’ordinateur, donc tout le Bus Drums se décale du reste du mix ; et **en parallèle** du Bus Drums ou avec le Bus Parallel actif, ce retard crée un filtrage en peigne — refaire le test d’annulation de 4.4 sur le chemin USB avant tout usage. Le coût en canaux est celui de 7.10 (un canal de retour par côté). Dosage à l’oreille. *Registre 8.7.*

## 4.2 Bus Instru — FlexMix 11+12 (stéréo)

*Contenu.* Basse, contrebasse, guitares, claviers, cuivres, bois — tout sauf batterie et voix.

*Compresseur.* FC-670. **Régler l’Input Gain en premier** : c’est lui qui pilote la profondeur de compression. Monter jusqu’à obtenir 2–4 dB de réduction, puis affiner le point de déclenchement au Threshold, vers -18 dB. Time Constant en position 3 (lente) : les graves de la basse ont le temps de se propager avant que la compression intervienne.

*EQ.* Alpine EQ-550 — fréquences à sept crans par bande (2.3) : « vers » veut dire **le cran le plus proche** de la valeur indiquée, ici comme en Partie 6. *L’addendum ne liste pas les sept fréquences de chaque bande : elles se lisent sur le panneau et sont à relever (registre 8.7). Tant que la liste n’est pas dans ce guide, un preset écrit « Alpine, bande Low, cran le plus proche de 100 Hz » — jamais une fréquence de cran supposée.* Bande Low vers 100 Hz : **vérifier à l’oreille avant de couper.** Le -1 dB en shelf de l’ancienne configuration supposait que la basse était ailleurs. Maintenant qu’elle est sur ce bus, ce cut peut rendre le fond maigre — laisser flat par défaut et ne couper que si le bas s’empâte. Bande Mid vers 2 kHz, +2 dB, pour la présence du groupe d’instruments. Bande High vers 8 kHz, +1 dB, en shelf, pour l’air.

*Limiteur.* **OFF par défaut, ON dès qu’une source électronique à dynamique imprévisible est sur le bus** — synthé analogique dont on ouvre le filtre en montée, groovebox, machine. Ces sources peuvent gagner 10 dB en une seconde sans prévenir, et le FC-670 en Time Constant lente ne les rattrape pas. Quand il est ON : Threshold -1 dB, Release 250–300 ms.

*Fader.* -3 à 0 dB vers Main L/R.

**Option à tester — la compression « dual mono ».** *Condition d’emploi, à lire d’abord : elle n’a d’intérêt que si aucune source grave centrée ne domine ce bus — basse sortie vers le Bus Basse (4.6), ou formation sans basse. Sinon, rester en détection couplée.* Le Fat Channel n’a pas de modèle de compresseur dual mono, mais la console a mieux : un réglage qui s’applique à **n’importe quel** modèle. Dans les réglages d’un canal ou d’un bus couplé, les *Options de couplage stéréo* contiennent une case **Comp./Limiter**. Le manuel est explicite : activée, « les signaux détectés sur n’importe lequel des deux canaux couplés entraînent une réduction de gain identique sur les deux » ; désactivée, elle laisse « le compresseur/limiteur agir indépendamment sur chacun des deux canaux couplés ». C’est exactement la définition du dual mono.

*Ce que ça change sur ce bus.* En détection couplée, une guitare panoramiquée à gauche qui attaque fort fait reculer aussi le clavier placé à droite. En dual mono, chaque côté est compressé pour ce qu’il contient : le clavier ne bouge pas quand la guitare tape. Sur un bus de sources hétérogènes et panoramiquées, c’est plus transparent.

*Les deux limites à connaître avant d’y toucher.* **Une source centrée déclenche les deux côtés de la même façon** : tant que la basse est sur ce bus, c’est elle qui commande la réduction, à gauche comme à droite, et le dual mono n’apporte presque rien — il ne prend son sens que si la basse en sort (4.6). **Deux côtés compressés différemment, c’est une image stéréo qui peut bouger** : une source placée entre le centre et un bord se déplace légèrement quand un seul côté est réduit. Avec 2–4 dB de réduction en Time Constant lente, l’effet attendu est faible, mais c’est précisément ce que le test doit établir.

*Ce que le manuel dit, et ne dit pas.* L’option appartient au périmètre **Channel Strip** des scènes (« Options de couplage ») : elle est donc rappelée scène par scène, ce qui permet de l’activer en rock et de la laisser couplée en dub. Le modèle de compresseur reste commun aux deux côtés. Le manuel ne précise pas si le réglage vaut aussi pour le gate, ni comment le FC-670 — dont l’original possède ses propres modes de liaison — se comporte en détection séparée : **non documenté, à écouter**.

*Le test.* Bruit rose ou morceau de référence sur le bus, réduction réglée à 3 dB. Envoyer une source forte d’un seul côté et regarder le mètre de réduction de l’autre : en couplé il bouge, en dual mono il doit rester immobile. Puis, sur le groupe, écouter une source centrée pendant qu’un instrument latéral joue fort : si elle se déplace, revenir en couplé. **Statut : à tester — rester en détection couplée par défaut.** Le Bus Drums et le Bus Voix restent couplés dans tous les cas : sur l’un le kick et la caisse claire sont au centre, sur l’autre la voix lead aussi.

## 4.3 Bus Voix — FlexMix 13+14 (stéréo)

*Contenu.* Toutes les voix, lead et chœurs.

*Compresseur.* Tube CB, **mode Manual obligatoire** — le mode Fixed verrouille Attack à 1 ms et Release à 50 ms sans recours, ce qui ne laisse aucune marge d’adaptation au chanteur. Threshold -15 dB, Gain +2 dB, réduction visée 4–6 dB. Les temps et le ratio varient selon le style (voir Partie 6).

*EQ.* Selon le style, Vintage 1970s pour le mordant ou Alpine EQ-550 pour la chaleur (voir Partie 6).

*Limiteur.* Threshold -2 à -3 dB selon le style, **Release 150–200 ms** (catégorie Voix).

*Fader.* -3 à 0 dB vers Main L/R.

## 4.4 Bus Parallel — FlexMix 15 (mono)

**⚠️ Statut : à tester.** L’alignement des deux chemins n’a jamais été vérifié (voir le test ci-dessous et le registre 8.7). Tant qu’il ne l’est pas, ce bus est un effet à doser à l’oreille, pas un renfort garanti.

*Contenu.* Copie parallèle de kick, caisse claire et toms — les mêmes sources que le Bus Drums, envoyées en plus ici.

*Compresseur.* Comp 160. Threshold réglé au mètre de réduction de gain (2.1 : BELOW et ABOVE sont très probablement des voyants, pas des positions — vérification au registre), Output Gain +10 dB. **Cible = résultat, pas position** : 8–12 dB au mètre de réduction de gain sur les frappes. *Méthode :* commande Compression dans la moitié haute de sa course (sa graduation n’est pas un ratio, 2.1 — les « 7–8 sur 10 » des versions précédentes étaient une position, pas une valeur), puis descendre le Threshold jusqu’à lire 8–12 dB ; si le Threshold arrive en butée avant, monter Compression et recommencer. Si l’un des deux voyants s’avère être une commande, noter ce qu’elle change et le consigner ici.

**⚠️ Vérification préalable à faire une fois — l’alignement des deux chemins.** Toute la compression parallèle repose sur une hypothèse que ce guide a toujours posée sans la vérifier : que le signal du Bus Parallel arrive **exactement en même temps** que celui du Bus Drums. Si les deux chemins présentent le moindre décalage — latence de traitement du Comp 160, différence de parcours entre deux bus — leur somme au Master ne renforce plus le punch, elle produit un filtrage en peigne. Le manuel PreSonus ne chiffre nulle part la latence des modèles de plug-ins ni l’alignement entre bus. Ça ne se déduit pas : ça se mesure.

*Le test, dix minutes une seule fois.* **Utiliser une source large bande, pas le kick** : la caisse claire, ou mieux un bruit rose ou une piste de batterie complète en lecture (balance virtuelle, 7.12). Le kick est trop indulgent : son énergie est dans le grave, où un petit décalage ne creuse presque rien. Calcul : avec la polarité inversée, un décalage τ laisse un résidu de 2 |sin(π f τ)| par rapport à un bus seul. Pour 13 échantillons à 48 kHz (0,27 ms), il vaut environ -20 dB à 60 Hz — le kick a l’air de passer le test — mais il est **maximal vers 1,85 kHz**, où le décalage vaut une demi-période. C’est la même fréquence où, en somme normale, les deux bus creusent une encoche. Sur une source large bande, seule une coïncidence à l’échantillon près donne une annulation profonde.

Envoyer cette source vers Bus Drums et Bus Parallel. **Aucun traitement chargé sur les deux bus**, mêmes niveaux de fader. Noter le niveau au mètre du Main avec un seul bus, puis les deux ensemble avec la polarité du Bus Parallel inversée.

*Critère de réussite : un résidu au moins 20 dB sous le niveau d’un bus seul.* Ce seuil est **calculé, pas documenté** : un résidu à -20 dB signifie que les deux chemins diffèrent de moins de 10 % en amplitude, donc qu’en somme normale l’écart reste sous ±0,5 dB — plus aucun peigne audible. Un résidu à -10 dB laisse jusqu’à environ ±1,6 dB d’ondulation : audible. Si le critère est atteint, les deux chemins sont alignés, l’addition est propre, et la compression parallèle fonctionne comme prévu.

*Deuxième temps.* Charger le Comp 160 sur le Bus Parallel mais le laisser **bypassé** (Processor Off), et refaire le test d’annulation. Si le silence tient toujours, le simple fait de charger le plug-in n’introduit pas de retard. S’il ne tient plus, le plug-in ajoute une latence : elle se compense au **retard de sortie** du bus le plus rapide (voir 7.8), par petits pas, jusqu’à retrouver l’annulation.

*Si l’annulation ne se produit jamais*, même sans traitement : le montage n’est pas une addition transparente sur cette console. Le Bus Parallel reste alors utilisable, mais **comme un effet assumé** — on le dose à l’oreille pour ce qu’il apporte, sans prétendre qu’il renforce proprement le signal d’origine. Noter le résultat du test ici une fois pour toutes.

*EQ.* RC-500. Bande Low vers 100 Hz flat. Bande Mid vers 250 Hz, -2 dB, pour éviter le bas-médium lourd que génère la compression extrême. Bande High vers 3 kHz, +2 dB, pour la présence.

*Limiteur.* Threshold -1 dB, **Release 150 ms**. Ce bus reçoit le kick : la règle de 2.4 s’applique (sur le grave, jamais plus court que 150 ms, sous peine de distorsion par suivi de la forme d’onde). En pratique, le Comp 160 en amont a déjà tassé les crêtes et ce limiteur travaille peu — mais s’il travaille, il doit le faire sans salir le bas.

*Fader.* **-∞ par défaut.** Monter par incréments de 1 dB jusqu’à sentir le punch se renforcer. Plafond utile : -12 à -6 dB. Au-delà, le son devient étouffé et artificiel.

*Principe.* C’est la compression parallèle new-yorkaise en live : le signal naturel reste intact sur le Bus Drums, on ajoute par-dessous une couche écrasée qui apporte du punch brut sans détruire la dynamique.

*Alternative à tester — le Class-A FET en position « All ».* Le Comp 160 n’est pas le seul candidat historique pour ce poste. La position **All** du Class-A FET reproduit le fameux *All Buttons In* du 1176 (voir 2.8) : ratio instable, attaque et relâchement déformés, son explosif et saturé. Toute la littérature s’accorde sur un point — **ce mode ne s’utilise qu’en parallèle, jamais en direct sur un canal**, ce qui décrit exactement ce bus. Deux caractères très différents à comparer : le Comp 160 écrase avec le grain VCA, le FET en All apporte de la saturation et de la texture. **Jamais testé ici. Le bus existe déjà, le test ne coûte qu’un changement de modèle.**

## 4.5 Bus Divers — FlexMix 16

*Usage.* Instruments imprévus, effets externes, toute source qui ne rentre dans aucune case. C’est le bus qui évite de bricoler un routage en urgence.

*Compresseur.* Standard Compressor, neutre. Threshold -18 dB, Ratio 3:1, Attack 10 ms, Release Auto.

*EQ.* Standard EQ, à ajuster en trente secondes selon ce qui arrive.

*Limiteur.* Threshold -1 dB, Release 250–300 ms (ligne Bus, 2.4) ; **150 ms** si la source imprévue est grave.

*Fader.* 0 dB Unity.

## 4.6 Bus Basse — option sur sous-groupe fixe

**Statut : option à tester, hors architecture par défaut.** Les bus du guide restent sur les FlexMix ; celui-ci utilise la réserve des sous-groupes fixes (1.3) et ne déplace rien.

*Quand il se justifie.* Quand la basse arrive par **deux sources ou plus** — DI et micro d’ampli, ou DI et sortie XLR de tête d’ampli, ou basse et contrebasse sur un même set. Avec une seule source, un bus à elle seule n’apporte rien que le canal ne fasse déjà : rester sur l’architecture standard — **à une exception près** : quand le compresseur du canal de basse est réservé au ducking par le kick (3.3, 2.5), le canal ne compresse plus la basse, et le Bus Basse redevient justifié même avec une seule source, parce qu’il porte cette compression.

*Montage.* Les canaux de basse s’assignent au **sous-groupe fixe A**, laissé en mono, lui-même assigné au Main — et **désassignés du Bus Instru**. *Point de contrôle :* le manuel PreSonus ne dit pas si un canal peut être affecté à deux sous-groupes à la fois ; si c’est possible et qu’on oublie de le retirer du Bus Instru, la basse arrive deux fois au Main. Vérifier au mètre du Bus Instru que la basse n’y apparaît plus. La phase entre DI et micro se règle d’abord aux canaux (2.9, 7.7) : un bus ne répare pas deux sources mal alignées, il les colle telles quelles.

*Ce qu’on y gagne.* Un seul fader pour toute la basse. Une seule compression commune sur la somme des sources, au lieu de deux compresseurs qui réagissent chacun à leur moitié du son. Et un Bus Instru délesté du grave continu : sa compression ne respire plus au rythme de la basse, ce qui rend l’option dual mono de 4.2 pertinente.

*Ce qu’on y perd.* La « cohésion harmonique » voulue en 1.3 : la basse n’est plus liée aux guitares et aux claviers par le FC-670. En reggae et en dub, où cette liaison fait le son, **ne pas l’utiliser**.

**⚠️ Ce que ce bus ne permet pas.** Key Source n’existe que sur les canaux d’entrée (2.5). Le ducking kick → basse **ne peut pas** se faire sur le Bus Basse : il reste sur chaque canal de basse, Key Source = canal kick, comme décrit en 2.5. Toute fiche qui placerait ce sidechain sur le bus serait fausse.

*Traitement.* Aucun réglage de bus n’a été validé — ne pas en reconstituer un. Point de départ logique : retirer la compression des canaux de basse quand ils sont deux, et reporter sur le bus le compresseur prescrit pour la basse en 3.3, avec la même cible de réduction — par défaut, faute d’essai. *Candidat à comparer :* le **FC-670** (2.1), le compresseur de bus que le guide utilise déjà pour lier la basse au reste en 4.2, position 3. Comparaison A/B à faire sur un enregistrement (7.12) ; limiteur Threshold -1 dB, **Release 150 ms, jamais plus court** (2.4). À arrêter à l’oreille au premier essai, puis à consigner ici.

# PARTIE 5 — MASTER & FX

## 5.1 Traitement Master

*Compresseur.* Everest C100A. Attack Fast, Release Fast. **Réduction 1–2 dB maximum.** Si le compresseur Master travaille davantage, le problème est en amont : corriger les bus, pas le Master.

*EQ.* Passive Program EQ. Low Boost +1 dB vers 60 Hz pour la fondation, High Boost +1 dB vers 10 kHz pour l’air. **Règle absolue : ±1 à 2 dB maximum.**

*À tester — le tour de passe-passe Pultec (voir 2.8).* Au lieu du Low Boost seul : **Low Boost +1 à +2 dB ET Low Atten +1 à +2 dB, tous les deux à 60 Hz**, simultanément. Sur ce circuit passif les deux ne s’annulent pas — le boost est un pic large, l’atténuation un plateau qui démarre juste en dessous. Résultat attendu : une fondation plus ferme *et* un sub nettoyé sous les 40 Hz, d’un seul geste. C’est la technique la plus documentée de ce modèle, et le panneau PreSonus partage bien le même sélecteur de fréquence entre les deux commandes. **Non testé sur cette config — à comparer en A/B avec le réglage actuel avant de l’adopter.**

*Limiteur.* Threshold selon le style (voir Partie 6), **Release 250–300 ms**. Crête après limiteur : **-1 dBFS maximum** (voir 1.2).

*Niveaux par style — comment lire ce tableau.* Ces valeurs RMS ne sont **pas des standards musicaux** et ne se comparent à rien d’extérieur. Le RMS dépend de la fenêtre de mesure, du spectre, du facteur de crête et de l’appareil qui mesure : deux mix à -10 dBFS RMS peuvent être perçus à des volumes très différents. Ce tableau sert à une seule chose, mais il la fait bien : **retrouver d’une date à l’autre la densité qui a fonctionné**, mesurée toujours sur le même mètre, celui de la console. C’est un repère de reproductibilité, pas un objectif de niveau.

Le niveau réel en salle se règle au système de diffusion et se juge à l’oreille et au sonomètre, jamais en poussant le mix vers une valeur du tableau.

| **Style** | **RMS repère** | **Limiteur** | **Rendu** |
| --- | --- | --- | --- |
| Punk / Métal | -10 à -8 dBFS | -2 dBFS | Dense et agressif |
| Rock | -11 à -9 dBFS | -2 dBFS | Dense mais respire |
| Hip-Hop | -12 à -10 dBFS | -3 dBFS | Dynamique préservée |
| Reggae | -13 à -11 dBFS | -3 dBFS | Respire, naturel |
| Dub | -12 à -10 dBFS | -3 dBFS | Grave dominant, espace |
| Techno Live | -10 à -8 dBFS | -2 dBFS | Compact et impactant |

## 5.1bis Le rack d’effets — ce que la console propose réellement

Quatre processeurs d’effets stéréo, chacun avec son propre bus auxiliaire. Neuf types disponibles : **Digital XL Reverb, PAE-16 Digital Reverb, 335 Digital Reverb, Vintage Plate Reverb, Mono Delay, Stereo Delay, Ping Pong Delay, Chorus, Flanger.**

*Les quatre reverbs et leurs commandes réelles* (manuel 9.1.2.1 à 9.1.2.4) :

| **Reverb** | **Caractère** | **Commandes documentées** |
| --- | --- | --- |
| Digital XL | Convolution, émule un espace acoustique | Predelay · Reflection · Size · LPF Freq · LF Damping Freq · LF Damping Gain |
| 335 Digital | Numérique années 70 | Predelay · Diffusion · Reflection · Size · Low Pass · LF Damp Freq · LF Damping Gain |
| PAE-16 Digital | Numérique années 80 | Predelay · Diffusion · Reflection (Time) · Low Pass · LF Damp Freq · LF Damping Gain |
| Vintage Plate | Plaque mécanique | Predelay · Reflection · Low Pass · LF Damp Freq · LF Damping Gain |

*Ce que fait chaque commande, et comment s’en servir sans Decay.*

**Reflection — la commande la plus importante des quatre reverbs.** Elle règle le niveau des premières réflexions. Le manuel donne la clé de lecture : **plus les premières réflexions sont fortes, plus le local semble petit.** C’est donc elle, et non un réglage de durée, qui décide si on entend une petite pièce ou un grand espace. Reflection haut donne un espace proche et dense, qui claque ; Reflection bas donne un espace grand et lointain *(lecture de ce guide à partir de la phrase du manuel ; le manuel ne parle que de taille perçue, pas de durée)*. En extérieur, Reflection bas (voir 5.6).

**Predelay.** Temps entre le son direct et les premières réflexions. Il crée de la place entre la voix et sa reverb, et donc de l’intelligibilité, sans rien allonger. C’est le premier réglage à monter quand une reverb noie le texte.

**Diffusion** (335 et PAE-16 seulement). Densité de la queue de reverb. Faible, on entend des échos individuels ; élevée, un nuage continu. C’est le seul paramètre qui approche la notion de texture de queue.

**Size** (Digital XL et 335 seulement). **Largeur de l’image stéréo, pas taille de pièce.** Le manuel est explicite. En diffusion mono ou sur un public non centré, une Size large n’apporte rien à la majorité des auditeurs ; la garder modérée.

**Low Pass / LPF Freq.** Assombrit la reverb en coupant le haut. *(La description du manuel français est erronée sur ce point, voir 2.6.)* C’est le réglage qui empêche une reverb de siffler par-dessus les cymbales.

**LF Damp Freq et LF Damping Gain.** Accentuent une zone de graves choisie pour réchauffer. **Deux commandes à laisser tranquilles en live** : elles ajoutent du bas dans un effet qu’on passe déjà son temps à nettoyer — et le retour n’a pas de HPF pour le faire (5.2). Gain à zéro, sauf besoin identifié.

**Les réglages sans échelle documentée — convention et méthode.** Le manuel décrit Reflection (un niveau, en décibels), Size, Diffusion, Spread et Width, mais **ne donne ni plage ni valeur par défaut** pour aucun des cinq. Ce guide ne peut donc pas les chiffrer ; il fixe une convention et une méthode, valables pour toutes les Parties 5 et 6.

*Convention.* Sur la course affichée à l’écran : **« bas » = tiers inférieur, « modéré » = milieu de course, « haut » = tiers supérieur** ; « au plus bas » = butée basse ; « modéré à bas » = entre le milieu et le tiers inférieur. « Assez haut » = entrée du tiers supérieur.

*Méthode — Reflection (une minute, source seule, départ ouvert).* Partir du milieu de course. Monter jusqu’à entendre nettement une petite pièce — la « salle de bains » sur une voix, la « boîte » sur une caisse claire. Redescendre jusqu’à ce que cette pièce disparaisse. Pour une cible « modéré à bas » (voix), s’arrêter là. Pour une cible « assez haut » (batterie), remonter jusqu’à la limite où la pièce commence à s’entendre et rester juste en dessous. Pour « au plus bas » (extérieur), aller en butée et ne remonter que si la reverb devient inaudible.

*Méthode — Size, Spread, Width (largeur stéréo).* Partir du milieu de course. Écouter depuis un côté de la salle, pas au centre : si l’effet disparaît ou si la source semble se déplacer, réduire. « Modéré » = la valeur la plus large qui reste lisible depuis les côtés. En diffusion mono, ces réglages n’ont pas d’effet utile : les laisser au milieu.

*Méthode — Diffusion.* Partir du milieu. Si des échos distincts s’entendent sur les transitoires de batterie, monter ; si la queue devient un nuage qui masque le texte, descendre.

*À relever une fois, console seule (registre 8.7) :* pour chaque effet, la plage et la valeur par défaut de ces cinq commandes. Une fois relevées, les qualificatifs du guide seront remplacés par des valeurs.

*Les delays et leurs commandes réelles* (manuel 9.1.2.5 à 9.1.2.7). Point le plus utile, ignoré jusqu’à la V13 : **les delays filtrent deux fois.**

| **Delay** | **Commandes documentées** |
| --- | --- |
| Mono | Delay Time · Tap Assign · Feedback · LP Filter · HP Filter |
| Stereo | Delay Time A/B · Tap Assign A/B · Feedback A/B · Spread · LP Filter · HP Filter · **Fb A/B LPF** · **Fb A/B HPF** |
| Ping Pong | Time Left/Right · Tap Assign L/R · Width · Feedback · **Fb Time** · LP Filter · HP Filter · **Fb LPF** · **Fb HPF** |

**LP Filter et HP Filter** agissent sur le signal retardé : ils façonnent **toutes** les répétitions de la même façon. C’est le vrai filtrage que le retour d’effet ne sait pas faire (pas de HPF sur ce type de canal, 5.2) : sur un delay, **le HP Filter de l’effet est le coupe-bas**.

**Fb LPF et Fb HPF** agissent sur le signal **réinjecté**, celui qui repasse dans la boucle. Chaque répétition subit donc le filtre une fois de plus que la précédente : la première est claire, la deuxième plus sombre, la troisième encore plus. **C’est le seul moyen d’obtenir un delay qui s’éteint en s’assombrissant**, le geste central du dub, et c’est impossible à reproduire avec le filtre du retour.

**Fb Time** (Ping Pong). Décale le retard du signal réinjecté par rapport au retard principal : les rebonds se déphasent progressivement au lieu de se superposer. Utile pour désynchroniser une nappe d’échos.

**Tap Assign.** Le tempo se bat à la touche TAP. Une fois la touche assignée au Time d’un delay, elle le reste, quelle que soit la page affichée. Sur un plateau, c’est le moyen le plus rapide de recaler un delay entre deux morceaux — plus rapide et plus juste que de calculer des millisecondes.

*Le paramètre Decay.* **Aucune des quatre reverbs ne documente de commande Decay.** Les versions V5 à V13 de ce guide en prescrivaient pourtant des valeurs précises. Le mot n’apparaît dans le manuel qu’en 13.9.1, un exposé général sur la réverbération qui n’est pas un descriptif de l’éditeur d’effets. **À vérifier une fois sur la console** : ouvrir chaque reverb, lister les paramètres réellement affichés à l’écran, et noter le résultat ici. Si un Decay existe, il redevient l’outil principal de longueur et cette section sera à reprendre. En attendant, la longueur se règle par **Reflection** (taille perçue), **Predelay** (séparation) et **Diffusion** quand elle existe, et surtout par le **choix du type de reverb**.

## 5.2 FX A — Reverb Voix

*Type.* **Vintage Plate Reverb.** La plaque est le choix historique de la voix : dense, sans signature de pièce, elle n’ajoute pas de géométrie parasite à un lieu qui en a déjà une.

*Réglages.* Predelay **40 ms** — assez pour détacher la reverb du mot et préserver l’articulation. Reflection **modéré à bas** : réflexions trop fortes = petite pièce = effet de salle de bains sur une voix. Low Pass **8 kHz** en intérieur (5–6 kHz en extérieur, voir 5.6). LF Damping Gain à **zéro**. Le dosage se fait aux départs et au fader du retour. *(Les versions précédentes écrivaient « Mix 100 % » : le manuel ne documente aucune commande Mix sur les reverbs, 9.1.2.4. Si l’écran en affiche une, la mettre à 100 %.)*

*Ducking de la reverb par la voix — exclu sur le retour, non tranché par renvoi sur un canal d’entrée.* Jusqu’à la V28, ce guide prescrivait ici un compresseur sur le retour avec Key Source = canal voix lead. Le manuel ne le permet pas : Key Source est réservé aux **canaux d’entrée** (manuel 6.8.3 et 6.8.4, « canaux d’entrée uniquement »), et le tableau 6.1 range les **retours d’effet** dans une catégorie à part. Reste à savoir si le retour d’un effet interne peut être renvoyé sur un canal d’entrée, qui, lui, accepte un Key Source. **Le manuel se contredit, donc ce n’est ni acquis ni exclu** : les listes de sources des départs analogiques, AVB et USB (12.3.2 à 12.3.4) ne citent que le **mixage de départ d’effet, pris avant le processeur**, jamais le retour ; mais le tableau 6.1 inscrit « Départ USB » dans la colonne des retours d’effet comme dans les autres. *Deux vérifications de trente secondes sur la console :* le compresseur du retour FX A propose-t-il un Key Source ; et le menu **USB Sends** propose-t-il le retour FX A comme source.

*Si USB Sends propose le retour FX A :* la reverb interne part en USB et revient aussitôt sur un canal d’entrée, sans plugin (l’ordinateur ne sert que de boucle). Ce canal accepte un Key Source = voix lead : le ducking se fait alors avec la reverb de la console. *Registre 8.7.*

*Si USB Sends ne le propose pas — la voie documentée, à tester :* faire produire la reverb par l’ordinateur (7.10, « Les effets de la table traités par l’ordinateur ») : départ FX A pré-processeur vers USB, reverb dans le logiciel, retour sur un canal d’entrée en Source USB, et sur ce canal un compresseur avec Key Source = voix lead. C’est un montage sur l’effet le plus important du guide : à éprouver d’abord en balance virtuelle (7.12), jamais en premier montage un soir de concert. *En natif, la lisibilité du texte se gagne autrement :* Predelay (ci-dessus), Reflection modéré à bas, et départs dosés depuis les voix.

*EQ du retour.* **Le Fat Channel d’un retour d’effet n’a pas de filtre passe-haut** (tableau 6.1) — le « HPF 300 Hz » des versions précédentes n’existait pas. **Le levier à essayer en premier : la bande LOW du Standard EQ en plateau** (Low Shelf, manuel UC Surface 3.3), réglée en atténuation. Le plateau est documenté pour le Standard EQ ; sa présence sur un retour d’effet reste à vérifier (registre 8.7). Un plateau qui coupe tout le grave sous sa fréquence se rapproche bien plus d’un HPF qu’une cloche ; la V29 disait à tort que le Standard EQ n’avait que des cloches. Fréquence et profondeur à l’oreille, en partant du repère des versions précédentes (vers 300 Hz) ; la pente d’un plateau reste plus douce qu’un vrai filtre. Le **Vintage 3-Band EQ** a un filtre passe-haut intégré (addendum 4.6), mais l’addendum ne chiffre pas sa plage et le manuel ne dit pas si les modèles d’EQ se chargent sur un retour d’effet : **à vérifier sur la console**. Cut -2 dB à 1 kHz et -2 dB à 8 kHz.

*Routing.* Retour affecté au Bus Voix, fader du retour à -18 dB. *Le manuel (5.5.1) : le bus d’effet « dispose d’un retour dans chaque mixage Flex ainsi que dans le mixage principal », réglable en sélectionnant le mixage puis le canal « FX A ».* C’est aussi par là que se dose la reverb dans un retour de scène.

## 5.3 FX B — Stereo Delay

*Type.* Stereo Delay.

*Réglages.* Delay Time A/B calés au tempo **à la touche TAP** : le résultat est toujours plus juste qu’une valeur en millisecondes calculée à l’avance. À défaut de TAP, 375/500 ms pour un feel ternaire (hip-hop, reggae), 250/500 ms pour un feel binaire (punk, rock). Feedback A/B **40 %. LP Filter 6 kHz** et **HP Filter 200 Hz** réglés dans l’effet lui-même. **Fb LPF 5 kHz** pour que les répétitions s’assombrissent en s’éloignant. Spread modéré.

*EQ du retour.* Le filtrage étant fait dans l’effet, le retour peut rester quasi flat : un cut -3 dB à 6 kHz, Q 2.0, si ça siffle encore.

*Ducking du delay par la voix.* Même limite qu’en 5.2 : pas de Key Source sur un retour d’effet. Si les répétitions masquent les fins de phrase, la voie est l’ordinateur (7.10) — FabFilter Timeless 3 a son propre ducking par sidechain. En natif : Feedback plus bas et départs plus courts sur les passages chargés.

*Routing.* Retour affecté au Bus Voix, fader du retour à -20 dB. **Affectation au Bus Instru seulement quand un instrument reçoit du delay** : un instrument soliste (guitare lead, cuivre, mélodica) ou un geste d’effet voulu par le style (les envois de skank et de caisse claire du dub, 6.6). Pas d’affectation « par défaut » : sans départ depuis un instrument, elle ne sert à rien, et un delay permanent sur une rythmique brouille le tempo. *Les versions précédentes donnaient deux niveaux différents (-20 dB vers le Bus Voix, -24 dB vers le Bus Instru) : sur un FlexMix en mode sous-groupe, le manuel ne documente qu’une affectation, pas un niveau propre à chaque bus (6.7). Si la console en propose un, garder 4 dB de moins vers le Bus Instru ; sinon, le dosage se fait aux départs des canaux.*

## 5.4 FX C — Reverb Drums

*Type.* **Digital XL Reverb**, la convolution donnant l’espace le plus crédible sur des transitoires.

*Réglages.* Predelay **20 ms**. Reflection **assez haut** — on cherche un espace court et dense qui colle au kit, pas une cathédrale. **Size modéré** *(largeur d’image stéréo : à ne pas ouvrir en grand, ça décentre la caisse claire par rapport aux overheads)*. LPF Freq **6–8 kHz**. LF Damping Gain à zéro.

*EQ du retour.* Pas de filtre passe-haut sur un retour d’effet (tableau 6.1, voir 5.2). Bande LOW du Standard EQ **en plateau** (Low Shelf, UC Surface 3.3), en atténuation, jusqu’à ce que les toms ne fassent plus vaser la reverb — ou le HPF du Vintage 3-Band EQ, si la console le propose sur ce retour. Le meilleur levier reste en amont : **pas de départ depuis le kick**, départs modérés depuis les toms.

*Routing.* Retour affecté au Bus Drums, fader du retour à -18 dB. Départs depuis caisse claire et toms, **jamais depuis le kick** : une reverb sur un kick n’apporte que de la boue.

## 5.5 FX D — Ping Pong Delay

*Type.* Ping Pong Delay.

*Réglages.* Time Left/Right **500 ms** ou calés au TAP, Feedback **30 %**, Width modéré, **LP Filter 5 kHz, HP Filter 300 Hz, Fb LPF 4 kHz**.

*EQ du retour.* Cut -4 dB à 8 kHz si nécessaire.

*Routing.* Main direct, fader à **-∞ par défaut**. Disponible pour les effets ponctuels — typiquement un dub delay sur une fin de phrase.

## 5.6 Adaptation extérieur / chapiteau

Contexte fréquent : plein air, chapiteau, guinguette. Moins de réflexions naturelles, le son se disperse. Les réglages pensés pour l’intérieur ne fonctionnent pas tels quels.

*Choix du type.* **Vintage Plate en priorité.** Une plaque n’essaie pas de simuler un lieu ; dehors, une reverb qui simule une pièce qui n’existe pas s’entend comme un artifice. Éviter la Digital XL sur les voix en extérieur pour la même raison.

*Reflection.* **Réglage bas.** Des premières réflexions fortes annoncent un petit local ; en plein air, l’oreille n’en trouve aucune confirmation et l’effet sonne faux.

*Predelay.* **Raccourcir, 20–30 ms.** Dehors, l’énergie directe domine et un predelay long détache l’effet au point qu’on l’entend comme un écho séparé plutôt que comme un espace.

*Low Pass du retour et de l’effet.* **5–6 kHz.** La brillance excessive accentue le côté artificiel.

*Grave du retour FX.* Sans mur pour absorber, la reverb bouillonne dans les graves : atténuer plus franchement qu’en intérieur, avec la bande LOW du retour en plateau (5.2). Le retour n’a pas de filtre passe-haut ; pour les delays, le **HP Filter intégré à l’effet** fait ce travail.

*Delays.* Ils fonctionnent mieux que les reverbs en extérieur : un écho reste lisible là où une queue de reverb se dilue. Sur un plateau en plein air, remplacer une partie de la reverb par du delay court est souvent le meilleur choix.

*GEQ.* Voir 7.3 : dehors, il ne sert quasiment plus, le travail se déplace vers les FX et le placement des enceintes.

Ces ajustements se font sur les presets existants (5.2 et 5.4) — ne pas créer de FX séparés, juste modifier Reflection, Predelay, Low Pass et l’EQ du retour selon le lieu.

## 5.7 Chorus et Flanger

Présents dans le rack, jamais utilisés par ce guide, mais autant savoir ce qu’ils font avant qu’un groupe les demande.

**Chorus** — Rate, Depth, Width, LFO Polarity, Shape, Offset, Feedback. Épaissit une source en la mélangeant à des copies désaccordées et modulées. Usage live plausible : une guitare claire de reggae ou de post-punk, un clavier trop maigre. À doser très bas, l’effet devient vite daté.

**Flanger** — même famille, modulation plus courte et plus résonante. Usage ponctuel sur une guitare ou un synthé, en effet de transition plutôt qu’en réglage permanent.

*Rappel.* Il n’y a que **quatre slots**. Charger un Chorus, c’est renoncer à une reverb ou à un delay. Sur les scènes de ce guide, les quatre slots sont déjà tous attribués — ce serait un remplacement délibéré, pas un ajout.

# PARTIE 6 — SCÈNES PAR STYLE

Six scènes sauvegardées dans la mémoire du 32SC, plus une configuration Techno Live. Chacune se rappelle en quelques secondes ; seuls les gains d’entrée demandent un ajustement au groupe du jour.

Les paramètres non mentionnés dans une scène restent ceux des Parties 3, 4 et 5 (règle de priorité complète dans le Bloc assistant, en tête de document).

## 6.1 PUNK

*Bus Voix — compresseur.* Tube CB Manual, Attack Fast, Release Fast, Ratio 4:1, Threshold -15 dB. Réduction 4–6 dB. Rapide sur les consonnes dures, relâche vite pour ne pas étouffer entre les mots.

*Bus Voix — EQ.* Vintage 1970s. **Low Freq déplacée vers 200 Hz** (60 Hz par défaut, 2.3), gain +2 dB pour le corps. L-Mid 700 Hz +1 dB, **H-Mid 4,8 kHz +3 dB** pour l’agressivité qui fait percer la voix, High +2 dB (fréquence fixe, non chiffrée par le manuel : doser à l’oreille sur les sifflantes — si les « s » durcissent, revenir à +1 dB ou à zéro).

*Bus Voix — limiteur.* Threshold -2 dB, Release 150–200 ms.

*Bus Drums.* Brit Comp réduction 4–5 dB, plus appuyée que la base. Solar 69 High **+1 à +2 dB** — avec les overheads Lewitt, pas plus (4.1).

*Bus Parallel.* Fader -8 à -6 dB — présent et agressif.

*Master.* Limiteur -2 dBFS, RMS -10 à -8 dBFS.

*FX.* Delay B en times binaires 250/500 ms (ou au TAP). **Reverb A courte : Reflection haut, Predelay court (20–30 ms), Low Pass 6 kHz.** En punk, moins de reverb vaut mieux : ça brouille l’énergie.

*HPF voix.* 100 Hz.

## 6.2 ROCK

*Bus Voix — compresseur.* Tube CB Manual, Attack Fast, Release Medium, Ratio 4:1, Threshold -15 dB. Réduction 4–5 dB. Un peu plus de souplesse qu’en punk : les voix rock tiennent des notes.

*Bus Voix — EQ.* Vintage 1970s. Low Freq vers 200 Hz, +2 dB ; L-Mid +1 dB, H-Mid +2 dB (moins agressif qu’en punk), High +2 dB.

*Bus Voix — limiteur.* Threshold -2 dB, Release 150–200 ms.

*Bus Drums.* Brit Comp réduction 3–4 dB. Solar 69 Mid +2 dB, High **+1 à +2 dB** (overheads Lewitt, 4.1).

*Bus Instru.* FC-670 réduction 3–4 dB. Alpine Mid +2 dB pour que les guitares tiennent leur place.

*Bus Parallel.* Fader -10 à -8 dB.

*Master.* Limiteur -2 dBFS, RMS -11 à -9 dBFS.

*FX.* Delay B binaire 250/500 ms (ou au TAP). Reverb A : Reflection modéré, Predelay 40 ms.

*HPF voix.* 100 Hz.

## 6.3 MÉTAL

*Bus Voix — compresseur.* Tube CB Manual, Attack Fast, Release Fast, Ratio 6:1, Threshold -18 dB. Réduction 6–8 dB. Un chant hurlé a une dynamique brutale : il faut serrer plus fort qu’ailleurs.

*Bus Voix — EQ.* Vintage 1970s. Low Freq vers 200 Hz, +1 dB seulement — le bas est déjà saturé par les guitares accordées bas. L-Mid +1 dB, H-Mid +3 dB pour percer le mur de guitares, High +2 dB.

*Bus Voix — limiteur.* Threshold -2 dB, Release 150 ms.

*Double grosse caisse rapide — une tension à connaître, pas une valeur à recopier.* *Calcul :* à 200 BPM en doubles croches, deux frappes sont séparées de 60 000 / 200 / 4 = **75 ms**. Le compresseur du kick (3.1, Release Auto = 150 ms) n’a pas le temps de relâcher entre deux coups : sur ces passages il cesse d’agir comme une compression et devient une baisse de niveau quasi fixe. Le raccourcir ne résout rien : sous quelques dizaines de millisecondes, on entre dans la zone de distorsion par suivi de la forme d’onde décrite en 2.4 — et le limiteur reste à 150 ms. **Piste à tester :** sur un set à double pédale rapide, réduire la compression du canal kick plutôt que ses temps, et obtenir l’articulation par l’EQ du clic de batte (3.1) ; si le gate est utilisé, son Release doit rester inférieur à l’intervalle entre frappes pour que chaque coup se détache — valeur à déterminer à l’oreille sur le set. *Statut : à tester, registre 8.7.*

*Bus Drums.* Brit Comp réduction 5–6 dB, Attack 10 ms. Solar 69 Mid en mode **Trough** pour creuser vers 400–500 Hz si la batterie s’empâte dans les guitares — c’est le cas d’usage type du notch. *Méthode pour trouver la fréquence (trente secondes, groupe en train de jouer) :* rester d’abord en mode **Peak**, monter le gain Mid de quelques décibels, balayer la fréquence entre 300 et 600 Hz jusqu’à l’endroit où l’empâtement devient le plus laid ; basculer en **Trough** sans toucher la fréquence, puis doser le gain jusqu’à ce que les guitares se détachent. La fréquence dépend du kit et de l’accord du jour : elle se trouve, elle ne se recopie pas.

*Vigilance overheads Lewitt en métal.* Le Brit Comp ajoute de la saturation sur les transitoires (c’est voulu, ça donne le punch), et les overheads Lewitt sont déjà très brillants par nature (+6 dB dès 4 kHz, sommet 15 kHz). Le cumul des deux peut vite devenir fatigant sur un kit métal joué fort et rapide. Garder le Solar 69 High **flat ou +1 dB maximum** ici (le maximum de +1 à +2 dB des scènes punk et rock ne s’applique pas ici), et ne pas hésiter à couper -1 à -2 dB vers 6–8 kHz sur le canal overheads lui-même si le rendu pique après 20 minutes de set.

*Bus Instru.* Alpine Low band en cut léger si le mur de guitares mange la basse. Mid +2 dB.

*Bus Parallel.* Fader -8 à -6 dB — le kick doit rester lisible dans le mur.

*Master.* Limiteur -2 dBFS, RMS -10 à -8 dBFS.

*FX.* **Reverb minimale : Reflection haut, Predelay court, Low Pass 5–6 kHz**, fader du retour très bas. En métal, la reverb noie tout. Delay quasi inutilisé.

*HPF voix.* 100 Hz. *HPF guitares rythmiques.* 100 Hz, sans hésiter.

## 6.4 HIP-HOP

*Bus Voix — compresseur.* Tube CB Manual, **Attack Slow, Release Slow**, Ratio 3:1, Threshold -15 dB. Réduction 4–6 dB. Les temps lents laissent la dynamique du MC s’exprimer — c’est ce qui distingue un rap qui respire d’un rap écrasé.

*Bus Voix — EQ.* Alpine EQ-550. Low band ~250 Hz **+3 dB en Peak** pour la chaleur dans les bas-médiums, Mid band ~2 kHz +2 dB pour l’intelligibilité, High band ~8 kHz +1 dB en Shelf pour la définition.

*Bus Voix — limiteur.* Threshold -3 dB, Release 150–200 ms.

*Sources.* Souvent table DJ ou playback en direct Main (voir 3.8), plus les voix. La batterie acoustique est rare.

*Bus Parallel.* Fader -12 à -10 dB, ou -∞ s’il n’y a pas de batterie acoustique.

*Master.* Limiteur -3 dBFS, RMS -12 à -10 dBFS. La dynamique compte plus que le volume.

*FX.* Delay B en times ternaires 375/500 ms. Reverb A courte et détachée (Predelay, Reflection bas) — l’intelligibilité du texte prime sur tout. Le ducking de la reverb ne se fait pas sur le retour d’effet ; deux voies à vérifier en 5.2.

*HPF voix.* 80 Hz.

*Plateau multi-MC.* Voir 3.7 et 7.2.

*Ducking de la musique par le MC — à tester.* La technique décrite en 2.5 (usage 3) et en 8.4 s’applique directement ici : compresseur sur le canal de la table DJ ou du playback, **Key Source = micro du MC**, Threshold bas, ratio élevé, attaque rapide, retour long. La musique recule quand le MC parle entre deux morceaux et revient d’elle-même. *Trois limites :* Key Source ne prend **qu’un seul canal** — choisir le MC qui parle au public ; la profondeur du recul se règle à l’oreille, aucune valeur n’est documentée — **relever au mètre de réduction de gain la valeur retenue et la consigner ici** après le premier essai ; et sur une table en stéréo couplée, vérifier au mètre que les deux côtés reculent ensemble (option Comp./Limiter du couplage, 4.2). À couper pendant les morceaux si le MC rappe sur la musique : là, on ne veut pas qu’elle recule. *Registre 8.7.*

## 6.5 REGGAE

*Bus Voix — compresseur.* Tube CB Manual, Attack Medium, Release Slow, Ratio 3:1, Threshold -15 dB. Réduction 4–5 dB.

*Bus Voix — EQ.* Alpine EQ-550. Low ~250 Hz +2 dB, Mid ~2 kHz +2 dB, High ~8 kHz +1 dB en Shelf.

*Bus Voix — limiteur.* Threshold -3 dB, Release 200 ms.

*Bus Instru.* C’est le bus clé du reggae. FC-670 Time Constant 3, mais réduction plus douce : 2–3 dB. La basse doit rester ronde et présente, pas serrée. Alpine Low band **flat ou +1 dB** — ne surtout pas couper le bas ici.

*Basse.* Sur le canal, alléger le cut à 60 Hz : -2 dB au lieu de -3 dB. La basse reggae porte le morceau.

*Bus Drums.* Brit Comp réduction 3 dB, doux. Le one-drop respire, ne pas l’écraser.

*Bus Parallel.* Fader -14 à -12 dB, très en retrait, ou -∞.

*Master.* Limiteur -3 dBFS, RMS -13 à -11 dBFS.

*FX.* Reverb A : Reflection bas (espace ample), Predelay 40 ms. Delay B ternaire 375/500 ms, Feedback un peu plus haut (45–50 %) sur les fins de phrase.

*HPF voix.* 80 Hz.

## 6.6 DUB

Le dub est un reggae où les effets deviennent un instrument joué en direct. La scène part de la scène Reggae avec des différences nettes.

*Bus Voix.* Comme en reggae. Tube CB Manual Medium/Slow, Alpine EQ-550. *Option à tester :* Tube EQ à la place de l’Alpine (2.3) — sa portée de 200 Hz à 5 kHz ne peut pas entrer en conflit avec les delays et la reverb qui occupent les extrêmes. *Point de départ et méthode (rien d’éprouvé) :* les trois bandes à zéro ; la bande Mid ne fait qu’atténuer (DIP, 0,2–5 kHz sur le panneau, 2.8) — la balayer pour retirer la zone nasale de la voix du jour ; Low PEAK (0,3–1 kHz) pour le corps et High PEAK (1,5–5 kHz) pour la présence, un à deux décibels, seulement si la voix en manque après le DIP.

*Bus Instru.* FC-670 doux, réduction 2–3 dB. Alpine Low flat.

*FX B — Delay.* C’est le cœur du dub. Time calé au tempo **à la touche TAP, Feedback 55–65 %** — assez pour que les répétitions s’auto-nourrissent sans partir en oscillation. **Fb LPF 3–4 kHz : c’est cette commande, et elle seule, qui fait que chaque répétition est plus sombre que la précédente.** Le LP Filter principal (5 kHz) assombrit l’ensemble ; le Fb LPF assombrit progressivement. Les deux se combinent. Envoi géré **en direct depuis les départs FX des canaux**, pas depuis un niveau fixe : on envoie une caisse claire, une phrase de voix, un accord de guitare, puis on coupe.

*FX D — Ping Pong.* Sorti de la réserve et utilisé activement. Time 500 ms au TAP, Feedback 40–50 %, **Fb LPF 4 kHz, Fb Time décalé** pour que les rebonds se désynchronisent. Fader monté à -12 dB, prêt à servir.

*FX A — Reverb.* **Reflection au plus bas** pour l’espace le plus vaste, Predelay 50–60 ms, Low Pass 4–5 kHz. Vintage Plate ou 335 (sa Diffusion élevée donne une queue plus nuageuse, très dub). En dub, on veut justement que la reverb envahisse.

*Bus Drums.* Brit Comp doux, réduction 2–3 dB. Le kick et la caisse claire doivent rester secs et nets pour ressortir quand on les envoie dans le delay.

*Master.* Limiteur -3 dBFS, RMS -12 à -10 dBFS.

*Piste à vérifier — le delay envoyé dans la reverb.* Geste classique du dub : les répétitions du delay se noient dans la reverb au lieu de s’arrêter net. Le tableau 6.1 du manuel indique que les **retours d’effet ont des départs Aux** (vers les FlexMix) ; il **ne dit pas** qu’un retour d’effet peut alimenter un autre bus d’effet (FX B vers FX A). À vérifier sur la console avant de compter dessus. Si ce départ n’existe pas, la voie de 7.10 (effets de la table traités par l’ordinateur) permet de chaîner delay et reverb dans le logiciel. *Registre 8.7.*

*Geste live.* Garder une main sur les départs FX et l’autre sur le feedback du delay. Le dub se mixe en jouant, pas en réglant.

*Précaution.* Un feedback à 65 % peut décoller très vite. Repérer avant le set le point exact où le delay s’emballe, et savoir où couper.

## 6.7 TECHNO LIVE

Configuration plutôt que scène, la structure variant beaucoup selon l’artiste.

*Si sorties séparées.* Kick machine et percussions vers Bus Drums, basses et synthés vers Bus Instru. Traitement selon les presets correspondants, avec HPF kick à 25–30 Hz et Release limiteur 150 ms.

*Si sortie master unique.* Direct Main, Everest C100A léger, EQ flat.

*Bus Drums.* Brit Comp Attack 10 ms, réduction 4–5 dB. Solar 69 High +2 dB.

*Bus Instru.* FC-670 réduction 3–4 dB.

*Bus Parallel.* Fader -10 à -8 dB si le kick vient d’une source séparée — ça densifie beaucoup.

*Master.* Limiteur -2 dBFS, RMS -10 à -8 dBFS. Compact et impactant.

*GEQ.* C’est le style où la correction de salle compte le plus : un grave qui traîne ruine un set techno. Voir 7.3.

*Contrainte DI.* Voir la note en 3.8 — c’est le format qui sature le plus vite le parc de DI.

# PARTIE 7 — WORKFLOW & OPÉRATIONS

## 7.1 Soundcheck — 60 minutes

*Préparation (10 min).* Rappel de la scène de style. Vérification du routing et des assignations bus. Contrôle des FlexMix 1 à 6 (retours). Phantom activé uniquement sur ce qui en a besoin — avec le parc actuel : le kick BD 500 Beta, les deux overheads Lewitt, et la DI active selon la source (voir 1.5).

*Line check (10 min).* Canal par canal : signal présent, pas de buzz, pas de larsen, phase correcte, faders à Unity. C’est aussi le moment de repérer un câble douteux avant qu’il lâche en plein set.

*Gain staging (20 min).* Préamplis d’abord (peak -12 à -6 dBFS), puis les bus (-6 à -3), puis le Master (-3 à -1). Dans cet ordre, jamais l’inverse.

*Retours scène (10 min).* FlexMix 1 à 6, chaque musicien valide son retour. Vérifier l’absence de larsen à niveau réel, pas à mi-volume.

*Balance (10 min).* Équilibre des bus, niveaux FX, puis le Bus Parallel — fader à -∞ puis montée progressive jusqu’à sentir le punch. **Caler les delays à la touche TAP sur un morceau réel**, pas sur une valeur théorique.

## 7.2 Plateau multi-groupes / changements rapides

C’est le format le plus fréquent : plusieurs formations qui s’enchaînent, parfois avec des ingénieurs invités sur leur propre console.

*Patch fixe.* Établir un plan de patch valable pour tout le plateau, basé sur le dénominateur commun. On ne repatche pas entre deux groupes ; on mute et on ajuste les gains.

*Voix.* Garder tous les canaux voix ouverts et configurés pour toute la soirée, même si un groupe n’en utilise que deux. Les canaux inutilisés sont mutés, pas démontés.

*DJ et sources ligne.* Deux paires stéréo réservées en alternance (voir 3.8). Le suivant se branche et vérifie pendant que le précédent joue.

*Une scène par style, pas par groupe.* Sur un plateau à six groupes de punk, une seule scène Punk suffit — les différences se règlent au gain et au fader. Créer six scènes fait perdre du temps sans rien apporter.

*Sauvegarde en fin de plateau.* Enregistrer la scène telle qu’elle tourne réellement, sous un nom explicite. C’est cette version-là, ajustée au réel, qui sert de base la fois suivante.

*Ingénieur invité sur Wing ou Wing Rack.* Prévoir la passation : soit un split de scène, soit une bascule propre. Ne pas compter sur ses propres scènes ni sur ses presets — et récupérer son patch avant qu’il démonte.

## 7.3 GEQ — correction salle

Le GEQ 31 bandes est assigné au Main L/R. Il corrige l’acoustique du lieu, il ne sert pas à mixer. **Règle d’or : des coupures, ±3 dB maximum par bande — avec une seule exception, le boost de +1 dB dans l’aigu pour une salle morte (dernière ligne du tableau).**

| **Problème** | **Symptôme** | **Correction** |
| --- | --- | --- |
| Booming | Graves lourds, étouffants | Couper -2 à -3 dB entre 80 et 125 Hz |
| Honk | Son de carton désagréable | Couper -2 à -3 dB entre 250 et 400 Hz |
| Nasillard | Voix agressives | Couper -2 dB entre 800 Hz et 1,6 kHz |
| Stridence | Aigus douloureux | Couper -2 à -3 dB entre 2 et 4 kHz |
| Larsen | Fréquence qui monte | Couper -3 à -6 dB sur la fréquence identifiée |
| Salle morte | Son étouffé, sans air | Boost léger +1 dB entre 8 et 12 kHz |

Utiliser le RTA du 32SC pour visualiser les fréquences problématiques, activable depuis le GEQ.

*En extérieur ou sous chapiteau*, le GEQ sert beaucoup moins : il n’y a pas de résonance de salle à corriger. Le travail se déplace vers les FX (voir 5.6) et vers le placement des enceintes.

## 7.4 Monitoring & Solo

*Source Monitor Out.* Main L/R en général, avec possibilité de router un bus ou un FlexMix pour une écoute isolée.

*AFL.* Écoute après fader — niveau de production réel.

*PFL.* Écoute avant fader — utile pour le gain staging et le diagnostic.

*Solo et mix principal — ce que dit le manuel (10.1 et 10.1.1).* En AFL comme en PFL, presser Solo « envoie ce canal au bus solo et n’a pas d’effet sur le mixage principal » : c’est ce qui permet de vérifier une source pendant le set sans rien interrompre. Le seul mode qui coupe les autres canaux est le **SIP (Solo In Place), le « solo destructif »** : tout canal d’entrée non mis en solo est coupé dans les généraux. Le manuel le dit « dangereux durant un spectacle live » et recommande fortement de le désactiver une fois le spectacle commencé. **Vérifier que SIP est OFF avant le premier groupe** (touche Edit de la section Solo). Le SIP ne coupe pas les canaux dans les mixages Aux : il peut servir pendant la balance sans perturber les retours. *Modes de comportement :* Latch (plusieurs solos à la fois), Radio (un seul), CR (Control Room). La touche Clear annule tous les solos.

## 7.5 Troubleshooting

| **Problème** | **Cause probable** | **Solution** |
| --- | --- | --- |
| Pas de signal | Phantom, câble, ou fader à -∞ | Vérifier phantom, changer le câble, remonter le fader |
| Buzz 50 Hz | Boucle de masse | Passer par une DI symétrique, vérifier les masses |
| Larsen | Gain trop haut, micro mal placé | Baisser le gain, cut EQ sur la fréquence, GEQ |
| Pompage sur un bus | Ratio trop élevé ou release trop court | Réduire le ratio, allonger le release |
| Voix inaudible | Masquée par les instru | Baisser Bus Instru de 2 dB, vérifier le gain staging |
| Pas de retour scène | FlexMix mal configuré, câble AVB | Vérifier assignation FlexMix 1 à 6 et liaison AVB |
| Master qui sature | Gain staging des bus | Vérifier peak des bus (-6 à -3 dBFS) |
| Micro HF qui décroche | Batterie faible ou interférence | Changer les piles, vérifier la fréquence |

## 7.6 Backup & sauvegarde

Avant chaque date, sauvegarder la scène sous un nom explicite du type STYLE_Lieu_Date.

*Scènes minimum à garder disponibles :* les six scènes de style, la configuration Techno Live, et une scène RESET (faders Unity, tout flat) pour repartir de zéro en cas de problème.

Exporter les scènes sur clé USB après chaque date réussie. Synchroniser avec UC Surface pour un backup accessible depuis la tablette.

Sauvegarder aussi les presets Fat Channel par type de source dans la bibliothèque — c’est ce qui permet de configurer un canal imprévu en quelques secondes.

## 7.7 Retard d’entrée — aligner deux micros sur une même source

Chaque canal d’entrée dispose de **jusqu’à 85 ms de retard, réglable par paliers de 0,1 ms**. Le guide l’ignorait jusqu’à la V15. C’est pourtant l’outil qui complète la procédure de phase de la Partie 3 : **l’inverseur de polarité règle un problème binaire, le retard règle le décalage réel.**

*Le principe.* Le son parcourt environ 340 m/s, soit **2,9 ms par mètre**. Deux micros sur la même source à des distances différentes reçoivent le même événement à des instants différents ; leur somme produit un filtrage en peigne qui creuse le spectre à intervalles réguliers. Inverser la polarité déplace le problème sans le traiter. Retarder le micro le plus proche pour qu’il arrive en même temps que le plus lointain **aligne réellement les deux trajets** et fait disparaître le peigne qu’ils formaient entre eux. *À nuancer : ça aligne un trajet dominant, pas toute la scène. Les réflexions de sol, de mur et les autres sources continuent d’interagir — on supprime le peigne le plus audible, pas toutes les interactions acoustiques.*

**Usage 1 — deux micros sur le kick.** Kick in posé dans la caisse et kick out devant la peau de résonance sont typiquement séparés de 30 à 50 cm, soit **1 à 1,5 ms**. Retarder le micro **intérieur** (le plus proche de la source d’attaque) de cette valeur aligne les deux. Méthode : mesurer la distance entre les deux capsules, diviser par 0,34 pour obtenir les millisecondes, appliquer, puis affiner à l’oreille en écoutant les deux canaux ensemble. C’est plus fin que la seule touche Ø, et les deux se combinent.

**Usage 2 — caisse claire dessus et dessous.** Le manuel cite explicitement ce cas. Inverser la polarité du micro du dessous reste indispensable ; y ajouter le retard correspondant à l’écart entre les deux peaux resserre encore la frappe.

**Usage 3 — ampli basse et DI.** La DI arrive instantanément, le micro de baffle avec le temps de vol. Retarder la DI de la distance micro-baffle rend la basse nettement plus cohérente.

**Usage 4 — backline et micro de chant, sur petite scène.** C’est le cas d’usage principal du manuel, et il vise exactement les plateaux de 6 × 4 m. Sur une petite scène, l’ampli de guitare et la caisse claire entrent fortement dans le micro de chant. Le canal de guitare arrive donc deux fois au mix : une fois par son micro de proximité, instantanément, et une fois par le micro de chant, avec le retard du trajet. Retarder le micro de proximité de ce trajet **réduit fortement** ce filtrage en peigne et, selon le manuel, « renforce le mixage général et lui donne plus de clarté et de punch ».

*Procédure.* Mesurer la distance entre le baffle et le micro de chant en mètres, multiplier par 2,9 ms/m. Sélectionner le canal de guitare, ouvrir le retard d’entrée, entrer la valeur. Pour vérifier, passer le solo en **Solo In Place** et mode **Latch** — **à la balance uniquement, jamais pendant un set** (le SIP coupe la façade, 7.4) — mettre en solo guitare et chant ensemble, et écouter la différence en activant et désactivant le retard.

*⚠️ Statut de l’usage 4 : option de soundcheck, jamais procédure automatique.* Les usages 1 à 3 traitent deux micros sur **une même source** — le calcul suffit, le résultat est prévisible. L’usage 4 est d’une autre nature. Le micro de chant n’est pas un second micro de l’ampli : il reçoit aussi la batterie, les autres instruments, la façade et le public. Aligner le canal de guitare sur ce que le micro de chant reçoit de l’ampli peut donc **améliorer une interaction et en dégrader une autre** au même moment. À essayer sur une petite scène qui pose problème, à valider à l’oreille en A/B, et à retirer si le mieux n’est pas franc. Ne jamais l’appliquer par défaut sur une fiche.

*Limite à connaître.* Retarder un canal le retarde **peut-être aussi dans les retours**. En Pre2 et Post, les départs Aux sont pris après tout le Fat Channel ; en **Pre1**, réglage par défaut, le manuel (5.2.1) ne cite que l’inverseur de polarité, le HPF et le gate avant le point de départ — il ne dit pas où se place le retard. À vérifier à l’oreille ou au mètre avant de compter dessus. Sur quelques millisecondes c’est inaudible pour les musiciens ; ça n’en fait pas moins partie du raisonnement si on empile plusieurs retards.

## 7.8 Retard de sortie — aligner la façade sur la scène

*Aligner la façade sur le backline.* Sur une petite scène, le public entend l’acoustique directe de la batterie et des amplis **avant** la façade, ce qui brouille l’intelligibilité. La procédure du manuel : repérer l’instrument le plus puissant de la scène (généralement la caisse claire), mesurer la distance entre lui et les haut-parleurs de médiums de la façade, diviser par 0,34 pour obtenir le retard en millisecondes, et l’appliquer en **retard de sortie du mixage Main**. Ensuite, faire jouer des frappes isolées de caisse claire au niveau du concert, régler la façade au niveau acoustique de la caisse, et affiner le retard jusqu’à ce que les attaques se confondent.

*Système de renfort retardé.* Pour couvrir un site plus profond que la portée utile de la façade. En extérieur, le point où poser le renfort est celui où le brouhaha du public commence à atteindre le niveau de la sonorisation. Mesurer la distance entre l’enceinte de façade gauche et l’enceinte de renfort gauche, diviser par 0,34, configurer le FlexMix qui alimente cette sortie en sous-groupe et lui appliquer ce retard de sortie. Répéter à droite.

*⚠️ Ce qu’on aligne, et ce qu’on n’aligne pas.* On ne cherche pas à synchroniser toute la scène avec toute la salle — c’est impossible, chaque spectateur est à une distance différente de chaque source. On choisit **une source dominante** (la caisse claire en général), **une zone d’écoute de référence** (le public proche, celui qui entend le plus l’acoustique de scène) et on accepte que le reste soit un compromis. C’est un alignement **perceptuel**, pas absolu. Le critère de réussite est que les attaques se confondent à l’écoute au point de référence, pas qu’un calcul tombe juste.

*⚠️ Sortie physique pour un renfort retardé.* Sur la 32SC, les sous-groupes fixes **n’ont pas de sortie analogique dédiée** (contrairement aux 32S, 32SX et 32). Deux routes possibles, donc :

- **Route directe** — utiliser une sortie FlexMix, à arbitrer contre les besoins de retours du plateau. C’est la solution évidente et immédiate.

- **Route à tester** — le manuel indique que les sous-groupes des 32SC, 24 et 16 **peuvent être envoyés sur le réseau AVB**, et qu’ils sont adressables à d’autres appareils du réseau. Sur une configuration avec la 16R en stagebox, ça ouvre la possibilité d’alimenter un renfort depuis un **sous-groupe fixe** vers une sortie de la 16R, sans consommer un seul FlexMix. À vérifier concrètement sur la console avant de compter dessus pour une date : router un sous-groupe fixe vers une sortie 16R, confirmer que le signal sort, puis que le retard de sortie s’applique bien à ce chemin.

## 7.9 Réseau AVB — état du système et diagnostic

Le lien AVB entre la 32SC et la 16R porte **tout l’audio du plateau**. C’est le point de défaillance unique de cette configuration, et jusqu’ici le guide ne le documentait qu’en une ligne du tableau de dépannage. Cette section corrige ça.

**État du système — Milan, et ce que ça change**

Depuis le firmware v3, l’ensemble de la gamme Series III est **certifié Milan AVB**, sous condition que **tous** les appareils du réseau soient mis à jour. Les deux machines de ce parc tournent sur le même **3.4.0.111374**, donc la condition est remplie — mais ça se vérifie, ça ne se suppose pas, surtout après une mise à jour ou l’arrivée d’un appareil emprunté.

*Conséquence pratique, et elle est importante.* Sur un système entièrement PreSonus en firmware v3 ou supérieur, **il n’y a plus de configuration d’horloge à faire**. L’affichage attendu :

- Console seule allumée, rien d’autre connecté → **N/A** (aucun autre appareil AVB détecté)

- 16R allumée et connectée → **PTP Clock (Default)**, horloge en **bleu**

*⚠️ Les anciennes procédures d’horloge ne s’appliquent plus.* Toute la logique « une seule machine sur Internal, les autres sur Network Stream » que l’on trouve encore dans la documentation et sur les forums ne concerne que les firmwares **v2.8.2 et antérieurs**. Sur ce parc, aller régler ces paramètres à la main est au mieux inutile, au pire une source de panne. Si l’horloge n’est pas bleue avec les deux machines allumées, le problème est ailleurs : câble, port ou firmware désaccordé entre les deux appareils.

**Le câble — première cause à écarter, et la plus fréquente**

PreSonus est explicite : l’AVB exige un **lien gigabit**, donc **Cat5e minimum** (le Cat5 simple n’est pas compatible). Au-delà de la catégorie, ce sont la **qualité du sertissage** et la **tenue mécanique du connecteur** qui posent problème en pratique — une liaison qui a l’air branchée peut ne plus passer l’audio.

*Le test de traction — à faire sur chaque câble AVB du parc, une fois.* C’est la procédure officielle, elle prend deux minutes par câble :

- Brancher les deux extrémités sur des ports AVB d’appareils **allumés**.

- Repérer la **LED ambre** à côté du port AVB.

- **Tirer doucement sur le câble dans toutes les directions**, y compris près des connecteurs.

- Si la LED ambre s’éteint ne serait-ce qu’un instant, **le câble est à écarter de l’usage AVB**. Définitivement — il pourra servir en réseau de contrôle, pas en audio.

*Ce test explique la panne typique.* Un câble marginal tient parfaitement au repos, en soundcheck, sur une scène vide. Il lâche quand quelqu’un marche dessus, quand la boucle bouge, quand le connecteur prend un angle. D’où des coupures qui semblent aléatoires et qu’on n’arrive jamais à reproduire en régie.

*Points de vigilance sur le matériel :*

- **Cat5e ou Cat6**, sans intérêt à monter au-dessus : les ports sont gigabit, un câble 10 Gb n’apporte rien.

- **Blindage non nécessaire** en usage normal — PreSonus indique avoir validé électriquement ses produits AVB avec du non blindé. Le blindage ne se justifie qu’en environnement à fortes perturbations.

- **Connecteurs « snagless »** ou verrouillage etherCON, pour que la languette ne casse pas. Attention côté Neutrik : le porte-câble **NE8MC n’est pas recommandé** par PreSonus, et les **NE8FDY-C6 / NE8FDY-C6-B ne s’accouplent pas** avec d’autres etherCON. Le **NE8MX6** est celui qui est recommandé.

- **Longueur** : 100 m maximum tous segments confondus. Au-delà de 50 m en Cat5e, l’échauffement peut suffire à faire perdre le gigabit.

- **Câbles auto-sertis** : à considérer comme suspects par défaut tant qu’ils n’ont pas passé le test de traction. C’est là que se concentrent les problèmes.

**Procédure quand la façade tombe en plein set**

Le cas à connaître : **plus de son en façade, mais les mètres bougent encore et UC Surface répond**. Réflexe à avoir — *une interface de contrôle qui répond ne prouve pas que le réseau audio est sain*. Le contrôle et le transport audio ne suivent pas les mêmes exigences : un lien dégradé peut très bien continuer à faire vivre l’écran pendant que les flux audio décrochent.

*Dans l’ordre, sans paniquer :*

- **Mètre Main** — s’il bouge, le mix existe, le problème est en aval (routage Main, sortie physique, ampli). S’il est mort, remonter vers les bus.

- **Mètres des bus de groupe** — s’ils bougent et que le Main est mort, c’est une assignation ou un mute, pas le réseau.

- **Mètres des canaux venant de la 16R** — s’ils sont les seuls morts, le problème est bien la liaison AVB. Les canaux locaux de la 32SC continuent, eux, de fonctionner.

- **État de l’horloge** — doit afficher PTP Clock en bleu. Si elle passe en N/A, la 16R n’est plus vue du tout.

- **LED ambre des deux ports AVB** — éteinte ou instable d’un côté : c’est physique.

- **Changer le câble AVB** par le câble de secours, sans rien toucher d’autre. Si tout revient, la panne est trouvée.

- **Ne redémarrer que le maillon nécessaire**, jamais tout le système en réflexe : un redémarrage général en plein set coûte plusieurs minutes et efface les indices.

*Consigner l’incident.* Heure, durée, ce qui était branché, ce qui se passait sur scène, câble utilisé, ce qui a rétabli le son. Une coupure isolée ne se diagnostique pas ; trois coupures notées dessinent un motif — toujours au même endroit du set, toujours après un déplacement sur scène, toujours avec le même câble.

**Ce qui doit entrer dans le line check**

- Câble AVB : **passé au test de traction**, et un **câble de secours dans la caisse**, testé lui aussi.

- Horloge : **PTP Clock, bleue**, les deux machines allumées.

- Firmware identique sur les deux appareils.

- Alimentation propre : les deux machines sur un circuit avec terre correcte, idéalement via un conditionneur. PreSonus cite explicitement l’alimentation parmi les causes de coupures réseau.

## 7.10 Insert externe — matériel ou ordinateur

Le Fat Channel couvre l’essentiel, mais il lui manque des outils que la console n’a pas : de-esser dédié, tranche vocale spécialisée, traitement particulier sur une voix lead. Trois voies existent.

**Voie A — Le Key Filter détourné, sans rien brancher**

Sur un compresseur de canal à réaction rapide (Class-A FET ou RC-500), monter le **Key Filter vers 7–8 kHz** force le déclenchement à ne réagir qu’à l’énergie aiguë : un « sss » fait alors chuter brièvement le canal. **Ce n’est pas un vrai de-esser** — il baisse tout le signal (ducking large bande), pas seulement la bande sifflante, et ça s’entend si la réduction est forte. Mais c’est gratuit, natif, ça marche à chaque date sans rien brancher. **À essayer en premier, avant d’investir quoi que ce soit.** *Sa limite se juge à l’oreille, pas à un chiffre* : dès que la réduction s’entend comme un pompage de toute la voix, la voie A a atteint son plafond — passer à la voie C. Aucune source ne chiffre ce plafond, et il dépend de la voix et du Bus Voix (le +3 dB à 4,8 kHz du Vintage 1970s en 6.1 et 6.3 renforce ensuite, sur le bus, la sibilance que le canal a laissé passer ; en hip-hop et en reggae, le Bus Voix est sur Alpine EQ-550 et ce renfort n’existe pas). Un cut statique bien placé au canal (3.7) peut sonner mieux qu’un ducking trop poussé.

**Voie B — Insert matériel externe**

Méthode documentée au manuel (5.2.3) : une **sortie Mix libre** vers le processeur, retour sur une **entrée Aux**. **Ce n’est pas un vrai insert par canal — la 32SC n’en a pas.** C’est une boucle effet (send/return), fonctionnellement proche mais techniquement différente : elle mobilise un bus entier et une paire d’entrée Aux, pas un point d’insertion dans la tranche elle-même.

La 32SC dispose de **2 paires d’entrées Aux stéréo** (Aux A et Aux B) en face arrière, dédiées à cet usage — les jacks TRS contournent le préampli, niveau ligne direct. *⚠️ La contrainte qui décide de tout :* un de-esser matériel 2 canaux — format standard du marché — mobilise donc une bonne partie de cette capacité pour un seul boîtier. Sur un plateau à plusieurs voix, traiter chaque micro séparément en matériel est vite hors d’atteinte. Réserver ça à **la voix lead**.

**Voie C — Insert par USB vers l’ordinateur**

**⚠️ Statut : à tester.** Architecture vérifiée au manuel PreSonus, jamais éprouvée en concert. Le tableau des vérifications ci-dessous et le registre 8.7 disent ce qui reste à faire.

C’est la voie la plus souple, et celle qui a été auditée le plus sérieusement. Ce qui suit remplace toute version antérieure de cette section.

**⚠️ Câblage : l’ordinateur se branche sur la 32SC, jamais sur la 16R.** En stagebox, la 16R est un satellite piloté depuis la console — pas un second point d’entrée USB. Les canaux qui arrivent de la 16R par AVB apparaissent comme des canaux locaux dans la matrice USB de la 32SC : aucun canal-relais n’est nécessaire pour ça.

**⚠️ Contrainte dure à connaître avant de dimensionner quoi que ce soit : la 32SC est plafonnée à 32 canaux internes, point final.** Ce n’est pas une limite logicielle contournable — le moteur à 64 canaux est une puce différente, exclusive au StudioLive 64S. Tout montage doit tenir dans ce budget.

**L’architecture à deux canaux par voix traitée — les rôles ne sont pas symétriques**

Le mécanisme clé : chaque canal a un réglage **Départ numérique Pre/Post** par rapport à son propre Fat Channel — Pre prend le signal juste après le préampli (avant HPF/gate/comp/EQ), Post après tout le traitement. Et la **Source d’entrée** d’un canal (Analogique/USB/Réseau/Carte SD) est un sélecteur exclusif : jamais les deux en même temps sur le même canal.

**⚠️ C’est ce verrou qui empêche mécaniquement un larsen numérique.** Si un même canal envoyait en USB et recevait le retour, la sortie alimenterait son entrée en boucle fermée — exactement le mécanisme d’un Larsen acoustique, avec du gain qui monte jusqu’à saturer. Le montage à deux canaux n’est donc pas une convention pratique, c’est ce qui rend la boucle structurellement impossible :

- **Canal A — le départ.** Micro en entrée, **Source = Analogique en permanence**. Départ numérique = **Pre** : le plugin reçoit le signal **avant tout le Fat Channel de A** (manuel 6.8.2 : Pre, « le signal est envoyé avant traitement par le Fat Channel »). Le Fat Channel de A ne sert donc **qu’aux retours de scène** qui partent de ce canal (ci-dessous). **Fader verrouillé à Unity, jamais touché pendant le show.** **Désaffecté du Main et de tous les bus de groupe** — Bus Voix surtout, mais aussi Drums, Instru, Parallel, Divers et sous-groupes fixes (touche d’affectation du mixage principal et touches d’affectation des sous-groupes, mode Aux Sends du Fat Channel, manuel 6.7) —, **départs d’effets FX A à D fermés** (la reverb et le delay se prennent sur B, sinon l’effet reçoit la voix brute en plus de la voix traitée), départs Aux ouverts vers les retours seulement. C’est le point de vérification n°1 avant chaque set : le chanteur seul au micro, B coupé, deux contrôles. **(1) A n’atteint pas la façade :** ni le Main ni aucun **bus de groupe** (Drums, Instru, Voix, Parallel, Divers, sous-groupes fixes) ne doit bouger. **(2) A alimente bien le retour :** le mètre du FlexMix Aux du chanteur **doit** bouger, et le chanteur confirme qu’il s’entend — un départ Aux resté fermé passerait le premier contrôle sans que personne ne s’en aperçoive. Si A fuit quelque part en plus de B, on obtient une voix doublée avec un léger décalage, un comb filtering audible. **Enregistrer les scènes de style dans cet état** : une scène stockée avec A affecté le réaffecte au rappel. **Ne pas utiliser la touche Mute de A pour ça** : son effet sur les départs Aux dépend du mode **Link Aux Mutes** (manuel 12.1.5). En « Unlinked », réglage par défaut (tableau de réinitialisation, 9.6.6), couper A dans le Main laisse ses retours ; en « Main Mute Auxes » ou « Global Mute Link », le chanteur perd sa voix dans ses retours.

- **Canal B — la façade.** **Source = USB en permanence**, reçoit le retour traité. **C’est le seul fader qu’on touche en direct.** **Le Fat Channel complet de la voix est ici** (gate, comp, EQ selon la scène de style) : le plugin travaille sur le signal brut, la console traite ensuite. C’est l’ordre que ce montage a été conçu pour obtenir.

*⚠️ Correction V31.* Les versions précédentes mettaient le Fat Channel complet sur A **et** le départ en Pre : le traitement de A n’atteignait jamais l’ordinateur, et B, sans Fat Channel, envoyait en façade une voix non traitée. *Variante, si l’on veut le plugin après la console* (un de-esser derrière le compresseur, par exemple) : Fat Channel complet sur A, départ **Post**, B sans traitement. Le plan de secours change aussi (ci-dessous).

Verrouiller le fader de A à Unity, **dans les deux variantes**. Le manuel situe Pre et Post par rapport au Fat Channel, jamais par rapport au fader : qu’un départ Pre soit indépendant du fader est probable (le fader suit le Fat Channel dans tout le flux de la console), mais ce n’est pas écrit. **En variante Post, c’est le cas le plus incertain** : le manuel ne dit pas si le point « Post » inclut le fader — puisque ce fader ne bouge jamais, le niveau qui alimente le plugin reste stable quoi qu’il arrive en mix. On élimine la variable au lieu de devoir la vérifier.

**Coût réel en canaux : deux par voix traitée, pas un.** Pour 4 MC en hip-hop, ça fait 8 canaux sur 32 — largement jouable seul, mais à vérifier canal par canal sur un plateau déjà chargé (DJ, DI, batterie, instruments). Une astuce d’organisation (sans réduire ce coût) : patcher le canal A sur un numéro de tranche qu’on ne regarde jamais (ex. canal 25), pour ne garder visible que le canal B au numéro attendu.

**Pourquoi ne pas sommer les 4 voix en un seul retour stéréo pour économiser des canaux — la réponse est non.** Le gain (8 canaux → 6) est modeste, le coût structurel ne l’est pas : plus de fader/mute/pan individuel en direct (un mixage hip-hop où le micro circule a besoin d’un fader sous le doigt), plus de mètre par voix, et surtout **le risque se concentre** — un souci sur le retour couperait les 4 voix d’un coup au lieu d’une seule. Garder un retour par voix. La sommation peut avoir du sens pour des sources secondaires figées (chœurs pré-enregistrés, sample fixe) qui n’ont jamais besoin d’un ajustement indépendant en direct — pas pour les MC principaux.

**Où envoyer les retours de scène : depuis le canal A, jamais depuis B.** Les départs Aux (in-ears, wedges) doivent partir du canal source, avant l’ordinateur — sinon on impose au chanteur la latence de l’aller-retour PC sur sa propre écoute. Seul le FOH profite du plugin ; le monitoring reste instantané.

*Ce que le chanteur entend depuis A dépend du point de départ du FlexMix (manuel 5.2.1, voir 7.11).* En **Pre1**, réglage par défaut, seuls l’inverseur de polarité, le HPF et le gate de A sont dans son retour : régler ces trois-là sur A comme sur B. En **Pre2**, tout le Fat Channel de A part dans le retour : y **copier le Fat Channel de B** (copier/coller de Fat Channel, manuel 12.1.3) pour que le chanteur s’entende au plus proche de la façade : même gate, même compresseur, même EQ — seuls le de-plosive et le de-esser du plugin manquent dans son retour. Le choix se fait avec le musicien et se note sur la fiche groupe.

**Le plan de secours, à répéter avant que ça arrive en vrai.** Si le PC plante, gèle ou l’USB se déconnecte : silence total sur le canal B, pas de dégradation progressive. Le geste : rebasculer la Source d’entrée du canal B sur Analogique, même entrée que A. Comme le Fat Channel de la voix est sur B, la voix revient **traitée**, sans le plugin seulement. *En variante Post*, B est sans traitement : ce geste rendrait une voix brute. Le bon geste est alors **de réaffecter A au Bus Voix et de couper B** — A porte déjà tout le traitement. Ça doit être un réflexe entraîné en répétition, pas une improvisation le jour J.

**Convention de nommage stricte.** Canal A : « V1-SEND » (couleur distincte, sorti de toute couche de faders consultée en direct). Canal B : le nom réel du MC, dans la couche qu’on regarde.

**Ce qui reste à vérifier avant de s’appuyer dessus un soir de concert :**

| # | Point à vérifier | Comment |
| --- | --- | --- |
| 1 | Latence réelle de l’aller-retour USB | Transitoire (clap) enregistré en boucle, mesuré en échantillons, à la taille de buffer prévue en show |
| 2 | Horloge et fréquence d’échantillonnage | Console fixe à 48 kHz — la session DAW doit être réglée pareil, et le DAW doit prendre l’interface StudioLive comme horloge maître, pas son horloge interne |
| 3 | Tenue CPU dans la durée | Test de charge sur la durée réelle d’un set, pas une estimation |
| 4 | Persistance du montage au rappel de Scène | **Soldé au manuel PreSonus (9.6.3).** Le « Départ numérique pré/post » et la « Source de départ numérique » sont dans le filtre de scène **Channel Strip** : rappelés avec la scène. La **Source d’entrée** (Analogique, Réseau, SD, USB) est un paramètre de **Projet**, comme le patch USB : une scène de style ne la change pas. Conséquence : enregistrer les scènes de style **avec** le départ du canal A réglé sur Pre, sinon le rappel le remet dans l’état où la scène a été stockée. |

**Studio One plutôt qu’Ableton, pour une raison précise.** Les deux fonctionnent via le même pilote Universal Control, mais Studio One est l’intégration éditeur native pour cette interface — plus de retours d’expérience et de support en cas de souci de driver un soir de date. **Aucun des deux n’a besoin de « Pipeline XT » ou « External Audio Effect »** — ces fonctions servent à intégrer du matériel physique avec une latence à mesurer ; ici la console EST l’interface audio, donc c’est du routage I/O standard, latence déjà gérée par le driver.

*Studio One :* pilote choisi dans **Studio One > Options > Audio Setup** (Windows ; Studio One > Préférences sur Mac) ; entrées et sorties de la chanson dans **Song > Song Setup**, onglet **Audio I/O Setup**. *Chemins relevés sur une source tierce, pas dans un manuel au projet — à confirmer à l’écran.* Canal Audio Input mappé sur la paire USB du départ. Plugin sur ce canal ou un bus FX dédié. Bus de sortie routé vers la paire USB du retour. **Bouton Monitor activé** sur le canal d’entrée pour un passage continu, pas juste en lecture.

*Ableton Live (12.4) :* Preferences → Audio → ASIO Universal Control, canaux activés dans Input/Output Config. Piste audio ou piste de retour (Ctrl+Alt+T, plus logique si plusieurs sources partagent le même effet) : Input = Ext. In sur la paire USB du départ, Output = Ext. Out sur la paire USB du retour. **Monitor : In** (jamais Auto), essentiel puisqu’on ne joue pas un clip.

**Le PC : ce qu’il faut savoir avant de lui faire confiance.** Machine de référence ici : MSI GL62, **i5-6300HQ (quad-core, sans Hyper-Threading — moins de marge de parallélisation qu’un i7 de la même génération)**, 32 Go RAM, SSD (remplacé dès l’achat, pas de risque HDD). Buffer ASIO : commencer à 128 échantillons, descendre à 64 seulement pour un insert temps réel vraiment sensible. Câble USB direct, jamais de hub. Diagnostic de référence avant tout réglage à l’aveugle : **LatencyMon** (gratuit) — latence DPC max à surveiller sous 1000 µs ; sur une config avec GPU NVIDIA, le pilote audio HDMI de la carte graphique est un coupable fréquent des pics, à désactiver dans le Gestionnaire de périphériques si la sortie HDMI n’est pas utilisée.

**⚠️ La règle qui prime sur le choix de n’importe quel plugin : la latence.** Un plugin qui « regarde en avance » pour être plus précis introduit un délai réel. Deux coupables : **Look-ahead** et **Oversampling**. Chercher « zero latency » ou « live mode » dans la fiche produit, et si ces options existent, vérifier qu’elles sont désactivées.

**De-esser — l’échelle à suivre dans l’ordre, gratuit avant payant :**

- **Vérifier d’abord si Studio One 6 ou plus récent est déjà installé.** PreSonus y a intégré un **De-Esser natif gratuit** — bande étroite ou large, réduction -6 à -48 dB, bouton Listen, S-Mon. Si la licence le couvre déjà, c’est réglé sans dépenser un centime, avec l’éditeur de la console.

- **TDR Nova** (gratuit) — EQ dynamique multibande, à configurer en de-esser (bande resserrée 5–8 kHz, seuil bas, ratio élevé). Léger, sans latence significative par défaut.

- **FabFilter Pro-DS** ou **Pro-Q4** (payants) — Pro-Q4 en **Dynamic EQ classique, mode Zero Latency**, fait un de-esser fonctionnellement équivalent et ajoute des modes de saturation par bande (deux besoins couverts par un seul outil). **⚠️ Piège précis : la fonction « Spectral Dynamics » de Pro-Q4 introduit une vraie latence même quand le plugin est réglé en Zero Latency global** — ne jamais l’activer sur les voix, rester sur le Dynamic EQ classique.

**Écarté pour cet usage, et pourquoi :** Oeksound Soothe2 a une latence fixe d’environ 40 ms — inutilisable en insert live, ça décale la voix façade du reste du groupe et crée le même comb filtering que documenté sur les retards non maîtrisés (7.7). Soothe3 introduit un mode Low Latency (quasi nul) explicitement pensé live — à garder en tête pour un futur problème de résonance large spectre (cymbale stridente, ampli agressif), pas pour du simple de-essing aujourd’hui.

**Coloration/saturation — utile en complément, jamais prioritaire.** Le Fat Channel couvre déjà bien ce terrain (Tube CB, VT-1, Tube EQ). Si un besoin réel persiste : **FabFilter Pro-R2** (reverb, zero-latency confirmé — la confusion courante avec la latence linéaire-phase de Pro-Q ne s’applique pas à Pro-R), **Valhalla VintageVerb/Room/Delay** (légers, conçus pour tourner par dizaines d’instances), **Soundtoys SuperPlate**, **Decapitator** (saturation légère) ou **FabFilter Saturn2** (plus riche ; **sur une piste parallèle uniquement**, 2× d’oversampling au maximum — sur la piste de nettoyage, la règle « ni look-ahead ni oversampling » ne souffre pas d’exception). Écarter **LiquidSonics Seventh Heaven Professional** sur ce PC précis : specs officielles 8 cœurs physiques + 32 Go recommandés, très au-dessus d’un quad-core sans Hyper-Threading — basculer sur la version Standard ou sur Valhalla si une reverb premium est vraiment nécessaire.

*Contrainte d’exploitation à ne pas oublier :* la voie C impose un ordinateur allumé et fonctionnel pendant tout le set — un point de défaillance de plus, au même titre que le lien AVB (7.9).

**La chaîne voix lead retenue par Louis — état au 10 novembre 2026**

Ce qui suit consigne les choix arrêtés dans cette discussion. **Aucune de ces chaînes n’a encore tourné en concert** : tout est au statut *à tester*, et les valeurs de réglage ne sont volontairement pas figées ici — elles se trouvent à l’oreille, plugin ouvert, pas sur le papier.

*Architecture dans Studio One.* Une **piste de nettoyage** reçoit le départ USB du canal A et porte les traitements en série. Elle sort vers un **bus « Voix Lead OUT »**, lui-même routé vers la paire USB de retour du canal B. Les traitements de caractère ne sont pas en série : ce sont des **pistes parallèles alimentées par des Sends** depuis la piste de nettoyage, qui reviennent toutes au même bus. Le signal propre reste intact, le caractère se dose au fader de chaque piste parallèle — et couper une piste parallèle ne coupe jamais la voix.

*En série sur la piste de nettoyage :* de-plosive, de-esser, limiteur de sécurité en fin de chaîne. **Seulement ce que la console ne sait pas faire** : le gate, le compresseur et toute l’EQ restent sur le canal B (montage Pre), pour qu’il n’y ait jamais deux EQ ou deux gates actifs sur la même voix. Le limiteur de la piste protège le chemin de retour USB ; celui de B garde son rôle (2.4). En variante Post, la console a déjà tout fait : la piste ne porte que de-plosive et de-esser.

- **De-esser : Lindell 902** — choix de Louis, à l’oreille. Calqué sur le dbx 902, il fonctionne **sans réglage de seuil** : il compare la bande aiguë au signal large bande, donc il reste efficace sur un passage fort comme sur un passage doux. C’est le même principe que le BDX902 de la WING (8.6) et que le DSR de la HD96. *Autres de-essers « automatiques » évoqués, non retenus à ce stade :* sonible smart:deess, Waves Sibilance — latence à vérifier sur la fiche de chacun avant tout essai en insert live.

- **De-plosive.** Il n’existe pas d’outil dédié sans latence qui ait été retenu. Le montage équivalent est un **compresseur dont la détection est filtrée en passe-bas** : il ne réagit qu’à la bouffée grave d’un « p » ou d’un « b » et laisse le reste passer. À compléter par le HPF du canal, qui reste la première défense.

- **Gate : FabFilter Pro-G** — *écarté du montage Pre depuis la V32 : le gate est sur le canal B.* Ne reste candidat qu’en variante Post. Style **Vocal**, **Lookahead désactivé** : c’est le lookahead qui crée la latence, et la règle énoncée plus haut prime sur le confort de réglage. Sur une voix, viser une expansion douce plutôt qu’une coupure, comme en 3.7.

- **Limiteur : ZeroLimit** — candidat gratuit. *L’EQ (ZL Equalizer, ReaEQ) est écarté du montage Pre : toute l’EQ est sur le canal B.* Candidats à vérifier un par un au clap-test avant de leur faire confiance.

*En parallèle :*

- **Decapitator** (Soundtoys) — choix de Louis, pour le grain. Toujours en parallèle, jamais en série sur la voix.

- **Reverb : Exponential Audio R2** — installée et appréciée. Les presets s’y cherchent **par mots-clés** dans le navigateur ; l’inventaire exact des presets n’est pas documenté ici, donc aucun nom de preset n’est prescrit. R2 possède un module **Gate** intégré, utile pour couper la queue sans ajouter un plugin.

- **Delay : FabFilter Timeless 3** — choix de Louis. Sur une piste parallèle, **verrouiller le Mix à 100 % wet** (Lock Mix), sinon chaque changement de preset réintroduit du signal direct et double la voix. Le **ducking par sidechain** de Timeless fait reculer les répétitions pendant que la voix chante : c’est, côté ordinateur, ce que la console ne sait pas faire sur un retour d’effet (5.2). **Sa latence n’est chiffrée par aucune source consultée — clap-test obligatoire.**

*Écartés par Louis :* **VocalStrip 2**, essayé et non apprécié. *Rappel de prix :* les reverbs et delays Valhalla sont payants, 50 $ pièce ; seuls **Supermassive** et **Freq Echo** sont gratuits.

*Pourquoi la latence compte moins sur les pistes parallèles d’effet.* Un retard de quelques millisecondes sur une reverb ou un delay s’entend comme un pré-délai un peu plus long, pas comme un filtrage en peigne — tant que la piste est **100 % wet**. Sur la piste de nettoyage, en revanche, chaque milliseconde décale la voix façade : c’est là que la règle « zéro lookahead » ne souffre aucune exception.

**Les effets de la table traités par l’ordinateur**

Le manuel (12.3.4, USB Sends) liste, parmi les sources envoyables en USB, les **« Mixages de départ d’effets (pré-processeur d’effets) »**. Autrement dit : le bus de départ d’un effet, pris **avant** le processeur interne, peut partir vers l’ordinateur. Les départs FX de chaque canal — déjà réglés, déjà mémorisés dans les scènes — alimentent alors une reverb ou un delay VST à la place de l’effet interne, sans consommer un seul FlexMix.

*Le retour* revient par USB sur un canal dont la Source d’entrée est USB (ou une paire, en stéréo), assigné au bus voulu. C’est ce canal qui coûte : un canal en mono, deux en stéréo, sur le budget de 32.

*Par où commencer.* **Par FX D, jamais par FX A.** FX A porte la reverb voix (5.2), c’est le cœur du son de voix du guide : on ne le confie pas à un montage non éprouvé. FX D (Ping Pong Delay) est l’effet dont l’absence un soir de panne se remarquerait le moins.

*Ce que le manuel ne dit pas* : si le processeur interne du slot continue de tourner en même temps (auquel cas il faut muter son retour pour ne pas doubler l’effet). **À vérifier au premier essai — voir 8.7.**

## 7.11 Retours de scène — GEQ par FlexMix et AFS

**⚠️ Statut : à tester.** Procédures relevées dans les manuels PreSonus, dbx Venu360 et dbx PA2, jamais éprouvées par Louis sur ses propres retours. Les deux manuels dbx ne sont plus au projet (0.1) : la partie AFS ci-dessous ne peut plus y être revérifiée.

Jusqu’ici le guide traitait les retours en une ligne de soundcheck. Deux outils déjà possédés permettent de faire mieux, et le premier n’avait jamais été exploité.

**Le point de départ de chaque retour — le réglage qui décide de tout le reste** (manuel 5.2.1). Chaque FlexMix en mode Aux choisit où il prend les canaux : **Pre1** (par défaut) — après l’inverseur de polarité, le HPF et le gate, **avant** le compresseur, l’EQ, le limiteur et le fader ; **Pre2** — après tout le Fat Channel, avant le fader ; **Post** — après tout le Fat Channel et le fader. Le conseil du manuel : **Pre2 pour les casques et les in-ears**, pour un son « de type studio », et **à éviter sur les wedges**, « car la compression peut causer des problèmes d’accrochage ». Règle de ce guide : wedges en Pre1, in-ears en Pre2, jamais Post sur un **retour de musicien** (un geste de façade changerait son écoute). Le FlexMix 7 (Cue / Talkback) n’est pas un retour de musicien : son point de départ se choisit selon ce qu’on veut y entendre, et un départ Post y est légitime si l’on veut y suivre la balance de la façade. *Conséquence en Pre1 :* les corrections EQ de façade n’atteignent pas les wedges — c’est le GEQ ci-dessous qui fait ce travail. *Effets dans un retour :* chaque mixage a son propre niveau de retour d’effet (manuel 5.5.1) — sélectionner le FlexMix du musicien, puis régler le canal « FX A » dans ce mixage.

**Un GEQ 31 bandes par retour**

Le manuel (11 et 11.1) : la console dispose de **huit** égaliseurs graphiques 31 bandes, « librement assignés au mixage principal ou à votre choix de mixages Flex », et les **insère après le fader**. Le guide n’en utilisait qu’un, sur le Main (7.3). Il en reste sept : un par retour, FlexMix 1 à 6, avec encore un de réserve.

*Affectation.* Sélectionner le FlexMix, touche GEQ, toucher le mixage dans l’écran. Le compteur en haut à droite indique combien de GEQ restent disponibles.

*Méthode — le « ring out » à la main.* Micros ouverts au niveau de travail, personne ne joue. Monter lentement le départ général du retour jusqu’à la première accroche. Repérer la fréquence au RTA, couper **la** bande concernée de 3 dB, pas ses voisines. Remonter jusqu’à la suivante. S’arrêter à **trois ou quatre bandes** : au-delà, on ne gagne plus de marge, on dégrade le timbre du retour — et un retour sourd pousse le musicien à demander plus fort, ce qui ramène le larsen. Redescendre ensuite le départ au niveau de jeu : la marge gagnée est la sécurité, pas un volume supplémentaire.

*Règles :* **coupures uniquement, sans exception** — plus strict qu’en 7.3, et c’est voulu. L’exception « salle morte » de 7.3 corrige la couleur d’une salle ; ici le GEQ corrige un couple micro–enceinte, et tout boost dans une boucle micro–retour retire de la marge avant larsen. Un retour terne se traite à la source (EQ du canal, placement), pas en remontant une bande. Le GEQ ne mixe pas.

**⚠️ Ce que le rappel de scène fait aux GEQ — vérifié au manuel PreSonus (9.6.3).** « Affectations des bus GEQ et réglages des courbes » figurent dans les **filtres de Projet**, pas de Scène. Les courbes de retours survivent donc à un changement de scène de style en cours de plateau. En contrepartie, elles voyagent avec le Projet : en changeant de lieu, repartir d’un GEQ plat ou désactiver le filtre GEQ au rappel du projet.

**L’AFS des processeurs dbx — Venu360 et PA2**

Les deux appareils embarquent le même algorithme (le manuel du Venu360 précise qu’il a été introduit sur le PA2). Il pose des **filtres en encoche étroits** là où un GEQ en tiers d’octave enlève une tranche entière du spectre — c’est l’argument du constructeur, et il est physiquement fondé : moins de timbre perdu pour la même marge.

*Où il agit.* Le module AFS est **fixe, dans l’étage d’entrée** du processeur. Il traite donc ce qui entre dans l’appareil : placé entre la console et l’amplification de façade, il protège la façade ; pour protéger des retours, il faut que **les départs de retours passent par le processeur**. Sur un système où le Venu360 est entièrement occupé par la façade, c’est le **PA2** qui peut prendre ce rôle, inséré entre les sorties de retours et leur ampli — à condition qu’il ne soit pas prêté ce soir-là.

*L’ordre, tel que le manuel l’impose.* Structure de gain et limiteurs d’abord, **égalisation du système ensuite** (AutoEQ ou à l’oreille), **ring out à l’AFS en dernier** : « After system EQ has been applied ». Dans l’autre sens, l’AFS pose des filtres sur des défauts que l’égalisation aurait corrigés, et les gaspille.

*La procédure manuelle, commune aux deux manuels.*

- Faire une balance grossière avec tous les micros qui seront ouverts, et **noter la position** des faders généraux (ou du départ général du retour). La cible du ring out est **2 à 5 dB au-dessus** de ce niveau selon le manuel du Venu360, environ 5 dB selon celui du PA2.

- **Bypasser les gates** des micros concernés — un gate fermé cache le larsen à l’AFS. Les réactiver après.

- Faire taire la scène, descendre complètement les faders.

- AFS sur ON, **MODE = FIXED**, **TYPE = MUSIC** (les filtres les plus étroits), **FIXED FILTERS = 12**.

- Monter lentement jusqu’à la cible, ou jusqu’à épuisement des filtres fixes. Puis redescendre au niveau de travail.

- **Réduire FIXED FILTERS** au nombre de filtres réellement posés : les filtres inutilisés deviennent des filtres Live. Ne pas descendre en dessous, on effacerait des filtres posés.

- **MODE = LIVE**, **TYPE = SPEECH/MUSIC** : protection en temps réel pendant le concert.

*Trois pièges écrits dans les manuels.* En mode Fixed, **tout son capté pose un filtre** : micros ouverts mais silence total sur scène. L’AFS analyse une **somme mono** : si les deux signaux qui l’alimentent sont en opposition de polarité, le larsen s’annule avant l’analyse et n’est jamais détecté. Et **couper l’AFS retire tous les filtres d’un coup** : baisser les niveaux avant de le désactiver ou d’effacer les filtres.

*Limite de principe.* L’AFS ne remplace pas le principe NOM (2.2), ni le placement des retours, ni le choix du micro. Il achète quelques décibels de marge sur un système déjà sain ; sur un système mal posé il épuise ses filtres en dix minutes.

*Suivi :* registre 8.7.

## 7.12 Balance virtuelle — régler sans le groupe

**C’est l’outil qui manquait pour solder le registre 8.7.** Presque tous les tests en attente achoppent sur la même chose : il faut un groupe sur scène, et un soundcheck de soixante minutes ne laisse pas dix minutes pour comparer deux compresseurs. La console sait rejouer un concert enregistré dans ses propres tranches.

*Ce que dit le manuel (8.4).* Touche **Soundcheck** → écran de chargement de session → choisir une session Capture déjà enregistrée sur la carte SD → la touche **Recall** clignote, la presser : la session se charge et **tous les retours de canaux SD s’activent**. La scène de la console est sauvegardée automatiquement avec chaque session ; l’option **Load Mix** la recharge en même temps. Les commandes de transport lisent l’enregistrement, et le mixage se règle comme si le groupe jouait. Presser de nouveau **Soundcheck** ferme la session et **désactive tous les retours SD**.

*Condition préalable.* Avoir enregistré : une carte SD dans la console, et l’enregistrement multipiste lancé pendant un concert ou un soundcheck. Un seul enregistrement par style suffit à constituer une banque de travail.

*Ce que ça permet, concrètement.*

- **Solder les tests du registre à la maison ou à la MJC, console seule** : alignement du Bus Parallel, Class-A FET en All, tour de passe-passe Pultec, modèles d’EQ alternatifs, dual mono du Bus Instru. Chacun demande un A/B répété sur le même passage — impossible en concert, trivial sur une boucle.

- **Préparer une date** : rejouer le dernier concert d’un style, et arriver avec une scène ajustée sur du vrai signal plutôt que sur des valeurs de départ.

- **Régler la façade avant l’arrivée du groupe** : le cas décrit par le manuel lui-même.

*Les limites à garder en tête.* Le signal rejoué est pris **après le préampli** : tout ce qui se règle au gain, au placement de micro ou à la phase acoustique ne se teste pas ainsi. La repisse enregistrée est celle de la scène de ce soir-là. Et **les retours ne se testent pas en balance virtuelle** : sans micros ouverts sur scène, il n’y a pas de boucle de larsen à étudier.

*Deux points non documentés, à vérifier au premier essai.* Si le départ numérique des canaux doit être en Pre pour que l’enregistrement soit pris avant le Fat Channel — sinon on rejoue un signal déjà traité, à travers le traitement une seconde fois. Et l’état dans lequel la sortie du mode laisse un canal dont la Source d’entrée était **USB** (canal B de 7.10) : le manuel dit seulement que les retours SD sont désactivés.

# PARTIE 8 — TRANSFÉRER LA MÉTHODE SUR UNE AUTRE CONSOLE

Le parc de référence reste la **StudioLive 32SC + 16R**. Tout ce qui précède est écrit pour elle. Cette partie sert au cas où il faut travailler sur une autre machine — en festival, en remplacement, sur une scène équipée.

**Le principe : ce qui se transfère, c’est la méthode, pas les chiffres.**

## 8.1 Niveaux de confiance par console

L’erreur à éviter est d’affirmer sur une console dont on n’a pas la documentation. Trois niveaux, à annoncer clairement :

| Niveau | Consoles | Ce qui est permis |
| --- | --- | --- |
| **Spécialiste** | StudioLive 32SC / 16R | Affirmer sans revérifier. Manuel + addendum des plug-ins disponibles. |
| **Connaissance documentée** | Allen & Heath SQ · Behringer WING / COMPACT / RACK · Midas M32 · Yamaha DM3 · Behringer X-AIR (XR12/16/18) · Soundcraft Ui24R · **Midas HD96-24** | Affirmer **en citant le manuel**, qui est dans le projet. Ne pas extrapoler au-delà. Pour la HD96, le manuel du projet est une **version bêta (V1.16)** : prudence redoublée. |
| **Aucune documentation** | Soundcraft Si Expression, et toute machine non listée | **Ne rien affirmer de mémoire.** Chercher, demander une photo de l’écran, ou appliquer le protocole 8.3. |

*Consoles réellement pratiquées par Louis, hors parc personnel :* Yamaha DM3 (un ami la possède, dates régulières ensemble), Behringer WING (guinguette de Saint-Lys, été 2026), Midas M32 (une fois), **Allen & Heath SQ6 (Tram Fest, 3 octobre 2026 — mixage complet du plateau, retour d’expérience en 8.6)**. Ce ne sont pas des hypothèses d’école.

*Rencontrées sans les mixer :* **Behringer XR18** et **Soundcraft Ui24R** au Festival Habibi (septembre 2026), exploitées par d’autres techniciens sur les scènes After et Guinguette — Louis y était régisseur technique. Elles restent au niveau « documentation », sans retour de mixage personnel.

*En attente de pratique :* **Midas HD96-24**, console d’une salle où Louis travaille sans pouvoir encore y intervenir ; formations spécifiques prévues à l’automne 2026. Fiche en 8.6.

## 8.2 La méthode exprimée en fonctions, pas en noms de plug-ins

Sur une autre console, les modèles portent d’autres noms et n’ont pas les mêmes commandes. Ce qui se transfère est la **fonction recherchée**. Voici la méthode dépouillée de tout ce qui est propre à PreSonus :

| Étage | Fonction recherchée | Sur StudioLive | Quoi chercher ailleurs |
| --- | --- | --- | --- |
| Canal | Nettoyage, contrôle dynamique, coloration si la source le justifie | Standard Comp, Standard EQ, HPF | Le compresseur le plus neutre de la console, un EQ paramétrique, un HPF |
| Bus Drums | Coller la frappe, punch, saturation légère des transitoires | Brit Comp (VCA), Attack 10 ou 30 ms | Un compresseur de type VCA. À défaut, le plus neutre — on perd la saturation, pas la cohésion |
| Bus Instru | Glue douce sur des sources hétérogènes, sans pomper dans le grave | FC-670 (lampes, variable-mu), temps lents | Un compresseur à lampes ou optique, ou à défaut à temps lents. Réduction 2–4 dB, jamais plus |
| Bus Voix | Contrôle rapide sans perdre la clarté | Tube CB | N’importe quel compresseur à attaque rapide et ratio modéré. Le caractère est secondaire |
| Bus Parallel | Densité et punch ajoutés sous le signal intact | Comp 160, bus dédié | **Vérifier d’abord si la console fait la compression parallèle en natif** — voir 8.4 |
| Master | Glue finale, 1–2 dB maximum | Everest C100A + Passive Program EQ | Le compresseur le plus transparent, EQ à ±1–2 dB |

**Ce qui ne se transfère jamais tel quel :** les valeurs de Threshold (dépendent du gain staging de la machine), les fréquences fixes (propres au modèle émulé), et les noms de modes (Fixed/Manual, All) qui n’existent que sur PreSonus.

**Ce qui se transfère intégralement :** la philosophie Nettoyage → Coloration → Glue, l’architecture en quatre bus, le gain staging en zones, les cibles de réduction en dB, les zones de sommation (2.9), la procédure de phase, les principes de la Partie 2.9, et tout le raisonnement sur les gates.

## 8.3 Protocole — arriver sur une console inconnue

À faire avant de toucher un réglage. C’est là que les hypothèses coûtent cher.

- **L’ordre du signal.** Où sont HPF, gate, EQ, compresseur, delay les uns par rapport aux autres ? Il varie d’une console à l’autre, et l’ordre EQ/compresseur change le résultat. Ne pas supposer qu’il est identique à la StudioLive.

- **Ce que fait le gate exactement.** Y a-t-il un Hold ? Le filtre de détection est-il seulement passe-haut, ou aussi passe-bas ? La profondeur va-t-elle jusqu’à -∞ ou est-elle bornée ? Trois réponses qui changent tous les réglages de batterie.

- **La structure des bus.** Combien de bus, configurables en aux ou en groupe ? Y a-t-il des DCA ? Sur beaucoup de consoles, les DCA remplacent avantageusement certains usages de sous-groupes.

- **Les points d’insert et leur compensation de latence.** Un insert non compensé introduit un décalage — critique si une partie du signal passe par l’insert et une autre non.

- **La compression parallèle native.** Si la console la fait par canal, le Bus Parallel du guide devient inutile.

- **Le rappel de scène et son périmètre.** L’équivalent du Recall Scope : qu’est-ce qui est rappelé, qu’est-ce qui ne l’est pas.

## 8.4 Deux principes transversaux, à lire avant les fiches

**Le limiteur séparé n’existe presque nulle part ailleurs.** Sur SQ, WING, M32/X32 et Ui24R, il n’y a **pas de bloc Limiteur distinct du compresseur** — confirmé texto sur les quatre sources : SQ (“Ratio = 1:1 to Infinity (limiting)”), Ui24R (“Ratio infinity to 1:1”), WING (“At ∞:1, the compressor acts as a limiter”), M32 (bouton **COMP/LIMIT** sur le même effet). Le limiteur, c’est le compresseur poussé à ratio infini — un mode, pas un étage séparé. **La StudioLive est l’exception** : Gate, compresseur, EQ et **Limiteur**, quatre étages distincts sur chaque canal (ordre compresseur/EQ inversable, voir 1.6). Avant de chercher “le limiteur” sur une autre console, se rappeler qu’il n’y a rien à chercher séparément — c’est le même bouton que le compresseur, à l’autre bout de l’échelle de Ratio. Seule nuance : la WING a un vrai bloc Limiter séparé, mais uniquement dans son outil **Speaker Manager** (Filter/Dyn EQ/Limiter) — protection de sortie, pas un étage de canal.

**Sidechain — qui peut recevoir un déclenchement externe, et comment.**

| Console | Gate | Compresseur | Filtre de détection | Particularité |
| --- | --- | --- | --- | --- |
| **StudioLive** | Key Source (tout canal) | Key Source (la plupart des modèles) | **passe-haut seul** | Voir 2.5 |
| **SQ** | Self Keyed ou tout canal | Self Keyed ou tout canal | **HPF/BPF/LPF** | Signal pris **après tout le traitement du canal source**, delay inclus |
| **WING** | Key Source + **Key Tap** | Key Source + **Key Tap** | **HPF/LPF/BPF/notch** | Key Tap choisit *où* dans la chaîne, pas seulement *quel* canal |
| **M32/X32** | Key source, toute E/S | probable (non détaillé) | fréquence + **pente réglable** | Écoute du key sur bus solo |
| **DM3** | **Self Pre/Post EQ, autre canal, ou bus MIX** | **⚠️ Self Pre/Post EQ SEULEMENT — jamais un autre canal** | aucun | **Le ducking kick→basse n’est possible que via le Gate (DYN1) en mode Ducking — pas via le Compresseur (DYN2)** |
| **X-AIR** | Key Filter HP/LP/BP + source, **+ mode Ducker dédié** | Key Filter séparé | HP/LP/passe-bande | Deux blocs distincts, chacun son propre Key Filter (voir correction en 8.6) |
| **Ui24R** | **aucun trouvé** | **aucun trouvé** | — | Autodéclenchement uniquement, sur tout le panorama de dynamique |

**Technique transposable, trouvée dans la doc WING avec un exemple concret directement réutilisable :** ducker posé sur le canal musique/DJ, micro de l’animateur ou du MC en Key Source — la musique baisse automatiquement dès que quelqu’un parle. Prêt à l’emploi sur un plateau hip-hop avec MC qui s’adresse au public entre les morceaux, sur toute console qui a un Key Source (StudioLive incluse, avec le Standard Compressor sur le canal DJ/lecture).

## 8.5 Tableau comparatif des gates — sept consoles

C’est le point où les consoles divergent le plus, et où recopier un preset fait le plus de dégâts. Valeurs relevées dans les manuels présents au projet.

|  | StudioLive 32SC | A&H SQ | Behringer WING | Yamaha DM3 | Midas M32 | Behringer X-AIR | Soundcraft Ui24R |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Gate séparé du comp.** | oui | oui | oui | oui | oui | oui *(corrigé — voir 8.6)* | oui |
| **Hold** | **absent** | 10 ms – 5 s | oui | oui | oui | oui | oui |
| **Profondeur** | Range → **-∞** | Depth, 0–60 dB | selon modèle | Range | Range | Depth | Depth |
| **Filtre de détection** | **passe-haut seul** | HPF / BPF / LPF | **HPF / LPF / BPF / notch** | **aucun** (Key In seulement) | fréquence + **pente réglable** | non documenté | non documenté |
| **Key Source** | oui | oui (post-traitement) | oui + **Key Tap** | Self pre/post EQ, autre canal, MIX | Self ou toute E/S | non documenté | non documenté |
| **Disponibilité** | tous canaux | tous canaux | tous canaux | **CH 1–16 uniquement** | tous canaux | tous canaux | tous canaux |

**⚠️ Le constat qui dérange : sur les gates, la StudioLive est la plus limitée du lot.**

C’est le seul modèle **sans Hold**, et le seul dont le filtre de détection ne peut pas couper les aigus. La limite documentée en 2.2 — impossible de traiter la repisse de cymbale par le Key Filter — **est propre à la StudioLive**. Sur SQ, WING et M32, c’est faisable. Ce n’est pas une raison de changer de console, mais il faut le savoir : un problème insoluble sur le parc personnel peut avoir une solution directe sur la machine d’un festival.

**Autre limite propre à la StudioLive, découverte cette session : l’absence de de-esser natif.** SQ (payant, RackFX), WING (BDX902 + 2-Band De-Esser, gratuits), et **Ui24R (natif sur chaque canal, gratuit, sans même un insert à câbler)** savent tous de-esser nativement. Toute l’architecture à deux canaux de la Partie 7.10 est une réponse à un manque propre au Fat Channel — pas une méthode universelle à transposer ailleurs. Sur Ui24R en particulier, le problème entier ne se pose simplement pas.

**Ce que le Hold change, partout où il existe.** Sans Hold, le maintien de la porte dépend entièrement du Release — d’où les **150–200 ms** prescrits sur les toms en 3.2. Avec Hold, on sépare les deux : la porte reste grande ouverte pendant une durée fixée, puis le Release fait la fermeture. Résultat plus net et plus reproductible. **Sur SQ, WING, DM3, M32 et HD96, ne pas recopier tel quel le Release de la StudioLive : le répartir entre Hold et Release, à l’oreille.**

**La HD96 n’est pas dans ce tableau, faute de place — elle se range du côté des mieux dotées :** gate séparé du compresseur (entrées uniquement), Hold, Range jusqu’à -∞, filtre de détection passe-bande balayable à quatre largeurs avec écoute, mode Ducker, déclenchement externe par le patch. Détail en 8.6.

## 8.6 Fiches par console

### Allen & Heath SQ (SQ-5 / SQ-6 / SQ-7)

**⚠️ Retour d’expérience — Tram Fest, 3 octobre 2026, SQ6, plateau hip-hop. Statut : validé en concert.**

C’est la première fiche de cette partie qui ne repose plus seulement sur un manuel. Ce que Louis a réellement fait, tel qu’il le rapporte :

- **Sur chaque voix : un de-esser**, un **passe-haut vers 80 Hz**, une **égalisation légère**.

- **Un bus de voix**, avec une **égalisation dynamique 4 bandes** — « super efficace » selon ses mots.

- **Micros HF** : remis en **réglages d’usine**, puis un réglage à **-6 dB directement sur le micro**.

- Une **émulation de préampli**, dont il ne se rappelle plus le modèle.

- **Reverb plate** sur les voix.

*Résultat :* « c’était top ». **Aucun larsen**, y compris quand les groupes descendaient chanter dans le public.

*Ce qui est établi, et ce qui ne l’est pas.* Les modules exacts ne sont pas identifiés : l’égalisation dynamique 4 bandes est vraisemblablement le **DynEQ4** listé plus bas, l’émulation de préampli possiblement le **Tube Stage Preamp** — **deux inférences, à confirmer** en rouvrant le show ou à la prochaine date sur SQ. Le nombre de de-essers simultanés non plus : chacun consomme un emplacement RackFX, sur huit au total.

*Ce que cette date apprend au guide.*

- **L’étagement à deux niveaux fonctionne en hip-hop** : nettoyage minimal et identique sur chaque micro, puis **un seul traitement intelligent sur la somme des voix**. C’est la philosophie Nettoyage → Coloration → Glue (1.1), avec un outil que la StudioLive n’a pas.

- **L’égalisation dynamique sur le bus voix est le traitement à retenir** dès qu’une console en propose une : elle ne creuse une fréquence que lorsqu’elle dépasse, donc elle retient une voix qui durcit ou un micro qui s’approche d’une enceinte sans assombrir le reste du temps. Sur un plateau où neuf formations se partagent les mêmes micros, c’est ce qui évite de re-régler l’EQ à chaque passage.

- **Baisser le niveau à l’émetteur plutôt qu’à la console** : le -6 dB sur le micro HF agit avant toute la chaîne. L’explication probable de son effet — plus de marge avant saturation de l’émetteur sur des MC qui crient dans la capsule — est **une inférence**, la référence des micros HF n’étant pas connue.

- **Sur la StudioLive, rien de tout cela n’est natif.** Pas de de-esser (7.10), pas d’égalisation dynamique. Le Bus Voix de la 32SC ne peut pas recevoir d’insert logiciel direct ; l’équivalent passerait par un sous-groupe envoyé en USB et un retour sur canal — montage non conçu, non testé, à n’envisager qu’après validation de la voie C sur une seule voix.

**Référence manuel**

**Compresseur.** Attack 30 µs – 300 ms · Release 50 ms – 2 s · Ratio 1:1 à ∞ · Threshold -46 à +18 dB · Gain 0 à +18 dB · détection **RMS ou Peak** · Soft Knee · sidechain filtrable HPF/BPF/LPF.

**⚠️ Compression parallèle native, par canal.** Le compresseur SQ dispose d’un chemin parallèle avec mélange Dry/Wet, et A&H indique explicitement que les signaux restent cohérents, **sans filtrage en peigne**. Conséquence : **sur SQ, le Bus Parallel du guide (FM 15) n’a pas lieu d’être** — la compression parallèle se fait au canal, mieux placée, et la question d’alignement qui reste ouverte sur StudioLive (4.4) y est réglée par construction.

**Gate.** Attack 50 µs – 300 ms · Hold 10 ms – 5 s · Release 10 ms – 1 s · Threshold -72 à +18 dB · Depth 0–60 dB.

**Autres points.** HPF 20 Hz – 2 kHz, pente commutable **12 / 18 / 24 dB par octave** (la StudioLive est fixe à -12). Delay de sortie de bus jusqu’à **682 ms**, affichable en mètres — directement utilisable pour la Partie 7.8. Inserts routables partout, **non compensés en latence**. 8 DCA. Sidechain pris **après tout le traitement du canal**, delay compris.

**⚠️ Correction : il existe bien des modèles vintage — via DEEP, en add-on.** Ce que le manuel de base documente (ci-dessus) est le compresseur natif générique. Mais A&H vend une couche **DEEP Processing** qui remplace le traitement natif par des émulations portées du système haut de gamme dLive, **sans latence ajoutée et sans limite d’instances** (contrairement aux RackExtra FX ci-dessous, qui partagent 8 emplacements). Trouvé dans une discussion Tram Fest antérieure, à retenir pour la date :

- **Tube Stage Preamp** — gratuit pour tout utilisateur SQ (valeur 149$)

- **De-Esser** — payant, consomme un emplacement RackFX (pas DEEP, donc partagé et limité à 8 au total sur toute la console)

- **16VU Compressor Limiter** (VCA, RMS), **Opto Compressor**, **Mighty Compressor** — modèles payants embarqués par canal

- **DynEQ4** — EQ dynamique, l’équivalent le plus proche d’un traitement réactif en fréquence façon Soothe/Pro-Q

- **Vocal Gridder** (correction de pitch hip-hop/trap), **Vocal Shifter** — pertinents si un show demande un effet vocal marqué

**AMM (Automatic Mic Mixer)** — répond directement au principe NOM (2.2) par un mécanisme différent du gate manuel : deux mixeurs automatiques de 24 canaux, ou un combiné à 48, zéro latence ajoutée. Pensé conférence/multi-micros, mais transposable à une scène à plusieurs voix ouvertes en continu.

*Avant toute date sur SQ :* vérifier quels add-ons DEEP/RackFX sont activés sur la console utilisée — ça change ce qui est réellement disponible ce soir-là, au-delà de ce que le manuel de base décrit. À Tram Fest, un de-esser, une égalisation dynamique et une émulation de préampli l’étaient.

*Le reste de la Partie 2.8 (Fairchild, 1176, Pultec, Neve, API) reste sans objet pour le compresseur natif générique — mais devient pertinent si DEEP est activé, puisque les modèles portés de dLive visent justement ces mêmes références.*

### Behringer WING / WING COMPACT / WING RACK

**La plus riche du panorama en traitement natif nommé.** Structure : 40 canaux d’entrée, 8 Aux, 16 Bus, 8 Matrices, **4 Main stéréo**, 16 DCA, Automix à deux groupes (X et Y).

**Le slot Gate accepte n’importe quel modèle de dynamique** — ducker, émulations de gates analogiques, compresseurs, Wave Designer, Auto Rider, émulation de préampli, EQ dynamique. Ce n’est pas un gate figé.

**Trois fonctions que rien d’autre n’a :**

- **ACCENT** — relève temporairement le gain à l’ouverture du gate, pour compenser une ouverture tardive. C’est la réponse structurelle au problème récurrent du gate qui mange le début de la frappe.

- **KEY TAP** — choisit le point du trajet du signal d’où le déclenchement est prélevé. Le Key Source classique ne choisit que la source ; ici on choisit aussi l’endroit.

- **XOVER MODE** — applique un filtre au signal entrant dans le compresseur, **et réintroduit les fréquences retirées après compression**, pour leur conserver leur dynamique d’origine. C’est de la compression par bandes séparées. **Conséquence directe : la WING sait faire un vrai de-esser nativement**, sans insert externe ni ordinateur — tout le problème traité en 7.10 disparaît sur cette console.

**Compresseur.** THR · RATIO · KNEE · ATTACK · **HOLD** · RELEASE, avec DETECTOR (Peak/RMS), ENVELOPE (linéaire ou logarithmique), AUTO ENV, GAIN. Key Filter passe-haut, passe-bas, passe-bande **ou notch**.

**⚠️ Découverte majeure : contrairement à la SQ, tout est natif et gratuit.** La WING embarque **80 émulations analogiques**, et Behringer les nomme explicitement — aucune ambiguïté comme sur le Fat Channel PreSonus. Ça valide rétroactivement toute l’identification faite en 2.8 : ce sont exactement les mêmes machines de référence (1176, LA-2A, Fairchild 670, Pultec, Neve, dbx 160, SSL) qui reviennent partout dans l’industrie, pas des cas isolés.

*Compresseurs nommés :* UREI 1176 (avec son **All Buttons In** confirmé, boutons de synchronisation inversés — 1 = le plus lent, 7 = le plus rapide), Teletronix LA-2A, Fairchild 670, SSL Bus Compressor (4000G, glue de bus), SSL 9000 (channel, plus transparent), Neve 33609, Focusrite RED3, Drawmer DL241, Elysia mPressor/Xpressor, Empirical Labs Distressor, dbx 160/560A, **dbx 902 (De-Esser dédié, natif, gratuit)**, un équivalent de Waves Vocal Rider natif (Auto Rider).

*EQ nommés :* Pultec EQP-1A, Neve 84/88, Focusrite ISA 110, SSL 4000E.

*Gates nommés :* Neve 88RS, Neve Portico 5045, Drawmer DL241 (expandeur à ratio auto-adaptatif selon le niveau d’entrée).

**Aide-mémoire « pour quoi, quelle machine » — trouvé dans la doc WING elle-même :** voix posée → LA-2A · voix qui doit percer, rapide → 1176 · bus ou master → SSL 4000G · basse ou kick/snare qui doit taper fort → dbx 160 ou Distressor.

**EQ nommés confirmés** : Pultec EQP-1A, Neve 84, Neve 88-Formant, Focusrite ISA 110, **SSL 4000E** (4 bandes paramétriques). **Speaker Manager** — outil de protection de sortie à part, structuré en trois sections Filter/Dyn EQ/**Limiter** : c’est le seul endroit de toute la WING où existe un vrai bloc Limiteur séparé du compresseur (voir le principe transversal en 8.4).

*Conséquence pratique pour Louis :* sur WING, ne pas chercher un équivalent du Brit Comp ou du FC-670 (2.8) — prendre directement le vrai modèle nommé. Le Bus Drums devient littéralement un SSL Bus Compressor ou un dbx 160, le Bus Instru un FC-670 devient un vrai Fairchild 670 nommé comme tel.

**⚠️ De-esser natif confirmé et détaillé — deux modèles, pas un.** Le **BDX902** (calqué sur le vrai dbx 902 matériel) fonctionne **sans réglage de seuil** : il compare en continu le niveau de la bande aiguë au niveau large-bande plutôt que de réagir à un seuil fixe, donc il reste efficace aussi bien sur un passage fort que sur un passage doux, sans réglage manuel entre les deux. Commandes : Solo (écoute isolée de la bande aiguë), **HF Only** (n’atténue que l’aigu — sinon toute la bande large est affectée, comme le Key Filter détourné du Fat Channel), Frequency, Range. C’est objectivement supérieur à tout ce qui a été envisagé pour la StudioLive en 7.10 — natif, gratuit, adaptatif, sans ordinateur. Un second modèle, le **2-Band De-Esser** (calqué sur un appareil allemand), attaque séparément deux bandes de sibilantes en stéréo ou mid-side — mais **uniquement disponible en insert FX Rack**, pas en traitement de canal direct.

**⚠️ Découverte majeure, absente jusqu’ici du guide : des simulations d’ampli guitare natives.** Section 11.10, trois modèles :

- **Rack Amp** — calqué sur un processeur analogique américain, préamp+ampli+baffle, avec Drive, des bandes Buzz/Punch/Crunch dédiées par registre de fréquence, simulation de baffle commutable.

- **UK Rock Amp** — calqué sur les amplis britanniques classiques du rock, avec **SAG** (émulation de l’affaissement de l’alimentation d’un ampli à lampes Classe AB sous forte sollicitation — l’effet de compression naturelle qu’un vrai ampli lampe produit en étant poussé fort).

- **ANGEL Amp** — **explicitement positionné pour le métal et les styles agressifs et saturés.** Mêmes commandes SAG/Bass/Middle/Treble/Master.

*Conséquence directe pour le guide :* sur WING, une guitare en DI (basse de secours, ou guitariste sans ampli à une date dépannage) peut recevoir un vrai grain d’ampli métal **dans la console**, sans micro ni cabinet — l’ANGEL Amp est taillé pour exactement le style que Louis couvre le plus souvent. À garder en tête pour un plan de secours guitare sans passer par un ampli emprunté.

### Midas HD96-24

**Niveau de confiance (8.1) : connaissance documentée, jamais pratiquée.** Source unique : le manuel utilisateur **bêta V1.16** déposé au projet (deux fichiers, pages 1–343). Console d’une salle où Louis travaille ; formations spécifiques prévues à l’automne 2026. Le firmware de la salle peut être plus récent que ce manuel. Tout ce qui suit est relevé dans le texte du manuel ; les schémas n’ont pas été lus.

**Structure.** 144 entrées, **96 bus Aux** configurables un par un en départ, en **Group** (post-fader et post-pan, gain fixé à l’unité : le sous-groupe classique) ou en **Flexi-Aux** (un Aux qui peut lui-même être envoyé vers d’autres Aux, pour un mixage par stems aligné en temps), 24 matrices, masters stéréo et mono, 24 VCA, 24 groupes POP. Fréquence d’échantillonnage 96 kHz.

*Transposition de l’architecture du guide :* Bus Drums, Instru, Voix = trois Aux stéréo en mode Group ou Flexi-Aux. Le Flexi-Aux a un avantage que la StudioLive n’offre pas : un groupe de batterie déjà compressé peut être renvoyé tel quel dans les retours.

**Gain.** Préampli distant de -2,5 à +45 dB par pas de 2,5 dB (sur la plupart des boîtiers de scène), plus un Trim numérique de -40 à +20 dB. Aucune valeur de gain du guide ne se recopie.

**Ordre du signal.** Le manuel donne **DYN → Insert → EQ** comme ordre par défaut (chapitre Channel AI), réordonnable par glisser-déposer ; le gate précède toujours le compresseur. C’est l’ordre par défaut de la StudioLive aussi, mais **l’inverse** de l’ordre EQ → compresseur que ce guide règle sur ses canaux (1.6) : à trancher en premier, avant tout réglage.

**Filtres.** HPF à 12 ou 24 dB/octave, LPF à 6 ou 12 dB/octave. **⚠️ Les plages sont contradictoires dans le manuel lui-même** : HPF 10 Hz–10 kHz dans une section, 10–400 Hz dans une autre ; LPF 40 Hz–20 kHz ici, 2–20 kHz là. À lire sur l’écran, pas dans le manuel.

**EQ.** 4 bandes paramétriques, ±16 dB, 16 Hz–25 kHz, largeur 0,3 à 5,3 octaves. Bandes 1 et 4 commutables en plateau avec trois caractères : **Deep / Classic / Warm** pour le grave, **Bright / Classic / Soft** pour l’aigu. Le manuel conseille *Classic* par défaut (modelé sur la XL4) et réserve Deep et Bright — dits « à perturbation harmonique minimale » — aux **sources uniques**, pas aux prémix. Sur les sorties : 4 bandes avec modes passe-haut/passe-bas.

**Compresseur de canal — quatre modes, décrits par le manuel.** *Corrective* : détection crête, rapide, agressif, conseillé pour une basse très dynamique. *Adaptive* : détection RMS, enveloppe qui s’adapte, conseillé pour les voix. *Creative* : crête à attaque linéaire, transparent, conseillé pour la batterie et la guitare acoustique. *Vintage* : crête adaptative, ajoute des harmoniques, pour les instruments acoustiques. Threshold -50 à +25 dB, Ratio 1:1 à 25:1, Attack 0,2–100 ms, Release 0,05–3 s, Make-up 0–24 dB, Knee Hard (4 dB) / Medium (12 dB) / Soft (40 dB).

*Limiteur.* Pas d’étage séparé sur les canaux : à partir de 10:1 le compresseur « agit comme un limiteur » — le principe transversal de 8.4 s’applique. Le manuel mentionne un « soft clip limiter » sur les matrices et les masters, **sans en documenter les réglages**.

**Gate — entrées uniquement.** Threshold -50 à +25 dB, **Range jusqu’à -∞**, Attack 0,02–20 ms, **Hold jusqu’à 2 s**, Release 2 ms–2 s, mode **Gate ou Ducker**. Pas de gate sur les sorties (le manuel renvoie à l’effet SQ1 en mode gate).

*Sidechain du gate et du compresseur.* Filtre **passe-bande balayable**, 50 Hz–15 kHz, quatre largeurs (0,1 / 0,3 / 1 / 2 octaves), avec **Listen** vers le bus solo. Déclenchement externe par le patch (« Gate Key », « Comp SC »). Deux exemples donnés par le manuel, directement alignés sur le guide : gate de caisse claire avec le filtre vers **2 kHz en largeur 0,3 octave**, et basse compressée par le kick. La repisse de cymbale, intraitable sur la StudioLive (2.2), devient réglable.

**Retards.** Entrée 0–50 ms (85 ms sur la 32SC), sortie 0–500 ms (170 ms sur la 32SC, manuel 13.7), affichés en millisecondes et en mètres.

**Phase variable.** Un filtre passe-tout réglable de 0 à 90° ou de 0 à 180°, en plage High ou Low — il **prend la place du LPF** quand il est actif. Le manuel le destine aux prises à plusieurs micros : batterie, ampli à deux micros. La StudioLive n’a que l’inversion de polarité et le retard (7.7).

**Inserts et effets.** 3 emplacements d’effet par canal, **24 slots DSP** au total pour la console, certains effets tenant à quatre instances par slot, d’autres occupant plusieurs slots (la reverb VSS4 en prend trois). Le budget se surveille : l’indicateur vire au rouge sous quatre slots restants.

*De-esser — natif, en insert, sans ordinateur.* **DSR** : indépendant du niveau d’entrée (même logique que le dbx 902), un curseur de fréquence de coupure et un curseur de quantité ; **attention, son bouton Listen remplace la sortie principale par le signal filtré**, il ne part pas seulement au solo. **Dual De-Esser** : deux bandes, vers 6–7 kHz et vers 11 kHz. **M6** (multibande 6 bandes) et **Dynamic EQ** 4 bandes couvrent le même besoin en plus fin. Toute l’architecture USB de 7.10 est sans objet sur cette console.

*Égalisation dynamique.* Le **Dynamic EQ** 4 bandes (compression ou expansion par bande, mode Below, mode Fixed) est l’équivalent direct du traitement qui a fait ses preuves sur le bus voix à Tram Fest. **À essayer en premier sur le groupe de voix.**

*Expandeur de voix.* Le **PIE** (Prime Input Expander) est présenté comme « un gate taillé pour les voix » ; le manuel propose comme point de départ une détection passe-bande à 2 kHz, largeur 1, profondeur -12 dB.

*Modèles nommés.* **HD-2A** (« inspired by the original LA-2A »), **KT 1176** (Rev. E, position All), **KT Bus Compressor** (console 4000 G), **HD 670** (« inspired by Fairchild 670 », modes stéréo, double mono et LAT/VERT), **MTEC EQP-HD** (Pultec EQP-1A), **MTEC MEQ-HD** (Pultec MEQ-5), **XL4 EQ**, **R-Comp**, **SQ1**, **Wave Designer**. Le **Stressor** est décrit comme inspiré d’un « célèbre compresseur moderne » que le manuel ne nomme pas — ne pas le nommer à sa place. Les machines de 2.8 se retrouvent donc presque toutes, sous leur vrai nom.

*HD 670.* Le manuel chiffre ses six constantes de temps et recommande la **position 1** en live. Ne pas recopier la « Time Constant 3 » du FC-670 du guide : rien n’établit que les deux échelles se correspondent.

*Compression parallèle intégrée.* HD-2A, KT 1176, KT Bus Comp, HD 670, R-Comp, Stressor et Wave Designer ont un réglage **Mix** sec/traité. Le Bus Parallel du guide devient inutile — mais le manuel **ne chiffre aucune latence** : refaire le test d’annulation par inversion de polarité (4.4) avant de s’y fier.

*Effets utiles aux styles du guide.* **Plate Reverb avec un vrai Decay** (0,5–10 s), ce qui manque à la StudioLive (5.1bis). **TC 2290** avec tap tempo global et divisions pointées ou ternaires, que le manuel recommande explicitement pour le dub. **Sub Monster** et **Enlightenment Bass** pour renforcer le grave en hip-hop et en techno. **Rack Amp** (16 baffles) et **UNCL.HD** (distorsion multibande, 11 baffles) pour une guitare ou une basse en DI.

**Compensation de latence.** Réglable par couche (entrées, Aux, Flexi-Aux, masters et matrices) et par nombre d’inserts compensés, avec des préréglages. Le manuel recommande **FOH** « en cas de doute » et déconseille *Minimum* (filtrage en peigne possible).

**Scènes.** Hiérarchie Show → Playlist → Scène, avec une **Master Scene** qui sert de valeur par défaut à tout ce qu’une scène ne redéfinit pas. **Ouvrir un show ne charge aucune scène.** Huit **Safes** par canal d’entrée, plus un **Recall Scope** et un **Store Scope** réglables cellule par cellule — le manuel met lui-même en garde contre le Store Scope. Le rappel du patch avec les scènes dépend des préférences « Automate patching ». Sauvegarde : Auto Save à chaque stockage de scène, *Save & Mark*, retour arrière sur 25 versions, export USB.

**Trois outils de travail sans équivalent sur la StudioLive.** **True Audition** : retoucher l’EQ en ne l’entendant qu’au solo, puis appliquer ou annuler — la façade et les retours n’entendent rien pendant le réglage. **Manchino** : édition de plusieurs canaux à la fois, en absolu ou en relatif (monter toute la batterie dans trois retours d’un seul geste, couper tous les gates pour un line check). **Flip Target** : épingler sous un fader le départ d’un micro vers un retour, pour garder la main sur un larsen.

*Channel AI.* Analyse quatre secondes de signal, propose un nom d’instrument et des réglages de trim, EQ, gate et compresseur. Les propositions ne sont pas audibles tant qu’on n’active pas les traitements. Un point de départ, pas une méthode — et le manuel précise qu’il suppose l’ordre de traitement par défaut.

*Balance virtuelle.* Possible, mais **une carte CM-1** (USB, MADI, Dante ou AES50) doit être installée dans la console.

**⚠️ Deux réglages à vérifier avant de toucher un fader.** Le **Solo In Place** coupe la façade de tout ce qui n’est pas en solo ; il demande un appui long, mais vérifier qu’il est éteint. Et **« Input Solo Follows Select »** : s’il est actif, sélectionner un canal l’envoie au solo.

**Non documenté dans ce manuel :** la latence de la console et des effets, la référence des vumètres, le coût DSP de chaque effet, les réglages du soft clip limiter. Les chapitres 22 et 23 sont vides (« TBA »).

**À vérifier en formation :** ordre du signal par défaut sur le show de la salle · plages réelles du HPF et du LPF · préférences « Automate patching » et Safes en place · présence d’une carte CM-1 · préréglage de compensation de latence utilisé · test d’annulation sur le Mix d’un compresseur en insert.

### Midas M32

Architecture proche du X32, préamplis Midas. **Gate** : threshold, range, attack, hold, release, **key filter avec fréquence et pente réglables**, key source au choix parmi n’importe quelle entrée ou sortie, écoute du key sur le bus solo.

**Point à retenir : l’insert de canal est commutable pre- ou post-EQ/compresseur.** C’est un choix qui n’existe pas sur StudioLive et qui change tout pour un traitement externe — un de-esser placé avant ou après le compresseur ne fait pas le même travail.

Canal : gain, low-cut, delay numérique, source assignable.

**Effets natifs, gratuits, même famille que la WING mais deux fois moins d’emplacements.** Behringer confirme que la WING a “le double de moteurs d’effets et de points d’insert par rapport au X32” — le M32 (architecture X32) a donc la même bibliothèque en substance, avec moins de place pour la faire tourner partout en même temps. Plus de 50 effets “FX Plug-Ins” : **Ultimo Compressor** (1176 — Input Gain pilote gain ET seuil, comme le Class-A FET du Fat Channel, ratios 4:1/8:1 en compresseur, 12:1/20:1/**ALL en limiteur**), **LA Compressor** (LA-2A), **Fairchild 670**, **Pultec EQP-1A et EQ5**, un compresseur multibande 5 bandes, 4 reverbs stéréo qualité studio, 8 canaux de GEQ 31 bandes.

*Retour d’expérience croisé, trouvé dans les forums Behringer :* le 160 (dbx) et le 560 donnent de bons résultats sur toms, caisse claire et basse — cohérent avec la logique déjà établie en 2.8 pour le Comp 160/dbx 160 sur ce type de source.

*Différence par rapport à la StudioLive à garder en tête :* ces modèles sont nommés explicitement, donc pas de travail d’identification à faire comme en 2.8 — mais moins d’emplacements simultanés que sur WING, donc arbitrer où les utiliser en priorité (bus plutôt que sur chaque canal).

### Yamaha DM3

**⚠️ Contrainte majeure à vérifier en premier : le gate (DYN1) n’existe que sur les canaux 1 à 16.** Sur une configuration batterie complète plus voix et instruments, ça se planifie — les sources qui ont besoin d’un gate doivent être patchées dans les seize premiers canaux. À arbitrer avant même de poser les micros.

**DYN1** : bascule GATE ou **DUCKING** · Threshold · Range · Attack · **Hold** · Decay (le pas de réglage correspond à une variation de 6 dB). Key In au choix : **Self Pre EQ, Self Post EQ, un autre canal (1–16 post-EQ), ou un bus MIX (1–6)**. Pas de filtre sur le key — seulement le choix de la source. *Corollaire :* la source « autre canal » est elle aussi limitée aux canaux 1–16 — **le kick doit donc être patché dans les seize premiers canaux pour servir de déclencheur**, en plus de la basse qui reçoit le ducking.

*Conséquence pratique :* sans filtre de détection, le ducking kick → basse (2.5) se règle uniquement par le Threshold et les temps. Et le choix **Self Pre EQ / Self Post EQ** est une finesse absente ailleurs : déclencher avant ou après l’EQ du canal change ce que le gate entend, ce qui peut remplacer en partie un Key Filter — si l’EQ du canal creuse déjà les graves, prendre le key en Post EQ revient à filtrer la détection.

**DYN2 (compresseur)** : mode 1-knob simplifié ou mode manuel complet.

**EQ — 4 bandes paramétriques partout, sans modèle de caractère.** CH 1-16 : HPF + 4 bandes ; ST IN/FX RTN/MIX/STEREO/MATRIX : 4 bandes seules. Bande basse commutable Low-shelving ou Bell (+ HPF sur les canaux qui en ont un) ; bande haute commutable LPF, High-shelving ou Bell. **Mode 1-knob avec deux presets nommés** : « Vocal » et « Intensity » (ce dernier interpole entre plat et un réglage manuel intense). Sur les sorties uniquement, un troisième preset **« Loudness »** — booste simultanément le grave et l’aigu, la courbe classique pour compenser la perception à bas volume. RTA intégré à l’écran EQ.

*Aucun modèle vintage nommé, confirmé sur l’ensemble du DM3* — cohérent avec le constat déjà posé : console généraliste Yamaha, pas de bibliothèque de caractère comme WING ou M32.

**⚠️ Pas de Limiteur séparé trouvé sur DM3.** Aucune section dédiée dans le manuel — cohérent avec le principe transversal de 8.4 : ici aussi, c’est vraisemblablement le compresseur (DYN2) poussé fort qui tient lieu de limitation, sans bouton ni étage nommé « Limiter ».

### Behringer X-AIR (XR12 / XR16 / XR18)

**⚠️ Correction d’une erreur du V21 : le Gate est bien séparé du Compresseur.** Une première lecture avait manqué la section « 5.4 Porte », distincte de la section « 5.5 Dynamique ». Ce sont deux blocs à part entière, chacun avec son propre bouton marche/arrêt et son propre Key Filter — l’architecture standard, pas une exception.

**5.4 Porte (Gate)** — Threshold, Hold, Release, Attack, et surtout un **Key Filter complet** : passe-haut/passe-bas/passe-bande commutable, pente réglable, fréquence sélectionnable en glissant directement sur un graphique de fréquences, plus une sélection de source. Le sélecteur **Gate Type** propose quatre réglages : **EXP2/EXP3/EXP4** (expansion graduée, de douce à marquée), **Gate** (coupure franche), et **Ducker** — celui-ci atténue le signal d’une quantité fixe *dès que* le niveau *dépasse* le seuil, l’inverse logique d’un gate. C’est un vrai outil de ducking intégré au Gate lui-même, sans avoir besoin d’un compresseur en sidechain pour ça.

**5.5 Dynamique (Compresseur/Expandeur)** — bloc séparé, qui lui bascule effectivement entre action Compresseur ou Expandeur via un seul contrôle. Threshold, Knee, Ratio, Attack, Peak/RMS, **Hold**, Release, et son propre Key Filter indépendant de celui du Gate.

*Ce qui reste vrai malgré la correction :* le bloc Dynamique ne peut agir QUE comme compresseur OU comme expandeur, jamais les deux en même temps — mais ça ne l’empêche pas de tourner en parallèle du Gate, qui lui gère l’ouverture/fermeture. Un canal peut donc légitimement avoir Gate + Compresseur actifs simultanément, exactement comme le prescrit ce guide ailleurs (3.1 et suivants) — l’inverse de ce que disait le V21.

**Départs Aux/FX pris pré ou post EQ**, même logique de finesse que le DM3 (Self Pre EQ / Self Post EQ).

**Bibliothèque de reverbs à héritage explicite** (comme la WING, contrairement au flou volontaire de PreSonus) : Hall/Ambience/Room/Chamber inspirées du Lexicon 480L, Plate Reverb inspirée du Lexicon PCM-70, **Vintage Reverb inspirée de l’EMT250**, Vintage Room inspirée du Quantec QRS, Gated Reverb inspirée du Lexicon 300/480L — utile pour un son de caisse claire type années 80 ou pour épaissir un kick, cité explicitement dans le manuel.

*Pas de de-esser natif ni de simulation d’ampli trouvés dans ce manuel*, contrairement à la WING et à l’Ui24R ci-dessous.

### Soundcraft Ui24R

**⚠️ La meilleure nouvelle de toute cette recherche : un vrai de-esser natif, sur chaque canal, gratuit.** Contrairement à tout ce qui a motivé la section 7.10 sur la StudioLive (montage à deux canaux, USB, ordinateur dédié, risque de latence), l’Ui24R intègre un de-esser directement dans le bloc EQ paramétrique de **chaque canal d’entrée, retour FX et master de sous-groupe** — pas un ajout payant, pas un insert à câbler. Commandes : **Threshold, Ratio, Frequency**, manipulables via une interface graphique tactile (une “boule” qu’on fait glisser — haut/bas = seuil, gauche/droite = fréquence, pincer = ratio). Si Louis pose un jour la main sur cette console, le problème entier de la Partie 7.10 disparaît : de-esser une voix lead devient un geste natif d’un seul canal, sans montage.

**Gate et Compresseur restent deux blocs séparés** (contrairement au X-AIR) : Gate — Threshold, Attack, Hold, Depth, Release ; Compresseur — Threshold, Attack (en microsecondes), Ratio, Release, Gain, Hold, Soft/Hard Knee partagé entre les deux blocs.

**EQ à deux visages** : parametric 4 bandes + HPF sur les canaux, **GEQ 31 bandes sur les masters de sous-groupe et Aux**, avec RTA (analyseur temps réel) intégré à l’écran EQ pour viser une fréquence à l’oreille ET à l’œil.

**dbx AFS2 (Automatic Feedback Suppression) intégré au GEQ des sorties.** Un algorithme dbx matériel, pas une simple app — pertinent en complément du principe NOM (2.2) pour la gestion du gain avant larsen sur un plateau à micros nombreux.

**4 processeurs FX Lexicon authentiques** — Reverb, Delay, Chorus — la vraie marque Lexicon (Harman possède les deux marques), pas une émulation “inspirée de”. Différent de la WING/X-AIR qui imitent Lexicon sans le nommer : ici c’est licencié et revendiqué comme tel.

*Pas de simulation d’ampli trouvée dans ce manuel*, contrairement à la WING.

## 8.7 Registre des tests en attente

Pistes argumentées, **aucune validée en conditions réelles**. À cocher au fur et à mesure.

*État au 10 novembre 2026 :* **aucun test de ce registre n’a été réalisé depuis septembre** (confirmé par Louis). Le seul retour de terrain nouveau est celui de Tram Fest sur SQ6, consigné en 8.6 — il ne solde aucune ligne ci-dessous, toutes propres à la StudioLive ou à d’autres consoles.

*La méthode pour avancer :* la balance virtuelle (7.12). Les lignes marquées **BV** se soldent console seule, sur un enregistrement, sans groupe.

| Test | Où | Quoi vérifier |
| --- | --- | --- |
| **BV** — Alignement du Bus Parallel | 4.4 | Source large bande ; résidu ≥ 20 dB sous un bus seul, sans traitement puis avec Comp 160 bypassé |
| Class-A FET en position All | 4.4 | Alternative au Comp 160 sur le Bus Parallel — jamais en direct sur un canal |
| Tour de passe-passe Pultec | 5.1 | Low Boost +1/+2 dB **et** Low Atten +1/+2 dB à 60 Hz simultanément, en A/B |
| Vintage 3-Band EQ | Guitare lead | Alternative au Standard EQ quand l’ampli est agressif |
| VT-1 EQ | Voix hip-hop/reggae | Cohérence avec le VT-1 Compressor déjà en poste |
| Tube EQ | Bus Voix dub | Portée limitée 200 Hz–5 kHz comme protection face aux effets |
| Q proportionnel Alpine | Overheads, caisse claire | Boosts plus francs que d’habitude, la bande se resserre seule |
| De-esser en insert USB | 7.10 | Voie A (Key Filter détourné) d’abord, puis plugin si insuffisant |
| Sous-groupe fixe vers AVB | 7.8 | Alimenter un renfort sans consommer de FlexMix |
| Test de traction des câbles AVB | 7.9 | LED ambre, sur chaque câble du parc |
| **BV** — Premier enregistrement multipiste SD | 7.12 | Un concert ou un soundcheck par style ; vérifier que le signal est pris avant le Fat Channel |
| **BV** — Dual mono du Bus Instru | 4.2 | Option Comp./Limiter décochée : mètre de l’autre côté immobile, image centrale stable |
| Bus Basse sur sous-groupe fixe A | 4.6 | Basse à deux sources, ou source unique dont le compresseur de canal sert au ducking ; consigner le traitement retenu |
| Sous-groupe fixe vers une sortie Mix | 1.3 | Patch numérique, Analog Sends : le sous-groupe sort-il bien sur la sortie choisie ? |
| GEQ sur chaque retour | 7.11 | Ring out à la main, 3–4 bandes au plus ; tenue des courbes au changement de scène |
| AFS sur les retours | 7.11 | PA2 entre sorties de retours et ampli ; Fixed puis Live ; marge gagnée en dB |
| Voix lead par USB, chaîne retenue | 7.10 | Clap-test de chaque plugin (Timeless 3 en priorité) ; tenue CPU sur la durée d’un set |
| Effet de la table par USB | 7.10 | Départ FX D pré-processeur vers une reverb ou un delay VST ; le processeur interne tourne-t-il encore ? |
| Identifier les modules utilisés sur SQ6 | 8.6 | Nom de l’égalisation dynamique et de l’émulation de préampli de Tram Fest |
| HD96 — vérifications de formation | 8.6 | Ordre du signal, plages HPF/LPF, Automate patching, carte CM-1, latence du Mix |
| HPF des overheads en 4 micros | 3.1 | 80 Hz contre 60–70 Hz : corps du floor tom contre repisse du kick |
| **BV** — Limiteur du Bus Parallel à 150 ms | 4.4 | Le limiteur travaille-t-il réellement derrière le Comp 160 ? À faire dans la même séance que l’alignement |
| **BV** — Plafond du de-esser voie A | 7.10 | Voix lead enregistrée, Key Filter 7–8 kHz : noter la réduction (en dB) à laquelle le pompage devient audible, et l’inscrire en 7.10 |
| Authenticité des Beta58 | Annexe C | Mesure au multimètre broches 2–3 ; propager le résultat en 0.2 et Annexe B |
| **BV** — Échelle du Time Constant du FC-670 | 2.1 | Positions 1 à 6 sur un enregistrement : les temps s’allongent-ils de 1 à 4, et 5–6 réagissent-ils au programme ? |
| Ducking de la musique par le MC | 6.4 | Key Source = micro MC sur le canal DJ ; les deux côtés reculent-ils ensemble ? |
| Saturation ou transient shaper sur le Bus Drums par USB | 4.1 | Latence du chemin USB et test d’annulation avant usage |
| Key Source et modèles d’EQ sur un retour d’effet | 5.2 | Sélectionner le retour FX A : le compresseur propose-t-il un Key Source ? Le Vintage 3-Band EQ se charge-t-il, et quelle plage pour son HPF ? |
| **BV** — Reverb voix produite par l’ordinateur, avec ducking | 5.2 | Départ FX A pré-processeur en USB, retour sur canal d’entrée, Key Source = voix lead |
| Voyants BELOW/ABOVE du Comp 160 | 2.1, 4.4 | Lequel s’allume quand le mètre de réduction de gain bouge ? L’un des deux réagit-il au toucher ? |
| Kick à deux micros, PGA52 | 3.2 | Position (près de la batte ou devant), retard 7.7 et touche Ø |
| Low Shelf sur l’EQ d’un retour d’effet | 5.2, 5.4, 5.6 | Dans UC Surface, sélectionner le retour FX A : le bouton Low Shelf est-il présent ? |
| Insert USB, ordre plugin → console | 7.10 | Départ Pre de A, Fat Channel sur B : entendre le plugin seul sur A en solo côté logiciel, puis la voix traitée sur B |
| Retard d’entrée et départ Pre1 | 7.7 | Retarder un canal de 10 ms : le retour en Pre1 est-il retardé ? |
| Ordre EQ → compresseur sur les canaux | 1.6 | Canal neuf : bouton Comp>EQ dans l’état par défaut ? Le réglage inversé est-il rappelé avec la scène et le preset de Fat Channel ? |
| Plages du Class-A FET | 2.1, 3.1, 3.4, 3.6 | Butées réelles d’Attack et de Release ; les Attack de 3 et 5 ms et le Release de 150 ms sont-ils réglables ? |
| Crans du Release du Brit Comp | 4.1 | Valeurs imprimées sur le panneau |
| Retour d’effet dans la liste USB Sends | 5.2 | Le retour FX A est-il proposé comme source ? Si oui, ducking avec la reverb de la console |
| Niveau d’un retour d’effet vers un bus en mode sous-groupe | 5.3 | Affectation seule, ou niveau réglable par bus ? |
| Plages et défauts des effets | 5.1bis | Pour chaque reverb et delay : plage et valeur par défaut de Reflection, Size, Diffusion, Spread, Width ; présence d’un Mix ou d’un Decay à l’écran |
| Crans de fréquence de l’Alpine EQ-550 | 4.2 | Les sept fréquences de chaque bande, lues sur le panneau |
| Réduction retenue pour le ducking | 2.5, 6.4 | Valeur lue au mètre une fois le réglage satisfaisant |
| Départ d’un retour d’effet vers un autre FX | 6.6 | Le retour FX B propose-t-il un départ vers FX A (delay dans la reverb) ? |
| **BV** — Double grosse caisse rapide | 6.3 | Sur un enregistrement de métal : moins de compression au canal kick contre réglage standard ; release du gate sous l’intervalle entre frappes |

**Regroupement par séance — pour solder le registre en trois fois.**

*Séance 1 — console seule, sans son, environ vingt minutes. Ce ne sont que des lectures d’écran.* Plages du Class-A FET · crans du Release du Brit Comp · crans de l’Alpine EQ-550 · plages et défauts des effets, présence d’un Mix ou d’un Decay · Key Source et modèles d’EQ sur un retour d’effet · Low Shelf sur un retour d’effet · retour d’effet dans la liste USB Sends · niveau d’un retour d’effet vers un bus en mode sous-groupe · départ d’un retour d’effet vers un autre FX · état par défaut du bouton Comp>EQ · sous-groupe fixe vers une sortie Mix.

*Séance 2 — console et enregistrement multipiste (balance virtuelle, 7.12), une à deux heures.* Toutes les lignes marquées **BV**, plus : voyants du Comp 160 · Class-A FET en All · tour de passe-passe Pultec · retard d’entrée et départ Pre1 · rappel de l’ordre EQ → compresseur avec la scène · insert USB (ordre plugin → console, clap-test, tenue CPU) · effet de la table par USB.

*Séance 3 — avec des musiciens, en balance ou en concert.* GEQ et AFS sur les retours · HPF des overheads · kick à deux micros · ducking de la musique par le MC et réduction retenue · Bus Basse · Vintage 3-Band, VT-1 EQ, Tube EQ, Q proportionnel de l’Alpine.

*Hors StudioLive :* modules de la SQ6, vérifications HD96, authenticité des Beta58, câbles AVB.

# ANNEXE A — RÉCAPITULATIF PLUGINS

**Compresseurs**

| **Plugin** | **Technologie** | **Poste** |
| --- | --- | --- |
| Standard Compressor | Numérique transparent | Canaux — contrôle précis sans couleur |
| Tube Leveling Amp | Opto-lampe | Sax, orgue, Rhodes, voix douces |
| Class-A FET | FET agressif — pas de Threshold | Caisse claire, guitare rythmique, cuivres |
| Brit Comp | Double VCA | Bus Drums |
| Classic Compressor | Smooth — pas d’Attack | Contrebasse, acoustique, accordéon |
| Comp 160 | VCA extrême | Bus Parallel uniquement |
| Everest C100A | Leveling doux | Master, claviers, table DJ |
| FC-670 | Lampes, variable-mu (Fairchild 670) — Input Gain d’abord | Bus Instru |
| RC-500 Comp | FET, ratio fixe 3:1 | Basse DI, vinyle |
| Tube CB | Opto-lampe — Manual sur voix | Bus Voix (tous styles) |
| VT-1 Comp | FET-lampe | Voix lead expressive |

**Égaliseurs**

| **Plugin** | **Structure** | **Poste** |
| --- | --- | --- |
| Standard EQ | Paramétrique | Canaux — chirurgie, HPF |
| Passive Program EQ | Lampe passif | Master |
| Vintage 1970s EQ | 4 bandes, Low en plateau, High à fréquence fixe | Bus Voix — punk, rock, métal |
| Alpine EQ-550 | 3 bandes, 7 points | Bus Instru, Bus Voix hip-hop et reggae |
| Baxandall EQ | Plateaux larges | Canal Kick |
| RC-500 EQ | 3 bandes semi-param | Bus Parallel |
| Solar 69 EQ | Brit, notch, High réglable | Bus Drums |
| Tube EQ | Passif lampe, 200 Hz–5 kHz uniquement (Peak/Dip/Peak) | Chaleur subtile sur une voix · option Bus Voix dub |
| Vintage 3-Band | Actif mordant | Canal guitare ou voix sans présence |
| VT-1 EQ | 4 bandes semi-param | Voix — finesse |

**Effets — rack FLEX DSP**

| **Effet** | **Commandes clés** | **Poste** |
| --- | --- | --- |
| Vintage Plate Reverb | Predelay, Reflection, Low Pass | FX A — voix, tous styles, et extérieur |
| Digital XL Reverb | Predelay, Reflection, Size, LPF Freq | FX C — batterie |
| 335 Digital Reverb | + Diffusion, Size | Alternative dub (queue nuageuse) |
| PAE-16 Digital Reverb | + Diffusion | Alternative |
| Stereo Delay | Times A/B, Feedback, LP/HP, **Fb LPF/HPF** | FX B — voix et instruments |
| Ping Pong Delay | Times L/R, Width, **Fb Time, Fb LPF** | FX D — dub, effets ponctuels |
| Mono Delay | Time, Feedback, LP/HP | Slap simple |
| Chorus / Flanger | Rate, Depth, Width, Shape | Non utilisés par défaut (5.7) |

*⚠️ Aucune des quatre reverbs ne documente de commande Decay. La longueur perçue se règle par Reflection, Predelay et Diffusion. Voir 5.1bis.*

**Retards — souvent oubliés, très utiles**

| **Outil** | **Plage** | **Poste** |
| --- | --- | --- |
| Retard d’entrée | 0 à 85 ms, pas de 0,1 ms | Aligner kick in/out, caisse claire dessus/dessous, DI/ampli, backline sur micro de chant (7.7) |
| Retard de sortie | jusqu’à 170 ms, pas de 0,1 ms (manuel 13.7), par mixage Flex et sur le Main | Aligner la façade sur le backline, systèmes de renfort (7.8) |
| Repère | 2,9 ms par mètre | distance ÷ 0,34 = retard en ms |

# ANNEXE B — PATCHS TYPES PAR FORMATION

Chaque patch distingue le **parc personnel** (garanti) de l’**emprunt** (à confirmer date par date).

**Groupe rock / punk — 4 musiciens, 100 % autonome**

Canal 1 kick (BD 500 Beta, 48 V) · Canal 2 caisse claire (i5 sur D-Vice) · Canaux 3-4 overheads (Lewitt, 48 V, couplés en stéréo) · Canal 5 basse (DI active) · Canal 6 guitare (SM57) · Canaux 7-8 voix (Beta58 ×2) · Canaux 9-10 chœurs (SM58 ×2).

*10 canaux, uniquement du matériel personnel, un seul pied de micro.* C’est la configuration de référence.

**Groupe métal — 5 musiciens, avec emprunt**

Base identique, plus : Canal 11 seconde guitare (SM57 MJC) · Canaux 12-13 toms (les deux e604 de la MJC). **HPF des overheads : 300–400 Hz seulement si tous les toms du kit sont micés** ; avec deux toms micés sur un kit qui en compte trois ou plus, rester à 80–120 Hz (3.2).

*13 canaux, dont 3 en emprunt.* *Correction V33 : l’ancien patch prévoyait trois toms (11-13) alors que la MJC prête deux e604, et comptait « 4 emprunts » pour un total qui faisait 14.*

**Plateau rap — jusqu’à 4 MC + DJ**

Canaux 1-2 voix lead (Beta58 ×2 — **sous réserve du test d’authenticité, Annexe C** ; à défaut, SM58 de la MJC) · Canaux 3-4 voix (SM58 ×2) · Canal 5 HF invité (fourni par le lieu ou l’artiste) · Canaux 6-7 table DJ stéréo · Canaux 8-9 seconde paire DJ pour l’enchaînement.

*9 canaux.* La batterie n’est pas mobilisée : c’est le format le plus léger en montage.

**Reggae / dub — 5 à 6 musiciens**

Canaux 1-4 batterie (kit autonome) · Canal 5 basse (DI active) · Canal 6 guitare skank (SM57) · Canal 7 clavier mono (DI passive) · Canaux 8-10 voix et toaster.

*10 canaux.* **Si le clavier est stéréo :** canaux 7-8 sur la Palmer River Elde, voix en 9-11 — *11 canaux*. Dans les deux cas, avec la basse sur la DI active, la formation tient sans emprunt de DI.

**Techno live — sorties séparées**

Canaux 1-2 kick et sub · Canaux 3-4 percussions · Canaux 5-6 synthé stéréo · Canaux 7-8 second synthé.

*8 canaux, mais la capacité DI est le facteur limitant.* Privilégier les sorties symétriques directes des machines quand elles existent.

**Configuration minimale — petite date, montage express**

Canaux 1-4 batterie · Canal 5 basse (DI active) · Canaux 6-7 voix (Beta58 + SM58 — Beta58 sous réserve de l’Annexe C).

*7 canaux, montage en moins de dix minutes.*

# ANNEXE C — VÉRIFICATION AUTHENTICITÉ BETA58

Deux Beta58 du parc ont une origine incertaine. À vérifier avant de leur confier une voix lead sur une date qui compte.

*Test au multimètre — le plus fiable.* Mesurer la résistance entre les broches 2 et 3 du XLR. Un Beta58A authentique afficherait environ **20 ohms**, une contrefaçon **500 à 600 ohms**. **⚠️ Ces deux valeurs viennent de retours d’usage, aucune source constructeur n’est au projet.** Mesure la plus parlante : comparer les deux micros entre eux, et si possible à un Beta58A dont l’origine est sûre. Un écart d’un facteur dix entre deux exemplaires du même modèle tranche ; une valeur isolée ne prouve rien.

*Inspection visuelle, en complément.* Mousse sous la grille (dense et régulière sur un authentique), anneau bleu (couleur franche, pose nette), gravure du modèle (profonde, bien centrée), poids général (un authentique est sensiblement plus lourd).

*Si contrefaçon confirmée.* Le micro reste utilisable en chœur ou en secours, pas en voix lead sur une date importante. Le remplacement passe alors en priorité 5 de la feuille de route. **Conséquence sur les patchs types (Annexe B)** : les postes notés « Beta58 » en voix lead passent sur SM58 (0.2) ou sur un SM58 de la MJC (0.6). *Si authenticité confirmée* : retirer la mention « authenticité douteuse » en 0.2 et les réserves de l’Annexe B.

# ANNEXE D — MODÈLE DE FICHE GROUPE

Structure à remplir pour chaque formation d’un plateau. L’objectif est qu’une fiche tienne sur une page et se lise en trente secondes en situation.

**En-tête**

Nom du groupe · Style · Durée du set · Ordre de passage · Scène de style à rappeler (Partie 6).

**Formation**

Nombre de musiciens, instruments, nombre de voix. Signaler tout instrument inhabituel qui demandera le Bus Divers (FM 16).

**Patch**

Tableau canal par canal : numéro, source, micro ou DI utilisé, alimentation fantôme requise, bus de destination. **Indiquer clairement ce qui est en emprunt.**

**Écarts par rapport au preset de base**

Uniquement ce qui diffère de la Partie 3. Si un chanteur mange le micro, noter le HPF relevé. Si le batteur frappe très fort, noter le gain réduit sur les overheads. Le reste est dans le guide, inutile de le recopier.

**Retours**

Affectation FlexMix 1 à 6, avec le contenu demandé par chaque musicien et, pour chacun, le **point de départ** : Pre1 pour un wedge, Pre2 pour des in-ears (7.11).

**Points de vigilance**

Ce qui a posé problème la fois précédente, ou ce qui est annoncé comme risqué : niveau de scène élevé, chanteur qui se déplace, machine capricieuse, DI empruntée non confirmée.

**Timing de changement**

Ce qui reste en place, ce qui bouge, ce qui se démonte. Sur un plateau serré, c’est la partie la plus utile de la fiche.

*💡 Une fiche groupe ne redit jamais ce que contient le guide. Elle note uniquement le patch, les écarts et les risques. Tout le reste se lit dans les Parties 3 à 6.*

# HISTORIQUE — NE PAS CITER

*Section de traçabilité. Les valeurs « avant » sont périmées et ne doivent jamais être reprises comme valeurs de travail : seul le corps du guide fait foi. Une recherche textuelle peut tomber ici avant d’atteindre la prescription courante : la protection est la consigne du bloc assistant, pas le texte.*

### CE QUI CHANGE PAR RAPPORT À LA V34

Mission transmise par Louis (cahier des charges rédigé avec DeepSeek) : rendre le guide directement exploitable par une IA qui produit des presets. Chaque demande a été vérifiée au manuel avant d’être appliquée.

- **Bloc assistant.** Ajouts : règle de priorité entre sections ; règle unique pour les valeurs non vérifiées, avec règle de repli ; renvoi pour les qualificatifs ; « Construire un preset complet » (périmètre, ordre, lignes obligatoires, omissions permises, différence avec la fiche groupe). Le cahier des charges demandait un « tableau canal par canal » : non retenu, les fiches restent en prose (instructions de projet), le patch seul est en tableau. Manuel UC Surface : toujours cité par son nom.

- **5.1bis.** Convention « bas / modéré / haut » et méthodes de réglage pour Reflection, Size, Spread, Width, Diffusion — le manuel (9.1.2) ne donne ni plage ni défaut. **5.2.** « Mix 100 % » : commande non documentée, retirée. « Reflection haut = reverb courte » signalé comme lecture du guide.

- **2.1, 2.5, 2.7.** Méthodes de convergence du Tube CB et de l’Everest (trois positions nommées par l’addendum) ; méthodes des usages 2 et 3 du sidechain ; cinq lignes ajoutées au tableau des plages. **3.3, 3.4.** Recovery du Classic Compressor : « medium » → mi-course avec méthode.

- **4.4.** Comp 160 : « graduation autour de 7–8 sur 10 » retiré, méthode à la place. **4.1.** Brit Comp : Release « vers 200 ms » → cran le plus proche de 200–300 ms. **4.2.** Alpine : crans à relever, règle d’écriture en attendant. **6.3.** Méthode pour trouver la fréquence du Trough. **3.4, 6.6.** Points de départ et méthodes du Vintage 3-Band et du Tube EQ. **6.1.** Vintage 1970s High : critère d’écoute.

- **7.10.** Test du canal A : « aucun mètre de bus » → aucun bus de groupe, et contrôle que le retour du chanteur est bien alimenté. **5.2.** Sous-titre du ducking. **3.1.** Variante hip-hop : même ratio que la base, dit clairement. **5.3.** Retour du delay vers le Bus Instru : seulement quand un instrument reçoit du delay — le cadre « instrument soliste uniquement » proposé n’est pas retenu tel quel, le dub envoie des éléments rythmiques dans le delay (6.6). **7.11.** « Jamais Post » limité aux retours de musiciens.

- **Annexe D.** Point de départ Pre1 ou Pre2 par retour. **8.7.** Trois lignes ajoutées et regroupement du registre en trois séances.

### CE QUI CHANGE PAR RAPPORT À LA V33

Audit de DeepSeek (six remarques de cohérence, toutes retenues), puis contrôle par Claude de chaque passage réécrit depuis la V29 contre les sections auxquelles il renvoie.

- **3.3, 4.6, 2.5.** Le Bus Basse proposé en 3.3 pour une basse à source unique contredisait 4.6 : exception écrite en 4.6, renvoi ajouté en 2.5.

- **5.2 et 6.4.** « Ne peut pas être renvoyé sur un canal d’entrée » suivi d’une « seconde porte » : une seule formulation, le manuel se contredit (12.3.4 contre tableau 6.1), deux vérifications console. Titre : « pas faisable en natif » → « pas faisable sur le retour lui-même ».

- **7.11.** « Règles reprises de 7.3 : coupures uniquement » → coupures sans exception, justifié.

- **7.10.** Canal A désaffecté de tous les bus (pas seulement Bus Voix), départs d’effets fermés sur A, scènes enregistrées dans cet état. Retour en Pre2 : « comme en façade » → sans le de-plosive ni le de-esser.

- **3.1 (Claude).** Variante hip-hop de la caisse claire : « Ratio 3:1 » → 4:1, le Class-A FET n’a pas de 3:1. Réserve sur les plages étendue aux valeurs d’Attack (2.1, 3.1, 3.4, 3.6).

- **5.2, 5.3, 5.4 (Claude).** Routage des retours d’effet réécrit d’après le manuel 5.5.1. Ancien 5.3 : « Bus Voix à -20 dB, Bus Instru à -24 dB » — deux niveaux non documentés pour des bus en mode sous-groupe.

- **1.4 (Claude).** « Latence inférieure à 1 ms » du lien AVB : sans source, retiré. **2.6, 8.2.** Dernières mentions de BELOW/ABOVE comme « zones » ou « modes ». **7.10.** Oversampling de Saturn2 limité aux pistes parallèles. **7.11.** Dosage des effets dans un retour.

### CE QUI CHANGE PAR RAPPORT À LA V32

Audit complet de Claude, relecture intégrale du corps du guide contre le manuel, l’addendum et le manuel UC Surface, croisé avec deux passes de Gemini. Version préparée pour l’audit suivant de DeepSeek.

- **1.6 et propagations (Partie 4, 8.4, 8.6).** Ancien texte : « sur les canaux, le routage interne place l’EQ avant le compresseur ». Faux : par défaut, compresseur puis EQ (manuel 6.8.4). Le guide garde l’EQ avant le compresseur sur les canaux, en inversant l’ordre au bouton Comp>EQ.

- **2.3, 6.1, 6.2, 6.3, Annexe A.** Vintage 1970s : « 4 bandes à fréquences fixes, Low ~200 Hz, High ~12 kHz » → Low en plateau réglable (60 Hz par défaut), L-Mid et H-Mid réglables, High à fréquence fixe non chiffrée. Le Bus Voix déplace maintenant le Low vers 200 Hz.

- **2.1.** Class-A FET : plages « 0,1–60 ms » et « 250 ms–3 s » retirées, sans source. RC-500 : plages de l’addendum ajoutées (Fast/Slow = butées). **3.7.** VT-1 : « Fast / Medium / medium » → 1 ms, 200 ms, 4:1. **4.1 et 8.2.** Brit Comp : « Attack 10–20 ms » → 10 ou 30 ms (crans du panneau).

- **3.3.** Ducking de la basse par le kick : le compresseur du canal ne peut pas faire les deux ; trois issues décrites. **4.5.** Limiteur ajouté. **2.9.** ERB à 100 Hz : « dépasse l’octave » → environ une demi-octave.

- **3.7 et Annexe B.** Micros HF « de la MJC » : la MJC n’en a pas (0.6). **Annexe B métal.** Trois toms → deux, total et emprunts recomptés, condition du HPF 300–400 Hz rétablie. **Annexe C.** Valeurs d’ohms signalées comme non sourcées.

- **5.1bis, 6.3, 7.7, 7.10, 2.6, 1.3, 1.5.** Restes de l’ancien « HPF du retour » retirés ; « +3 dB punk/rock » aligné ; SIP limité à la balance ; candidats gate et EQ de la chaîne USB alignés sur la division de V32 ; errata réorganisés et contradiction du manuel sur le gate des bus notée ; phantom de la Palmer à vérifier.

- **5.2.** Piste ajoutée : le retour d’effet figure peut-être dans USB Sends (tableau 6.1) ; si oui, ducking de reverb natif possible.

- **3.8, 2.4, 2.1 (Gemini).** Entrées Aux et Tape sans HPF, gate, limiteur ni panoramique (tableau 6.1) : avertissement ajouté. Exception du Bus Parallel justifiée par le mécanisme. Comp 160 : « position BELOW à tenir » retiré de 2.1 et 4.4.

- **Non retenus (Gemini) :** sorties FlexMix de la 32SC (troisième fois — le tableau 3.1.4 liste 6 XLR et 4 jacks TRS) ; HPF des overheads abaissé à 60–70 Hz par défaut (déjà prévu comme réglage à l’oreille et au registre) ; « notch Q 4.0 » contre la sibilance (le cut étroit Q 3.0 ou plus est déjà en 3.7, et le Q maximal n’est pas chiffré par le manuel).

### CE QUI CHANGE PAR RAPPORT À LA V31

Audit de DeepSeek (huit remarques, surtout sur la refonte de 7.10), vérifié au manuel. Tout est retenu ; en vérifiant, deux trous plus larges sont apparus.

- **7.10, canal A.** « Mute sur tous les bus de sortie » → désaffectation du Main et du Bus Voix ; la touche Mute dépend du mode Link Aux Mutes (12.1.5). Contenu du Fat Channel de A selon le point de départ des retours. Division explicite : plugin = de-plosive, de-esser, limiteur ; gate, compresseur et EQ sur B (l’ancien texte mettait « EQ de correction » des deux côtés). Variante Post : plan de secours corrigé (réaffecter A). « En Pre, donc avant le fader » ramené à une inférence.

- **7.11 (Claude).** Points de départ Pre1, Pre2 et Post des FlexMix ajoutés (manuel 5.2.1) : le guide ne les mentionnait nulle part. Wedges en Pre1, in-ears en Pre2.

- **7.7 (Claude).** « Les départs Aux sont pris après le Fat Channel d’entrée » : faux en Pre1, réglage par défaut. Effet du retard d’entrée sur les retours mis à vérifier.

- **3.5.** « Tout ce qui se joue entre 40 et 80 Hz passe intact » → calcul chiffré, Butterworth supposé. **5.2.** « Le levier documenté » → « à essayer en premier ». **2.3.** Effet du Q en plateau : non documenté.

### CE QUI CHANGE PAR RAPPORT À LA V30

Deux audits croisés (DeepSeek, neuf remarques ; Gemini, six remarques, balayage systématique) et un audit de Claude. Tout vérifié au manuel, à l’addendum et au manuel UC Surface.

- **7.10, erreur bloquante (relevée par Gemini).** Canal A : Fat Channel complet **et** départ Pre — le traitement n’atteignait jamais l’ordinateur, et B, « sans Fat Channel actif », envoyait une voix non traitée. Courant : A en Pre, Fat Channel de la voix sur B ; variante Post décrite. Plan de secours mis à jour.

- **2.3, 5.2, 5.4, 5.6 (Claude).** Ancien texte V29 : « le Standard EQ n’a que des bandes en cloche ». Faux : le manuel UC Surface (3.3) documente Low Shelf et High Shelf. Les retours d’effet utilisent maintenant un plateau grave en atténuation.

- **3.5.** Justification du limiteur du clavier reformulée (registre 40–80 Hz), sans changer de valeur. **4.1.** Solar 69 High : « +3 dB » → **+1 à +2 dB** avec les Lewitt. **2.4.** Exception Bus Voix ajoutée à la règle des bus. **3.7.** Motif du Threshold -2 dB. **3.3.** DI et ampli ensemble : ne pas cumuler le cut à 60 Hz. **4.6.** FC-670 candidat à comparer. **3.8.** Lignes Gate ajoutées ; compresseur du playback en Auto. **6.4.** Valeur de ducking à relever. **3.6.** Flûte : Release Fast → **Medium**.

- **3.4 et 2.3 (Claude).** « Le manuel dit explicitement qu’il vise une guitare qui manque de présence » : le manuel ne le dit pas. « Hi Q sur la bande haute » : l’addendum ne précise pas la bande. **6.6.** Option Tube EQ inscrite, comme 2.3 l’annonçait. Huit passages à la mise en forme cassée réparés.

- **Non retenus :** sorties FlexMix de la 32SC (Gemini, deuxième fois — le tableau 3.1.4 liste 6 XLR et 4 jacks TRS en sorties, les entrées Aux sont dans le tableau des entrées) ; valeurs de ducking « 3 à 6 dB, au-delà le public croit à une panne » (DeepSeek, aucune source) ; HPF du clavier à 30 Hz (pas nécessaire, voir 3.5).

### CE QUI CHANGE PAR RAPPORT À LA V29

Audit de Gemini (gemini-3.5-flash), lancé directement depuis la session avec le guide, l’addendum et le mode d’emploi. Neuf remarques, vérifiées une à une.

- **7.4.** « Solo Isolate » retiré : la fonction n’apparaît ni dans le mode d’emploi ni dans le manuel UC Surface. Remplacé par le comportement documenté du solo (10.1) et l’avertissement sur le SIP.

- **3.2.** Fiche du PGA52 ajoutée : 0.6 y renvoyait, elle n’existait pas. Positions tirées du guide de l’utilisateur Shure ; « devant la peau de résonance » signalé comme usage non documenté par Shure. 0.6 mis à jour.

- **2.1, 2.6, 4.4.** Comp 160 : sur le dbx 160 d’origine, BELOW et ABOVE sont des voyants d’état du seuil (manuel UA). Ajouté comme inférence à vérifier ; la citation de l’addendum fournie par l’auditeur n’existe pas.

- **8.6 et Annexe, retard de sortie.** 170 ms sur la 32SC (manuel 13.7) ajouté.

- **7.10, Studio One.** Ancien chemin : « Song Setup → Audio Setup ». Corrigé, source tierce.

- **Non retenus :** 32SC à 6 sorties FlexMix seulement (faux : le tableau 3.1.4 liste 6 XLR et 4 jacks TRS) ; « 40 départs USB et non 32 » (le guide parle des 32 canaux de mixage, pas des départs USB) ; Release Fast de l’Everest au Master contraire à 2.4 (le tableau 2.4 concerne le limiteur) ; HPF voix à 120–150 Hz en punk et métal (aucune source, le passage cité du manuel ne le dit pas).

### CE QUI CHANGE PAR RAPPORT À LA V28

Second audit de DeepSeek (fichier reçu interrompu au point 9), vérifié au manuel PreSonus et par le calcul. En vérifiant le point 8, deux erreurs anciennes du guide sont apparues ; elles sont corrigées partout.

- **5.2 et propagations (2.5, 5.3, 6.4, 6.6, 7.10).** Ancienne prescription : compresseur sur le retour FX A, Key Source = voix lead. Le manuel réserve Key Source aux canaux d’entrée (6.8.3, 6.8.4) et classe les retours d’effet à part (tableau 6.1) : retiré. Voie ordinateur ajoutée, à tester. Titre de 5.2 : « avec sidechain ducking » supprimé.

- **5.2, 5.4, 5.6.** Anciennes valeurs : « HPF 300 Hz », « HPF 400 Hz », « HPF 350–400 Hz » sur les retours d’effet. Le tableau 6.1 ne donne pas de filtre passe-haut à ce type de canal : remplacé par une atténuation de la bande LOW, et le Vintage 3-Band EQ à vérifier.

- **3.1.** « C’est le seul cas où Attack 10 ms et Release Auto sont compatibles » : faux, la combinaison est compatible partout où elle figure. Rappel des libellés du Baxandall ajouté.

- **3.5 et 2.4.** Clavier : Release 100 ms → **150 ms**. Orgue/Rhodes : limiteur ajouté, 150 ms. Ligne du tableau 2.4 étendue aux claviers.

- **3.6.** Trompette : « Input Gain vers -15 dB » → méthode de 3.1 et 3.4 (correction de la V27 qui n’avait pas été propagée ici).

- **6.1 et 6.2.** Solar 69 High : +3 dB → **+1 à +2 dB**, cohérent avec 4.1 (overheads Lewitt).

- **4.4.** Calcul du test d’alignement reformulé : ancien texte « résidu sous -20 dB à 60 Hz » (réel : -19,8 dB) et « encoche » attribuée au résidu, alors que le résidu y est maximal.

- **Annexe B, reggae/dub.** Contradiction clavier mono / stéréo levée.

- **0.1 et 7.11.** Manuels Venu360 et PA2 retirés du projet ; mention mise à jour.

- **Non retenu :** point 6 (le manuel 12.3.4 liste bien les « Mixages Flex », sans restriction de mode).

### CE QUI CHANGE PAR RAPPORT À LA V27

Audit de DeepSeek (dix remarques, parties musicales), transmis par Louis depuis l’application DeepSeek, vérifié point par point.

- **2.1, FC-670.** Ancienne valeur : « Time Constant en position lente (5–6) », contredite par 4.2 et 6.5 (position 3). Position de référence courante : **3**. Échelle du Fairchild d’origine ajoutée, donnée comme inférence pour le FC-670. Correction trouvée en vérifiant ce point : le FC-670 était décrit comme « opto » (2.1, 2.8, 8.2, Annexe A) ; le Fairchild 670 est à lampes à pente variable. L’addendum PreSonus ne parle pas d’optique.

- **7.3, GEQ.** Ancienne règle : « coupures uniquement », contredite par le boost « salle morte » du tableau. Règle courante : coupures, avec cette seule exception.

- **2.4 et Partie 3, limiteurs.** Trois catégories ajoutées au tableau par extension du mécanisme existant (guitares, cuivres et bois ; synthé ; sources déjà mixées). Limiteur ajouté aux presets saxophone, flûte, synthé, vinyle et playback ; justification ajoutée à la table DJ.

- **7.7.** « multiplier par 2,9 ms » devient « 2,9 ms/m ».

- **6.4 et 4.1** — ducking de la musique par le MC, saturation et transitoires par l’ordinateur : pistes à tester, sans valeur.

- **Non retenu** : réduire la compression du Bus Voix en métal (le serrage fort y est un choix de style, déjà argumenté en 6.3).

### CE QUI CHANGE PAR RAPPORT À LA V26

Premier audit réalisé par une autre famille d’IA (Gemini, Google), appelée directement depuis la session avec le guide, l’addendum et le mode d’emploi StudioLive en pièces jointes. Huit remarques, vérifiées une à une au manuel, à l’addendum (illustration comprise) et par le calcul.

- **3.1, couple ORTF** — raisonnement inversé corrigé : en ORTF, les capsules sont *plus* écartées que les fixations, pas moins. Ancienne formulation : « l’écartement réel entre les capsules sera légèrement inférieur ». Calcul ajouté ; la valeur de 7–9 cm proposée par l’auditeur n’est pas reprise (elle suppose une distance pince–capsule non documentée).

- **3.1 et 3.4, Class-A FET** — ancienne mention : « Input Gain typiquement vers -18 dB », non sourcée. Remplacée par : partir de la valeur par défaut (-24 dB, manuel 6.5.3) et monter jusqu’à la réduction voulue au mètre. La valeur « vers 0 dB » proposée par l’auditeur n’est pas reprise (non sourcée non plus).

- **2.1, Tube CB** — Attack et Release sont des boutons continus (illustration de l’addendum 3.7) ; Fast/Medium/Slow précisés comme repères de course. Errata 2.6 : numérotation fausse dans le texte de l’addendum.

- **6.3, double grosse caisse** et **6.6, delay dans la reverb** — pistes ajoutées au statut « à tester », avec calcul pour la première et vérification console pour la seconde. **8.6, DM3** — le kick déclencheur doit aussi être dans les canaux 1–16.

- **Rejetés** : « la 32SC a 4 sorties de sous-groupe » — faux, le manuel 3.2.2 réserve ces sorties aux 32S, 32SX et 32, et le tableau 14.2.2 n’en donne aucune à la 32SC ; le guide était juste. « Baxandall High Cut non vérifiable » — lecture du panneau déjà consignée en 2.6 et confirmée visuellement par Louis.

### CE QUI CHANGE PAR RAPPORT À LA V25

Suite du second retour du même auditeur, vérifié point par point.

- **3.3 Basses** : le titre était collé à la fin du paragraphe précédent (défaut hérité de versions antérieures), donc absent de la table des matières. Rétabli comme titre de section ; table reconstruite.

- **Règle de renvoi au manuel** (bloc assistant) alignée sur l’usage réel : dans les Parties 0 à 7, « le manuel » désigne la documentation PreSonus ; tout autre document est nommé.

- **Registre 8.7** : la ligne du limiteur du Bus Parallel passe en BV ; ajout d’une ligne BV pour mesurer le plafond du de-esser voie A.

- **Non retenu** : un seuil chiffré a priori pour la voie A (« 3 dB ») — aucune source ne le donne ; il sera mesuré en balance virtuelle et inscrit en 7.10.

### CE QUI CHANGE PAR RAPPORT À LA V24

Suite d’un audit externe de la V24 (rédigé par un autre assistant ; le fichier reçu s’arrêtait au milieu de son point 5.6), vérifié point par point contre le guide, les manuels du projet et la FAQ Shure. Les points acceptés sont appliqués ; les points rejetés ne le sont pas.

**Structure.** L’historique quitte la tête du document pour cette section, afin qu’une recherche sur une ancienne valeur ne remonte plus le changelog avant la prescription. Table des matières reconstruite à partir de tous les titres. Statut « à tester » placé en tête de 4.4, de la voie C de 7.10 et de 7.11. Bloc assistant : règle de non-citation de l’historique, convention de renvoi au manuel, liste de ce que le guide ne couvre pas. Les numéros de section, 5.1bis compris, sont volontairement conservés : ils sont cités dans d’autres discussions et fiches.

**Valeurs modifiées.**

- **4.4, limiteur du Bus Parallel.** Ancienne valeur : Release 50 ms. Valeur courante : **150 ms** (règle du grave, 2.4).

- **4.4, test d’alignement.** Ancien protocole : kick seul, critère « disparaître quasi complètement ». Courant : **source large bande, critère chiffré -20 dB** (calcul en 4.4).

- **3.1, HPF des overheads.** Valeur de départ inchangée (80 Hz) ; ajout de l’option 60–70 Hz si le floor tom manque de corps, et de l’estimation d’atténuation à 60 Hz.

**Nuances.** SM57/SM58 (1.5) aligné sur la FAQ Shure. Bande critique (2.9) précisée selon la fréquence. Isolation de l’i5 (0.3) requalifiée en retour d’usage. Voie A de 7.10 : « suffisant pour beaucoup de voix » retiré, critère d’oreille ajouté. Projection des 16 bus sur les sorties physiques (1.4). Point de contrôle de double affectation (4.6). Beta58 : renvois croisés Annexe B ↔ Annexe C.

**Points de l’audit rejetés.** Conflit 1.3 / 4.6 (inexistant). Renvoi circulaire vers 8.7 (inexistant). Transformateur différent sur le SM58 (non confirmé par Shure). Réduction de la fiche HD96 (console de formation de Louis). Tableaux en liste et nuance « mur avec mémoire » du limiteur (formulation).
