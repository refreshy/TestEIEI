from Tkinter import *

"""paint.py: not exactly a paint program.. just a smooth line drawing demo."""

b1 = "up"
xold, yold = None, None

def b1down(event):
    global b1
    b1 = "down"           # you only want to draw when the button is down

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

