from pyensembl import EnsemblRelease

# ------------------------------
# Fonction Ensembl
# ------------------------------
def fetch_ensembl_gene_sequence(gene_name: str, release=109):
    """
    Récupère les séquences protéiques pour un gène Ensembl
    """
    ensembl = EnsemblRelease(release)
    # S'assurer que la base de données est téléchargée
    ensembl.download()
    ensembl.index()
    
    # Chercher le gène
    genes = ensembl.genes_by_name(gene_name)
    if not genes:
        raise ValueError(f"Gène {gene_name} non trouvé dans Ensembl release {release}")

    gene = genes[0]

    sequences = {}
    for transcript in gene.transcripts:
        if transcript.protein_sequence:
            sequences[transcript.id] = transcript.protein_sequence

    return sequences


# ------------------------------
# Script test
# ------------------------------
if __name__ == "__main__":
    test_genes = [
        "BRCA1",
        "TP53",
        "INVALID_GENE"
    ]

    for gene in test_genes:
        try:
            seqs = fetch_ensembl_gene_sequence(gene)
            if seqs:
                print(f"✅ {len(seqs)} séquences protéiques trouvées pour {gene}")
                for tid, seq in list(seqs.items())[:3]:  # afficher max 3 transcript
                    print(f"  Transcript {tid}: {seq[:50]}... ({len(seq)} aa)")
            else:
                print(f"⚠️ Aucun transcript codant trouvé pour {gene}")
        except ValueError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue pour {gene}: {e}")
