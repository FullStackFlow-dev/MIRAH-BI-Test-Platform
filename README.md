# MIRAH-BI Test Platform

## Présentation

MIRAH-BI Test Platform est un environnement de test et de validation de données que j'ai conçu dans le cadre du développement de la plateforme BI de MIRAHTEC.

L'objectif est de disposer de jeux de données réalistes, reproductibles et multi-sectoriels permettant de :

- développer les pipelines Data Engineering ;
- tester les connecteurs de bases de données ;
- valider les processus ETL/ELT ;
- tester les tableaux de bord Power BI ;
- expérimenter les KPI métiers ;
- préparer les futures fonctionnalités d'analyse avancée et d'intelligence artificielle de MIRAH-BI.

Cette approche permet de ne pas dépendre uniquement des données provenant de ServiceAdmin durant les phases de conception, de développement et de validation de la plateforme.

---

# Contexte

Le projet MIRAH-BI a vocation à accueillir des données provenant de plusieurs partenaires et secteurs d'activité.

Afin de garantir la fiabilité, la robustesse et l'évolutivité de la plateforme, il est nécessaire de disposer de jeux de données réalistes permettant :

- d'effectuer des tests de performance ;
- de valider les pipelines de données ;
- de tester les différents connecteurs SGBDR ;
- de valider les KPI métiers ;
- de tester les tableaux de bord ;
- de préparer les futurs agents BI et IA.

MIRAH-BI Test Platform constitue donc un laboratoire de données permettant de simuler différents environnements métiers avant l'arrivée des données réelles des partenaires MIRAHTEC.

---

# Objectifs du projet

## Objectifs techniques

- Génération de données synthétiques réalistes
- Tests PostgreSQL
- Tests MySQL
- Tests SQL Server
- Tests Snowflake
- Automatisation avec Apache Airflow
- Architecture Bronze / Silver / Gold
- Validation Power BI
- Contrôle qualité des données
- Préparation des futurs Agents BI

## Objectifs pour MIRAH-BI

- Tester la robustesse de la plateforme
- Tester les scénarios partenaires
- Valider les importations multi-SGBDR
- Tester les performances
- Préparer les futurs connecteurs
- Vérifier les KPI métiers
- Valider les tableaux de bord
- Préparer les fonctionnalités IA

---

# Technologies

## Data Engineering

- Python
- Pandas
- NumPy
- Faker
- SQLAlchemy

## Bases de données

- PostgreSQL
- MySQL
- SQL Server
- Snowflake

## Orchestration

- Apache Airflow

## Business Intelligence

- Power BI

## Exploration des données

- Jupyter Notebook

## Tests

- PyTest

---

# Architecture Générale

```text
Bronze
│
├── restaurants.json
├── clients.json
├── commandes.json
├── paiements.json
└── avis.json

        ↓

PostgreSQL
MySQL
SQL Server
Snowflake

        ↓

Silver

        ↓

Gold

        ↓

Power BI

        ↓

MIRAH-BI
```

---

# Architecture du projet

```text
mirah-bi-test-platform/

├── configs/
│   ├── settings.py
│   ├── logging.yaml
│   └── airflow_connections.template.json
│
├── dags/
│   └── restaurant_pipeline.py
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── logs/
│
├── notebooks/
│   └── exploration.ipynb
│
├── scripts/
│   ├── generate_data.py
│   └── load_postgres.py
│
├── sql/
│   ├── create_schema.sql
│   └── analytics.sql
│
├── .env.example
├── requirements.txt
└── README.md
```

---

# Domaines métiers ciblés par MIRAH-BI

L'objectif est de tester MIRAH-BI avec plusieurs secteurs d'activité afin de garantir sa capacité à intégrer et analyser différents types de données partenaires.

---

## 1. Partenaire Restaurant (Projet actuel)

Dataset simulé :

```text
restaurants
clients
commandes
paiements
avis
```

KPIs :

- Chiffre d'affaires total
- Chiffre d'affaires par restaurant
- Chiffre d'affaires par quartier
- Chiffre d'affaires par catégorie
- Nombre de commandes
- Panier moyen
- Modes de paiement
- Satisfaction client
- Top restaurants
- Top clients

---

## 2. Partenaire E-commerce

Dataset simulé :

```text
produits
clients
commandes
paiements
livraisons
stocks
```

KPIs :

- Ventes
- Produits les plus vendus
- Taux de livraison
- Valeur des stocks
- Panier moyen
- Chiffre d'affaires

---

