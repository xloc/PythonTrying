import ImageFont, ImageDraw, Image
import numpy as np
from image_show import show

font = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 64)


def rare_appending(im, element):
    row_count_addition = 8 - im.shape[0]%8

    # print row_count_addition

    return np.append(im, [[element]*im.shape[1]]*row_count_addition, axis=0)


def char2matrix(c):
    def draw_char(text):
        # type: (string) -> Image,tuple
        sz = font.getsize(text)
        print sz

        img = Image.new("L", sz, "white")
        draw = ImageDraw.Draw(img)

        draw.text((0, 0, 0, 0), text, fill="black", font=font)

        return img, sz

    c, sz = draw_char(c)

    im = np.array(c.getdata(), np.uint8).reshape(sz[::-1])

    return im






img = char2matrix('0');


def threshold(im, val):
    # type: (np.ndarray) -> np.ndarray
    return im < val

img = threshold(img, 255/2)
img = rare_appending(img, element=False)

split = np.vsplit(img, img.shape[0]/8)
merged = np.hstack(split)

# show(img, scale=3)
# show(merged)
print merged.shape

# Merge axis -1 to axis 0
serial_data = np.packbits(merged, axis=0)
print serial_data.shape
# print serial_data



