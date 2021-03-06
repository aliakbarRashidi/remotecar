#!/usr/bin/python
import serial
try:
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(3,GPIO.OUT)
        p = GPIO.PWM(3,100)
        p.start(40)
except ImportError:
        print ("Cannot import GPIO. Are you on Raspi?")
try:
	import tkinter as tk
	from tkinter import *
except ImportError:
	import Tkinter as tk
	from Tkinter import *


try:
        ser = serial.Serial('/dev/ttyACM0', 9600)
except:
        print ("Check if Arduino is connected")
        pass
def center(win):
        """
        centers a tkinter window
        :param win: the root or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()
def forward():
	ser.write("a")
	if (w1.get() == 0):
            w1.set(20)
            speed(20)
	print ("forward")
def backward():
	ser.write("b")
	if (w1.get() == 0):
            w1.set(20)
            speed(20)
	print ("backward")
def fastleft():
	ser.write("c")
	if (w1.get() == 0):
            w1.set(40)
            speed(40)
	print ("fast left")
def fastright():
	ser.write("d")
	if (w1.get() == 0):
            w1.set(40)
            speed(40)
	print ("fast right")
def slowleft():
        ser.write("e")
	if (w1.get() == 0):
            w1.set(30)
            speed(30)
	print ("slow left")
def slowright():
        ser.write("f")
	if (w1.get() == 0):
            w1.set(30)
            speed(30)
	print ("slow right")
def speed(val):
	print (val)
        p.start(float(val))
def stop():
	speed(0)
	w1.set(0)

root = tk.Tk()
root.title("Control your car")

frame = tk.Frame(root)
frame.pack()

slogan = tk.Button(frame,
                   text="Forward",
                   bg="#0066ff",
                   fg="white",
                   font=("Arial",12,"bold"),
                   height="6",
                   width="9",
                   command=forward)
slogan.pack(side=tk.TOP)

slogan = tk.Button(frame,
                   text="Backward",
                   bg="#3d9c35",
                   fg="white",
                   font=("Arial",12,"bold"),
                   height="6",
                   width="9",
                   command=backward)
slogan.pack(side=tk.BOTTOM)

slogan = tk.Button(frame,
                   text="Fast Left",
                   bg="#f9531c",
                   fg="white",
                   font=("Arial",12,"bold"),
                   height="6",
                   width="9",
                   command=fastleft)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Left",
                   bg="#f5e220",
                   fg="black",
                   font=("Arial",12,"bold"),
                   height="6",
                   width="9",
                   command=slowleft)
slogan.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Fast Right",
                   bg="#f9531c",
                   fg="white",
                   font=("Arial",12,"bold"),
                   height="6",
                   width="9",
                   command=fastright)
slogan.pack(side=tk.RIGHT)

slogan = tk.Button(frame,
                   text="Right",
                   bg="#f5e220",
                   fg="black",
                   font=("Arial",12,"bold"),
                   height="6",
                   width="9",
                   command=slowright)
slogan.pack(side=tk.RIGHT)
slogan = tk.Button(frame,
                   text="Stop",
                   bg="#ff5050",
                   fg="black",
                   font=("Arial",12,"bold"),
                   height="6",
                   width="9",
                   command=stop)
slogan.pack(side=tk.BOTTOM)



root.update()
width = root.winfo_width()

w1 = Scale(root, from_=0, to=100,length = 0.8*width, width = width/6, tickinterval=10, font=("Arial",15,"bold"),resolution=10, orient=HORIZONTAL,command=speed)
w1.set(40)
w1.pack()
center(root)
root.mainloop()
