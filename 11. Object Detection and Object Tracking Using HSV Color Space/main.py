import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)  # Access the computer camera

#  Create trackbar for lower and upper bound of HSV
cv2.namedWindow('Tracking Image')
cv2.createTrackbar('LH', 'Tracking Image', 0, 255, nothing)  # range from 0 to 255, with initial value = 0
cv2.createTrackbar('LS', 'Tracking Image', 43, 255, nothing)  # range from 0 to 255, with initial value = 43
cv2.createTrackbar('LV', 'Tracking Image', 107, 255, nothing)  # range from 0 to 255, with initial value = 107
cv2.createTrackbar('UH', 'Tracking Image', 255, 255, nothing)  # range from 0 to 255, with initial value = 255
cv2.createTrackbar('US', 'Tracking Image', 255, 255, nothing)  # range from 0 to 255, with initial value = 255
cv2.createTrackbar('UV', 'Tracking Image', 255, 255, nothing)  # range from 0 to 255, with initial value = 255

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 360))

    # convert the frame's color storage method from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get the current value of HSV bound
    l_h = cv2.getTrackbarPos('LH', 'Tracking Image')
    l_s = cv2.getTrackbarPos('LS', 'Tracking Image')
    l_v = cv2.getTrackbarPos('LV', 'Tracking Image')
    u_h = cv2.getTrackbarPos('UH', 'Tracking Image')
    u_s = cv2.getTrackbarPos('US', 'Tracking Image')
    u_v = cv2.getTrackbarPos('UV', 'Tracking Image')

    # set up an array contains the lower and upper bound of the HSV value
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # create a mask that could mask out the colors that are out of the HSV range
    mask = cv2.inRange(hsv, l_b, u_b)

    # use bitwise_and to do the mask
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)  # show the original frame
    cv2.imshow('mask', mask)  # show the mask, only the color that is in the HSV boundary would be white
    cv2.imshow('res', res)  # show the result

    key = cv2.waitKey(1)

    if key == 27:  # if exc is pressed, exit the loop
        break

cap.release()
cv2.destroyAllWindows()
