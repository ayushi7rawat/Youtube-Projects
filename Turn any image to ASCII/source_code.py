'''
Turn any images to ASCII art using Python
Author: Ayushi Rawat
'''

#import the necessary module!
import pywhatkit as kt

#display welcome msg
print("Let's turn images to ASCII art!")

#capture source and target path
source_path = 'flower.png'
target_path = 'demo_ascii_art2.text'
#target_path = 'demo_ascii_art.text'

#call the method
kt.image_to_ascii_art(source_path, target_path)

--------------------------------------------------------------

#2 lines of code

import pywhatkit as kt
kt.image_to_ascii_art('flower.png', 'demo_ascii_art2.text')
