-- ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT metal_bands.origin, SUM(metal_bands.fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
