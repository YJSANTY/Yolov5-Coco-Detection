import torch
import cv2
import pandas
from PIL import Image
import requests

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

# Set the model to inference mode
model.eval()

# Function to perform object detection on a frame and filter out water bottles
def detect_water_bottles(frame):
    # Perform inference
    results = model(frame)

    # Filter out detections corresponding to the class "water bottle" (class ID: 39)
    water_bottle_detections = results.pred[0][results.pred[0][:, -1] == 39]

    # Draw bounding boxes for water bottle detections
    for detection in water_bottle_detections:
        box = detection[:4].int().tolist()
        frame = cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

    return frame

# Open video capture device (webcam)
video_capture = cv2.VideoCapture(0)

# Loop to read frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # If the frame was not read correctly, break the loop
    if not ret:
        break

    # Perform object detection and filter out water bottles
    annotated_frame = detect_water_bottles(frame)

    # Display the annotated frame
    cv2.imshow('Water Bottle Detection', annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close the OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
