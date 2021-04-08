import cv2 as cv

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Boston', img)

# 1. Converting to grayscale
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grayImage)

# Blur
blurredImage = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# (5, 5) is the size of the gaussian kernel that is applied on the image
cv.imshow('Blur', blurredImage)

# Find Edges (using Canny algorithm)
cannyImage = cv.Canny(img, 300, 500)  # the 2 last arguments are threshold values related to Canny algorithm
cv.imshow('Canny', cannyImage)

# Dilating the image
dilatedImage = cv.dilate(cannyImage, (3, 3), iterations=3)
cv.imshow('Dilated', dilatedImage)

# Eroding the image (opposite of dilating)
eroded = cv.erode(dilatedImage, (3, 3), iterations=3)
cv.imshow('Eroded', eroded)

cv.waitKey(0)