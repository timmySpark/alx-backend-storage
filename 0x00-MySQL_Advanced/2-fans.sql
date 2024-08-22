-- Task : 2. Best band ever! - ranks country origins of bands, ordered by the number of (non-unique) fans
-- script can be executed on any database
SELECT origin, sum(fans) nb_fans 
FROM metal_bands
GROUP BY ORIGIN
ORDER BY nb_fans DESC;
