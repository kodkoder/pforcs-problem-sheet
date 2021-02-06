# bitcoin.py
# This program pulls the latest price of bitcoin from coindesk.com
# and displays to the user the following data:
# 1. Bitcoin price in US Dollars
# 2. All three currencies, in a neat way...
#
# author: Tomasz
 
import requests

# Request the latest bitcoin data.

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()

# We specfify a name of the dictionary key where bitcoin rates are located.
bitPriceRate = bitCoinDict['bpi']

# Now we find a dictionary/key holding Bitcoin prices in USD Dollars and print it.
bitCurrencyUSD = bitPriceRate['USD']
bitRateUSD = bitCurrencyUSD['rate']
print("\n")
print("Bitcoin price in USD = {}.".format(bitRateUSD))
print("\n")

# The same process is automated for three currencies by using a For Loop. 
for item in bitPriceRate:
    print("Bitcoin price in {} = {}.".format(item,bitPriceRate[item]['rate']))