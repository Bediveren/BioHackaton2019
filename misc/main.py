from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt
import math
import numpy as np

im = io.imread('redbloodcell.jpg', as_grey=True)
sample = io.imread('singlecell.jpg', as_grey=True)

val = filters.threshold_otsu(im)
image_filtered = ndimage.binary_fill_holes(im < 0.6)
cell = ndimage.binary_fill_holes(sample < 0.6)

cell_height, cell_width = cell.shape
image_height, image_width = image_filtered.shape

cell_height_offset = math.floor(cell_height / 2)
scan_height_start = cell_height_offset;
scan_height_end = image_height - cell_height

cell_width_offset = math.floor(cell_width / 2)
scan_width_start = cell_width_offset;
scan_width_end = image_width - cell_width

plt.imshow(image_filtered, cmap='gray')
plt.show()

plt.imshow(cell, cmap='gray')
plt.show()



match_matrix = np.zeros((scan_height_end, scan_width_end))

import itertools

for h, w in itertools.product(range(0, scan_height_end, 10), range(0, scan_width_end, 10)):
    np.isclose(cell[0:cell_height, 0:cell_width], image_filtered[h:h + cell_height, w:w + cell_width])
    print(h,w)

#for h in range(0, scan_height_end):
#    for w in range(0, scan_width_end):
#        np.isclose(cell[0:cell_height, 0:cell_width], image_filtered[h:h + cell_height, w:w + cell_width]




#plt.imshow(im < val, cmap='gray')
#plt.show()

#plt.imshow(cells, cmap='Greys') #'greys' does not work
#plt.show()

#from skimage import measure
#cellcount = measure.label(cells)
#print(cellcount.max())


#from skimage.feature import canny
#edges = canny(im < 0.6);
#plt.imshow(edges, cmap='gray');
#plt.show();
