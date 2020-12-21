import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo-white.png')

cv2.imshow('original image', img)

# replace img[273:333, 100:160] with ball
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
cv2.imshow('added ball', img)

img = cv2.resize(img, (548, 342))  # cv2.add requires two images with the same size
img2 = cv2.resize(img2, (548, 342))  # use cv2.resize to to resize the two images

dst_without_weight = cv2.add(img, img2)  # cv2.add directly with 1 and 1 weighted, may exceed 255
dst_with_weight = cv2.addWeighted(img, .8, img2, .2, 0)  # sum of weight should be 1 to remain below 255

cv2.imshow('use cv2.add', dst_without_weight)
cv2.imshow('use cv2.addWeighted', dst_with_weight)
cv2.waitKey(0)
cv2.destroyAllWindows()
