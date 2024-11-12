# Snake_HandMotion_Control
This innovative project combines the classic Snake game with gesture control, utilizing advanced technologies such as MediaPipe, OpenCV, and Pygame. The goal is to allow users to control the snake solely through hand gestures, providing an immersive and interactive gaming experience.
https://github.com/user-attachments/assets/d9ad1933-4efb-474c-9c34-cccc0d3f0cff
# Demo 
Here's how you can run snake game using hand gestures 
```python
python main.py
```
# Directory
```tree
.
├── model
│   ├── keypoint_classifier
│   │   ├── keypoint_classifier_label.csv
│   │   ├── keypoint_classifier.keras
│   │   ├── keypoint_classifier.py
│   │   ├── keypoint_classifier.tflite
│   │   └── keypoint.csv
│   ├── point_history_classifier
│   │   ├── point_history_classifier_label.csv
│   │   ├── point_history_classifier.hdf5
│   │   ├── point_history_classifier.py
│   │   ├── point_history_classifier.tflite
│   │   └── point_history.csv
│   └── __init__.py
├── src
│   ├── game.py
│   └── gestures_manager.py
├── utils
│   ├── __init__.py
│   └── cvfpscalc.py
├── main.py
├── README.md
└── requirements.txt
```
# Classifier Model Architecture 
![102246771-7481ff00-3f42-11eb-8ddf-9e3cc30c5816](https://github.com/user-attachments/assets/20146fa6-7500-4207-9e34-2a6e015aaf4e)

