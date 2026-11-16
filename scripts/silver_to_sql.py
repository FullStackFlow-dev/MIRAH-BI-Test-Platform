import glob
import pandas as pd

batch_size = 1000  # Regrouper par lots

# Parcourir tous les fichiers .parquet du dossier Silver
for input_file in glob.glob("*.parquet"):
  # Utiliser le nom du fichier (sans .parquet) comme nom de table SQL
  table_name = input_file.replace(".parquet", "")
  output_file = f"{table_name}_insert.sql"

  print(f"Traitement du fichier Parquet {input_file} -> table '{table_name}'...")

  # Charger le fichier Parquet avec Pandas
  df = pd.read_parquet(input_file)
  columns = df.columns.tolist()
  cols_str = ", ".join(columns)
  insert_prefix = f"INSERT INTO {table_name} ({cols_str}) VALUES\n"

  batch = []
  with open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write("BEGIN;\n")
    f_out.write(insert_prefix)

    # Parcourir chaque ligne du DataFrame
    for _, row in df.iterrows():
      vals = []
      for col in columns:
        val = row[col]

        # Gestion des valeurs nulles, nombres et textes
        if pd.isna(val):
          vals.append("NULL")
        elif isinstance(val, (int, float)):
          vals.append(str(val))
        else:
          # Échapper les apostrophes pour éviter les erreurs SQL
          val_escaped = str(val).replace("'", "''")
          vals.append(f"'{val_escaped}'")

      val_str = "(" + ", ".join(vals) + ")"
      batch.append(val_str)

      # Écrire par lots pour optimiser la taille et la vitesse
      if len(batch) >= batch_size:
        f_out.write(",\n".join(batch) + ";\n")
        batch = []
        f_out.write(insert_prefix)

    # Écrire le reste du lot s'il en reste
    if batch:
      f_out.write(",\n".join(batch) + ";\n")

    f_out.write("COMMIT;\n")

print("Conversion des fichiers Parquet Silver en SQL terminée avec succès !")