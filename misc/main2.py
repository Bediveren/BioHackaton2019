from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt
import math
import numpy as np
from skimage.exposure import histogram

#Preparing data
im = io.imread('redbloodcell.jpg', as_grey=True)

val = filters.threshold_otsu(im)
image_filtered = ndimage.binary_fill_holes(im < val)
image_eroded = ndimage.binary_erosion(image_filtered, structure=np.ones((3,3)))

plt.imshow(image_eroded, cmap='gray', interpolation='nearest')
plt.show()

#Remove irregular areas
cellcount = measure.label(image_eroded)
unique_labels, unique_label_count = np.unique(cellcount, return_counts=True)
#image_opening = ndimage.binary_opening(image_filtered) #structure=np.ones((5,5))
#plt.imshow(image_opening, cmap='gray', interpolation='nearest')
#plt.show()

#Measuring

from skimage import measure
cellcount = measure.label(image_eroded, neighbors=8)
print(cellcount.max())


#histogram = ndimage.measurements.histogram(unique_label_count, 0, 1, unique_labels.max())
#print(histogram)
#print(unique_labels)
#print(unique_label_count)
unique_data = np.asarray((unique_labels, unique_label_count))

#print(unique_data)

#from skimage.feature import canny
#edges = canny(im < 0.6);
#filled_edges = ndimage.binary_fill_holes(edges < val)

#plt.imshow(edges, cmap='gray');
#plt.show();

#sobelimage = filters.sobel(im)
#plt.imshow(edges, cmap='gray');
#plt.show();
