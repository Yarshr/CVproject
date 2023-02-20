import tkinter
import tkinter as tk
import cv2
capture = cv2.VideoCapture(0)
RELIEFS = [tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE, tk.FLAT]
class App():
    def __init__(self, window, window_title):


        self.window = window
        self.window.title(window_title)
        self.canvas = tkinter.Canvas(window, width=1200, height=900)
        self.canvas.pack()
        self.btn = tkinter.Button(window,text= "Show me", width=20, height=3, command=self.show)
        self.btn.pack (anchor=tkinter.CENTER, expand=True)
        self.window.resizable(False,False)
        self.btn.place(x=100,y=111)





        self.window.mainloop()

    def show(self):
        while (True):

            ret, frame = capture.read()

            cv2.imshow('Original video', frame)
            if cv2.waitKey(1) == 27:
                break

        capture.release()
        cv2.destroyAllWindows()






class Video():
    def __init__(self,video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()

            # Initialization of filters
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            trip = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            smur = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            barb = cv2.cvtColor(frame, cv2.COLOR_HLS2RGB_FULL)
            filt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Converting to negative
            negativegray = abs(255 - gray)
            negativeTrip = abs(255 - trip)
            negativeSmurfik = abs(255 - smur)
            negativeBarbie = abs(255 - barb)
            negativehz = abs(255 - filt)

            # Normal filters
            # cv2.imshow('Original video', frame)
            # cv2.imshow('Grayscale', gray)
            # cv2.imshow('Tripped', trip)
            # cv2.imshow('Smurf', smur)
            # cv2.imshow('Pinkie', barbie)

            # # Negative filters
            # cv2.imshow('Original video', frame)
            # cv2.imshow('Negative Gray', negativegray)
            # cv2.imshow('Negative Tripped ', negativeTrip)
            # cv2.imshow('Negative Smurf', negativeSmurfik)
            # cv2.imshow('Negative Pinkie', negativeBarbie)
            # cv2.imshow('Negative filter', negativehz)
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


App(tkinter.Tk(), "Tkinter and OpenCV")