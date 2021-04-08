import cv2 as cv


# Function to rescale images, videos and live videos
def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading video example
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')  # use 0 or 1 to capture webcam video

if not capture.isOpened():
    print("Error opening video stream or file")

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        # Using our function to rescale the frame by 0.5
        frame_resized = rescaleFrame(frame, 0.5)

        # Display the resulting frames
        cv.imshow('Frame', frame)
        cv.imshow('Frame resized', frame_resized)

        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
