---
name: "demarrer-regie-auka"
description: "Installer ou mettre à jour automatiquement la régie Auka sur le PC de Louis depuis son Google Drive (dossier Regie-Auka) : documents, serveur console StudioLive, configuration. À utiliser quand Louis dit d'aller chercher la régie dans son Drive ou de la mettre à jour."
---

# Démarrer ou mettre à jour la régie Auka

À utiliser dans Claude Code sur le PC Windows de Louis, quand il demande d'aller chercher la régie dans son Drive, de l'installer ou de la mettre à jour. Louis ne doit rien installer, décompresser ni télécharger à la main : tu fais tout, en lui demandant seulement les autorisations que Claude Code exige.

Ce skill ne s'applique pas dans une session cloud ou claude.ai : seulement quand tu as un shell sur le PC.

## Repères

- Dossier Drive racine : `Regie-Auka`, id `1NhEZ8haRy-l8kzS-ICPvLANI-ZNXozv0`. Sous-dossiers : `guide`, `contexte`, `manuels`, `retours`, `code`, `skills`. Si l'id ne répond plus, chercher le dossier par son nom avec le connecteur Google Drive.
- Dossier local : `%USERPROFILE%\Regie-Auka` (pas besoin de droits administrateur). Le code va dans `%USERPROFILE%\Regie-Auka\code`.
- Outils : le connecteur Google Drive (fourni par le compte claude.ai de Louis) pour **lister** les fichiers ; PowerShell et `curl.exe` pour **télécharger** directement sur le disque. Ne jamais faire passer un fichier volumineux par la conversation (pas de `download_file_content` sur le guide, les manuels ou le zip du code).

## 1. Vérifier les prérequis

