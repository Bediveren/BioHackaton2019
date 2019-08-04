from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt
import math
import numpy as np
from skimage.exposure import histogram
from skimage import measure, transform
from skimage.transform import rescale, resize, downscale_local_mean
from PIL import Image


def count_cells():
    #Preparing data
    im = io.imread('ImageRecieved.jpg', as_grey=True)
    #image_rescaled = rescale(im, 2.5, anti_aliasing=True)
    #io.imsave('../data/ScaleRotate15gimg1.jpg', image_rotated)
    #im = np.asarray( image, dtype="int32" )
    val = filters.threshold_otsu(im)
    image_filtered = ndimage.binary_fill_holes(im <  val)
    image_eroded = ndimage.binary_erosion(image_filtered, structure=np.ones((2,2)))

    extremas = ndimage.extrema(im)
    print(len(extremas))

    #Remove irregular areas
    cellcount = measure.label(image_filtered)
    #print('CELL COUNT' + str(cellcount.max()))
    #io.imsave('result.jpg', image_filtered)

    im = Image.fromarray(image_filtered)
    im.save("result.jpeg")
    return cellcount.max()
