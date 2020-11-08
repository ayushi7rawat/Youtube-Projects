'''
Generate Jokes with Python
Author - Ayushi Rawat

'''

#import the necessary package
import pyjokes

#fetch the joke
joke1 = pyjokes.get_joke(language='en', category='all')

#display the joke
print(joke1)

#a different category
joke2 = pyjokes.get_joke(language='en', category='neutral')

#display the joke
print(joke2)

#fetch a bunch of jokes
jokes = pyjokes.get_jokes(language='en', category='neutral')

for i in range(5):
    print(i+1,".",jokes[i])