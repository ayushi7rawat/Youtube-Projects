'''
Take Screenshot using python with just 3 lines of code.
Author: Ayushi Rawat
'''

#Without GUI
import pyautogui

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\imar\Desktop\Python Tutotial\screenshot.png')


#With GUI
import pyautogui
import tkinter as tk

root= tk.Tk()
root.title('Sc taker')

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def myScreenshot():
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\imar\Desktop\Python Tutotial\screenshot1.png')

myButton = tk.Button(text='Take Screenshot', command=myScreenshot, bg='green',fg='white',font= 15)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()
