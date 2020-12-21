import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1)  # read image
img = np.zeros([512, 512, 3], np.uint8)  # create a 512*512 black image

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)  # add line
# (img var, 1st point, 2nd point, BGR, line thickness)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 5)  # add arrow
# (img var, 1st point, 2nd point, BGR, line thickness)

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 225), 3)  # add rectangle
# (img var, 1st point, 2nd point, BGR, line thickness OR fill color)
img = cv2.rectangle(img, (384, 150), (510, 200), (0, 0, 225), -1)  # add rectangle and fill it
# fill the color if 5th argument is -1

img = cv2.circle(img, (447, 63), 60, (0, 255, 0), -1)  # add circle
# (img var, center point, radius, BGR, line thickness OR fill color)

font = cv2.FONT_HERSHEY_DUPLEX  # set font
img = cv2.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)
# (img var, text, bottom left coordinate, font, font size, BGR, thickness, line type)

cv2.imshow('image', img)  # show image

cv2.waitKey(0)
cv2.destroyAllWindows()
