SELECT
    r.name,
    SUM(c.montant) AS chiffre_affaires
FROM commandes c
JOIN restaurants r
    ON c.restaurant_id = r.restaurant_id
GROUP BY r.name
ORDER BY chiffre_affaires DESC;