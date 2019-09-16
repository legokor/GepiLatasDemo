import cv2

from utils import *


@display_returned_image
def canny_demo(img, slider_val):
    if len(img.shape) > 2:  # TODO: assume BGR for now
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        grey = img

    blurred = cv2.blur(grey, (3, 3))
    edges = cv2.Canny(blurred, slider_val, slider_val * 3.5, apertureSize=3)

    return grey * (edges != 0)


# 'name of trackbar': [initial value, max value, callback func]
#     order matters!

TRACKBARS = {
    'Canny edge detection': [50, 100, canny_demo],
}
