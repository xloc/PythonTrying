import cv2
import numpy as np

img = cv2.imread('/Users/oliver/Desktop/a.jpg')

trn,  a = cv2.imencode('.jpg', img)


# c = np.arange(10)
# c.dtype


print a.dtype

cv2.imshow('test', img)

cv2.waitKey(0)
