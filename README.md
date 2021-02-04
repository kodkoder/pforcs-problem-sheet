# Programming For Security course - weekly tasks with solutions

##  Week 2 - Body Mass Index Calculator
Write a program that calculates somebody's Body Mass Index (BMI):
* The inputs are the person's height in centimetres and weight in kilograms.
* The output  is their weight divided by their height in metres squared.

### Code:
[bmi.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/bmi.py)

### Explaining the Code:
The user is prompted to input his/her weight and height. The input is stored as variables and then used to calculate the result. Format function is used to display two decimals only.

### References:
1.  https://www.w3schools.com/python/python_string_formatting.asp


##  Week 3 - Print out todays bitcoin price
Write a program (bitcoin.py) that outputs the current bitcoin price in US
Dollars. You may use the code snippet below to get a Dict object that contains the price.
Extra output all the price in the three currencies, in a neat way.

### Code:
[bitcoin.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/bitcoin.py)

### Explaining the Code:
1. The program uses coindesk.com API calls to pull data with the latest Bitcon prices. The data is returned in json format. 
2. Next we identify position of each rate within the dictionary. This is to identify dictionary keys holding bitcoin prices.
3. Finally, we we output to the user:
\t* Bitcoin price in USD
\t* Bitcoin price for all three currencies nicely formated 

### References:
1. https://www.w3schools.com/python/module_requests.asp
2. https://stackoverflow.com/questions/48894060/how-to-print-specific-key-value-from-a-dictionary
3. https://www.w3schools.com/python/python_string_formatting.asp

##  Week 3 