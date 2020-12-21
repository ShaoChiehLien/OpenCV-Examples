import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)  # print out all the events


def click_event(event, x, y, flag, param):  # call back function
    if event == cv2.EVENT_LBUTTONDOWN:  # when mouse's left button is clicked
        print(x, ', ', y)
        font = cv2.FONT_ITALIC  # set font type
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2)  # add text on img
        cv2.imshow('image', img)  # show image on 'image' window
    if event == cv2.EVENT_RBUTTONDOWN:  # when mouse's right button is clicked
        # opencv stores image matrix is (height, width, channel) format
        blue = img[y, x, 0]  # channel = 0, blue
        green = img[y, x, 1]  # channel = 0, green
        red = img[y, x, 2]  # channel = 0, red
        font = cv2.FONT_ITALIC  # set font type
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)  # add text on img
        cv2.imshow('image, img')  # show image on 'image' window


img = cv2.imread('lena.jpg')
cv2.imshow('image', img)  # show the image on 'image' window

cv2.setMouseCallback('image', click_event)  # listen mouse event on 'image' window

cv2.waitKey(0)
cv2.destroyAllWindows()