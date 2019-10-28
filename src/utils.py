import os
import cv2
from functools import wraps
from layout_main import GUI

__all__ = ['update_global_image_var', 'display_returned_image']


IMAGE = None
ROOT_WINDOW = None
tkimage = None
canvas = None



def update_global_image_var(f):
    @wraps(f)
    def wrapped(*args, **kwds):
        global IMAGE
        res = f(*args, **kwds)
        if res is not None:
            IMAGE = res

    return wrapped


def display_returned_image(f):
    @wraps(f)
    def wrapped(*args, **kwds):
        res = f(IMAGE, *args, **kwds)
        if res is not None:
            if os.name == "nt":
                ROOT_WINDOW.image_show(res)
            else:
                cv2.imshow('main', res)
            return res

    return wrapped

def init_windows():
    global ROOT_WINDOW
    ROOT_WINDOW = GUI()
    return ROOT_WINDOW
