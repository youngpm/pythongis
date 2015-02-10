#!/usr/bin/env python 

from osgeo import gdal

if __name__ == '__main__':
    in_file = '../images/portland_chip.tif'
    out_file = '../images/portland_chip_out.tif'
    try:
        # Open the input dataset.
        ds_in = gdal.Open(in_file)

        # Read entire image into a numpy array.
        im = ds_in.ReadAsArray()

        # Do some image processing on im...

        # Create a dataset.
        dvr = gdal.GetDriverByName("GTiff")
        ds_out = dvr.CreateCopy(out_file, ds_in)  # dvr.Create(...) is also an option // HL

        # Write to the created dataset.
        for b in range(im.shape[0]):
            band = ds_out.GetRasterBand(b+1)
            band.WriteArray(im[b,:,:])

    finally:
        ds_out = None
        ds_in = None


