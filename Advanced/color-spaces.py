import cv2 as cv

img = cv.imread('../Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

# BGR ("RGB") to Grayscale
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', grayscale)

# BGR to HSV (hue, saturation, value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)

# BGR to RGB (OpenCV works with BGR format so it will display inverted color is this case)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)
