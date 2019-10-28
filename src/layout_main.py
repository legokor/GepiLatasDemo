import PIL.Image, PIL.ImageTk
import cv2
import tkinter as tk
import numpy as np

class GUI:
    root = None
    tkimage = None
    canvas = None
    label = None

    def __init__(self):
        self.root = tk.Tk()

    def image_show(self, img):
        assert isinstance(img, np.ndarray)
        height, width, *_ = img.shape
        if self.label is None:
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
            self.label = tk.Label(self.root, image=photo)
            self.label.pack(anchor=tk.E)
            self.label.image = photo
        else:
            photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
            self.label.config(image=photo)
            self.label.image = photo
            self.label.pack(anchor=tk.E)

    def create_button(self, name, **args):
        button = tk.Button(self.root, text=name, command=args["onChange"])
        button.pack(anchor=tk.W)

    def mainloop(self):
        self.root.mainloop()