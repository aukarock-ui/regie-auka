# Retour — 23 novembre 2026 — Approches musicales par style (Partie 6)

Objet : donner une intention musicale aux scènes de la Partie 6 du Guide V35 (6.1 à 6.7), et proposer deux scènes absentes (folk, fusion latine), à partir d'approches **publiées et attribuables** d'ingénieurs façade et d'auteurs reconnus. À intégrer depuis le projet « Mix Live » (skill `maj-guide-mixage`). Rien n'a été modifié dans le guide local.

## Comment lire ce retour

- **Ce que disent les sources** : résumés en français, citations de moins de quinze mots, une par source au plus. Chaque source a été ouverte et lue le 23/11/2026 ; ce qu'elle ne dit pas n'est pas mis à son compte.
- **Traduction 32SC** : tout est **hors guide, à valider à l'oreille**. Aucune valeur n'est inventée. Les seuls chiffres sont ceux du guide V35 (section citée) ou ceux de la source (désignée). Quand rien ne chiffre, une méthode et un critère d'écoute.
- **Limite commune** : presque toutes les sources sont des tournées d'aréna ou de festival avec du matériel bien plus lourd qu'une 32SC. On en retient l'intention et le geste, pas le matériel.
- **Ce retour porte sur la console seulement.** Plusieurs sources parlent d'égaliser le système (Burton, Chirnside) : ces passages sont signalés, mais leur traitement relève de la discussion calage.

## Faits console relevés en vérifiant (manuel 32SC, à reporter dans le guide)

1. **Les touches User Function n'existent pas sur la 32SC.** Le manuel (12.1.2, p. 109) les décrit (groupes de mutes 1–8, Tap Tempo par effet, Quick Scenes), puis précise qu'elles manquent sur la 32SC et la 16 à cause de leur format compact. Conséquence pour le dub : les drop-outs se font aux touches Mute des canaux ou par **groupes Filter DCA** (manuel 2.2.5 et 4.3, p. 25), et non par des mutes groupés sur touche.
2. **La touche Tap de la section Master Control existe** (manuel 9.1, p. 79–80). Avec plusieurs delays chargés, on choisit celui qu'elle pilote par **Tap Assign** dans l'éditeur. La recommandation « au TAP » du guide tient donc, mais avec une seule touche pour B et D : choisir le delay assigné avant le morceau.
3. **Pas de phaser ni de pitch shifter dans le rack** : neuf types seulement (guide 5.1bis, manuel 9.1.2). Plusieurs sources (dub, reggae, latin) s'en servent. Rien en natif : chorus et flanger ne les remplacent pas. La seule voie est l'ordinateur (guide 7.10).

---

## Référence générale

**Dave Swallow, *Live Audio: The Art of Mixing a Show*, Focal Press, Burlington MA / Oxford, 2011 (ISBN 9780240816043).** Existence et plan vérifiés dans les catalogues de bibliothèque (Texas A&M, Max Planck) : deux parties, « Pre Show » et « Show Day », avec les chapitres 14 « Soundcheck », 15 « The Mix » et 16 « The Show ». **Le contenu n'a pas pu être lu** (pas d'aperçu accessible). Rien ne lui est attribué ici. À consulter si Louis peut l'emprunter : c'est l'ouvrage général le plus proche de sa pratique.

**Ken « Pooch » Van Druten** — Tom Flint, « Ken 'Pooch' Van Druten: FOH Mix Engineer », *Sound On Sound*, avril 2020, https://www.soundonsound.com/people/ken-pooch-van-druten-foh-mix-engineer. Façade d'Iron Maiden, Linkin Park, Jay-Z, Justin Bieber. Trois idées valables pour tous les styles :
- la voix d'abord : il passe les premières heures sur les voix, place le reste puis l'« oublie » ;
- compression parallèle sur le bus batterie (proportion fixe) et parfois sur la voix (proportion variable) ;
- il joue la dynamique du morceau à la sortie : sur Linkin Park, façade baissée de 3 à 6 dB dans les couplets, remontée à 0 sur le premier temps du refrain.

---

## 6.1 PUNK

### Intention
Un mur d'énergie à niveau constant, où la voix reste devant sans dureté. La dynamique vient des gestes (une guitare poussée sur un riff mélodique), pas de nuances. Peu d'effets : le son est droit.

### Ce que disent les sources
- **Kevin Lemoine (Green Day)** — « Kevin Lemoine: FOH Engineer — On Tour With Green Day », *Sound On Sound*, novembre 2013 (pas de signature lisible), https://www.soundonsound.com/people/kevin-lemoine-foh-engineer. Le mix rock idéal selon lui : batterie et guitares solides, voix claire, puissant sans dureté. Il garde la main sur les faders pour de petits ajustements permanents, selon l'instrument qui doit passer devant. Effets rares : un delay de temps en temps sur la voix, de la reverb en extérieur, une plaque sur la batterie. Gates sur la batterie.
- **Kyle Chirnside (Fall Out Boy)** — Keith Clark, « Tour Profile: Fall Out Boy », *Mix*, 1er juillet 2006, https://www.mixonline.com/live-sound/tour-profile-fall-out-boy-367900. Le style est, selon lui, à peu près « un seul niveau tout le temps ». Il crée la dynamique en poussant une guitare ou en la panoramiquant pour un riff mélodique. Le compresseur de la voix lead la tient au-dessus du mix sans qu'il ait à monter le fader. Gates et compression réduits au minimum. Une touche de reverb sur la voix. Niveau façade 105–107 dB.
- **Jonah Kay (Four Year Strong)** — Mix Staff, « Mixing Four Year Strong on the Road », *Mix*, 5 mai 2026, https://www.mixonline.com/live-sound/tours/four-year-strong-hits-the-road. Il vise la constance d'une salle à l'autre, avec sa propre console. Voix doublée sur deux canaux, l'un propre, l'autre saturé. Guitares stéréo pour la largeur, mais un passage en mono sur les couplets à une seule guitare, pour la séparation.

