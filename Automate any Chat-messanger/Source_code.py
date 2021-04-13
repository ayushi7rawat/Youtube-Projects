#import the necessary module!
from pyautogui import click 
from pyautogui import typewrite
from pyautogui import press
from pyautogui import locateOnScreen
from time import sleep 

Messengers = ("Whatsapp","Instagram","Facebook")

def typed(text):
    while(True):
        sleep(5)
        typewrite(text)
        press("Enter")


def thelocater(target_client,text):


    if target_client == 1:
        target_click = locateOnScreen("instagramtext.png")
        click(target_click)
        print("Clicked In The Message Box")
        typed(text)



    if target_client == 0:
        target_click = locateOnScreen("whatsapptext.png")
        click(target_click)
        print("Clicked In The Message Box")
        typed(text)

    
        
    if  target_client == 2:
        target_click = locateOnScreen("facebooktext.png")
        click(target_click)
        print("Clicked In The Message Box")
        typed(text)

        




def main():
    print("Enter The Client Number:")
    print("0.Whatsapp 1.Instagram 2.Facebook")
    target = int(input("Enter The Number:"))
    target_client = Messengers[target]
    print("Enter The Text")
    text = input("Here:")
    print("Default Sleep Time Is 5 Seconds")
    print("Open The Website On The Side and Run This Script On the Other Side")
    print("Starting in 5 Seconds!!")
    sleep(5)
    print("Using:"+ target_client,"Message:" + text)
    thelocater(target,text)

try:
    main()
except ImportError:
    print("Import Error")
    print("Use pip install pillow and Try Again")

