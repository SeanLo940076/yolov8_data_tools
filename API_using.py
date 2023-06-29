from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("yolov8x.pt")
# model = YOLO("./runs/detect/yolov8n_Self_Driving_3070/weights/best.pt")
#model = YOLO("./runs/detect/yolov8n_Self_Driving_3070/weights/best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source=r"C:\Users\Sean\Desktop\ultralytics\datasets\Test_model\FPS_8.mp4", show=True)
# results = model.predict(source=1, show=True)
results = model.predict(source=r"C:\Users\Sean\Desktop\ultralytics\datasets\Test_model\FPS_8.mp4")