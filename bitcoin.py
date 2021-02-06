# bitcoin.py
# This program pulls the latest price of bitcoin from coindesk.com
# and displays to the user the following data:
# 1. Bitcoin price in US Dollars
# 2. All three currencies, in a neat way...
#
# author: Tomasz
 
import requests

# We specify the url from where data will be requested,
# make a request and store returned data as a dictionary.

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()

# We specfify a name of the key where bitcoin rates are located:
bitPriceRate = bitCoinDict['bpi']

# Now we find a dictionary holding Bitcoin prices in USD Dollars. We store the price in a variable.
bitCurrencyUSD = bitPriceRate['USD']
bitRateUSD = bitCurrencyUSD['rate']

# Now we display the result for US Dollars. We use '\n' characters for readability
print("\n")
print("Bitcoin price in USD = {}.".format(bitRateUSD))
print("\n")

# The same process can be automated for three currencies by using a For Loop. For each key in a dictionary 'bpi' 
# we display that key name and from its dictionary we print out a value for a key with a name 'rate'
for item in bitPriceRate:
    print("Bitcoin price in {} = {}.".format(item,bitPriceRate[item]['rate']))