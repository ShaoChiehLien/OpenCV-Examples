import cv2
import numpy as np

img = cv2.imread('lena.jpg')
cv2.imshow("Original image", img)
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):  # Makes image 1/4 of the size than the original image by pyrDown
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)

# laplacian_pyramid_list start from the smallest image in Gaussian Pyramid, and expand it til the original size
layer = gaussian_pyramid_list[5]
laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])  # extend the image to 4x of its size

    # Compare and subtract two same size images, one is extended from pryUp(low quality)
    # and one is reduced from pryDown(high quality)
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)

    # Show the images
    cv2.imshow(str(i) + '. Image reduced from pryDown', gaussian_pyramid_list[i-1])
    cv2.imshow(str(i) + '. Image extended from pryUp', gaussian_extended)
    cv2.imshow(str(i) + '. Laplacian', laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
