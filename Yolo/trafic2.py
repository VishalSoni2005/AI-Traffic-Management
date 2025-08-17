import cv2  # Ensure OpenCV is imported
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Define custom label mapping
custom_labels = {
    "car": "vehicle",
    "truck": "vehicle",
    "bus": "vehicle",
    "motorcycle": "vehicle",
    "bicycle": "vehicle",
    "cell phone": "vehicle"  # Rename cell phone to 'vehicle' as well
}

# Path to the video file (0 for webcam or provide the actual video path)
vpath = 'toytraffic.mp4'

# Open the video file
cap = cv2.VideoCapture('https://192.168.0.106:8080/video')

# Check if video opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file {vpath}")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model.predict(source=frame, conf=0.3)  # Adjust confidence as needed

    # Process results
    for result in results:
        for detection in result.boxes:
            # Convert tensor to numpy array
            boxes = detection.xyxy.cpu().numpy()  # Bounding box coordinates
            class_ids = detection.cls.cpu().numpy()  # Class IDs
            confidences = detection.conf.cpu().numpy()  # Confidence scores

            # Draw bounding boxes and labels
            for box, class_id, confidence in zip(boxes, class_ids, confidences):
                x1, y1, x2, y2 = map(int, box)  # Convert coordinates to integers
                class_id = int(class_id)  # Convert class ID to integer
                confidence = float(confidence)  # Convert confidence to float

                # Get class name based on the ID, or default to 'Unknown'
                class_name = model.names[class_id] if class_id < len(model.names) else "Unknown"

                # Check if class name exists in custom_labels, else use the original class name
                class_name = custom_labels.get(class_name, class_name)

                # Define colors
                blue = (255, 0, 0)  # Color for bounding box
                white = (255, 255, 255)  # Color for text

                # Draw background rectangle for the label
                text_size, _ = cv2.getTextSize(f"{class_name}: {confidence:.2f}", cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)
                text_w, text_h = text_size
                cv2.rectangle(frame, (x1, y1 - text_h - 10), (x1 + text_w, y1), blue, cv2.FILLED)

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), blue, 2)
                cv2.putText(frame, f"{class_name}: {confidence:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, white, 2)

    # Display the frame with annotations
    cv2.imshow("Detection", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()