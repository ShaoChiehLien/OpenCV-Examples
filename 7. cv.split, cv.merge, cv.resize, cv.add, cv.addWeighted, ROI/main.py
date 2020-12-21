import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo-white.png')

print(img.shape)  # return a tuple of number of rows, columns, and channels
print(img.size)  # return total pixels that is accessed, rows * columns * channels
print(img.dtype)  # return image data type

b, g, r = cv2.split(img)  # split the image

# b, g, r are 2D array, so it will be gray scale
cv2.imshow('gray scale: blue image with only one channel', b)
cv2.imshow('gray scale: green image with only one channel', g)
cv2.imshow('gray scale: red image with only one channel', r)

# create a 3D array blueBGR, so it could be shown with color
blueBGR = np.zeros(img.shape, np.uint8)  # declare a 342 * 548 * '3' image with all the pixels = 0
# don't forget to specify uint8!!!
blueBGR[:, :, 0] = b  # only set the blue pixel to b
cv2.imshow('blue image', blueBGR)

# create a 3D array greenBGR, and fill the non green pixels with zero
zeros = np.zeros(g.shape, np.uint8)
# declare a  342 * 548 * '1' channel with all the pixels = 0, because merge only take in 2D array
# don't forget to specify uint8!!!
greenBGR = cv2.merge((zeros, g, zeros))  # use merge to merge three channel together
cv2.imshow('green image', greenBGR)

# create a 3D array redBGR, and fill the non red pixels with zero
redBGR = np.zeros(img.shape, np.uint8)  # declare a  342 * 548 * '3' image with all the pixels = 0
# don't forget to specify uint8!!!
redBGR[:, :, 2] = r  # only set the red pixel to r
cv2.imshow('red image', redBGR)

# cv2.add take in 3D array, width * length * 3, images
b_plus_g = cv2.add(blueBGR, greenBGR)  # use cv2.add to add two image
cv2.imshow('Use add: blue plus green', b_plus_g)
b_plus_g_plus_r = cv2.add(b_plus_g, redBGR)  # use cv2.add to add two image
cv2.imshow('Use add: b plus g plus r', b_plus_g_plus_r)

# cv2.merge take in 2D array, width * length * 1, channel
img = cv2.merge((b, g, r))  # use cv2.merge to merge three channels
cv2.imshow('Use merge: merge b, g, r', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
