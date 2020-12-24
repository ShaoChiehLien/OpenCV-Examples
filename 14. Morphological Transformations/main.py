import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
# pixel that are less than 220 are set to 1, otherwise, 0
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# Declare a 5*5 white square
kernal = np.ones((5, 5), np.uint8)

# Reference https://legacy.imagemagick.org/Usage/morphology/#kernel
# Dilation: Use a square to do the convolution with the  image. Scan the 5*5 square through the image,
# if it touch the white area on image, the point on the image where the square's current middle
# point is located will be set to 1
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)  # erosion and then dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)  # dilation and then erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)  # difference between opening and closing
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)  # difference between image and the opening image

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')

    plt.title(titles[i])

    plt.xticks([])
    plt.yticks([])

plt.show()

