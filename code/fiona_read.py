import fiona

with fiona.open('../images/roads.shp') as source:
    for rec in source:
        print('Geometry {} is of type {}'.format(rec['id'], rec['geometry']['type']))
