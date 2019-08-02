from skimage import io, filters
from scipy import ndimage
import matplotlib.pyplot as plt

im = io.imread('cellsMisc.jpg', as_grey=True)
val = filters.threshold_otsu(im)
cells = ndimage.binary_fill_holes(im < val)
plt.imshow(cells, cmap='gray')
plt.show()

plt.imshow(im < val, cmap='gray')
plt.show()

plt.imshow(cells, cmap='Greys') #'greys' does not work
plt.show()

from skimage import measure
cellcount = measure.label(cells)
print(cellcount.max())


from skimage.feature import canny
edges = canny(im);
plt.imshow(edges, cmap='gray');
plt.show();
