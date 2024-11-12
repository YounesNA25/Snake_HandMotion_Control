# Snake_HandMotion_Control
This innovative project combines the classic Snake game with gesture control, utilizing advanced technologies such as MediaPipe, OpenCV, and Pygame. The goal is to allow users to control the snake solely through hand gestures, providing an immersive and interactive gaming experience.
https://private-user-images.githubusercontent.com/149947081/385327449-b39c8d6f-b9ab-4c2a-bca5-5e4c31de2dac.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE0MjI1NDcsIm5iZiI6MTczMTQyMjI0NywicGF0aCI6Ii8xNDk5NDcwODEvMzg1MzI3NDQ5LWIzOWM4ZDZmLWI5YWItNGMyYS1iY2E1LTVlNGMzMWRlMmRhYy5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTEyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTExMlQxNDM3MjdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05M2NiMmM0YzY3ZTk5ZGM0MTFkNTY5ZWU3MGJiYTg5OTMzMTQ0NWQ2ZWRiNTUwMzE4YjgwNTgyMjg3M2E0ZjhhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.OauO9VL_sGdaZEH-zRdOoW0NFswJ0cArK7DoJE3NT_c
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

