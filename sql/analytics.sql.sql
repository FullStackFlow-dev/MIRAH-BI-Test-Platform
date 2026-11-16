-- =========================================================
-- MIRAH-BI ANALYTICS
-- =========================================================

-- =========================================================
-- 1. TOP 10 RESTAURANTS PAR CHIFFRE D'AFFAIRES
-- =========================================================

SELECT
    r.name,
    SUM(c.montant) AS chiffre_affaires_fcfa
FROM restaurants r
JOIN commandes c
    ON r.restaurant_id = c.restaurant_id
GROUP BY r.name
ORDER BY chiffre_affaires_fcfa DESC
LIMIT 10;

-- =========================================================
-- 2. CHIFFRE D'AFFAIRES PAR QUARTIER
-- =========================================================

SELECT
    r.quartier,
    SUM(c.montant) AS chiffre_affaires_fcfa
FROM restaurants r
JOIN commandes c
    ON r.restaurant_id = c.restaurant_id
GROUP BY r.quartier
ORDER BY chiffre_affaires_fcfa DESC;

-- =========================================================
-- 3. CHIFFRE D'AFFAIRES PAR CATEGORIE
-- =========================================================

SELECT
    r.categorie,
    SUM(c.montant) AS chiffre_affaires_fcfa
FROM restaurants r
JOIN commandes c
    ON r.restaurant_id = c.restaurant_id
GROUP BY r.categorie
ORDER BY chiffre_affaires_fcfa DESC;

-- =========================================================
-- 4. NOMBRE TOTAL DE COMMANDES
-- =========================================================

SELECT
    COUNT(*) AS total_commandes
FROM commandes;

-- =========================================================
-- 5. PANIER MOYEN
-- =========================================================

SELECT
    ROUND(
        AVG(montant),
        2
    ) AS panier_moyen_fcfa
FROM commandes;

-- =========================================================
-- 6. CHIFFRE D'AFFAIRES GLOBAL
-- =========================================================

SELECT
    SUM(montant) AS chiffre_affaires_total_fcfa
FROM commandes;

-- =========================================================
-- 7. COMMANDES PAR MOIS
-- =========================================================

SELECT
    DATE_TRUNC(
        'month',
        date_commande
    ) AS mois,
    COUNT(*) AS nombre_commandes,
    SUM(montant) AS chiffre_affaires_fcfa
FROM commandes
GROUP BY mois
ORDER BY mois;

-- =========================================================
-- 8. REPARTITION DES MODES DE PAIEMENT
-- =========================================================

SELECT
    mode_paiement,
    COUNT(*) AS nombre_paiements,
    SUM(montant) AS montant_total_fcfa
FROM paiements
GROUP BY mode_paiement
ORDER BY montant_total_fcfa DESC;

-- =========================================================
-- 9. TOP 10 CLIENTS
-- =========================================================

SELECT
    cl.nom,
    COUNT(c.commande_id) AS total_commandes,
    SUM(c.montant) AS montant_total_fcfa
FROM clients cl
JOIN commandes c
    ON cl.client_id = c.client_id
GROUP BY cl.nom
ORDER BY montant_total_fcfa DESC
LIMIT 10;

-- =========================================================
-- 10. SATISFACTION MOYENNE
-- =========================================================

SELECT
    ROUND(
        AVG(note),
        2
    ) AS note_moyenne
FROM avis;

-- =========================================================
-- 11. TOP 10 RESTAURANTS PAR NOTE
-- =========================================================

SELECT
    r.name,
    ROUND(
        AVG(a.note),
        2
    ) AS note_moyenne,
    COUNT(a.avis_id) AS nombre_avis
FROM restaurants r
JOIN avis a
    ON r.restaurant_id = a.restaurant_id
GROUP BY r.name
HAVING COUNT(a.avis_id) >= 10
ORDER BY note_moyenne DESC,
         nombre_avis DESC
LIMIT 10;

-- =========================================================
-- 12. KPI GLOBAL MIRAH-BI
-- =========================================================

SELECT
    (SELECT COUNT(*) FROM restaurants) AS total_restaurants,

    (SELECT COUNT(*) FROM clients) AS total_clients,

    (SELECT COUNT(*) FROM commandes) AS total_commandes,

    (SELECT COUNT(*) FROM paiements) AS total_paiements,

    (SELECT COUNT(*) FROM avis) AS total_avis,

    (SELECT SUM(montant) FROM commandes) AS chiffre_affaires_total_fcfa;