### Traduction 32SC — hors guide, à valider à l'oreille
**Voix lead — doublage propre/saturé (geste Kay)** : copier le canal voix (copier/coller du canal, manuel 6.1.2) sur un canal libre alimenté par la même entrée. Second canal : compresseur plus dur, EQ plus agressif. Le doser sous le canal propre jusqu'à ce que la voix gagne en grain sans perdre ses consonnes. Si deux canaux sur la même entrée créent un filtrage en peigne (guide 2.9), réduire le second ou l'abandonner. Le Fat Channel n'a pas de saturation déclarée : le grain vient du modèle de compresseur (Brit Comp ou FET, guide 2.8), à essayer.
**Voix lead — compresseur** : la scène 6.1 (Tube CB, 4:1, réduction 4–6 dB) va dans le sens de Chirnside, le compresseur remplace le fader. Critère : la voix reste au-dessus du mur sans qu'on touche le fader dans un couplet.
**Guitares — dynamique par le geste** : pas de réglage, un geste. Pousser d'un cran la guitare qui joue le riff mélodique, la remettre ensuite (Chirnside). Si les guitares sont en stéréo, les rapprocher du centre sur un couplet à guitare seule (Kay).
**Bus Drums** : 6.1 inchangée.
**FX** : 6.1 va déjà dans le sens des trois sources (peu de reverb). Ajout possible : un delay ponctuel sur une fin de phrase, envoyé à la main, pas en permanence (Lemoine).

### Désaccords
- Aucune source ne donne de réglage de compresseur ou d'EQ : les valeurs de 6.1 restent celles du guide, sans appui extérieur.
- Chirnside et Kay viennent du pop-punk et du hardcore mélodique, Lemoine du punk-rock de stade. Aucune source sur le punk de salle associative (Louis) n'a été trouvée.

---

## 6.2 ROCK

### Intention
La voix d'abord, puis une section rythmique qui a de l'impact. Chaque musicien doit être entendu, avec l'accent sur celui qui prend le solo. La dynamique du morceau (couplet, refrain) se joue au fader, pas seulement dans les compresseurs.

### Ce que disent les sources
- **Pooch Van Druten**, *SOS*, avril 2020 (voir Référence générale) : la voix d'abord ; sur un groupe comme Iron Maiden, chaque musicien doit être entendu avec l'accent sur les solos ; la façade baissée dans les couplets et remontée au refrain.
- **Kevin Lemoine**, *SOS*, novembre 2013 (voir 6.1) : batterie et guitares solides, voix claire, puissance sans dureté, petits mouvements de fader continus.
- **Clive Young, « Mixing The Iron Maiden 'Legacy Of The Beast' Tour, Part 2 »**, *Mix*, 28 mars 2023, https://www.mixonline.com/live-sound/tours/mixing-iron-maiden-tour-part-2 : la voix est l'élément le plus fort, puis la basse. Guitares panoramiquées selon leur place sur scène. À chaque solo, une scène ramène le soliste au centre, la suivante le remet à sa place.

### Traduction 32SC — hors guide, à valider à l'oreille
**Voix — hiérarchie** : régler la voix lead en premier, groupe en train de jouer, avant d'équilibrer le reste (Pooch). Critère : chaque mot compris depuis le fond de salle.
**Panoramique des guitares** : selon la place sur scène, sans extrêmes (chez Iron Maiden, Dave Murray est à droite mais pas à fond). Critère : depuis un côté de la salle, aucune guitare ne disparaît.
**Solos** : la 32SC n'a pas de Quick Scenes sur touche (manuel 12.1.2). Le geste se fait à la main : fader du soliste un cran plus haut, éventuellement panoramique ramené vers le centre, puis retour à la position d'origine.
**Dynamique couplet/refrain (geste Pooch)** : sur la 32SC, au fader Main. Pooch donne 3 à 6 dB : ce sont **ses** chiffres, en aréna. À essayer d'abord sur un seul morceau, en vérifiant que le limiteur Master (5.1) n'est pas déjà en action au refrain, sinon le geste ne s'entend pas.
**Bus Parallel** : 6.2 inchangée ; la compression parallèle de batterie est la pratique de Pooch, ce qui conforte le bus 4.4.

### Désaccords
- Pooch rattache la gestion du sub au processeur du système, pas au mix : c'est la discussion calage.
- Le guide ne parle pas de mouvement de fader Main dans 6.2. C'est un ajout, pas une contradiction.

---

## 6.3 MÉTAL

