'''
Create Progress Bar with Python
Author: Ayushi Rawat
            
'''

#import the necessary module!
from tqdm import tqdm, trange
from time import sleep 

for i in trange(10):
    sleep(0.4)
    
#OR

for i in tqdm(range(5)):
    sleep(0.4)
