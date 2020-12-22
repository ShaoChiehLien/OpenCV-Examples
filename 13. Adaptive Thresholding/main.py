import cv2

img = cv2.imread('sudoku.png', 0)  # MUST set to grayscale, adaptiveThreshould only take in grayscale image
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# THRESH_BINARY: if pixel's value exceed cv2.ADAPTIVE_THRESH_MEAN_C - 2(6th argument), set it to 255(2nd argument)
# ADAPTIVE_THRESH_MEAN_C = the mean pixel value of its neighbor, block size 11*11(5th argument)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Image', img)
cv2.imshow('THRESH_BINARY', th1)  # bad result because of the shadow
cv2.imshow('ADAPTIVE_THRESH_MEAN_C', th2)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
