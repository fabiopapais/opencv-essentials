import cv2 as cv

img = cv.imread('../Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

# split image into rgb channels
b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', r)
cv.imshow('Red', r)

# merge images into one image (that is equal to the first)
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

cv.waitKey(0)