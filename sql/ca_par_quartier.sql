SELECT
    quartier,
    SUM(c.montant) AS chiffre_affaires
FROM restaurants r
JOIN commandes c
    ON r.restaurant_id = c.restaurant_id
GROUP BY quartier
ORDER BY chiffre_affaires DESC;