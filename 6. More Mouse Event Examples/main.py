import cv2
import numpy as np


def click_event(event, x, y, flag, param):  # call back function
    if event == cv2.EVENT_LBUTTONDOWN:  # when mouse left button is clicked
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # add a circle
        points.append((x, y))  # add a new point in the list
        if len(points) >= 2:  # connect the last two points in the list together
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 3)
        cv2.imshow('image', img)  # update the image


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)
points = []  # store all the position of points that are clicked
cv2.setMouseCallback('image', click_event)  # 'image' window is listening the mouse events

cv2.waitKey(0)
cv2.destroyAllWindows()
