import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

import tensorflow_datasets as tfds


#Added camera functionality via openCV library
#Close video by pressing 'q' key
import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = cam.read()
    cv2.imshow("Live Camera", img)
    key = cv2.waitKey(1) & 0Xff
    if key == ord('t'):
        cam.release()
        break

