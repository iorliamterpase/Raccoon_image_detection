from ultralytics import YOLO

model= YOLO('raccoon_best.pt') #load trained model


results= model('C:\\Users\\HP\\OneDrive\\Desktop\\Raccoon_detector_yolov8\\download.jpeg')

print(results)
