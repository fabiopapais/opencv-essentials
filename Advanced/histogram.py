import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Resources/Photos/lady.jpg')

# Grayscale Histogram
grayscaleImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Lady', grayscaleImage)
# cv.calcHist() receives: images: Any, channels: Any, mask: Any, histSize: Any, ranges: Any,
gray_hist = cv.calcHist([grayscaleImage], [0], None, [256], [0, 256])

# using pyplot to show the histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Color Histogram
# preparing the pyplot figure
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    # cv.calcHist() receives: images: Any, channels: Any, mask: Any, histSize: Any, ranges: Any
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    # plotting each channel separately
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)