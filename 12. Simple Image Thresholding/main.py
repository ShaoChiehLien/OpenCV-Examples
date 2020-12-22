import cv2

img = cv2.imread('gradient.png', 0)

# See the threshold type on: https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#gaa9e58d2860d4afa658ef70a9b1115576
# The threshold is 50 (2nd argument), if the pixel value is smaller than 50, it is set to 0
# , otherwise it is set to the maximum value 200 (3rd argument)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)  # inverse of binary

# The threshold is 127 (2nd argument), if the pixel value is smaller than 127, it remains the same
# , otherwise it is set to the value of 127
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# The threshold is 127 (2nd argument), if the pixel value is larger than 127, it remains the same
# , otherwise it is set to the value of 0
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # inverse of to zero

# Show the image and each thresholds
cv2.imshow('Image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
