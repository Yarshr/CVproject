import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog

win = Tk()
win.geometry("900x700")
items = "Camera", "image"
com3 = ttk.Combobox(win, values=items)
com3.current(0)
com3.place(x=5, y=10, width=80)
win.resizable(False, False)

label = Label(win)
global is_on
is_on = False

def change():
    global is_on
    if is_on == False:
        on_button.config(image=on)
        neg_text.config(text="Turn off negative")
        is_on = True
    else:
        on_button.config(image=off)
        neg_text.config(text="Turn on negative")
        is_on = False


on = PhotoImage(file="photos/on.png")
off = PhotoImage(file="photos/off.png")
on_button = Button(win, image=off, bd=0, command=change)
on_button.place(x=450)
neg_text = Label(win, text="Turn on negative")
neg_text.place(x=350, y=15)

def to_pil(img, label, x, y, w, h):
    img = cv2.resize(img, (w, h))
    img = cv2.flip(img, 1)
    image = Image.fromarray(img)
    pic = ImageTk.PhotoImage(image)
    label.configure(image=pic)
    label.image = pic
    label.place(x=x, y=y)

def choose():
    global cap, image
    if com3.get() == "Camera":
        cap = cv2.VideoCapture(0)

    if com3.get() == "image":
        path = filedialog.askopenfilename(title="Select file", filetypes=(('JPG', '*.jpg'), ('PNG', '*.png')))
        image = cv2.imread(path)
        cap = cv2.VideoCapture()
    show()

button3 = Button(win, text='switch', command=choose, width=20, height=2)
button3.pack(anchor=tkinter.S, expand=True)

imgs = "original", "grayscale", "tripped", "smurf", "pinkie", "eightys", "countor"
switch = ttk.Combobox(win, values=imgs)
switch.place(x=800, y=10, width=80)
switch.current(0)


def show():
    if com3.get() == "Camera":
        _, frame = cap.read()
    if com3.get() == "image":
        frame = image

    original = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    tripped = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
    smurf = cv2.cvtColor(original, cv2.COLOR_BGR2RGBA)
    pinkie = cv2.cvtColor(original, cv2.COLOR_HLS2RGB_FULL)
    eightys = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    countor = cv2.Canny(grayscale, 100, 200)

    negativeoriginal = abs(255 - original)
    negativegray = abs(255 - grayscale)
    negativeTrip = abs(255 - tripped)
    negativeSmurfik = abs(254 - smurf)
    negativeBarbie = abs(255 - pinkie)
    negativehz = abs(255 - eightys)
    negativecountor = abs(255 - countor)

    if (is_on == False):
        if switch.get() == "original":
            to_pil(original, label, 50, 50, 800, 600)
        if switch.get() == "grayscale":
            to_pil(grayscale, label, 50, 50, 800, 600)
        if switch.get() == "tripped":
            to_pil(tripped, label, 50, 50, 800, 600)
        if switch.get() == "smurf":
            to_pil(smurf, label, 50, 50, 800, 600)
        if switch.get() == "pinkie":
            to_pil(pinkie, label, 50, 50, 800, 600)
        if switch.get() == "eightys":
            to_pil(eightys, label, 50, 50, 800, 600)
        if switch.get() == "countor":
            to_pil(countor, label, 50, 50, 800, 600)
    else:
        if switch.get() == "original":
            to_pil(negativeoriginal, label, 50, 50, 800, 600)
        if switch.get() == "grayscale":
            to_pil(negativegray, label, 50, 50, 800, 600)
        if switch.get() == "tripped":
            to_pil(negativeTrip, label, 50, 50, 800, 600)
        if switch.get() == "smurf":
            to_pil(negativeSmurfik, label, 50, 50, 800, 600)
        if switch.get() == "pinkie":
            to_pil(negativeBarbie, label, 50, 50, 800, 600)
        if switch.get() == "eightys":
            to_pil(negativehz, label, 50, 50, 800, 600)
        if switch.get() == "countor":
            to_pil(negativecountor, label, 50, 50, 800, 600)
    label.after(30, show)


win.mainloop()

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

