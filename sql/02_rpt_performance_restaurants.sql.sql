SELECT
    r.name,
    COUNT(c.commande_id) AS total_commandes,
    SUM(c.montant) AS chiffre_affaires
FROM restaurants r
JOIN commandes c
    ON r.restaurant_id = c.restaurant_id
GROUP BY r.name
ORDER BY chiffre_affaires DESC;