from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt
import math
import numpy as np
from skimage.exposure import histogram
from skimage import measure, transform
from skimage.transform import rescale, resize, downscale_local_mean
#Preparing data
im = io.imread('../data/img3.jpg')
image_rescaled = rescale(im, 2.5, anti_aliasing=True)
image_rotated = transform.rotate(image_rescaled, 15)
io.imsave('../data/Mazphoto3.jpg', image_rescaled)

val = filters.threshold_otsu(im)
image_filtered = ndimage.binary_fill_holes(im < val)
image_eroded = ndimage.binary_erosion(image_filtered, structure=np.ones((2,2)))

plt.imshow(im, cmap='gray', interpolation='nearest')
#plt.show()
plt.imshow(image_filtered, cmap='gray', interpolation='nearest')
#plt.show()
plt.imshow(image_eroded, cmap='gray', interpolation='nearest')
#plt.show()

#Remove irregular areas
cellcount = measure.label(image_eroded)
print('CELL COUNT' + str(cellcount.max()))
unique_labels, unique_label_count = np.unique(cellcount, return_counts=True)
unique_data = np.asarray((unique_labels, unique_label_count))
print(unique_labels[0:7])
print( unique_label_count[0:7])
print('Median:' + str(ndimage.median(unique_label_count[0:])))
print('Variance:' + str(ndimage.variance(unique_label_count[1:])))
print('Deviation:' + str(ndimage.median(unique_label_count[1:])))

#image_opening = ndimage.binary_opening(image_filtered) #structure=np.ones((5,5))
#plt.imshow(image_opening, cmap='gray', interpolation='nearest')
#plt.show()

#Measuring

#from skimage import measure
#cellcount = measure.label(image_eroded, neighbors=8)
#print(cellcount.max())


#histogram = ndimage.measurements.histogram(unique_label_count, 0, 1, unique_labels.max())
#print(histogram)
#print(unique_labels)
#print(unique_label_count)
#unique_data = np.asarray((unique_labels, unique_label_count))

#print(unique_data)

#from skimage.feature import canny
#edges = canny(im < 0.6);
#filled_edges = ndimage.binary_fill_holes(edges < val)

#plt.imshow(edges, cmap='gray');
#plt.show();

#sobelimage = filters.sobel(im)
#plt.imshow(edges, cmap='gray');
#plt.show();
