import cv2

from utils import *


UNCHECKED = 0
CHECKED = 1


@update_global_image_var
@display_returned_image
def load_image(*_):
    return cv2.imread('resources/test.jpeg', cv2.IMREAD_COLOR)


@update_global_image_var
@display_returned_image
def toggle_hsv(img, btn_state, *_):
    if btn_state == CHECKED:
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    else:
        return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)


# 'buttonType' values:
#     one of: QT_CHECKBOX / QT_PUSH_BUTTON / QT_RADIOBOX
#     QT_NEW_BUTTONBAR is kinda like a linebreak

BUTTONS = {
    'Load image': {'onChange': load_image},
    'Toggle HSV': {'onChange': toggle_hsv, 'buttonType': cv2.QT_CHECKBOX},
}
