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

# improved code 
import requests
def get_weather(city):
  '''fetches weather report for a given city.
Args:
 city(str):City Name
Returns:
str:Weather report'''
  url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)
  print(res.text)
def main():
  city=str(input("Enter city name:"))
  print(f'Displaying weather report for:{city}')
  weather_report=get_weather(city)
  print(weather_report)
if_name_=='__main.__':
    main()
