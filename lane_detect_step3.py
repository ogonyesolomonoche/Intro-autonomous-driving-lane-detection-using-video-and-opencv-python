# Import the opencv and numpy libraries
import cv2
import numpy as np

# We Load the video path
cap = cv2.VideoCapture("road_vid.mp4")  # ".."represents the video path (can be changed
# to your desired video path)

# Set the Frame Width and Height ( you can change to your desired Frame Width and Height )
cap.set(4, 640)  # set Width
cap.set(3, 480)  # set Height


# We Define the Video as Canny Image
def canny(img):
    if img is None:
        cap.release()
        cv2.destroyAllWindows()
        exit()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to GrayScale
    kernel = 5
    blur = cv2.GaussianBlur(gray, (kernel, kernel), 0)  # Convert to Blur
    canny = cv2.Canny(blur, 50, 150)  # Convert to Canny Image
    return canny


# We Define the ROI From the Canny Image
def region_of_interest(canny):
    height = canny.shape[0]  # The Height of the Frame
    width = canny.shape[1]  # The Width of the Frame
    mask = np.zeros_like(canny)
    triangle = np.array([[  # We Draw a Triangle to the Canny
        (0, height),        # You can change the Triangle Geometry to your desired choice to fit your ROI
        (width / 1.95, height / 1.5),
        (478, height), ]], np.int32)
    cv2.fillPoly(mask, triangle, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image


while True:

    # The Captured video frame is read
    ret, frame = cap.read()

    # Display the resulting frame
    canny_image = canny(frame)
    cropped_canny = region_of_interest(canny_image)
    cv2.imshow("cropped_canny", cropped_canny)

    # The "s" button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('s'):  # you can change to your desired button of your choice
        break

# After the loop release the cap object
cap.release()
# All OpenCV windows are closed
cv2.destroyAllWindows()
