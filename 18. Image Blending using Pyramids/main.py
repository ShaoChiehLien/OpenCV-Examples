import cv2
import numpy as np

# More info for Image Blending: http://pages.cs.wisc.edu/~csverma/CS766_09/ImageMosaic/imagemosaic.html
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# Generate Gaussian pyramid for apple
apple_copy = apple.copy()
gaussian_pyramid_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gaussian_pyramid_apple.append(apple_copy)

# Generate Gaussian pyramid for orange
orange_copy = orange.copy()
gaussian_pyramid_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gaussian_pyramid_orange.append(orange_copy)

# Generate Laplacian pyramid for apple
apple_copy = gaussian_pyramid_apple[5]
laplacian_pyramid_apple = [apple_copy]
for i in range(5, 0, -1):  # Do the Laplacian for 1-5, but keep the 0 as Gaussian(with color)
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid_apple[i])
    laplacian = cv2.subtract(gaussian_pyramid_apple[i-1], gaussian_expanded)  # subtract order matters!
    laplacian_pyramid_apple.append(laplacian)

# Generate Laplacian pyramid for orange
orange_copy = gaussian_pyramid_orange[5]
laplacian_pyramid_orange = [orange_copy]
for i in range(5, 0, -1):  # Do the Laplacian for 1-5, but keep the 0 as Gaussian(with color)
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid_orange[i])
    laplacian = cv2.subtract(gaussian_pyramid_orange[i-1], gaussian_expanded)  # subtract order matters!
    laplacian_pyramid_orange.append(laplacian)

# Add left and right halves of images in each level, all of them are Laplacian except n=0 is Gaussian
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(laplacian_pyramid_apple, laplacian_pyramid_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Reconstruct the image, add the smallest laplace image to the smallest gaussian image, and expand the
# image. Because the laplace image (the difference between clear and blur image) is expanded, the edges
# is also expanded and blurred to achieve the image blending effect
apple_orange_reconstruct = apple_orange_pyramid[0]  # the !GAUSSIAN! colored image that combines apple and orange
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)  # expand the new image
    # combine the expanded image with the Laplacian image
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

    #  Show the images
    #  cv2.imshow(str(i)+'apple_orange_pyramid[i]', apple_orange_pyramid[i])
    #  cv2.imshow(str(i)+'apple_orange_reconstruct', apple_orange_reconstruct)


cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
