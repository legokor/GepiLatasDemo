import cv2

from buttons import BUTTONS
from trackbars import TRACKBARS


KEY_ESC = 27
WINDOW_NAME = 'main'


def populate_toolbars():
    for name, args in BUTTONS.items():
        cv2.createButton(name, **args)
    for name, args in TRACKBARS.items():
        cv2.createTrackbar(name, WINDOW_NAME, *args)


if __name__ == '__main__':
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
    populate_toolbars()

    while cv2.waitKey(30) != KEY_ESC:
        pass
