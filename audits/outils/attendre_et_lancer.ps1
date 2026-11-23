# Attend que la clé Gemini sorte de sa pause (quota du jour), puis lance les deux passes d'audit.
$racine = Split-Path (Split-Path $PSScriptRoot)
$vbs = Join-Path $env:USERPROFILE '.config\gemini\start-proxy.vbs'
for ($i = 0; $i -lt 96; $i++) {   # 16 h au plus, une vérification toutes les 10 min
    try {
        $h = Invoke-RestMethod -Uri http://127.0.0.1:8000/health -TimeoutSec 5
        $libre = @($h.keys | Where-Object { $_.available }).Count
        Write-Output ("{0:HH:mm} clés disponibles : {1}" -f (Get-Date), $libre)
        if ($libre -gt 0) { break }
    } catch {
        Write-Output ("{0:HH:mm} proxy arrêté, relance" -f (Get-Date))
        if (Test-Path $vbs) { Start-Process wscript.exe -ArgumentList "`"$vbs`"" }
    }
    Start-Sleep -Seconds 600
}
Set-Location $racine
python audits/outils/audit_gemini.py AB gemini-flash-latest
