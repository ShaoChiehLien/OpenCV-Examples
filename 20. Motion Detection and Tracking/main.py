import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.mov')

# set the output video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mov', fourcc, cap.get(cv2.CAP_PROP_FPS), (width, height))

_, frame1 = cap.read()  # read the first frame
_, frame2 = cap.read()  # read the second frame

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)  # only consider the part that moves between two frames
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # Convert the color to gray to reduce noise from color
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Mix the similar gray area by blurring to reduce noise

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)  # Set pixels with value from 20-255 to white
    dilated = cv2.dilate(thresh, None, iterations=3)  # Amplify the white area and reduce noise
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find the contour

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:  # if contour's area < 900, jump out of the for loop
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)  # if the area is large enough, add a rectangle

    out.write(frame1)  # write the result in out.mov

    cv2.imshow('real time motion detection', frame1)

    #  compare current frame 2 and its following frame in next loop
    frame1 = frame2
    _, frame2 = cap.read()

    # if esc is pressed, end the while loop
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()
