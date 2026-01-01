# =========================================================
#1️⃣2️⃣ EMDB
# =========================================================
import requests

def fetch_emdb_entry(emd_id: str):
    """
    Retrieve metadata for an EMDB entry using its EMD ID.
    """
    url = f"https://www.ebi.ac.uk/emdb/api/entry/{emd_id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"EMDB query failed for {emd_id}")

    return response.json()


# =========================================================
# Test de la fonction EMDB
# =========================================================
if __name__ == "__main__":
    test_emdb_ids = [
        "EMD-62871",
        "EMD-63528",
        "INVALID_ID"
    ]

    for emd in test_emdb_ids:
        try:
            data = fetch_emdb_entry(emd)
            title = data.get("admin", {}).get("title", "Pas de titre")
            print(f"✅ {emd} — titre : {title}")
        except ValueError as e:
            print(f"❌ {e}")
        except requests.RequestException as e:
            print(f"❌ Erreur réseau pour {emd}: {e}")
