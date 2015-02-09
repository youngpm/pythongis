#!/usr/bin/env python 
import sys
#// START OMIT
from osgeo import gdal

if __name__ == '__main__':
    im_file = '../images/portland_chip.tif'
    try:
        # Open a gdal dataset.
        ds = gdal.Open(im_file)
        
        # Read entire image into a numpy array.
        im = ds.ReadAsArray() # We can give arguments to read chunks, bands, etc // HL
    finally:
        # Ensure we release the dataset.
        ds = None

    # Proceed with image processing...
#// END OMIT
