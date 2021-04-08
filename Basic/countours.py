import cv2 as cv
import numpy as np

# Very simple processes to find contors on an image

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cat', img)

# 1. Grayscaling the image
grayscaleImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grayscaleImage)

# 2. Thresholding (binarizing) the image
ret, thresh = cv.threshold(grayscaleImage, 175, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded image', thresh)

# 3. Eroding the image
erodedImage = cv.erode(thresh, (30, 30), iterations=3)
cv.imshow('Eroded', erodedImage)

# Find the contours
contours, hierarchies = cv.findContours(erodedImage, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Drawing the contours into a blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0, 255, 0), thickness=1)
cv.imshow('Contours', blank)

cv.waitKey(0)
cv.destroyAllWindows()