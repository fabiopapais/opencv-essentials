import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging (simple, but not natural)
average = cv.blur(img, (15, 15))
cv.imshow('Average', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (15, 15), 0)
cv.imshow('Gaussian', gaussian)

# Median Blur
median = cv.medianBlur(img, 15)
cv.imshow('Median', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 30, 40, 40)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)