-- Task : 3. Old school band - lists all bands with Glam rock as their main style, ranked by their longevity
-- script can be executed on any database
SELECT band_name, (IFNULL(split, '2022') - formed) lifespan 
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC;
