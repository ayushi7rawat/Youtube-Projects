'''
Build Break Scheduler with Python
By: Ayushi Rawat
'''
#Let's import the necessary packages!
import time 
import webbrowser
from random import choice

url = "https://ayushirawat.com/"

breaks = 2
counter = 0
gap = 30
#60*60

messages = ["Time for a break!", "Let's take a break!"]

print("Initiating the Break Scheduler!")

while(counter < breaks):
    time.sleep(gap)

    #Let's print the break message
    print(choice(messages))

    #opening the browser window.
    webbrowser.open(url)

    #Let's increment the counter at the end
    counter += 1

print("Terminating the Break Scheduler!")
