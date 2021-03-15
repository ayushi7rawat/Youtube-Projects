'''
Automate Whatsapp | Facebook | Instagram (any)Chat-Messenger with Python
Author: Ayushi Rawat
'''

#import the necessary module!
import pyautogui
import time

#Use sleep to introduce some time margin for user to place the cursor at the right place.
time.sleep(5)

#Store the text you wish to use for Automation
text = 'I Love Python'

#Enclose the code in an indefinite loop!
while True:
    pyautogui.typewrite(text)
    
    time.sleep(1)
    pyautogui.press('enter')


