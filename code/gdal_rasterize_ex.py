#!/usr/bin/env python 

from osgeo import gdal, ogr

if __name__ == '__main__':
    in_file = '../images/portland_chip.tif'
    out_file = '../images/portland_roads.tif'
    road_file = '../images/roads.shp'
    try:
        # Open the input dataset.
        ds_in = gdal.Open(in_file)

        # Open the vector dataset.
        ds_vector = ogr.Open(road_file)
        lyr = ds_vector.GetLayer()

        # Create a dataset to write to.
        ds_out = gdal.GetDriverByName("GTiff").Create(out_file, 
                                                      ds_in.RasterXSize, 
                                                      ds_in.RasterYSize, 
                                                      3, gdal.GDT_Byte)
        ds_out.SetProjection(ds_in.GetProjection())
        ds_out.SetGeoTransform(ds_in.GetGeoTransform())

        # Rasterize.
        gdal.RasterizeLayer(ds_out, [1,2,3], lyr, burn_values=[255,0,0], 
                            options=['ALL_TOUCHED=TRUE'])

    finally:
        ds_out = None
        ds_vector = None
        ds_in = None
