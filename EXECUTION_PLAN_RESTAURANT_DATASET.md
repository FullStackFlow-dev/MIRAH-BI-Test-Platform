# MIRAH-BI Test Platform

# Plan d'Exécution Complet
## Dataset Restaurant

Auteur : Merphy Mademba
Rôle : Data Engineer

---

# OBJECTIF FINAL

Construire un cas d'usage Restaurant complet permettant de valider :

- PostgreSQL
- Airflow
- Bronze / Silver / Gold
- Cubes
- Dashboards
- KPI
- Agent MIRAH-BI

afin de tester MIRAH-BI dans des conditions proches du réel.

---

# PHASE 1
# Préparation de l'environnement

Objectif :

Installer tous les outils nécessaires au projet.

Livrable :

Environnement fonctionnel.

Checklist :

- ✅ Vérifier Python
- ✅ Vérifier pip
- ✅ Créer environnement virtuel
- ✅ Activer environnement virtuel
- ✅ Installer requirements.txt
- ✅ Vérifier les dépendances
- ✅ Vérifier PostgreSQL
- ✅ Vérifier Docker
- ✅ Vérifier Airflow

Fin attendue :

Le projet démarre sans erreur.

---

# PHASE 2
# Nettoyage des anciennes données

Objectif :

Supprimer les anciennes données Bronze.

Checklist :

- ✅ Supprimer anciens JSON
- ✅ Vérifier dossier Bronze vide

Fin attendue :

Aucun ancien fichier JSON.

---

# PHASE 3
# Nettoyage PostgreSQL

Objectif :

Supprimer anciennes tables.

Checklist :

- ✅ Exécuter create_schema.sql
- ✅ Supprimer anciennes tables
- ✅ Recréer schéma

Fin attendue :

Base PostgreSQL vide mais prête.

---

# PHASE 4
# Génération des données

Objectif :

Créer les nouveaux jeux de données.

Checklist :

- ✅ Lancer generate_data.py
- ✅ Vérifier restaurants.json
- ✅ Vérifier clients.json
- ✅ Vérifier commandes.json
- ✅ Vérifier paiements.json
- ✅ Vérifier avis.json

Fin attendue :

5 datasets générés.

---

# PHASE 5
# Contrôle qualité Bronze

Checklist :

- ✅ Vérifier noms clients
- ✅ Vérifier téléphones +221
- ✅ Vérifier devise FCFA
- ✅ Vérifier quartiers Dakar
- ✅ Vérifier catégories
- ✅ Vérifier paiements

Fin attendue :

Qualité Bronze validée.  ✅

---

# PHASE 6
# Chargement PostgreSQL

Checklist :

- ✅ Lancer load_postgres.py
- ✅ Vérifier restaurants
- ✅ Vérifier clients
- ✅ Vérifier commandes
- ✅ Vérifier paiements
- ✅ Vérifier avis

Fin attendue :

Toutes les tables alimentées.  ✅

---

# PHASE 7
# Validation PostgreSQL

Checklist :

- ✅ COUNT restaurants
- ✅ COUNT clients
- ✅ COUNT commandes
- ✅ COUNT paiements
- ✅ COUNT avis

Fin attendue :

Volumes conformes.  ✅

---

# PHASE 8
# Validation Analytics

Checklist :

- [ ] Top Restaurants
- [ ] CA global
- [ ] CA quartier
- [ ] CA catégorie
- [ ] Top Clients
- [ ] Satisfaction

Fin attendue :

Tous les KPI fonctionnent.

---

# PHASE 9
# Silver Layer

Checklist :

- ✅ Créer silver_transform.py
- ✅ Nettoyage
- ✅ Typage
- ✅ Déduplication
- ✅ Export Parquet

Livrables :

- restaurants_clean.parquet
- clients_clean.parquet
- commandes_clean.parquet
- paiements_clean.parquet
- avis_clean.parquet

---

# PHASE 10
# Gold Layer

Checklist :

- ✅ Créer gold_transform.py
- ✅ CA Restaurant
- ✅ CA Quartier
- ✅ KPI Global
- ✅ Top Restaurants

Livrables :

- ca_par_restaurant.parquet
- ca_par_quartier.parquet
- kpi_global.parquet
- top_restaurants.parquet

---

# PHASE 11
# Airflow

Checklist :

- [ ] generate_data
- [ ] load_postgres
- [ ] silver_transform
- [ ] gold_transform
- [ ] quality_check

Fin attendue :

Pipeline automatisé.

---

# PHASE 12
# Tests automatiques

Checklist :

- [ ] test_generate.py
- [ ] test_load.py
- [ ] test_silver.py
- [ ] test_gold.py
- [ ] test_quality.py

Fin attendue :

Qualité validée automatiquement.

---

# PHASE 13
# Power BI

Checklist :

- [ ] Connexion PostgreSQL
- [ ] CA Restaurant
- [ ] CA Quartier
- [ ] Top Restaurants
- [ ] Paiements
- [ ] Satisfaction

Fin attendue :

Dashboard Power BI.

---

# PHASE 14
# MIRAH-BI

Checklist :

- [ ] Source PostgreSQL
- [ ] Ingestion Bronze
- [ ] Pipeline Silver
- [ ] Pipeline Gold
- [ ] Cube
- [ ] Dashboard

Fin attendue :

Parcours MIRAH-BI complet.

---

# PHASE 15
# Validation Equipe

Checklist :

- [ ] Validation technique
- [ ] Validation Fatima
- [ ] Validation Aminata
- [ ] Corrections

Fin attendue :

Cas Restaurant validé.

---

# PHASE 16
# Agent MIRAH-BI

Checklist :

- [ ] Connexion Agent
- [ ] Rafraîchissement
- [ ] Pipeline automatique
- [ ] Dashboard à jour

Fin attendue :

Flux complet jusqu'à MIRAH-BI.

---

# PHASE 17
# Extensions Futures

- E-commerce
- Télécom
- Banque
- Logistique & Mobilité

Objectif :

Valider MIRAH-BI sur plusieurs secteurs d'activité.