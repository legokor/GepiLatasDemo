import cv2

from utils import *


@update_global_image_var
@display_returned_image
def load_image(*_):
    return cv2.imread('resources/test.jpeg', cv2.IMREAD_COLOR)


# 'buttonType' values:
#     one of: QT_CHECKBOX / QT_PUSH_BUTTON / QT_RADIOBOX
#     QT_NEW_BUTTONBAR is kinda like a linebreak

BUTTONS = {
    'Load image': {'onChange': load_image},
}
