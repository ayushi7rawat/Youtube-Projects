'''
Currency Converter using Python
Author: Ayushi Rawat
'''

#import the necessary module!
from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

test1 = CurrencyCodes()

#fetch Currency Symbol
cur_symbol = test1.get_symbol('INR')

#fetch Currency Name
cur_name = test1.get_currency_name('INR')

#display Currency Name & Symbol
print('\nThe currency name is: ' + cur_name)
print('The currency symbol is: ' + cur_symbol)

print('\n' + test1.get_symbol('USD'))
print(test1.get_currency_name('USD') + '\n')

test2 = CurrencyRates()

#fetch the Conversion rate
rate = test2.get_rate('USD', 'INR')
print(rate)

#perform conversion
res = test2.convert('USD', 'INR', 10)

#display result
print(res)

#BONUS
print('---------------------------------------')                          

#fetching BITCOIN details
bitcoin = BtcConverter()

#fetch the lastest price
price = bitcoin.get_latest_price('INR')

#display the output
print(price)
