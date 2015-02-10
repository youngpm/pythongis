import json
import fiona
from shapely import geometry, ops

with fiona.open('../images/roads.shp') as source:
    unioned_geom = ops.unary_union([geometry.shape(rec['geometry']) for rec in source])

buffered_geom = unioned_geom.buffer(0.00005).simplify(0.000001)

with open('../images/roads_buffered.json', 'w') as sink:
    json.dump(geometry.mapping(buffered_geom), sink)
