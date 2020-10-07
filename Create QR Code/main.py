'''
Create your own QR Code with Python
Author: Ayushi Rawat
'''

#import the module
import pyqrcode

#define the data
data = 'ayushirawat.com'

#create qrcode
img = pyqrcode.create(data)

#save the qrcode in png format with proper scaling
img.png('blogwebsite.png', scale= 10)
