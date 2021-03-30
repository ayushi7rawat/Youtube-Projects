'''
Fetch data of any Country with Python using Countryinfo
Author: Ayushi Rawat
'''

#import the necessary module!
from countryinfo import CountryInfo                                  

name = 'India'
country = CountryInfo(name)

data1 = country.alt_spellings()
print(data1)

data2 = country.capital()
print(data2)

data3 = country.currencies()
print(data3)

data4 = country.languages()
print(data4)

data5 = country.timezones()
print(data5)

data6 = country.area()
print(data6)

data7 = country.borders()
print(data7)

data8 = country.calling_codes()
print(data8)

data9 = country.wiki()
print(data9)

data10 = country.info()
for x,y in data10.items():
    print(f'{x} --> {y}')
    