import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from tkinter import *


class App():
    def __init__(self, window, window_title, video_source=0, ):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        super().__init__()
        self.btn = tkinter.Button(self, text="Show me", command=self.on_click)
        self.btn.pack(padx=120, pady=30)

        # open video source (by default this will try to open the computer
        self.vid = MyVideoCapture(video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width=1400, height=900)
        self.canvas.pack()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        btn = Button(window, text="Показать")
        btn.grid(column=1, row=0)

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg",
                        cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.after(self.delay, self.update)

    def on_click(self):
        print("In progress")


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            # # Initialization of filters
            # # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # # trip = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # # smur = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            # # barb = cv2.cvtColor(frame, cv2.COLOR_HLS2RGB_FULL)
            # # filt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #
            # # Converting to negative
            # negativegray = abs(255 - gray)
            # negativeTrip = abs(255 - trip)
            # negativeSmurfik = abs(255 - smur)
            # negativeBarbie = abs(255 - barb)
            # negativehz = abs(255 - filt)
            #
            # # Normal filters
            # cv2.imshow('Original video', frame)
            # cv2.imshow('Grayscale', gray)
            # cv2.imshow('Tripped', trip)
            # cv2.imshow('Smurf', smur)
            # cv2.imshow('Pinkie', barb)
            #
            # # Negative filters
            # cv2.imshow('Original video', frame)
            # cv2.imshow('Negative Gray', negativegray)
            # cv2.imshow('Negative Tripped ', negativeTrip)
            # cv2.imshow('Negative Smurf', negativeSmurfik)
            # cv2.imshow('Negative Pinkie', negativeBarbie)
            # cv2.imshow('Negative filter', negativehz)
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


App(tkinter.Tk(), "Tkinter and OpenCV")