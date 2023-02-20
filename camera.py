import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while (True):

    ret, frame = capture.read()

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


    # Negative filters
    cv2.imshow('Original video', frame)
    cv2.imshow('Negative Gray', negativegray)
    cv2.imshow('Negative Tripped ', negativeTrip)
    cv2.imshow('Negative Smurf', negativeSmurfik)
    cv2.imshow('Negative Pinkie', negativeBarbie)
    cv2.imshow('Negative filter', negativehz)
    if cv2.waitKey(1) == 27:
        break

capture.release()
cv2.destroyAllWindows()