# Programming For Cybersecurity course - weekly problems with solutions

##  Week 2 - Body Mass Index Calculator
### Task:
Write a program that calculates somebody's Body Mass Index (BMI):
* The inputs are the person's height in centimetres and weight in kilograms.
* The output  is their weight divided by their height in metres squared.

### Code:
[bmi.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/bmi.py)

### Explaining the Code:
1. The user is prompted to input his/her weight and height. The input is stored as variables and then used to calculate the result. 
2. Format function is used to display two decimals only. 
3. The result is displayed to the user.

### References:
1.  https://www.w3schools.com/python/python_string_formatting.asp


##  Week 3 - Print out todays bitcoin price
### Task:
Write a program (bitcoin.py) that outputs the current bitcoin price in US
Dollars. You may use the code snippet below to get a Dict object that contains the price.
Extra output all the price in the three currencies, in a neat way.

### Code:
[bitcoin.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/bitcoin.py)

### Explaining the Code:
1. The program uses coindesk.com API calls to pull data with the latest Bitcon prices. The data is returned in json format. 
2. We identify position of USD rate within the nested dictionary and print out the value to the user.
3. For the 2nd part of the task (three currencies displayed in a neat way), we automate the process using a For Loop. For each key in a dictionary 'bpi' 
    we display that key name and from its dictionary we print out a value for a key with a name 'rate'.
    
### References:
1. https://www.w3schools.com/python/module_requests.asp
2. https://stackoverflow.com/questions/48894060/how-to-print-specific-key-value-from-a-dictionary
3. https://www.w3schools.com/python/python_string_formatting.asp
4. https://www.w3schools.com/python/python_dictionaries_loop.asp
5. https://careerkarma.com/blog/python-nested-dictionary/

##  Week 4
### Task:
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.

### Code:
[collatz.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/collatz.py)

### Explaining the Code:
1. The program asks the user to provide a positive integer. 
2. The program uses while loop and perform following calculations:
* if the number ('x') is even, devides the number by 2
* if the number ('x') is odd, multiplies it by three and add one to it
* the calculations continues until 'x' equals 1
3. Results are displayed in one line.
    
### References:
1. https://www.w3schools.com/python/python_conditions.asp
2. https://www.w3schools.com/python/python_while_loops.asp
3. https://stackoverflow.com/questions/11856945/i-need-to-make-the-output-be-in-one-line