### Intention
Un bas puissant, un kick qui claque par-dessus, des guitares épaisses mais tenues hors de la zone qui fatigue l'oreille, une voix qui perce. Peu d'effets. L'EQ se fait plutôt sur les groupes que sur chaque source.

### Ce que disent les sources
- **« Big Mick » Hughes (Metallica)** — Sarah Benzuly, « Tour Profile: Metallica », *Mix*, 1er octobre 2003, https://www.mixonline.com/live-sound/tour-profile-metallica-367735. Il préfère le grave à l'aigu. Il évite la zone d'environ 1,8 à 4 kHz et y calme les guitares, en renforçant plutôt les zones moins agressives. Aucune EQ sur la guitare de Hetfield : « Absolutely no EQ at all. None » (« Aucune EQ, aucune »). Pas d'EQ non plus sur sa voix : les huit voix vont dans deux sous-groupes, égalisés au niveau du groupe. Gates des toms et du kick déclenchés par des capteurs collés sur les fûts. Voix gatée à cause des réflexions de scène. Pas de samples.
- **Iron Maiden** — *Mix*, 28 mars 2023 (voir 6.2) : voix devant, puis basse. Toms et kick gatés par capteurs, pas par le seuil du signal audio.
- **J.P. Huff (Pierce the Veil)** — Mix Staff, « FOH Engineer on Stem Mixing and Compatibility », *Mix*, 5 novembre 2026, https://www.mixonline.com/live-sound/foh-engineer-on-stem-mixing-and-compatibility (article de marque, console SSL). Structure par stems : voix, kick, caisse claire, batterie, batterie parallèle, batterie parallèle saturée, cymbales, toms. Guitares en mono jusqu'au stem. Micros public alignés dans le temps et compressés par le groupe, pour qu'ils remontent quand le groupe s'arrête.

### Traduction 32SC — hors guide, à valider à l'oreille
**Guitares — EQ** : essayer d'abord **sans EQ de canal** (EQ en bypass), comme Big Mick, en travaillant le placement micro. N'égaliser qu'au **Bus Instru**. Méthode pour la zone dure : sur l'Alpine du Bus Instru, bande Mid en cloche, gain monté de quelques décibels, balayer entre 1,8 et 4 kHz (la zone que cite Big Mick) jusqu'à l'endroit qui fatigue le plus, puis passer en coupure. Critère : après 20 minutes, les guitares restent épaisses sans piquer.
**Voix — EQ au bus** : 6.3 égalise déjà au Bus Voix, comme Big Mick. Il conforte la structure du guide.
**Gates toms et kick par capteur** : pas d'entrée trigger sur la 32SC. Piste : si le batteur a un capteur dont la sortie est un signal audio, le patcher sur une entrée et s'en servir comme **Key Source** du gate du tom ou du kick (guide 2.5, canaux d'entrée uniquement). Rien n'est documenté pour ce montage ; à tester en balance virtuelle (7.12) avant un concert.
**Micro d'ambiance et public** : à tester seulement si un micro public existe. Compresseur du canal ambiance avec **Key Source** = kick, pour que l'ambiance recule quand le groupe joue (Huff). Huff compresse avec tout le groupe ; la 32SC ne prend qu'un canal en Key Source (2.5). Le kick est le meilleur représentant disponible.
**Bus Parallel** : 6.3 inchangée. Huff utilise aussi une batterie parallèle saturée ; le FET en position All (guide 4.4, « jamais testé ») va dans ce sens.

### Désaccords
- **Big Mick : pas d'EQ sur la voix lead. Guide 6.3 : H-Mid +3 dB au Bus Voix** pour percer le mur. Les deux tiennent si l'EQ reste au bus, mais Big Mick fuit la zone 1,8–4 kHz pour les guitares, pas pour la voix. La voix du guide est poussée à 4,8 kHz, juste au-dessus. À comparer à l'oreille.
- **HPF guitares à 100 Hz (6.3)** : aucune source ne le chiffre. Big Mick n'égalise pas ses guitares et vante le grave. À réécouter : le HPF peut retirer le poids que Big Mick cherche.
- Les gates déclenchés par capteur (Metallica, Iron Maiden) sont l'option des deux tournées citées. Le guide ne gate qu'au seuil audio ; la piste Key Source ci-dessus reste à tester.

---

## 6.4 HIP-HOP

### Intention
La voix d'abord, toujours : chaque mot compris dès le premier, sans exception. Ensuite le grave, abondant mais égal jusqu'à l'aigu. Les effets de voix font partie du morceau et se recréent comme sur le disque.

### Ce que disent les sources
- **Phil Strong (Kanye West)** — Ray Ellis, « Tour Profile: Kanye West », *Mix*, 1er février 2006, https://www.mixonline.com/live-sound/tour-profile-kanye-west-367872. La voix est l'instrument principal et le mix se construit autour d'elle. Compression lampe transparente (Summit TLA-50) sur les voix et la table DJ : la voix doit ressortir tout en restant tenue. Delay et pitch bend ponctuels sur la voix. Chaque concert est enregistré et réécouté avec les artistes. Le retour DJ alimente aussi le casque du percussionniste.
- **Demetrius Moore (Drake)** — Ben Rogerson, MusicRadar, 6 novembre 2025, https://www.musicradar.com/artists/to-quote-prince-if-the-first-words-out-of-an-artists-mouth-when-they-hit-the-stage-arent-heard-youre-a-horrible-engineer-drakes-live-sound-engineer-on-why-he-had-to-be-at-the-top-of-his-game-from-first-song-to-last-on-his-recent-european-tour. Il cite Prince : si les premiers mots ne s'entendent pas, l'ingénieur a échoué. Il adapte le mix au morceau : intime en R&B, lourd en grave sur le rap, plus dansant ensuite. Sur le titre d'ouverture, il recrée l'effet du disque avec une chaîne gate inversé → reverb → delay. Il parle de sa console comme d'un instrument.

### Traduction 32SC — hors guide, à valider à l'oreille
**Voix — premier mot** : avant le set, faire parler le MC au micro à son niveau réel de rap, pas en parlant. Régler gain et compresseur sur ce niveau. Critère : la première phrase du set est comprise sans geste de fader (Moore).
**Voix — compresseur** : 6.4 (Tube CB, Attack et Release Slow) va dans le sens de Strong, qui veut une compression qui tient sans s'entendre. Strong utilise un compresseur optique à lampe : sur la 32SC, aucun modèle n'est décrit comme opto (guide 2.1). Le Tube CB reste le plus proche dans l'esprit, sans équivalence affirmée.
**Effets du disque** : le gate inversé n'existe pas dans le rack (5.1bis). Voie ordinateur (7.10) seulement, et seulement si l'artiste l'exige. Sinon, demander le titre et le moment, et remplacer par un delay calé au TAP sur cette phrase.
**Grave** : Strong et Moore parlent du grave de système. Sur la console, seul le niveau du canal table DJ ou playback relève de cette discussion. Le reste va au calage.
**Enregistrement du concert** : l'enregistreur SD 34 pistes (manuel 2.2.6) permet la réécoute de Strong et la balance virtuelle (7.12).

### Désaccords
- Aucun sur l'intention : le guide (« l'intelligibilité du texte prime sur tout ») et les deux sources disent la même chose.
- Moore insiste sur la recréation des effets du disque ; 6.4 les réduit (reverb courte, delay ternaire). Écart d'intention à trancher selon l'artiste.

