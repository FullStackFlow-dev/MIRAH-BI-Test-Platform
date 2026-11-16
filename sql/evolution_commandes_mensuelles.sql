SELECT
    DATE_TRUNC('month', date_commande) AS mois,
    COUNT(*) AS commandes
FROM commandes
GROUP BY mois
ORDER BY mois;