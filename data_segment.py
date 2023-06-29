import os
import shutil
from sklearn.model_selection import train_test_split

def create_dirs(base_dir, sub_dirs):
    for sub_dir in sub_dirs:
        os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)

def move_files(file_list, org_img_dir, org_label_dir, target_dir):
    target_img_dir = os.path.join(target_dir, 'images')
    target_label_dir = os.path.join(target_dir, 'labels')
    for fn in file_list:
        shutil.move(os.path.join(org_img_dir, fn), os.path.join(target_img_dir, fn))
        shutil.move(os.path.join(org_label_dir, fn.replace('.jpg', '.txt')), os.path.join(target_label_dir, fn.replace('.jpg', '.txt')))

# 創建新目錄
base_path = "/home/Sean/Desktop"
data_store = os.path.join(base_path, 'datasets')
train_dir = os.path.join(data_store, 'train')
test_dir = os.path.join(data_store, 'test')
valid_dir = os.path.join(data_store, 'valid')

create_dirs(train_dir, ['images', 'labels'])
create_dirs(test_dir, ['images', 'labels'])
create_dirs(valid_dir, ['images', 'labels'])

# 圖像與標籤文件的目錄
org_img_dir = os.path.join(base_path, 'ultralytics', 'Self_Driving_CarV2', 'datasets', 'images')
org_label_dir = os.path.join(base_path, 'ultralytics', 'Self_Driving_CarV2', 'datasets', 'labels')

# 獲取所有圖像文件的名稱
file_names = [f for f in os.listdir(org_img_dir) if f.endswith('.jpg')]

# 將數據分割為訓練集、驗證集和測試集
train_files, test_files = train_test_split(file_names, test_size=0.2, random_state=42) 
train_files, valid_files = train_test_split(train_files, test_size=0.25, random_state=42) 

# 將對應的圖像文件和標籤文件移動到相應的目錄
move_files(train_files, org_img_dir, org_label_dir, train_dir)
move_files(valid_files, org_img_dir, org_label_dir, valid_dir)
move_files(test_files, org_img_dir, org_label_dir, test_dir)