---

## 6.5 REGGAE

### Intention
La section rythmique devant, la basse pleine, et un mix qui bouge en permanence. Les deux sources reggae « dubbent » une partie de chaque concert : en live, le reggae et le dub ne sont pas étanches.

### Ce que disent les sources
- **Christian Cowlin (The Wailers)** — « Interview with Christian Cowlin: FOH & Sound Engineer for The Wailers », site officiel thewailers.com, 26 février 2023, https://www.thewailers.com/?p=4893 (interviewer non nommé). Il dit mixer au ressenti, par connaissance de la musique, sans méthode d'équilibre. Il garde quatre reverbs et quatre delays fixes : reverb caisse claire statique, reverb caisse claire « sweep » pour les dubs, reverb guitares/claviers, reverb voix ; delay caisse claire pour les dubs, delay voix au tap, slapback voix, delay « à attraper » pour les dubs (voix surtout). Placement précis du micro de caisse claire pour équilibrer peau frappée et cross-stick. Niveaux de guitare et de clavier repris à chaque morceau.
- **Michael Versteegt (SOJA)** — Keith Young, « Versteegt on Mixing Live Reggae and More », *Mix*, 22 mars 2018, https://www.mixonline.com/live-sound/versteegt-on-mixing-live-reggae-and-more. Phasers, reverbs et delays sont ses effets de base. D'habitude une grande reverb sur la caisse claire. Phaser sur les reverbs et sur le charleston, à la manière du dub. Delay joué sur une pédale à bandes pour la régénération à la main. Les faders ne restent jamais à plat. Il dubbe la plupart des soirs.

### Traduction 32SC — hors guide, à valider à l'oreille
**Caisse claire — micro** : placer le micro de caisse claire pour équilibrer peau et cross-stick (Cowlin). Critère : le rimshot du one-drop s'entend aussi clairement que la frappe pleine, sans monter le fader.
**FX — les huit effets de Cowlin sur quatre processeurs** : impossible tels quels (4 slots, 5.1bis). Répartition proposée, à juger : FX A reverb voix (guide 5.2) ; FX C reverb caisse claire, plus grande que la reverb batterie de 5.4 (Versteegt), départ depuis la caisse claire seule ; FX B Stereo Delay voix au TAP (5.3) ; FX D Ping Pong en delay « à attraper » pour les dubs (6.6). Pas de slapback dédié : en natif, un des deux temps du Stereo Delay court, à essayer.
**Phaser sur reverb et charleston (Versteegt)** : pas de phaser dans le rack. Voie ordinateur (7.10) ou abandon.
**Faders** : la scène est un point de départ, pas un état à tenir. Reprendre guitare et clavier à chaque morceau (Cowlin).

### Désaccords
- **6.5 est une scène statique avec peu d'effets.** Les deux sources dubbent en direct pendant les concerts de reggae. Proposition : 6.5 renvoie aux gestes de 6.6 pour les fins de morceau et les intros.
- Versteegt : « grande reverb sur la caisse claire ». 6.5 ne donne pas de reverb batterie propre (5.4 par défaut, espace court et dense). Écart d'esthétique à trancher à l'oreille.

