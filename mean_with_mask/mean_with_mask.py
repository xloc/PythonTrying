import cv2
import numpy as np

im = cv2.imread('./mrliu.png')



mk = np.zeros(im.shape)

cv2.circle(im, (30, 30), radius=5, color=(255, 255, 255))

cv2.imshow('show', im)


cv2.waitKey(0)