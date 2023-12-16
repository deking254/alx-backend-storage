-- returns the longevity of bands with glam_rock as a style
SELECT metal_bands.band_name, (IF(split IS NULL, 2020, split)-formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
