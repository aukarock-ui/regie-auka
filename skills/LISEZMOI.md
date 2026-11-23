# Skills de la régie Auka

`skills.zip` contient les skills de la méthode, un dossier par skill (`<nom>/SKILL.md`) :

| Skill | Rôle |
|---|---|
| maj-guide-mixage | mettre à jour le guide après une correction ou un audit, et le publier ici |
| audit-guide-par-ia-externe | faire auditer le guide par une autre IA et trier ses réponses |
| preparer-evenement-sono | préparer une date à partir des fiches techniques |
| transposer-preset-console | transposer les presets de la 32SC sur une autre console |
| integrer-retour-terrain | intégrer au guide ce qui a été constaté en régie |
| demarrer-regie-auka | installer ou mettre à jour la régie sur le PC depuis ce Drive |
| methode-calage | méthode de calage système |
| nouveau-systeme | décrire une sono inconnue avant de la caler |
| fiche-evenement | fiche d'un événement son avant tout calage |

Avec le compte claude.ai, ces skills arrivent tout seuls dans Claude Code. Cette copie sert de référence et de secours : `demarrer-regie-auka` installe depuis le zip ceux qui manqueraient, sans écraser ceux qui sont déjà là.

La version de référence de chaque skill est celle du compte claude.ai. Le zip est republié depuis le projet « Mix Live » quand un skill change.

## À recopier dans le compte claude.ai (23/11/2026)

Le zip du 23/11 contient quatre skills modifiés depuis la régie, qui ne sont pas encore dans le compte. Tant qu'ils n'y sont pas, Claude Code continue d'utiliser les anciennes versions du compte. Pour chacun, remplacer le skill du compte par le `SKILL.md` de ce dossier (Paramètres → Capacités → Skills, ou depuis le projet « Mix Live ») :

- `maj-guide-mixage` (repart de la version du compte) : ne pas charger le guide entier, vérification par l'agent `verif-manuel`, relecture par l'agent `relecteur`, publication seulement après validation, mise à jour de `TACHES.md`.
- `integrer-retour-terrain` : recherche des lignes par `verif-manuel`, mise à jour de `TACHES.md`.
- `audit-guide-par-ia-externe` : tri par `verif-manuel`, voies gratuites d'abord (proxy Gemini local, opencode), trois points déjà vérifiés de plus.
- `demarrer-regie-auka` : **ne plus effacer le dépôt git du serveur** à la mise à jour, installer `config-claude` (permissions et agents), serveur déclaré dans `.mcp.json` avec le journal des écritures.

Les agents ne fonctionnent que dans Claude Code, sur le PC de régie. Dans claude.ai, les skills disent de faire la vérification soi-même.
