import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # openCV use BGR white matplotlib use RGB

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)  # depth = -1, means the same depth as the source

# Same weight in the kernel
blur = cv2.blur(img, (5, 5))  # set kernel size to 5*5, could be rectangle

# The further to the center point, the lower its weight
gaussianBlur = cv2.GaussianBlur(img, (5, 5), 0)  # set kernel size to 5*5, could be rectangle

# Replace each pixel's value with the median of its neighboring pixels
# Note: Great when dealing with 'Salt and Pepper Noise'
medianBlur = cv2.medianBlur(img, 5)  # set kernel size 5*5, could only be square

# bilateralFilter(src, d, sigmaColor, sigmaSpace)
# d: Diameter of each pixel neighborhood that is used during filtering
# sigmaColor: A larger value of the parameter means that farther colors within
# the pixel neighborhood (see sigmaSpace) will be mixed together
# sigmaSpace:  A larger value of the parameter means that farther pixels will
# influence each other as long as their colors are close enough
# Note: Great with blurring image while keeping its edge sharpe
bilateralFiler = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Concolution', 'blur', 'GaussianBLur', 'median', 'bilateralFilter']
images = [img, dst, blur, gaussianBlur, medianBlur, bilateralFiler]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')

    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
