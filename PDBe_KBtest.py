import requests

# =========================================================
# 🔟 PDBe‑KB / PDBe REST API
# =========================================================

def fetch_pdbe_entry_summary(pdb_id: str):
 
    # Exemple d’endpoint PDBe REST API pour les métadonnées d’un PDB entry
    url = f"https://www.ebi.ac.uk/pdbe/api/pdb/entry/summary/{pdb_id.lower()}"
    
    r = requests.get(url)
    if r.status_code == 404:
        raise ValueError(f"PDBe entry not found: {pdb_id} (404)")
    r.raise_for_status()
    
    data = r.json()
    return data


# ------------------------------
# Script test
# ------------------------------
if __name__ == "__main__":
    test_pdb_ids = [
        "1cbs",        # PDB identifier known
        "4hhb",        # Another known structure (Hemoglobin)
        "XXXX"         # Invalid PDB ID
    ]

    for pdb_id in test_pdb_ids:
        try:
            info = fetch_pdbe_entry_summary(pdb_id)
            # Le JSON retourné a typiquement la clé pdb_id minuscule
            # ex. { "1cbs": [ { ... métadonnées ... } ] }
            entry_data = info.get(pdb_id.lower(), [{}])[0]
            title = entry_data.get("title", "Titre non disponible")
            exp_method = entry_data.get("experimental_method", "Méthode exp. inconnue")

            print(f"✅ {pdb_id} — Titre : {title} | Méthode : {exp_method}")

        except ValueError as e:
            print(f"❌ {e}")
        except requests.RequestException as e:
            print(f"❌ Erreur réseau pour {pdb_id}: {e}")
