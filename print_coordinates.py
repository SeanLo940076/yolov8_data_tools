import cv2
import random
from ultralytics import YOLO
model = YOLO('yolov8x-seg.pt')

# Set the confidence threshold for object detection
conf_thresh = 0.25

# Disable confidence display in bounding boxes
hide_conf = True

cap = cv2.VideoCapture('2.mp4')
frame_id = 0
while cap.isOpened():
    # img = cv2.imread('img0.jpg')
    ret, img = cap.read()
    if ret:
        results = model.predict(img, stream=True)

        # run prediction on img
        for result in results:
            boxes = result.boxes.cpu().numpy() # get boxes on cpu in numpy
            for box in boxes: # iterate boxes
                r = box.xyxy[0].astype(int) # get corner points as int
                class_name = result.names[int(box.cls[0])]
                print(class_name, r) # print boxes
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # generates random RGB values
                cv2.rectangle(img, tuple(r[:2]), tuple(r[2:]), color, 2)

        cv2.imshow('Frame', img)
        # cv2.imwrite(f'frame{frame_id}.jpg', img)
        frame_id += 1
        if cv2.waitKey(130) & 0xFF == ord('Q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows() # THIS IS GIVING ME BOUNDING BOXES ONLY HOW CAN I GET CLASSES USING THIS