## 3. Partenaire Télécom

Dataset simulé :

```text
abonnés
forfaits
consommation
recharges
factures
```

KPIs :

- ARPU
- Revenus
- Consommation
- Recharges
- Abonnés actifs
- Churn

---

## 4. Partenaire Banque

Dataset simulé :

```text
comptes
transactions
clients
agences
```

KPIs :

- Volume transactionnel
- Solde moyen
- Activité clients
- Performances agences
- Répartition des produits

---

## 5. Partenaire Logistique et Mobilité

Inspiré des plateformes de transport et mobilité telles que :

- Yango
- Heetch
- Yassir
- TeranGO
- Covoiturage.sn

Dataset simulé :

```text
conducteurs
passagers
courses
trajets
véhicules
paiements
avis
zones
```

KPIs :

- Nombre de courses
- Chiffre d'affaires
- Temps moyen de trajet
- Distance moyenne parcourue
- Top conducteurs
- Top zones
- Satisfaction clients
- Taux d'annulation
- Répartition des paiements

---

## 6. Vision Générale

À long terme, MIRAH-BI devra pouvoir intégrer des données provenant de :

- Restauration
- Commerce électronique
- Télécommunications
- Banque
- Logistique et mobilité
- Distribution
- Services numériques
- Administrations publiques

afin de proposer :

- des tableaux de bord dynamiques ;
- des rapports automatisés ;
- des alertes intelligentes ;
- des indicateurs métiers avancés ;
- des analyses prédictives ;
- des agents IA conversationnels spécialisés.

---

# Génération des données

```bash
python scripts/generate_data.py
```

Résultat :

```text
data/bronze/

├── restaurants.json
├── clients.json
├── commandes.json
├── paiements.json
└── avis.json
```

---

# Création de l'environnement

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

Installation :

```bash
pip install -r requirements.txt

Copier le fichier de configuration, puis renseigner les identifiants localement dans `.env` :
```powershell
Copy-Item .env.example .env
```

Ne jamais versionner `.env` ni placer des identifiants réels dans les fichiers suivis.
```

---

# Création de la base PostgreSQL

```sql
CREATE DATABASE restaurant_bi;
```

---

# Création du schéma

```bash
psql -U postgres -d restaurant_bi -f sql/create_schema.sql
```

---

# Chargement PostgreSQL

```bash
python scripts/load_postgres.py
```

---

# Démarrage Airflow

```bash
airflow standalone
```

Pipeline :

```text
restaurant-bi-pipeline
```

Workflow :

```text
generate_data.py
        ↓
Bronze
        ↓
PostgreSQL
        ↓
Analytics
        ↓
Power BI
        ↓
MIRAH-BI
```

---

# Démarrage Jupyter

```bash
jupyter notebook
```

---

# KPI actuellement disponibles

## Revenus

- Chiffre d'affaires total
- Chiffre d'affaires par restaurant
- Chiffre d'affaires par quartier
- Chiffre d'affaires par catégorie

## Commandes

- Nombre total de commandes
- Évolution mensuelle
- Panier moyen
- Répartition par canal

## Paiements

- Modes de paiement
- Montants encaissés
- Répartition des paiements

## Satisfaction

- Note moyenne
- Nombre d'avis
- Répartition des notes

## Classements

- Top restaurants
- Top clients
- Top quartiers
- Top catégories

---

# État d'avancement actuel

## Réalisé

✅ Architecture du projet

✅ Configuration du projet

✅ Gestion des variables d'environnement via `.env` local

✅ Génération de données synthétiques

⚠️ Chargement PostgreSQL (connexion requise)

✅ Airflow

✅ Architecture Bronze / Silver / Gold

✅ Scripts de chargement

✅ Requêtes analytiques

✅ Notebook d'exploration

✅ Jeux de données Restaurant

---

## Prochaines étapes

- Couche Silver
- Couche Gold
- Tests automatisés
- Jeux de données E-commerce
- Jeux de données Télécom
- Jeux de données Banque
- Jeux de données Mobilité
- Connecteurs multi-SGBDR
- Agents BI
- Intégration avancée Power BI

---

# Vision du projet

L'objectif final est de disposer d'une plateforme de validation permettant de tester MIRAH-BI dans plusieurs contextes métiers avant l'intégration des données réelles des partenaires et clients de MIRAHTEC.

MIRAH-BI Test Platform servira également de laboratoire de développement pour les futures fonctionnalités Data Engineering, Business Intelligence, Analytics avancée et Intelligence Artificielle.
