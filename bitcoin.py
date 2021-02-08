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

# We find a dictionary/item holding Bitcoin price in USD Dollars and print it.
bitRateUSD = (bitCoinDict["bpi"]["USD"]["rate"])
print("Bitcoin price in USD = {}.".format(bitRateUSD))
print("\n")

# We repeat the same process for three currencies by using a For Loop. 
# We specify the nested dictionary holding Bitcoin prices
bitPriceRate = bitCoinDict['bpi']
for item in bitPriceRate:
    print("Bitcoin price in {} = {}.".format(item,bitPriceRate[item]['rate']))