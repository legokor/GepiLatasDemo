import os
import cv2

from buttons import BUTTONS
from trackbars import TRACKBARS

from utils import init_windows


KEY_ESC = 27
WINDOW_NAME = 'main'
ROOT_WINDOW = None


def populate_toolbars():
    for name, args in BUTTONS.items():
        cv2.createButton(name, **args)
    for name, args in TRACKBARS.items():
        cv2.createTrackbar(name, WINDOW_NAME, *args)


def populate_toolbars_windows():
    for name, args in BUTTONS.items():
        ROOT_WINDOW.create_button(name, **args)


if __name__ == '__main__':
    if os.name == "nt":
        ROOT_WINDOW = init_windows()
        populate_toolbars_windows()
        ROOT_WINDOW.mainloop()

    else:
        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
        populate_toolbars()
        cv2.displayOverlay(WINDOW_NAME, 'press ctrl + p', 3000)
        while cv2.waitKey(30) != KEY_ESC:
            pass
