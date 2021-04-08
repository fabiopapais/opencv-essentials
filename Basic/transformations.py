import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Boston', img)

# Translation
def translate(img, x, y):
    translationMatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translationMatrix, dimensions)
    # Essentially what we are doing using warpAffine is
    # matrix multiplication and vector additions:
    # https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html

translatedImage = translate(img, 100, -50)
cv.imshow('Translated', translatedImage)


# Rotation
def rotate(img, angle, rotpoint=None):
    (height, width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width // 2, height // 2)

    # this time, we are getting the rotation matrix from opencv
    rotationMatrix = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotationMatrix, dimensions)

rotatedImage = rotate(img, -45, (100, 200))
cv.imshow('Rotated', rotatedImage)


# Resizing (another nice way that ignores aspect ratio)
resizedImage = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resizedImage)

# Flipping
flippedImage = cv.flip(img, -1)  # The flip code specifies how your image will be flipped
cv.imshow('Flip', flippedImage)

# Cropping (not an opencv method, but useful, since images are arrays)
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()
