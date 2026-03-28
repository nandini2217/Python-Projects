import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimensions = (width, height)

# to get video in avi format
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("test.mp4",fourcc,30.0,dimensions)

# how long the video will be recorded
now_time=time.time()
duration=10+4
end_time=now_time + duration

# recording the video
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    output.write(frame)

    if time.time() > end_time:
        break

# releasing the video 
output.release()
print("Video Recorded Successfully")

