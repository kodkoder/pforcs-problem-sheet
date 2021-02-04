# bitcoin.py
# bitcoin.py
# This program pulls the latest price of bitcoin from coindesk.com
# and displays to the user the following data:
# 1. Bitcoin price in USDollars
# 2. All three currencies, in a neat way
#
# author: Tomasz
 
import requests

# We specify the url from where data will be requested,
# make a request and store returned data as dictionary
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()

# We specfify a name of the key where rates are located within the dictionary
bitPriceRate = bitCoinDict['bpi']

# Now we identify each currency within the dictionary with corresponding rates
# We store those in newly creared variables 
bitCurrencyUSD = bitPriceRate['USD']
bitCurrencyEUR = bitPriceRate['EUR']
bitCurrencyGBP = bitPriceRate['GBP']
bitRateUSD = bitCurrencyUSD['rate']
bitRateEUR = bitCurrencyEUR['rate']
bitRateGBP = bitCurrencyGBP['rate']

# Not we display the result for US Dollars. We use \n characters for readability
print("\n")
print("Bitcoin price in USD = {}.".format(bitRateUSD))
print("\n")
# We display Bitcoin pricess in all three currencies
# Format 
print("Bitcoin price in US Dollars is {}, in Euro {} and in British Pound Sterling {}.".format(bitRateUSD,bitRateEUR,bitRateGBP))
print("\n")

