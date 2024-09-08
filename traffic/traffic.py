import cv2

# Open the video file
cap = cv2.VideoCapture('video.avi')

# Load the pre-trained car classifier
car_cascade = cv2.CascadeClassifier('cars.xml')

# Initialize the counter and storage for vehicle positions
count = 0
cars_tracked = []

# Define the position of the counting line
line_position = 400

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars in the grayscale frame
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # Draw the counting line
    cv2.line(frame, (0, line_position), (frame.shape[1], line_position), (0, 255, 0), 2)

    # List to hold the current frame's car positions
    new_cars_tracked = []

    for (x, y, w, h) in cars:
        # Calculate the center of the detected car
        center_y = y + h // 2

        # Draw a rectangle around the detected car
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Only count the car if it crosses the counting line
        if center_y > line_position:
            new_cars_tracked.append((x, y, w, h))

    # Update the counter based on cars that crossed the line
    for car in new_cars_tracked:
        if car not in cars_tracked:
            count += 1
            cars_tracked.append(car)

    # Display the counter on the video frame
    cv2.putText(frame, f"VEHICLE COUNTER: {count}", (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Show the updated frame
    cv2.imshow('Output', frame)

    # Exit the loop if the 'Enter' key is pressed
    if cv2.waitKey(100) == 13:
        print(count)
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
