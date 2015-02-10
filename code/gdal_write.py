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

        # Open a dataset to write to.
        ds_out = gdal.Open(out_file, gdal.GA_Update) # Note the special flag we pass in // HL

        # Write it to the output file.
        for b in range(im.shape[0]):
            band = ds_out.GetRasterBand(b+1)
            band.WriteArray(im[b,:,:])

    finally:
        # This is especially important when writing!
        ds_out = None
        ds_in = None


