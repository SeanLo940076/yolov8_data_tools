# image_to_video

import cv2
import os
import random

img = cv2.imread(r"C:\Users\Sean\Desktop\8500ALL\1.jpg")  # 讀取保存的任意一張圖片
fps = 24 # 設定影片的FPS
size = (img.shape[1],img.shape[0])  # 得到圖片大小資訊
print(size)
fourcc = cv2.VideoWriter_fourcc(*"XVID") # 影片編碼格式

# 根據圖片大小，創建寫入資訊(文件名稱，編碼器格式，幀數，影像大小)
videoWrite = cv2.VideoWriter(r"C:\Users\Sean\Desktop\NTUT_realtime_result_FPS24.avi",fourcc,fps,size)

files = os.listdir(r"C:\Users\Sean\Desktop\8500ALL")
out_num = len(files)
for i in tqdm(range(1, out_num)):
    fileName = "C:/Users/Sean/Desktop/8500ALL/" + str(i)+ '.jpg' # 利用迴圈讀取所有圖片，並以數字命名
    img = cv2.imread(fileName)
    videoWrite.write(img) # 將圖片輸入到影片框架中
videoWrite.release() # 釋放了才算是完成寫入，連續寫入多個影片的時候這個很關鍵
