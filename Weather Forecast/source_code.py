'''
Weather forecast with Python
By: Ayushi Rawat
'''

#import the necessary package!
import requests

#input the city name
city = input('input the city name')
print(city)

# or you can also hard-code the value
# city = 'bhopal'

#Display the message!
print('Displaying Weater report for: ' + city)

#fetch the weater details
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result!
print(res.text)
