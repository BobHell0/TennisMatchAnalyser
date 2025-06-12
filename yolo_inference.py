from ultralytics import YOLO
model = YOLO('yolov8x')

results = model.predict("./input_videos/vid1_tennisMatch.mp4", save=True)

for box in results[0].boxes:
    print(box)
