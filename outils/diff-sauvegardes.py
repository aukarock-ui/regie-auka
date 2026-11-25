"""Compare deux sauvegardes snapshot_console_state (rawState) et liste les clés changées.
Usage : python -I outils/diff-sauvegardes.py A.json B.json [--ignore motif ...]"""
import json, sys, re
a, b = sys.argv[1], sys.argv[2]
ign = [re.compile(p) for p in sys.argv[4:]] if len(sys.argv) > 3 and sys.argv[3] == '--ignore' else []
ign += [re.compile(r'(meter|clip|reduction|gainred|\.signalstrength|diskusage)')]
ra = json.load(open(a, encoding='utf-8'))['rawState']; rb = json.load(open(b, encoding='utf-8'))['rawState']
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
n = 0
for k in sorted(set(ra) | set(rb)):
    if any(p.search(k) for p in ign): continue
    va, vb = ra.get(k), rb.get(k)
    if va != vb and not (isinstance(va, float) and isinstance(vb, float) and abs(va - vb) < 1e-6):
        n += 1; print(f'{k}: {va!r} -> {vb!r}')
print(f'-- {n} clé(s) changée(s)')