---

## 6.6 DUB

### Intention
La console devient l'instrument. Le rythme (basse et batterie) est la fondation ; les autres parties entrent et sortent du mix comme des apparitions ; l'écho est rythmique, la reverb est le lien qui recolle les fragments. On mixe en jouant, en temps réel.

### Ce que disent les sources
- **Michael E. Veal, *Dub: Soundscapes and Shattered Songs in Jamaican Reggae*, Wesleyan University Press, Middletown CT, 2007 (ISBN 9780819565723).** Existence et titre vérifiés (fiches éditeur et libraire). **Le texte du livre n'a pas pu être lu** : rien n'est cité à une page. Ce qui suit vient de son interview.
- **Michael Veal** — Wills Glasspiegel, « Interview: Michael Veal », Afropop Worldwide, 26 mai 2010, https://afropop.org/articles/interview-michael-veal. Veal y résume la thèse du livre. Faire sortir et rentrer des parties est l'un des éléments clés du dub. Les parties deviennent des fantômes qui volent dans le mix. La reverb est « like the glue on the mix » (« comme la colle du mix ») : elle tient les fragments ensemble et donne l'espace. L'écho est d'abord un procédé rythmique. Filtres, reverb et écho occupent l'espace que le rocksteady avait libéré. Pas de grand dub sans un grand rythme. King Tubby, électronicien, modifiait ses propres circuits.
- **Andrea Terrano, « Dub Mixing — What Dub Mixing Is & How To Do It »**, *Sound On Sound*, juillet 2007, https://www.soundonsound.com/techniques/dub-mixing. La basse est haute dans le mix ; la voix est secondaire, souvent coupée. Boucle de réinjection : envoyer vers un delay (environ 0,7 s dans son exemple), monter le feedback jusqu'à quatre ou cinq répétitions, faire revenir le delay sur une tranche dotée d'un départ aux, et monter ce départ vers le delay lui-même ; couper la source quand les échos montent. Temps calé en triolets. Un EQ ou un filtre sur le retour enlève l'aigu de la boucle. Un limiteur sur le retour empêche l'écho de saturer. Un gate sur un retour de reverb ou de delay, seuil réglé pour hacher l'effet. « Room shot » : départ reverb ouvert sur une seule frappe de caisse claire, puis refermé. Il préfère la console analogique et juge que changer de page sur une numérique casse le jeu.
- **Mad Professor** — Andrea Terrano, « Mad Professor — Mixing Dub », *Sound On Sound*, août 2007, https://www.soundonsound.com/people/mad-professor. Sa reverb occupe toujours le premier aux stéréo ; delays dans chaque pièce ; phasers câblés à la console ; boucles de réinjection montées sur les départs aux. Il dit aborder chaque projet différemment.
- **Sean Williams, « Tubby's Dub Style: The Live Art of Record Production »**, dans S. Frith et S. Zagorski-Thomas (dir.), *The Art of Record Production*, Ashgate, 2012, ch. 15, p. 235–246. Existence vérifiée (portail de recherche de l'Université d'Édimbourg). Seul le résumé a été lu : le style de Tubby tient moins à des « armes secrètes » qu'à la rencontre entre son savoir technique et les limites de son matériel. Pas de geste précis à en tirer sans le texte.
- **Adrian Sherwood** — Larry Crane, « Adrian Sherwood: Pay It All Back », *Tape Op* n° 136, avril-mai 2020, https://tapeop.com/interviews/136/adrian-sherwood. Partie lisible seulement (le reste est payant) : souvenir de ses débuts en sonorisation avec une reverb à ressort, un Space Echo et un petit effet sur la caisse claire et la voix lead. Trop mince pour fonder un geste : cité pour mémoire.

### Traduction 32SC — hors guide, à valider à l'oreille
**Drop-outs (Veal, Terrano)** : le geste manque dans 6.6. Sur la 32SC, pas de mute groups sur touche (manuel 12.1.2). Deux voies : les touches Mute des canaux, ou un **groupe Filter DCA** par famille (batterie, cuivres, guitare/claviers ; manuel 4.3, p. 25), fader DCA descendu et remonté à la main. Préparer avant le set une couche de faders où tout ce qu'on joue est sous la main, pour ne pas changer de page pendant le morceau (Terrano). Critère : basse et batterie ne sortent presque jamais ; ce qui sort revient sur un temps fort.
**Boucle de réinjection par le retour (Terrano)** : c'est la piste déjà inscrite dans 6.6 (tableau 6.1 : les retours d'effet ont des départs vers les FlexMix ; un départ vers un bus d'effet n'est pas documenté). **Toujours à vérifier sur la console.** S'il existe, partir d'un départ du retour vers son propre delay à zéro et monter très lentement. Repérer le point d'emballement comme le demande la précaution de 6.6.
**Assombrissement des répétitions** : Terrano filtre l'aigu dans la boucle. Le Fb LPF de 6.6 et 5.1bis le fait dans l'effet, ce qui conforte le guide.
**Limiteur sur le retour d'écho (Terrano)** : la présence d'un limiteur sur le Fat Channel d'un retour d'effet n'est pas établie par le guide (tableau 6.1). À vérifier en même temps que le Key Source (5.2).
**Gate « hachoir » sur le retour (Terrano)** : idem, présence d'un gate sur un retour d'effet à vérifier. Sinon, voie 7.10.
**Room shot (Terrano)** : départ FX C (ou A) ouvert d'un coup sur une frappe de caisse claire, puis refermé. Pas de réglage : un geste, à répéter en balance virtuelle (7.12).
**Delay — temps** : 6.6 dit TAP ; Terrano dit triolets. Compatible : battre le TAP, puis comparer avec un temps ternaire. Critère : les répétitions tombent dans le skank.
**Phaser (Mad Professor, Versteegt)** : pas dans le rack ; voie 7.10.

