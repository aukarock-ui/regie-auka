---
name: "maj-guide-mixage"
description: "Mettre à jour le Guide de Mixage Live (projet Mix Live) après un audit ou une correction : vérification au manuel, script de remplacements, contrôle des raccords, changelog, docx, remplacement dans le projet."
---

# Mise à jour du Guide de Mixage Live

À utiliser dès que Louis transmet un audit du guide (DeepSeek, Gemini, autre IA, ou ses propres remarques), demande une correction, ou demande une nouvelle version. Les règles de fond (zéro approximation, format des fiches, statuts validé / à tester / emprunté) sont dans les instructions du projet et dans le Bloc assistant du guide : ce skill ne les répète pas, il fixe la méthode.

## 0. Mise en place

1. Lire la version courante du guide dans le projet (`claude/Guide_Mixage_Live_Vxx.md`). S'il y a plusieurs fichiers de guide, le signaler à Louis avant de continuer.
2. Copier ce fichier dans le dossier de travail temporaire sous le nom `vXX.md`. C'est la seule source : ne jamais repartir d'un docx ou d'un souvenir de conversation.
3. Extraire en texte les manuels utiles (mode d'emploi StudioLive parties 1 et 2, addendum Fat Channel, manuel UC Surface) pour pouvoir y chercher avec grep. Les tableaux perdent leur mise en page à l'extraction : relire les lignes brutes avant de conclure sur un tableau.

## 1. Vérifier chaque remarque avant de l'accepter

Un audit externe est non fiable par défaut. Pour chaque point, dans l'ordre :

1. Retrouver la citation dans le guide courant (elle peut venir d'une version périmée).
2. Si le point invoque le manuel : retrouver le passage exact. Une citation introuvable disqualifie l'argument, pas forcément le problème — vérifier quand même le fond.
3. Si le point est un calcul : refaire le calcul.
4. Classer : retenu, retenu en partie (dire quelle partie), rejeté (avec la phrase du manuel qui le contredit).
5. Une valeur proposée par l'auditeur sans source n'entre jamais dans le guide. On garde la méthode ou le critère d'écoute, pas le chiffre.

Ne jamais annoncer une correction après une lecture partielle : lire la section entière du guide et la section entière du manuel.

## 2. Écrire les corrections dans un script

Un script `make_vNN.py` par version, qui lit `vXX.md` et écrit `vNN.md` :

```python
import sys
t = open('vXX.md', encoding='utf-8').read()
n_done = 0
def rep(old, new, count=1):
    global t, n_done
    c = t.count(old)
    if c != count:
        sys.exit(f'ERREUR: {c} occurrence(s) au lieu de {count} pour: {old[:90]!r}')
    t = t.replace(old, new); n_done += 1

rep('**GUIDE DE MIXAGE LIVE — VXX**', '**GUIDE DE MIXAGE LIVE — VNN**')
# ... un rep() par correction ...
print('remplacements:', n_done)
print('lignes ** impair:', [i+1 for i, l in enumerate(t.split('\n')) if l.count('**') % 2])
open('vNN.md', 'w', encoding='utf-8').write(t)
```

Règles :
- Chaque `rep()` échoue si le texte d'origine n'apparaît pas exactement le nombre de fois attendu. Copier les chaînes depuis le fichier, apostrophes typographiques comprises.
- Jamais de réécriture à la main du fichier entier, jamais de remplacement global non compté.
- La liste « lignes ** impair » doit être vide.

## 3. Propager

Une correction s'applique partout où l'ancienne valeur ou l'ancienne idée apparaît. Pour chaque correction, chercher dans tout le corps du guide (hors section HISTORIQUE) : la valeur, le nom de la commande, le nom du modèle, les sections qui y renvoient, l'Annexe A, l'Annexe B, le registre 8.7, la Partie 8 (correspondances avec les autres consoles).

## 4. Contrôle des raccords — l'étape à ne jamais sauter

Les erreurs trouvées par les audits suivants viennent presque toutes des passages qu'on vient de réécrire. Avant de livrer :

1. Lister chaque passage ajouté ou réécrit dans cette version.
2. Pour chacun, relire toutes les sections auxquelles il renvoie et toutes celles qui renvoient à lui. Chercher : une affirmation « impossible » suivie d'un « peut-être » ; une règle « reprise de » une autre section qui en écarte une exception ; une option proposée ici et exclue ailleurs ; une valeur hors des plages ou des crans de la Partie 2 ; une vérification qui ne vérifie pas ce qu'elle annonce.
3. Relire le nouveau texte contre lui-même : deux corrections de la même version peuvent se contredire.
4. Chercher par script les formulations périmées qui doivent avoir disparu du corps (compter les occurrences, attendre zéro).

Si une erreur est de mon fait, le dire clairement à Louis au lieu de la corriger en silence.

## 5. Changelog

Insérer un bloc `### CE QUI CHANGE PAR RAPPORT À LA VXX` en tête de la section `# HISTORIQUE — NE PAS CITER`, avant le bloc de la version précédente. Il cite la source de l'audit, les valeurs exactes avant et après, section par section, et les points non retenus avec la raison. Condensé : seulement ce qui a changé.

## 6. Registre 8.7

Toute valeur qui dépend d'une vérification sur la console reçoit une ligne au registre, formulée comme un geste de trente secondes à deux minutes, et est rangée dans la bonne séance (console seule, balance virtuelle, avec musiciens).

## 7. Produire et publier

1. `pandoc vNN.md -o Guide_Mixage_Live_VNN.docx --from=markdown`, puis `zip -d Guide_Mixage_Live_VNN.docx '*/'`. Si le registre 8.7 a changé, régénérer aussi `Registre_verifications_console_VNN.docx` à partir de la section 8.7 du nouveau guide, jamais à partir de l'ancien registre.
2. Écrire `claude/Guide_Mixage_Live_VNN.md` dans le projet, puis supprimer `claude/Guide_Mixage_Live_VXX.md`. Une seule version du guide dans le projet.
3. Envoyer le docx à Louis.
4. Publier sur le Google Drive de régie, dossier `Regie-Auka` (id `1NhEZ8haRy-l8kzS-ICPvLANI-ZNXozv0`), sous-dossier `guide` (id `1Q-i3RR9fDn_nDgTjihXU5S3O2n4w_yJq`) : créer `Guide_Mixage_Live_VNN.md` (type `text/markdown`, conversion Google désactivée), puis mettre l'ancienne version à la corbeille. Le connecteur ne remplace pas le contenu d'un fichier : on crée le nouveau, puis on jette l'ancien. Faire de même pour le registre s'il a changé, et pour `VERSION.md` à la racine (version du guide, date, état du contexte). Si `CLAUDE.md` cite le nom du fichier du guide, le recréer aussi. Ne jamais laisser deux versions du guide dans le dossier.
5. Lire le sous-dossier `retours` (id `1D6Farkern9JFyf25iUgvGf17o1W2h-XN`) : les notes de régie qui y arrivent depuis le PC sont des retours de terrain à traiter avec le skill `integrer-retour-terrain`.

## 7bis. Avant tout audit externe

Quand la nouvelle version doit partir chez un auditeur (Gemini, DeepSeek…), faire d'abord sa propre relecture complète : les étapes 3 et 4 sur tout le guide, pas seulement sur les passages modifiés. L'ordre qui a fait ses preuves : relecture de l'assistant, puis audit par API, puis audit par copier-coller (skill `audit-guide-par-ia-externe`).

## 8. Compte rendu à Louis

Court, en français, dans cet ordre : ce qui est retenu (avec la source), ce qui est rejeté (avec la phrase du manuel), ce que le contrôle des raccords a trouvé en plus, les vérifications console ajoutées. Ne jamais promettre que le prochain audit ne trouvera rien.

## Règle d'arrêt

Quand un audit ne remonte plus que des remarques de formulation mineures, proposer à Louis de figer le guide : ce qui le fait progresser ensuite, ce sont les vérifications du registre 8.7 sur la console.