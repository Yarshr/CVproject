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

