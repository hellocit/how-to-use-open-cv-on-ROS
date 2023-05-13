#!/usr/bin/env python3

import cv2
from datetime import datetime
import time
import os

deviceid = 4  # USB接続の順番に依存します
capture = cv2.VideoCapture(deviceid)

save_directory = "photo_by_cv2"  # 写真の保存先ディレクトリ名

# 保存先ディレクトリが存在しない場合は作成します
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

while True:
    ret, frame = capture.read()

    if ret:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        image_path = os.path.join(save_directory, f"{current_time}.jpg")
        cv2.imwrite(image_path, frame)
        print(f"画像が保存されました: {image_path}")
    else:
        print("フレームをキャプチャできませんでした。")

    time.sleep(1)  # 1秒待機

capture.release()
