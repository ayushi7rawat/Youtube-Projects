'''
Currency Converter using Python
Author: Ayushi Rawat
'''

#import the necessary module!
import pywhatkit as kt
import getpass as gp

#display welcome msg
print("Let's Automate Whatsapp!")

#capture the target phone number
p_num = gp.getpass(prompt='Phoneumber: ', stream=None) 

#capture the message
msg = "I love Python"

call the method
kt.sendwhatmsg(p_num, msg, 10, 25)

--------------------------------------------------------------
#2 lines of code

import pywhatkit as kt
kt.sendwhatmsg("+919*********", "I love Python!", 10, 25)
