
# Water Bottle Detection using YOLOv5


## Explanation
This script utilizes the YOLOv5 object detection model to detect water bottles in real-time video streams captured from a webcam. It loads the pre-trained YOLOv5x model using PyTorch and performs inference on each frame of the video. Detected water bottles are filtered based on their class ID and annotated with bounding boxes using the OpenCV library. The annotated video stream is then displayed in a window.

Video link for complete output
https://drive.google.com/file/d/1fgGgAeKOiH5qHR2wTkil205M2u1_eLZ4/view?usp=sharing


![Screenshot (853)](https://github.com/YJSANTY/Yolov5-Coco-Detection/assets/115713790/491414dc-b24c-4bfa-b8f4-3fcc112802ed)
![Screenshot (854)](https://github.com/YJSANTY/Yolov5-Coco-Detection/assets/115713790/def17e6b-26c0-49a4-89a7-937e70b0c4d4)


## Requirements
- Python 3
- PyTorch
- OpenCV
- YOLOv5 model weights and configuration files

## Brief explanation of the process
1. Download the zip code and unzip the file.
2. Install the libraries mentioned above.
3. Run the script in your Python IDE.
4. It will start to run the code and automatically download the necessary files and the model from https://github.com/ultralytics/yolov5/releases
5. The webcam will activate, and you will see bounding boxes around detected water bottles in the video stream.
6. Press 'q' to exit the video stream.

## Code Explanation
Libraries: The script imports necessary libraries like torch, cv2, pandas, PIL, and requests.

Loading YOLOv5 Model: Utilizes torch.hub.load() to load the pre-trained YOLOv5 model (yolov5x).

Inference Mode: Sets the model to inference mode using model.eval().

Object Detection Function: detect_water_bottles() identifies water bottles in webcam frames, filtering out other objects.

Capturing Video Frames: cv2.VideoCapture() captures frames from the webcam.

Object Detection Loop: Each frame is passed through detect_water_bottles(), annotating detected water bottles with bounding boxes using cv2.rectangle().

Exiting the Loop: The program continues until 'q' is pressed, releasing the video capture device and closing OpenCV windows.

