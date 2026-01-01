import requests

def parse_pfam_entries(entries_json):
    """
    Transforme le JSON de l'endpoint InterPro Pfam en liste de domaines avec positions.
    """
    domains = []
    for entry in entries_json.get("results", []):
        pfam_accession = entry["metadata"]["accession"]
        pfam_name = entry["metadata"]["name"]

        for prot in entry.get("proteins", []):
            prot_id = prot["accession"]

            for loc in prot.get("entry_protein_locations", []):
                for frag in loc.get("fragments", []):
                    start = frag.get("start")
                    end = frag.get("end")
                    domains.append({
                        "protein": prot_id,
                        "pfam_accession": pfam_accession,
                        "pfam_name": pfam_name,
                        "start": start,
                        "end": end
                    })
    return domains


def fetch_pfam_domains(uniprot_id: str):
    """
    Récupère les domaines Pfam pour une protéine UniProt via InterPro API.
    """
    base_url = f"https://www.ebi.ac.uk/interpro/api/protein/uniprot/{uniprot_id}/entry/pfam"
    r = requests.get(base_url)
    r.raise_for_status()
    data = r.json()

    entries_url = data.get("entries_url")
    if not entries_url:
        return []

    r2 = requests.get(entries_url)
    r2.raise_for_status()
    entries_data = r2.json()

    return parse_pfam_entries(entries_data)


# 🧪 Test
if __name__ == "__main__":
    test_ids = ["P01308"]  # Insulin
    for uid in test_ids:
        domains = fetch_pfam_domains(uid)
        for d in domains:
            print(f"{d['protein']}: {d['pfam_accession']} {d['pfam_name']} ({d['start']}-{d['end']})")
