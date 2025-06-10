from ultralytics import YOLO
model = YOLO('yolov8x')

model.predict("./input_videos/ss1_tennisMatch.png", save=True)
