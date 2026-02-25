import leafmap
from geoai.download import (
    download_naip,
    download_overture_buildings,
    extract_building_stats,
)
m = leafmap.Map(center=[47.6526, -117.5923], zoom=16)
m.add_basemap("Esri.WorldImagery")
m
bbox = m.user_roi_bounds()
if bbox is None:
    bbox = (-117.6029, 47.65, -117.5936, 47.6563)