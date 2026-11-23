# Régie Auka : méthode de mixage live

Méthode de mixage live de Louis (« Auka »), technicien son associatif et freelance (MJC de Saint-Lys, région toulousaine), sur PreSonus StudioLive 32SC + stagebox 16R : punk, rock, métal, hip-hop, reggae, dub, techno live, parfois folk et fusion latine.

Règle de fond : **zéro approximation**. Chaque valeur est rattachée à une source (manuel constructeur, addendum, calcul détaillé ou validation en concert). Ce qui n'est pas vérifié est marqué « à tester » ou « à valider à l'oreille ».

## Relecture / audit

Pour relire la méthode (humain ou IA) et laisser des notes, voir [`AUDIT.md`](AUDIT.md) : dossier `audits/`, issues GitHub, commentaires de relecture.

## Contenu

| Chemin | Rôle |
|---|---|
| `guide/Guide_Mixage_Live_V38.md` | **La référence** : matériel, gain staging, Fat Channel, presets par source, bus, FX, scènes par style, workflow, transposition sur d'autres consoles, registre des vérifications 8.7 |
| `guide/Registre_verifications_console_V36.docx` | Registre des vérifications console (numéroté V36 parce que la section 8.7 n'a pas changé depuis : il reste valable pour la V38) |
| `contexte/` | Faits utiles hors guide : parc matériel, comportements console vérifiés |
| `retours/` | Constatations faites en régie ou en recherche, **pas encore intégrées** au guide |
| `skills/` | Skills Claude de la méthode, un `SKILL.md` par dossier (copie de référence ; la version active est celle du compte claude.ai). L'archive `skills.zip` de secours n'est pas versionnée ici : elle est dans le dossier Drive `skills` |
| `CLAUDE.md` | Consignes de l'assistant en régie |
| `VERSION.md` | Version en service du guide, du contexte et du serveur console |

**Hors de ce dépôt :**
- **Manuels constructeur** : sur le Google Drive, dossier `Regie-Auka/manuels` (droits d'auteur).
- **Serveur console** studiolive-mix-assistant : fork de [zarfld/presonus-studiolive-mcp](https://github.com/zarfld/presonus-studiolive-mcp), branche `guide-auka`, livré en zip par le Drive.
- **Calage du système** (processeurs, amplis, alignement) : dépôt `calage-sono`.

## Comment la méthode évolue

Le guide se modifie uniquement depuis le projet claude.ai « Mix Live » (skill `maj-guide-mixage`), qui publie chaque version sur le Drive puis ici. Une constatation faite en régie s'écrit dans `retours/AAAA-MM-JJ_lieu.md`. Une remarque d'audit retenue par Louis passe par le même chemin.