### Désaccords
- **Les drop-outs sont l'élément clé pour Veal et Terrano ; 6.6 n'en parle pas** et ne traite que les effets. Lacune d'intention, la plus importante de ce retour.
- **Terrano compte sur la console analogique** (une fonction, un bouton). La 32SC demande de préparer une couche de faders : condition pratique à ajouter à 6.6.
- Terrano chiffre 0,7 s et quatre ou cinq répétitions ; 6.6 chiffre le feedback en pourcentage (55–65 %). Mesures différentes, aucune contradiction démontrée : compter les répétitions audibles est un critère d'écoute utile pour régler le pourcentage.

---

## 6.7 TECHNO LIVE

### Intention
Le son vient déjà fini de la scène : l'artiste a fait ses choix de traitement. La façade garde la maîtrise du grave morceau par morceau et ajoute peu de dynamique. Les effets « de régie », quand il y en a, se jouent comme en dub.

**Aucune source sur une techno live au sens strict n'a été trouvée.** Les deux sources ci-dessous concernent des formations électroniques jouées en live (The Prodigy, New Order) : c'est le plus proche qui ait pu être vérifié.

### Ce que disent les sources
- **Jon Burton (The Prodigy)** — Sam Inglis, « Jon Burton: Mixing & Recording The Prodigy Live », *Sound On Sound*, octobre 2010, https://www.soundonsound.com/people/jon-burton-mixing-recording-prodigy-live. Faders de canaux à 0 dB et groupes VCA par musicien, qu'il monte quand le groupe arrive sur scène. Les échos et spin delays de style dub sur les voix partent des canaux. Ils doivent être réglés un mot en avance à cause du temps de vol entre scène et régie. Le delay dub sert sur environ la moitié des titres. Deux bons compresseurs sur les claviers. Il égalise le système plutôt que les canaux, et monte surtout le grave (relève du calage).
- **Shan Hira (FOH) et Paul Rattcliff (orchestre), New Order** — Tom Flint, « Mixing New Order Live », *Sound On Sound*, octobre 2017, https://www.soundonsound.com/techniques/mixing-new-order-live. Les synthés arrivent en **un stem stéréo de basse et un stem stéréo pour le reste**, pour que la façade et les retours maîtrisent le grave morceau par morceau. Les effets sont faits à la source, pas à la console. Très peu de traitement dynamique. Voix au-dessus, effets ensuite.

### Traduction 32SC — hors guide, à valider à l'oreille
**Patch — demander un stem basse séparé (Hira)** : dans la fiche groupe (annexe D), demander au minimum une sortie stéréo basse distincte du reste. Cela correspond au cas « sorties séparées » de 6.7. Critère : on peut baisser le grave d'un morceau sans toucher au reste.
**Fader d'arrivée (Burton)** : canaux à 0 dB et un groupe **Filter DCA** (manuel 4.3) par machine ou par musicien, descendu au départ et monté à l'arrivée de l'artiste. Critère : la mise en place se fait avec un seul fader par musicien.
**Compression des stems** : 6.7 met Brit Comp 4–5 dB au Bus Drums et FC-670 3–4 dB au Bus Instru. Hira n'en met presque pas et Burton seulement sur les claviers. Essai proposé : les deux compresseurs de bus en bypass, comparer avec et sans. Critère : si le kick perd de l'impact ou si les stems pompent avec compression, la retirer.
**Delay dub joué (Burton)** : FX D Ping Pong prêt comme en 6.6, départs depuis la voix ou un stem lead. Burton règle l'écho un mot en avance à cause du temps de vol : c'est sa situation de grande distance. À la MJC, caler au TAP et écouter depuis la régie.

### Désaccords
- **6.7 compresse les stems (Bus Drums 4–5 dB, Bus Instru 3–4 dB). Hira n'en met presque pas** et Burton très peu. Écart réel : des stems déjà finis par l'artiste risquent d'être compressés deux fois.
- Burton égalise le système et non les canaux : ce n'est pas un réglage console, à renvoyer à la discussion calage.

---

## PROPOSITION 6.8 — FOLK (absente du guide)

### Intention
Un mix naturel où chaque instrument a sa zone de fréquences. Le gain se joue juste sous le larsen : tout le métier est là. Peu de compression. Les voix et harmonies devant.

