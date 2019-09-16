import cv2
from functools import wraps

__all__ = ['update_global_image_var', 'display_returned_image']


IMAGE = None


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
            cv2.imshow('main', res)
            return res

    return wrapped
