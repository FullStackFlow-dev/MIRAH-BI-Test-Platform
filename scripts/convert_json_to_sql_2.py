import glob
import json

batch_size = 1000  # Regrouper par lots

# Parcourir tous les fichiers .json du dossier
for input_file in glob.glob("*.json"):
  # Utiliser le nom du fichier (sans .json) comme nom de table SQL
  table_name = input_file.replace(".json", "")
  output_file = f"{table_name}_insert.sql"

  print(f"Traitement de {input_file} -> table '{table_name}'...")

  batch = []
  columns = None
  insert_prefix = ""

  with open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write("BEGIN;\n")

    with open(input_file, "r", encoding="utf-8") as f_in:
      for line in f_in:
        if not line.strip():
          continue
        obj = json.loads(line)

        # Détecter dynamiquement les colonnes à partir du premier objet du fichier
        if columns is None:
          columns = list(obj.keys())
          cols_str = ", ".join(columns)
          insert_prefix = f"INSERT INTO {table_name} ({cols_str}) VALUES\n"
          f_out.write(insert_prefix)

        # Formater chaque valeur selon son type (nombre, texte, null)
        vals = []
        for col in columns:
          val = obj.get(col)
          if val is None:
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

print("Conversion dynamique de tous les fichiers terminée avec succès !")