### Ce que disent les sources
- **Ben Hines (Yonder Mountain String Band)** — Strother Bullins, « Tour Profile: Yonder Mountain String Band », *Mix*, 1er avril 2005, https://www.mixonline.com/live-sound/tour-profile-yonder-mountain-string-band-371884. Son travail : aller chercher le niveau jusqu'aux derniers pour cent avant le larsen, sur un groupe sans volume de scène. Pas de compression dure. Égaliseurs graphiques sur les guitares, coupures à 160 et 400 Hz, 400 Hz aussi sur la mandoline. Il préfère ajouter des fréquences, et vise quatre zones de fréquences pour quatre instruments. Retours sans wedges (in-ears).
- **Chris Korff, « Mixing Acoustic Guitars Live — Strum and Twang »**, *Sound On Sound*, juin 2013, https://www.soundonsound.com/techniques/mixing-acoustic-guitars-live. Piezo : DI, puis coupures de médiums souvent profondes ; avec balance, monter une bande médium, balayer pour trouver le « nasillard » et couper, en général entre 800 Hz et 3 kHz. Sans balance, partir à plat et creuser progressivement. En groupe avec basse et kick, amincir le grave de la guitare. Compression piezo rapide, ratio élevé, réduction qui oscille entre 0 et environ 3 dB. Compression de dynamique douce (ratio autour de 1,5:1, attaque et relâchement moyens à longs). Attention : la compression peut déclencher le larsen. Ne pas demander au musicien de changer l'EQ de son préampli.
- **Mark Kennedy (Robert Plant & Alison Krauss)** — Clive Young, *Mix*, 17 août 2023, https://www.mixonline.com/live-sound/tours/robert-plant-alison-krauss-raise-the-roof-on-the-road-part-2. Surtout des retours et des micros. Fait utile : Alison Krauss joue son violon dans son micro de chant, sans DI.

### Traduction 32SC — hors guide, à valider à l'oreille
**Micro et placement** : guide 3.4 (guitare acoustique). Si le violon passe dans le micro de chant (cas Krauss), ne pas creuser l'EQ de la voix au point de perdre le violon.
**Gain — juste sous le larsen (Hines)** : monter le gain, façade ouverte, jusqu'au premier signe d'accrochage, puis redescendre jusqu'à ce qu'il disparaisse franchement. Méthode larsen du guide (7.11) sur les retours.
**HPF guitare acoustique** : avec basse et kick en façade, monter le HPF jusqu'à ce que le grave cesse d'encombrer la voix (Korff). Solo ou duo : le laisser bas.
**EQ piezo (Korff)** : bande Mid en cloche, gain monté, balayage 800 Hz – 3 kHz, puis coupure là où ça nasille. Profondeur à l'oreille : Korff dit qu'elle est souvent forte, sans en faire une valeur de départ.
**EQ d'ensemble (Hines)** : chercher une zone par instrument, dans l'esprit de « quatre instruments, quatre zones ». Sur la 32SC, avec l'EQ de canal, pas le GEQ (réservé aux sorties, 7.3).
**Compresseur** : Standard Compressor doux sur la guitare (Korff : ratio autour de 1,5:1, temps moyens à longs). Surveiller le larsen après compression.
**Bus Parallel** : -∞.
**FX** : aucune source n'en parle. Point de départ neutre : FX A voix (5.2), dosé aux départs.

### Désaccords
- **Hines préfère ajouter ; Korff creuse (piezo).** Pas incompatible : Korff parle des piezos, Hines d'instruments déjà bien captés à gain élevé.

---

## PROPOSITION 6.9 — FUSION LATINE (absente du guide)

### Intention
Les percussions sont un instrument à part entière, réparties dans l'image. Elles soutiennent la voix et non la batterie. Cuivres présents et larges. Mix en trois dimensions : rien ne s'empile, tout bouge en permanence.

### Ce que disent les sources
- **Patrick Murray (Ozomatli)** — Heather Johnson, « Tour Profile: Ozomatli », *Mix*, 1er janvier 2008, https://www.mixonline.com/live-sound/tour-profile-ozomatli-368053. Neuf musiciens et beaucoup de percussions : il veut un mix en trois dimensions, sans empilement. Approche directe, peu d'effets. Compresseurs sur la voix lead, les cuivres et la basse. Rap sur canaux séparés, trois chœurs groupés en un groupe stéréo. Courte reverb « hall » sur les cuivres. Cuivres légèrement désaccordés (±4 cents) avec un peu de delay pour la largeur. Rarement « set and forget » (« réglé puis oublié »).
- **Victor Fernandez (Pepe Aguilar)** — FOH Staff, « Victor Fernandez Adds Latin Flavor to the Mix », *FOH Magazine*, 15 avril 2005, https://fohonline.com/articles/foh-interview/victor-fernandez-adds-latin-flavor-to-the-mix. Percussions dans un sous-groupe stéréo avec EQ et compresseur ou limiteur stéréo pour leur donner de la taille. Il joue sans arrêt du panoramique pour placer les instruments selon le rythme.
- **Brad Divens (Enrique Iglesias)** — Greg DeTogne, « Right Place, Right Time… », ProSoundWeb, 17 mars 2022, https://www.prosoundweb.com/right-place-right-time-audio-brings-the-heat-for-enrique-iglesias-and-ricky-martin-on-tour/. Batterie en deux groupes, l'un légèrement compressé, l'autre écrasé en parallèle. « Rear bus » (appris d'Andrew Scheps) : toutes les entrées sauf batterie et percussions dans un groupe compressé, ajouté au mix jusqu'à ce qu'il donne de la présence.
- **En complément, studio** : Dan Daley, « Recording Latin Percussion », *Sound On Sound*, décembre 2006, https://www.soundonsound.com/node/4911817. Article de **studio**, pas de live : Boris Milan garde les timbales près du centre et écarte les congas ; en salsa, les percussions soutiennent la voix. Javier Garza garde les percussions sèches. Milan réduit la reverb avec le tempo : au-dessus de 125 BPM, presque plus.

