-- Gather the information from metal_bands.sql
-- Columns: band_name, lifespan
SELECT DISTINCT band_name, IFNULL(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
