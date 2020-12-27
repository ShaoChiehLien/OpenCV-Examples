import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)

# Do the laplacian transform in CV_64F(double) type, so it could capture both
# White-to-Black transition(negative slope) and Black-to-White transition
# (positive slope). CV_8U only range from 0 to 255, so any White-to-Black
# transition(negative slope) would be zero
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

# take the absolute value to negative slope to positive slope and cast the
# type to uint8 so it could be plotted on matplotlib
lap = np.uint8(np.absolute(lap))

# Reference: https://stackoverflow.com/questions/4483502/edge-detection-techniques#:~:text=Sobel%2FPrewitt%20measure%20the%20slope,the%20change%20of%20the%20slope.&text=The%20result%20of%20a%20lapace,because%20the%20slope%20is%20constant.&text=Also%2C%20a%20Laplace%20filter%20is,noise%20than%20Sobel%20or%20Prewitt.
# Sobel is first order derivative while Laplacian is second order derivative
# Ex:
#   Edge: 0 0 0 0 1 1 1 1
#   Sobel result(1st derivative):    0 0 0 1 1 0 0 0
#   Laplace result(2nd derivative):  0 0 0 1 -1 0 0 0
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)  # take the derivatives on x direction
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)  # take the derivatives on y direction

# take the absolute value to negative slope to positive slope and cast the
# type to uint8 so it could be plotted on matplotlib
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# Use bitwise_or to combine sobelX and sobelY
sobelXY = cv2.bitwise_or(sobelX, sobelY)

# Plot the image
titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelXY']
images = [img, lap, sobelX, sobelY, sobelXY]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')

    plt.title(titles[i])

    plt.xticks([])
    plt.yticks([])

plt.show()
