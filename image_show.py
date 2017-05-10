import cv2
import numpy as np


def show(im, scale=1):
    im = np.array(im, dtype=np.uint8)

    im = cv2.equalizeHist(im);
    # im = cv2.resize(im, dsize=(0, 0), fx=scale, fy=scale)

    cv2.imshow('show', im)
    cv2.waitKey(0)


def show_image(im):
    for row in im:
        r = []
        for px in row:
            if px:
                r.append('x')
            else:
                r.append(' ')

        print "".join(r)