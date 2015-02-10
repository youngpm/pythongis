import fiona
import geojson

with fiona.open('../images/roads.shp') as source:
    geojson_coll = geojson.FeatureCollection([rec for rec in source])

with open('../images/roads.json', 'w') as sink:
    geojson.dump(geojson_coll, sink)
