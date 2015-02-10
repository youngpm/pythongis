#!/usr/bin/env python 
# START IMPORTS OMIT
from osgeo import gdal
# END IMPORTS OMIT

if __name__ == '__main__':
    input_file = '../images/portland_chip.tif'
    try:
        # Open a gdal dataset.
        in_ds = gdal.Open(input_file)
        
        # Read entire image into a numpy array.
        im = in_ds.ReadAsArray() # We can give arguments to read chunks, bands, etc // HL
    finally:
        # Ensure we release the dataset.
        ds = None

    # Proceed with image processing...
