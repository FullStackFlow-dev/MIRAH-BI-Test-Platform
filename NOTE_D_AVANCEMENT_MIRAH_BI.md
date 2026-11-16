# MIRAH-BI
## Note d'avancement Data Engineering

Auteur :
Merphy Mademba
Data Engineer

Date :
Octobre 2026

---

# 1. Contexte

Dans le cadre du développement de MIRAH-BI, j'ai entrepris la création d'une plateforme de test appelée :

MIRAH-BI Test Platform

L'objectif est de disposer d'environnements de données réalistes permettant de valider les fonctionnalités de MIRAH-BI avant l'arrivée des données réelles des partenaires.

Cette approche permet :

- de tester les connecteurs ;
- de tester les pipelines ;
- de tester les cubes ;
- de tester les dashboards ;
- de tester les KPI ;
- de préparer les futurs agents BI.

Cela évite de dépendre uniquement des données issues de ServiceAdmin.

---

# 2. Cas d'usage actuellement développé

## Restaurant

Données simulées :

- restaurants
- clients
- commandes
- paiements
- avis

Architecture :

Bronze
↓
PostgreSQL
↓
Silver
↓
Gold
↓
Cube
↓
Dashboard
↓
MIRAH-BI

Fonctionnalités déjà développées :

✅ Génération de données

✅ PostgreSQL

✅ Scripts d'ingestion

✅ Architecture Bronze/Silver/Gold

✅ Airflow

✅ KPI SQL

✅ Configuration multi-SGBD

---

# 3. Ce qui pourra être livré à MIRAH-BI

Une fois le dataset Restaurant finalisé :

Le Data Engineer pourra fournir :

- Source de données PostgreSQL
- Jeux de données réalistes
- Tables Bronze
- Pipelines Silver
- Pipelines Gold
- Cubes
- Documentation technique

Cela permettra à MIRAH-BI d'être testé dans des conditions proches du réel.

---

# 4. Ce que le Chef de Projet peut faire à partir de cette livraison

Fatima pourra :

- tester le parcours complet utilisateur ;
- valider l'intégration MIRAH-BI ;
- identifier les fonctionnalités manquantes ;
- vérifier le comportement de la plateforme sur des volumes importants ;
- préparer les démonstrations.

Conformément à la roadmap du BI, la validation des sources, pipelines, cubes et dashboards constitue le premier objectif avant les cas d'usage réels. 【1-4d5e3a】【2-e83225】

---

# 5. Ce que la Data Analyst pourra faire

Aminata pourra :

- construire les dashboards ;
- tester les cubes ;
- analyser les KPI ;
- concevoir les visuels ;
- effectuer les validations métier ;
- préparer les démonstrations utilisateurs.

Ce rôle correspond précisément au rôle Analyste / BI Developer décrit dans MIRAH-BI. 【2-e83225】

---

# 6. Proposition de nouveaux domaines de test

Afin de renforcer MIRAH-BI et couvrir plusieurs secteurs d'activité, je propose de créer progressivement plusieurs environnements de test.

---

## Domaine 1 : Restaurant

Dataset :

- restaurants
- clients
- commandes
- paiements
- avis

Objectif :

Tester les KPI de revenus, ventes et satisfaction.

---

## Domaine 2 : E-commerce

Dataset :

- produits
- clients
- commandes
- paiements
- livraisons
- stocks

Objectif :

Tester les ventes, marges, stocks et logistique.

---

## Domaine 3 : Télécom

Dataset :

- abonnés
- forfaits
- consommation
- recharges
- factures

Objectif :

Tester les KPI opérateurs.

---

## Domaine 4 : Banque

Dataset :

- comptes
- transactions
- agences
- clients

Objectif :

Tester les analyses financières et transactionnelles.

---

## Domaine 5 : Logistique et Mobilité

Inspiré de :

- Yango
- Heetch
- Yassir
- TeranGO
- Covoiturage.sn

Dataset :

- conducteurs
- passagers
- véhicules
- courses
- trajets
- paiements
- avis
- zones

Objectif :

Tester :

- revenus ;
- trajets ;
- distances ;
- zones de mobilité ;
- performances conducteurs ;
- satisfaction clients.

---

# 7. Bénéfices pour MIRAH-BI

Cette approche permettra de :

- disposer de données immédiatement exploitables ;
- valider les fonctionnalités avant les données réelles ;
- accélérer les développements ;
- réduire les risques techniques ;
- démontrer la plateforme à des prospects ;
- préparer les futurs agents IA ;

et surtout :

garantir que MIRAH-BI fonctionne sur plusieurs secteurs d'activité avant son déploiement auprès des partenaires et clients de MIRAHTEC.

---

# 8. Prochaine étape proposée

Finaliser le dataset Restaurant puis :

- construire le pipeline complet Silver ;
- construire le pipeline Gold ;
- créer les cubes ;
- produire les premiers dashboards ;
- effectuer les premiers tests de bout en bout dans MIRAH-BI.

---

# 9. Répartition des responsabilités proposées

## Mon rôle (Data Engineer)

Après livraison d'un dataset :

- génération des données ;
- ingestion Bronze ;
- pipelines Silver ;
- pipelines Gold ;
- création des cubes ;
- documentation technique ;
- contrôle qualité ;
- validation technique.

Livrables :

- sources de données ;
- pipelines ;
- tables Silver ;
- tables Gold ;
- cubes ;
- scripts SQL ;
- documentation.

---

## Rôle du Chef de Projet MIRAH-BI (Fatima)

Après livraison :

- validation du cas d'usage ;
- validation du parcours utilisateur ;
- validation fonctionnelle ;
- identification des besoins complémentaires ;
- priorisation des améliorations ;
- arbitrage métier ;
- organisation des démonstrations.

---

## Rôle Data Analyst / BI Developer (Aminata)

Après livraison :

- conception des dashboards ;
- conception des KPI ;
- validation des indicateurs ;
- création des visualisations ;
- tests d'expérience utilisateur ;
- retours métier ;
- documentation fonctionnelle.

---

## Objectif commun

Transformer chaque domaine métier :

Restaurant
↓
E-commerce
↓
Télécom
↓
Banque
↓
Logistique

en démonstration complète de MIRAH-BI :

Source
↓
Bronze
↓
Silver
↓
Gold
↓
Cube
↓
Dashboard
↓
Utilisateur final