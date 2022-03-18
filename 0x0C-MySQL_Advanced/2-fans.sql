-- Gather the information from metal_bands.sql
-- Columns: origin, nb_fans
SELECT DISTINCT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
