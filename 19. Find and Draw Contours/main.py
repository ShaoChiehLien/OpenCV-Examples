import numpy as np
import cv2

img = cv2.imread('pic3.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img_gray, 200, 255, 0)

# cv2.CHAIN_APPROX_NONE: store all the boundary points
# cv2.CHAIN_APPROX_SIMPLE: removes redundant point like points between a straight line to save memory
# cv2.RETR_TREE: retrieves all of the contours and reconstructs a full hierarchy of nested contours
# More info about hierarchy of nested contours: https://docs.opencv.org/master/d9/d8b/tutorial_py_contours_hierarchy.html
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.cv2.CHAIN_APPROX_NONE)
print('Number of contours = ' + str(len(contours)))
print(contours[0])

#  cv2.drawContours(src, contours, contour_index, color, thickness) directly draw on the source image
#  if contour_index == -1, draw all contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.drawContours(img_gray, contours, -1, (0, 255, 0), 3)

# Show the image
cv2.imshow('Image', img)
cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
