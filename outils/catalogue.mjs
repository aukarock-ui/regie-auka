// Recherche dans le catalogue UC Surface du serveur console (lecture seule).
// Usage : node outils/catalogue.mjs "fxreturn limit" "gatekeysrc" ...
// Prouve qu'un paramètre existe dans le logiciel, pas son effet : « catalogue, à confirmer à l'écran ».
import { fileURLToPath, pathToFileURL } from 'node:url'
import { dirname, join } from 'node:path'
import { existsSync } from 'node:fs'

const dist = join(dirname(fileURLToPath(import.meta.url)), '..', 'code', 'studiolive-mix-assistant', 'packages', 'presonus-domain', 'dist', 'index.js')
if (!existsSync(dist)) {
  console.error(`Serveur non compilé (${dist} absent) : lancer "npx -y pnpm@9 build" dans code/studiolive-mix-assistant.`)
  process.exit(1)
}
const m = await import(pathToFileURL(dist).href)
for (const q of process.argv.slice(2)) {
  const hits = m.searchUcnetCatalog(q, 200)
  const lines = [...new Set(hits.map((h) => `${h.pattern} :: ${h.id} (${h.paramList})`))]
  console.log(`=== ${q} : ${lines.length} paramètre(s)`)
  for (const l of lines.slice(0, 40)) console.log('  ' + l)
  if (lines.length > 40) console.log(`  … ${lines.length - 40} de plus : préciser la recherche`)
}
