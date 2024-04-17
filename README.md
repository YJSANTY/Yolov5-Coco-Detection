
# Water Bottle Detection using YOLOv5

This script detects water bottles in real-time video using the YOLOv5 object detection model. It draws bounding boxes around the detected water bottles and displays the annotated video stream.

Video link for complete output
https://drive.google.com/file/d/1fgGgAeKOiH5qHR2wTkil205M2u1_eLZ4/view?usp=sharing
![Screenshot (853)](https://github.com/YJSANTY/Yolov5-Coco-Detection/assets/115713790/491414dc-b24c-4bfa-b8f4-3fcc112802ed)
![Screenshot (854)](https://github.com/YJSANTY/Yolov5-Coco-Detection/assets/115713790/def17e6b-26c0-49a4-89a7-937e70b0c4d4)


## Requirements
- Python 3
- PyTorch
- OpenCV
- YOLOv5 model weights and configuration files

#Brief explanation of the process
1. Download the zip code and unzip the file.
2. Install the libraries mentioned above.
3. Run in your Python IDE.
4. It will start to run the code and automatically download the necessary files and the model from https://github.com/ultralytics/yolov5/releases
5. The webcam will activate, and you will see bounding boxes around detected water bottles in the video stream.
6. Press 'q' to exit the video stream.

## Installation
1. Install Python 3 if you haven't already.
2. Install PyTorch, OpenCV, and pandas using pip:
```
pip install torch opencv-python pandas
```
3. Clone the YOLOv5 repository:
```
git clone https://github.com/ultralytics/yolov5.git
```
4. Navigate to the cloned repository:
```
cd yolov5
```
5. Download the YOLOv5 model weights (`yolov5x.pt`) and configuration file (`yolov5x.yaml`) from the releases page: [YOLOv5 Releases](https://github.com/ultralytics/yolov5/releases)
6. Place the downloaded model weights and configuration file in the `yolov5` directory.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script (`main.py`).
3. Run the script:
```
python main.py
```
4. The webcam will activate, and you will see bounding boxes around detected water bottles in the video stream.
5. Press 'q' to exit the video stream.

## Explanation
This script utilizes the YOLOv5 object detection model to detect water bottles in real-time video streams captured from a webcam. It loads the pre-trained YOLOv5x model using PyTorch and performs inference on each frame of the video. Detected water bottles are filtered based on their class ID and annotated with bounding boxes using the OpenCV library. The annotated video stream is then displayed in a window.
