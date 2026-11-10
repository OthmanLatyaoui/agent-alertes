from pathlib import Path

import pandas as pd

dossier = Path("data")
sortie = dossier / "QUOT_SIM2_1990_2026.csv.gz"

fichiers = {
    annee: dossier / f"QUOT_SIM2_{annee}.csv.gz"
    for annee in range(1990, 2027)
}

manquants = [str(fichier) for fichier in fichiers.values() if not fichier.is_file()]
if manquants:
    raise FileNotFoundError("Fichiers manquants :\n" + "\n".join(manquants))

# Remplace ";" par "," si tes CSV sont séparés par des virgules.
separateur = ";"

# Vérifie les colonnes avant de commencer l'écriture.
colonnes = pd.read_csv(fichiers[1990], sep=separateur, nrows=0).columns.tolist()
for fichier in fichiers.values():
    entete = pd.read_csv(fichier, sep=separateur, nrows=0).columns.tolist()
    if entete != colonnes:
        raise ValueError(f"Colonnes différentes dans {fichier.name}")

premier_bloc = True

for annee, fichier in fichiers.items():
    print(f"Traitement de {annee}...")

    for bloc in pd.read_csv(fichier, sep=separateur, chunksize=100_000, dtype=str):
        bloc["année"] = annee
        bloc.to_csv(
            sortie,
            sep=separateur,
            index=False,
            header=premier_bloc,
            mode="w" if premier_bloc else "a",
        )
        premier_bloc = False

print(f"Fichier créé : {sortie}")