import cv2 as cv
import numpy as np

# Creates a 'blank' (actually all black) image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the (or part of) image in a certain color
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)

# 2. Draw a rectangle
# cv.rectangle receives (image, point1, point2, color, thickness, lineType)
cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=2)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), thickness=2)
cv.imshow('Text', blank)


# A nice example
ifpeBlank = np.zeros((700, 500, 3), dtype='uint8')
cv.rectangle(ifpeBlank, (270, 20), (480, 230), (0, 255, 0), thickness=cv.FILLED)
cv.rectangle(ifpeBlank, (20, 270), (230, 480), (0, 255, 0), thickness=cv.FILLED)
cv.rectangle(ifpeBlank, (270, 270), (480, 480), (0, 255, 0), thickness=cv.FILLED)
cv.circle(ifpeBlank, (125, 125), 105, (0, 0, 255), thickness=cv.FILLED)
cv.putText(ifpeBlank, 'IFOS', (20, 650), cv.FONT_HERSHEY_TRIPLEX, 6.0, (255, 255, 255), thickness=3)
cv.imshow('IFOS', ifpeBlank)

cv.waitKey(0)

