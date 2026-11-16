SELECT
    r.name,
    AVG(a.note) AS note_moyenne,
    COUNT(a.avis_id) AS nombre_avis
FROM restaurants r
JOIN avis a
    ON r.restaurant_id = a.restaurant_id
GROUP BY r.name
HAVING COUNT(a.avis_id) >= 20
ORDER BY note_moyenne DESC;