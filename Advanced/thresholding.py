import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Cats Grayscale', gray)

# Thresholding is a technique in which you can binarize an image by specifing a limit value

# Simple (absolute) Thresholding
# cv.threshold receives: image, thresh value, max_val (the value that will be put) and mode
threshold, thresholdedImage = cv.threshold(gray, 150, 150, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresholdedImage)

# Adaptive Thresholding
# cv.adaptiveThreshold receives: image, thresh value, max_val (the value that will be put) and mode
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_threshold)

cv.waitKey(0)