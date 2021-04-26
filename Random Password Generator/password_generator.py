'''
Random Password Generator using Python
Author: Ayushi Rawat
'''

#import the necessary modules!
from random import randint

print('hello, Welcome to Password generator!')

#input the length of password
length = int(input('\nEnter the length of password: '))                      

#define data
low = 32
up = 126 
#string.ascii_letters

#combine the data
temp = [chr(randint(low, up)) for x in range(length)]
#create the password 
password = "".join(temp)

#print the password
print(password)
