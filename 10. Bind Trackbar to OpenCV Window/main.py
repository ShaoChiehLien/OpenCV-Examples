import numpy as np
import cv2


def nothing(x):
    print(x)


cv2.namedWindow('image')  # create a window named 'image'

# add trackbars named 'R', 'G', 'B', range from 0 to 255 on window 'image'
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
# add a trackbar named 'gray', range from 0 to 1 on window 'image'
cv2.createTrackbar('gray', 'image', 0, 1, nothing)

while True:
    # must read the original colored image, because cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # could only convert colored to gray. Gray to gray would show an error
    img = cv2.imread('lena.jpg')

    # Create img1 with the BGR value that read from the trackbar
    img1 = np.zeros(img.shape, np.uint8)
    img1[:, :, 0] = cv2.getTrackbarPos('B', 'image')
    img1[:, :, 1] = cv2.getTrackbarPos('G', 'image')
    img1[:, :, 2] = cv2.getTrackbarPos('R', 'image')

    gray = cv2.getTrackbarPos('gray', 'image')

    key = cv2.waitKey(1)

    if key == 27:  # check if 'esc' is pressed
        break

    if gray == 0:  # check if gray scale is off
        img = cv2.add(img, img1)  # add the original colored image with the BGR value from trackbar
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert the original colored image to grayscale
        # Note: cv2.cvtColor(var, cv2.COLOR_BGR2GRAY), could only convert COLORED image to grayscale
        # can't convert an already grayscale image to grayscale

    img = cv2.imshow('image', img)

cv2.destroyAllWindows()
