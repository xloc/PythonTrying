import os
from glob import glob

import cv2
import numpy as np


img_paths = glob(os.path.expanduser('~/Downloads/imgs/*.JPG'))

for i, ip in enumerate(img_paths):
    rst_img = None
    img = cv2.imread(ip)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img = cv2.resize(img, dsize=(480, 340))

    for l, h in [(0,90), (90, 124), (124, 180)]:
        im = cv2.inRange(img, (l, 43, 46), (h, 255, 255))

        if rst_img is None:
            rst_img = im
        else:
            rst_img = np.hstack([rst_img, im])

    cv2.imwrite(os.path.expanduser('~/Downloads/{}.jpg'.format(i)), rst_img)

    # raw_input('enter to next')