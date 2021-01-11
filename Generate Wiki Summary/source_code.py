'''
Generate Wiki Summary using Python
Author: Ayushi Rawat
'''

#import the necessary module!
import pywhatkit as kt

#display welcome msg
print('Lets Generate Wiki Summary!\n')

target1 = "Python"
target2 = 'coronavirus'

#call the method
kt.info(target1,lines=3)

print('\n')
kt.info(target2,lines=3)

--------------------------------------------------------------

#2 lines of code

import pywhatkit as kt
kt.info('python')
