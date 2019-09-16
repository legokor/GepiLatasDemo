import cv2


KEY_ESC = 27
WINDOW_NAME = 'main'


def populate_toolbars():
    pass


if __name__ == '__main__':
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)
    populate_toolbars()

    while cv2.waitKey(30) != KEY_ESC:
        pass
