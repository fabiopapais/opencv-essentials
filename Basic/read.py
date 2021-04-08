# OpenCV is always imported as cv (mainly because of the C API, which is denoted as cv and C++ API, which is denoted
# as cv)
import cv2 as cv

# Reading images
img = cv.imread('./Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)
# cv.waitKey waits for specified milliseconds and returns all the pressed keys
cv.waitKey(0)

# Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')  # use 0 or 1 to capture webcam video

# Check if file/camera opened successfully
if not capture.isOpened():
    print("Error opening video stream or file")

# Read until video is completed
while capture.isOpened():
    # Capture frame-by-frame
    ret, frame = capture.read()
    if ret:
        # Display the resulting frame
        cv.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

# Releases the capture object
capture.release()
cv.destroyAllWindows()

# If you receive an error like "(-215:Assertion failed)" is because opencv couldn't find the file,
# in this case, the next frame
