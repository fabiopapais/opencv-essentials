import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats 2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Cats', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel (computes edges gradients in x and y)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=11)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=11)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel Combined', combined_sobel)

# Canny algorithm
canny = cv.Canny(img, 50, 100)
cv.imshow('Canny', canny)

cv.waitKey(0)