import os
import requests

BASE_DIR = outdir

def fetch_alphafold_structure(uniprot_id: str, output_dir=BASE_DIR):
    os.makedirs(output_dir, exist_ok=True)
    api_url = f"https://www.alphafold.ebi.ac.uk/api/prediction/{uniprot_id}"

    r = requests.get(api_url)
    if r.status_code != 200:
        raise ValueError(f"No AlphaFold predictions for {uniprot_id} (status {r.status_code})")

    data = r.json()
    # Vérifier qu'il y a au moins une prédiction
    if not data:
        raise ValueError(f"No prediction data found for {uniprot_id}")

    # URL du fichier PDB
    pdb_url = data[0].get("pdbUrl")
    if not pdb_url:
        raise ValueError(f"No PDB URL found for {uniprot_id}")

    # Télécharger le fichier
    output_path = os.path.join(output_dir, f"{uniprot_id}.pdb")
    resp = requests.get(pdb_url)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(resp.content)

    return output_path

# Exemple test
for uid in ["P69905", "Q9BYF1", "INVALID_ID"]:
    try:
        path = fetch_alphafold_structure(uid)
        print(f"✅ Structure téléchargée pour {uid} → {path}")
    except ValueError as e:
        print(f"❌ {e}")
    except requests.RequestException as e:
        print(f"❌ Erreur réseau pour {uid}: {e}")
