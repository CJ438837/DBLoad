
import os
import requests
from typing import List

def fetch_tcga_cases(project="TCGA-BRCA", size=10):
    """
    Retrieve TCGA cases metadata from GDC
    """
    url = "https://api.gdc.cancer.gov/cases"
    params = {
        "filters": {
            "op": "in",
            "content": {
                "field": "project.project_id",
                "value": [project]
            }
        },
        "format": "JSON",
        "size": size
    }

    response = requests.post(url, json=params)

    if response.status_code != 200:
        raise ValueError("TCGA query failed")

    return response.json()

def test_fetch_tcga_cases():
    test_projects = [
        "TCGA-BRCA",     # valide
        "TCGA-LUAD",     # valide
        "INVALID_PROJ"   # invalide
    ]

    for project in test_projects:
        try:
            print(f"\n🔍 Test projet : {project}")
            data = fetch_tcga_cases(project=project, size=3)

            hits = data.get("data", {}).get("hits", [])

            if not hits:
                print(f"⚠️ Aucun cas trouvé pour {project}")
                continue

            print(f"✅ {len(hits)} cas récupérés pour {project}")
            for case in hits:
                case_id = case.get("case_id", "NA")
                submitter_id = case.get("submitter_id", "NA")
                print(f"   • {submitter_id} ({case_id})")

        except ValueError as e:
            print(f"❌ Erreur API pour {project}: {e}")
        except requests.RequestException as e:
            print(f"❌ Erreur réseau pour {project}: {e}")

if __name__ == "__main__":
    test_fetch_tcga_cases()
