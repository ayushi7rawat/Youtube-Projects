'''
Create Digital Clock using Python
Author: Ayushi Rawat
'''
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title('Digital clock')

def clock():
	tick = strftime('%H:%M:%S %p')

	label.config(text =tick)

	label.after(1000, clock)

label = Label(root, font =('sans', 80), background = 'black', foreground = 'red')

label.pack(anchor= 'center')

clock()
mainloop()