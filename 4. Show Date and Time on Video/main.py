import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # print the width and height of the video
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()  # read each frame
    if ret:  # if frame is read in
        # set up font and text
        font = cv2.FONT_ITALIC
        text = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) \
               + ' Height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        text += ' ' + str(datetime.datetime.now())

        # add text to frame
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # show frame
        cv2.imshow('frame', frame)

        # break if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

