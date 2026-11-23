# Attend la remise à zéro du quota gratuit Gemini (minuit heure du Pacifique = 9 h à Paris), puis lance les quatre passes.
# On n'interroge pas /health : juste après une relance du proxy, il affiche « disponible » alors que le quota n'est pas revenu.
$racine = Split-Path (Split-Path $PSScriptRoot)
$vbs = Join-Path $env:USERPROFILE '.config\gemini\start-proxy.vbs'
$maintenant = Get-Date
$cible = $maintenant.Date.AddHours(9).AddMinutes(5)
if ($maintenant -ge $cible) { $cible = $cible.AddDays(1) }
Write-Output ("{0:HH:mm} attente jusqu'à {1:dd/MM HH:mm}" -f $maintenant, $cible)
Start-Sleep -Seconds ([int]($cible - (Get-Date)).TotalSeconds)
try { Invoke-RestMethod -Uri http://127.0.0.1:8000/health -TimeoutSec 5 | Out-Null }
catch { if (Test-Path $vbs) { Start-Process wscript.exe -ArgumentList "`"$vbs`""; Start-Sleep -Seconds 10 } }
Set-Location $racine
# Quatre passes d'environ 110 k tokens, espacées de 130 s (limite gratuite : 250 k tokens d'entrée par minute).
python audits/outils/audit_gemini.py A1,A2,B1,B2 gemini-flash-latest
