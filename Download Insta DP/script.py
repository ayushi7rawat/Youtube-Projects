'''
Download Display Picture of an Instagram Account with Python
Author: Ayushi Rawat
'''

#import the necessary module!
import instaloader

#create an instance
test = instaloader.Instaloader()

#fetch the account details
acc = input('Enter the Account Username: ')

#download the data
test.download_profile(acc, profile_pic_only = True)        