### Traduction 32SC — hors guide, à valider à l'oreille
**Micro et placement** : congas, bongos, timbales : pas de fiche dans le guide (Partie 3). À traiter comme une source nouvelle (cas 2 du `CLAUDE.md`) avant de chiffrer.
**Panoramique des percussions (Milan, Fernandez)** : timbales près du centre, congas plus écartées. Critère : chaque percussion se localise depuis un côté de la salle, sans trou au centre.
**Bus percussions (Fernandez)** : un FlexMix stéréo en sous-groupe, avec EQ et compresseur sur le bus. Les 16 FlexMix sont tous attribués (1.3) : il faudrait réaffecter un bus (par exemple Bus Divers, 4.5). Décision d'architecture pour Louis.
**« Rear bus » (Divens)** : toutes les entrées sauf batterie et percussions vers un bus compressé, dosé en parallèle. Même contrainte de bus libre. Critère : monter le bus jusqu'à ce que l'ensemble gagne en présence, et s'arrêter avant qu'on l'entende pomper.
**Cuivres — largeur (Murray)** : il utilise un léger désaccord et un delay. Pas de pitch shifter dans le rack. Seul le delay est faisable : départ cuivres vers un delay très court, à essayer. Le résultat ne vaut pas le geste de Murray.
**Cuivres — reverb** : courte, départ cuivres vers FX A ou C (Murray). Moins de reverb quand le tempo monte (Milan, en studio).
**Faders** : la scène est un point de départ, le mix se joue tout le temps (Murray, Fernandez).

### Désaccords
- Divens (pop latine d'aréna) et Murray (fusion de club) n'ont pas la même échelle ; Murray est le plus proche de Louis.
- La règle de Milan sur la reverb est une règle de studio, non transposée au live par la source.

---

## Bilan des sources par style

| Style | Sources vérifiées (lues) | Suffisant ? |
| --- | --- | --- |
| Punk | Lemoine (SOS 2013), Chirnside (Mix 2006), Kay (Mix 2026) | Oui, mais pop-punk et punk de stade ; rien sur le punk de salle |
| Rock | Pooch (SOS 2020), Lemoine (SOS 2013), Iron Maiden (Mix 2023) | Oui |
| Métal | Big Mick (Mix 2003), Iron Maiden (Mix 2023), Huff (Mix 2026) | Oui |
| Hip-hop | Strong (Mix 2006), Moore (MusicRadar 2025) | Oui |
| Reggae | Cowlin (thewailers.com 2023), Versteegt (Mix 2018) | Oui |
| Dub | Veal (interview Afropop 2010), Terrano (SOS 2007), Mad Professor (SOS 2007) ; Veal 2007 et Williams 2012 : existence seule | Oui pour les gestes ; le livre de Veal reste à lire |
| Techno live | Burton/Prodigy (SOS 2010), Hira/New Order (SOS 2017) | Deux sources, **aucune de techno au sens strict** |
| Folk | Hines (Mix 2005), Korff (SOS 2013), Kennedy (Mix 2023, mince) | Oui |
| Fusion latine | Murray (Mix 2008), Fernandez (FOH 2005), Divens (PSW 2022) ; Daley (SOS 2006, studio) | Oui |

**Non retenu** : blogs promotionnels (Ticket Fairy) et pages de marques sans ingénieur nommé ; le profil Meyer Sound de Jose Rivera (Marc Anthony, 2016) a été lu mais il est publié par le constructeur du système. Il dit seulement qu'il sépare chaque instrument par l'EQ et garde la voix comme point focal. Pages inaccessibles (403) : Audio Technology (Rüfüs du Sol), Harman (Kevin Madigan, CSN).

## À faire pour intégrer

1. Ajouter à chaque scène 6.1–6.7 un paragraphe « Intention », avec ses sources.
2. 6.6 : ajouter les drop-outs (mutes, Filter DCA) et la couche de faders préparée ; corriger toute mention implicite de mute groups sur touche (absents de la 32SC, manuel 12.1.2).
3. 6.5 : renvoyer aux gestes dub de 6.6.
4. 6.7 : trancher la compression des stems (essai A/B) et ajouter la demande de stem basse séparé.
5. 6.3 : réécouter le HPF guitares à 100 Hz et le H-Mid +3 dB voix à la lumière de Big Mick.
6. Décider s'il faut créer 6.8 Folk et 6.9 Fusion latine, et s'il faut libérer un FlexMix pour un bus percussions ou un rear bus.
7. Registre 8.7, nouvelles vérifications : Key Source depuis un canal trigger audio (gates batterie) ; limiteur et gate sur le Fat Channel d'un retour d'effet (gestes dub de Terrano).
