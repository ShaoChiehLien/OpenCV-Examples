import cv2
import numpy as np

# Use np.zeros to create a black image and add a white rectangle
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

# Use np.full to create a white image and add a black rectangle
img2 = np.full((250, 500, 3), 255, np.uint8)
img2 = cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)

# Use bit operation on two only black and white image
bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

# Show the result
cv2.imshow('image 1', img1)
cv2.imshow('image 2', img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

# Use bit operation on one black-white image and one colored image
# Check Hue diagram for the bit operation on colored image
colored_image = cv2.imread('messi5.jpg')
img2 = cv2.resize(img2, (548, 342))  # bitwise operation required two same size image
bitAnd = cv2.bitwise_and(colored_image, img2)
bitOr = cv2.bitwise_or(colored_image, img2)
bitXor = cv2.bitwise_xor(colored_image, img2)
bitNot1 = cv2.bitwise_not(colored_image)

# Show the result
cv2.imshow('colored_image', colored_image)
cv2.imshow('image 2', img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
