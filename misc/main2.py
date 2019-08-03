from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt
import math
import numpy as np
from skimage.exposure import histogram

im = io.imread('redbloodcell.jpg', as_grey=True)

val = filters.threshold_otsu(im)
image_filtered = ndimage.binary_fill_holes(im < val)

#plt.imshow(image_filtered, cmap='gray', interpolation='nearest')
#plt.show()

#plt.imshow(cells, cmap='Greys') #'greys' does not work
#plt.show()

from skimage import measure
cellcount = measure.label(image_filtered, neighbors=8)
print(cellcount.max())

unique_labels, unique_label_count = np.unique(cellcount, return_counts=True)
histogram = ndimage.measurements.histogram(unique_label_count, 0, 1, unique_labels.max())
print(histogram)
#print(unique_labels)
#print(unique_label_count)
unique_data = np.asarray((unique_labels, unique_label_count))

#print(unique_data)

from skimage.feature import canny
edges = canny(im < 0.6);
filled_edges = ndimage.binary_fill_holes(edges < val)

#plt.imshow(edges, cmap='gray');
#plt.show();

#sobelimage = filters.sobel(im)
#plt.imshow(edges, cmap='gray');
#plt.show();