1. Le connecteur Google Drive est-il disponible (`/mcp` le liste sous claude.ai) ? Sinon, dire à Louis de se connecter à Claude Code avec son compte claude.ai (`/login`) et de vérifier que Google Drive est connecté dans claude.ai, puis s'arrêter.
2. `node -v` : il faut Node.js 20 ou plus. S'il manque, l'installer avec `winget install --id OpenJS.NodeJS.LTS -e --accept-source-agreements --accept-package-agreements` (Claude Code demandera l'autorisation à Louis), puis recharger le PATH de la session PowerShell ou demander à Louis de relancer Claude Code si `node` reste introuvable.

## 2. Lister le Drive

Avec le connecteur, lister récursivement le dossier racine (`search_files` avec `parentId = '<id du dossier>'`, puis chaque sous-dossier). Pour chaque fichier, noter : id, nom, sous-dossier, `modifiedTime`, taille. Ignorer les fichiers à la corbeille. S'il y a deux versions du guide dans `guide`, le signaler à Louis et prendre la plus récente seulement après sa confirmation.

## 3. Télécharger

Pour chaque fichier, dans le sous-dossier local du même nom :

```powershell
curl.exe -L --fail -o "$env:USERPROFILE\Regie-Auka\<sous-dossier>\<nom>" "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"
```

- Le téléchargement par lien suppose que le dossier `Regie-Auka` est partagé en lecture « toute personne disposant du lien ». Si `curl` renvoie une page HTML de connexion ou une erreur 403/404 au lieu du fichier, le dire à Louis : le partage par lien n'est pas actif.
- Vérifier chaque fichier téléchargé : taille égale à celle du Drive, et pour un `.md`, `.txt` ou `.json`, que ce n'est pas du HTML.
- En mode mise à jour, ne retélécharger que les fichiers dont le `modifiedTime` a changé ou qui sont nouveaux ; supprimer localement un guide qui n'existe plus dans le Drive (une seule version à la fois).
- Ne jamais écraser `retours/` en local : les notes de régie y restent.

## 4. Installer ou reconstruire le serveur console

Si `code/studiolive-mix-assistant.zip` est nouveau ou a changé :

```powershell
$dst = "$env:USERPROFILE\Regie-Auka\code\studiolive-mix-assistant"
Remove-Item -Recurse -Force $dst -ErrorAction SilentlyContinue
Expand-Archive "$env:USERPROFILE\Regie-Auka\code\studiolive-mix-assistant.zip" -DestinationPath $dst
cd $dst
npx -y pnpm@9 install
npx -y pnpm@9 build
npx -y pnpm@9 test
```

Tous les tests doivent passer. Sinon, montrer à Louis les tests en échec et ne pas brancher le serveur.

## 4 bis. Analyseur de larsen

1. `python --version` : il faut Python 3.10 ou plus. S'il manque : `winget install --id Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements`, puis recharger le PATH.
2. `python -m pip install --user numpy sounddevice`.
3. Console branchée en USB : `python "$env:USERPROFILE\Regie-Auka\code\studiolive-mix-assistant\tools\detecteur-larsen\usb_spectra.py" --list`. Choisir avec Louis le périphérique de la console et noter son nom. Si Studio One enregistre en ASIO, prévenir Louis : le pilote n'accepte en général qu'une application à la fois.
4. Ce nom sert à l'étape 5 (`PRESONUS_USB_DEVICE`) : le serveur lance alors l'analyseur tout seul et Windows affiche une notification à chaque larsen.
5. Vérifier la chaîne sans console : serveur lancé, `usb_spectra.py --selftest` ; `get_feedback_alerts` doit montrer un larsen simulé vers 2 480 Hz.

## 4 ter. Skills de la régie

Le dossier Drive `skills` contient `skills.zip` : les skills de la méthode (guide, événements, transposition, retours, calage, installation). Ils arrivent normalement tout seuls avec le compte claude.ai. Pour chaque skill du zip absent de la liste des skills de la session, l'installer pour Claude Code :

```powershell
$tmp = "$env:TEMP\regie-skills"
Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
Expand-Archive "$env:USERPROFILE\Regie-Auka\skills\skills.zip" -DestinationPath $tmp
# copier seulement les dossiers manquants vers "$env:USERPROFILE\.claude\skills\<nom>"
```

Ne jamais écraser un skill déjà présent : deux versions du même skill se contrediraient. Signaler à Louis ceux qui ont été installés depuis le Drive.

## 5. Brancher le serveur à Claude Code

1. Demander à Louis l'adresse IP de la console, ou la trouver : console et PC sur le même réseau, puis `npx -y pnpm@9 probe:dev discover` dans le dossier du serveur. Relever aussi le numéro de série.
2. Enregistrer le serveur pour toutes les sessions de Louis (portée utilisateur), écriture coupée :

```powershell
claude mcp add --scope user studiolive -e PRESONUS_IP=<ip> -e PRESONUS_SERIAL=<serie> -e PRESONUS_ROLE=FOH -e PRESONUS_USB_DEVICE="<nom du périphérique USB, étape 4 bis>" -e PRESONUS_USB_CHANNELS=1-32 -- node "$env:USERPROFILE\Regie-Auka\code\studiolive-mix-assistant\packages\presonus-mcp-server\dist\index.js"
```

   Si le serveur existe déjà, le retirer d'abord (`claude mcp remove --scope user studiolive`) puis le réenregistrer. Ne jamais ajouter `PRESONUS_WRITE=1` sans demande explicite de Louis.
3. Dire à Louis de relancer Claude Code dans `%USERPROFILE%\Regie-Auka` : le serveur et le `CLAUDE.md` du dossier sont lus au démarrage.

## 6. Compte rendu

Court : version du guide installée (d'après `VERSION.md`), fichiers ajoutés ou mis à jour, état du serveur (tests, IP), ce qui reste à faire. Si des manuels PDF manquent dans le Drive (les gros fichiers y sont déposés à la main), le signaler sans bloquer : les versions texte suffisent pour la recherche.

## Retours de régie

Quand Louis fait une constatation pendant une session, l'écrire dans `retours/AAAA-MM-JJ_lieu.md` en local et la déposer dans le sous-dossier `retours` du Drive avec le connecteur (`create_file`, type `text/markdown`, sans conversion Google). Ne jamais modifier le guide ni le contexte en local.