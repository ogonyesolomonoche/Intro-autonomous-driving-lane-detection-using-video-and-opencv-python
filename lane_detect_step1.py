# Import the opencv library
import cv2

# We Load the video path
cap = cv2.VideoCapture("road_vid.mp4")  # ".."represents the video path (can be changed
# to your desired video path)

# Set the Frame Width and Height ( you can change to your desired Frame Width and Height )
cap.set(4, 640)  # set Width
cap.set(3, 480)  # set Height

while True:

    # The Captured video frame is read
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # The "s" button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('s'):  # you can change to your desired button of your choice
        break

# After the loop release the cap object
cap.release()
# All OpenCV windows are closed
cv2.destroyAllWindows()
