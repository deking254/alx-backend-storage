-- returns the longevity of bands with glam_rock as a style
select metal_bands.band_name, (if(split is null, 2020, split)-formed) as lifespan from metal_bands where style like '%Glam rock%' order by lifespan desc;
