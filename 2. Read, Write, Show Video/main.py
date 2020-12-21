import cv2

# cap = cv2.VideoCapture(0)  # using the computer camera
cap = cv2.VideoCapture('IMG_2070.MOV')  # using the existing videos

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4v is for .MOV file
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # width of video
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # height of video
print(cap.get(cv2.CAP_PROP_FPS))  # fps of video, the higher the frame is, the faster the output video is
out = cv2.VideoWriter('output.MOV', fourcc, cap.get(cv2.CAP_PROP_FPS), (1920, 1080))
# width and height of input and output video must be the same

while cap.isOpened():  # show the video frame by frame
    ret, frame = cap.read()  # ret = 1 if cap is read and store in frame
    if ret:
        # cv2.imshow('frame', frame)  # show the frame
        out.write(frame) # write the original frame to out's frame

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # change the color to gray
        cv2.imshow('frame', gray)  # show to converted frame

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
