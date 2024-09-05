import cv2

# Open the video stream from the IP camera
cap = cv2.VideoCapture(1)

# Check if the stream opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Continuously capture frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was not captured properly, break the loop
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Display the captured frame
    cv2.imshow('Camera Capture', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
