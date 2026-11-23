"""Audit du guide par Gemini, en deux passes, via le proxy local (127.0.0.1:8000).

Usage :  python audits/outils/audit_gemini.py [A|B|AB] [modele]
Les réponses brutes vont dans audits/_brut/ (non versionné) : elles ne valent
rien avant le tri contre le guide et les manuels (skill audit-guide-par-ia-externe).
"""
import json, sys, time, urllib.request, urllib.error
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
GUIDE = RACINE / "guide" / "Guide_Mixage_Live_V35.md"
MANUELS = RACINE / "manuels"
SORTIE = RACINE / "audits" / "_brut"
PROXY = "http://127.0.0.1:8000/v1beta/models/{m}:generateContent"


def lignes(debut, fin):
    """Lignes [debut, fin) du guide (numérotation à partir de 1)."""
    tout = GUIDE.read_text(encoding="utf-8").splitlines()
    return "\n".join(tout[debut - 1:fin - 1])


def doc(titre, texte):
    return f"\n\n=============== {titre} ===============\n\n{texte}"


def passe(nom):
    g = GUIDE.read_text(encoding="utf-8").splitlines()
    idx = {l.split(" — ")[0]: i + 1 for i, l in enumerate(g) if l.startswith("# ")}
    p5, hist = idx["# PARTIE 5"], idx["# HISTORIQUE"]
    bloc = lignes(1, 62)  # titre + Bloc assistant (règles de priorité)
    changelog_v35 = lignes(hist, hist + 20)
    partie_manuel = nom[1] if len(nom) > 1 else "12"
    nom = nom[0]
    if nom == "A":
        perim = "PASSE A : Parties 0 à 4 du guide (matériel, philosophie, Fat Channel, presets par source, bus)."
        corps = lignes(idx["# PARTIE 0"], p5)
        extra = ""
    else:
        perim = ("PASSE B : Parties 5 à 8 et annexes du guide (master, FX, scènes par style, workflow, autres consoles), "
                 "puis le retour « approches musicales par style » (propositions pas encore intégrées : vérifie surtout "
                 "que chaque source citée dit bien ce qu'on lui attribue et que la traduction 32SC est juste).")
        corps = lignes(p5, hist)
        extra = doc("RETOUR — approches par style (non intégré)",
                    (RACINE / "retours" / "2026-11-23_approches-par-style.md").read_text(encoding="utf-8"))
    consigne = (RACINE / "audits" / "outils" / "consigne_audit.md").read_text(encoding="utf-8")
    manuels = ""
    for p in partie_manuel:
        manuels += doc(f"MODE D'EMPLOI StudioLive 32SC/16R — partie {p}",
                       (MANUELS / f"StudioLive_32SC_16R_manuel_partie{p}.txt").read_text(encoding="utf-8", errors="replace"))
    if len(partie_manuel) == 1:
        perim += (f" Seule la partie {partie_manuel} du mode d'emploi est jointe à cette passe (limite de taille) : "
                  "pour un point qui relèverait de l'autre partie, écris « vérifiable sans manuel : non » plutôt que de citer de mémoire.")
    texte = (perim
             + doc("CHANGELOG V35 (hors périmètre)", changelog_v35)
             + doc("GUIDE — en-tête et Bloc assistant", bloc)
             + doc("GUIDE — partie auditée", corps)
             + extra
             + doc("ADDENDUM FAT CHANNEL (PreSonus)", (MANUELS / "Fat_Channel_Plugins_Addendum_V2.txt").read_text(encoding="utf-8", errors="replace"))
             + manuels)
    return consigne, texte


def appel(modele, consigne, texte, essais=6):
    corps = json.dumps({
        "systemInstruction": {"parts": [{"text": consigne}]},
        "contents": [{"role": "user", "parts": [{"text": texte}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 16000},
    }).encode("utf-8")
    for n in range(1, essais + 1):
        try:
            req = urllib.request.Request(PROXY.format(m=modele), data=corps, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=600) as r:
                rep = json.load(r)
            parts = rep["candidates"][0]["content"]["parts"]
            return "".join(p.get("text", "") for p in parts), rep.get("usageMetadata", {})
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")
            quota = [l.strip() for l in msg.split("\\n") if "metric" in l or "limit" in l.lower()]
            print(f"  essai {n} : HTTP {e.code} " + (" / ".join(quota)[:600] if quota else msg[:300]))
            if e.code == 429 and "jour" in msg.lower():
                break
        except Exception as e:  # réseau, réponse vide, blocage
            print(f"  essai {n} : {e}")
        time.sleep(70)
    return None, {}


def main():
    arg = (sys.argv[1] if len(sys.argv) > 1 else "A1,A2,B1,B2").upper()
    passes = ["A1", "A2", "B1", "B2"] if arg == "TAILLE" else arg.split(",")
    if arg == "TAILLE":  # vérification sans appel réseau
        for nom in passes:
            c, t = passe(nom)
            print(f"Passe {nom} : {len(c) + len(t):,} caractères (~{(len(c) + len(t)) // 4:,} tokens)")
        return
    modele = sys.argv[2] if len(sys.argv) > 2 else "gemini-flash-latest"
    SORTIE.mkdir(parents=True, exist_ok=True)
    for i, nom in enumerate(passes):
        if i:
            time.sleep(130)  # pause entre les passes (250 k tokens d'entrée par minute en gratuit)
        consigne, texte = passe(nom)
        print(f"Passe {nom} : {len(texte):,} caractères envoyés à {modele}")
        rep, usage = appel(modele, consigne, texte)
        if rep is None:
            print(f"Passe {nom} : échec, rien enregistré.")
            continue
        f = SORTIE / f"{time.strftime('%Y-%m-%d')}-gemini-passe{nom}.md"
        f.write_text(f"<!-- modèle {modele} ; usage {json.dumps(usage)} -->\n\n{rep}", encoding="utf-8")
        print(f"Passe {nom} : {len(rep):,} caractères reçus → {f}")


if __name__ == "__main__":
    main()
