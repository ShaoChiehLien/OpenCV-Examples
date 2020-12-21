import cv2

img = cv2.imread('lena.jpg', 1)  # read file in color
img1 = cv2.imread('lena.jpg', 0)  # read file in grayscale

print(img1)  # print array in numpy

cv2.imshow('image', img1)  # show image on a new opened window
k = cv2.waitKey(5000)  # wait 5 sec and store the read in char

if k == 27:  # if 'esc' is pressed
    cv2.destroyAllWindows()  # close all winder
elif k == ord('s'):  # if 's' is pressed
    cv2.destroyAllWindows()
    cv2.imwrite('lena_copy.png', img1)
