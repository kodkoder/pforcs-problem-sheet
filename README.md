# Programming For Cybersecurity course - weekly tasks with solutions

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

##  Week 4 - Flow control
### Task:
Write a program that asks a user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.

### Code:
[collatz.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/collatz.py)

### Explaining the Code:
1. The program asks a user to provide a positive integer. 
2. The program uses while loop and perform following calculations:
    * if the number ('x') is even, devides the number by 2
    * if the number ('x') is odd, multiplies it by three and add one to it
    * the calculations continues until 'x' equals 1
3. Results are displayed in one line.
    
### References:
1. https://www.w3schools.com/python/python_conditions.asp
2. https://www.w3schools.com/python/python_while_loops.asp
3. https://stackoverflow.com/questions/11856945/i-need-to-make-the-output-be-in-one-line

##  Week 5 - Square root
### Task:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

### Code:
[squareroot.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/squareroot.py)

### Explaining the Code:
1. We define a function to calculate a square root of a number (using Newton method)
2. We take a number from the user and story it as a float
3. Next we print out the number and its square root calculated by invoking the function and format it to display only one decimel.
    
### References:
1. https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method
2. https://careerkarma.com/blog/python-valueerror-invalid-literal-for-int-with-base-10/
3. https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
4. https://tarinder1103.wordpress.com/2017/02/09/finding-square-root-by-using-newton-raphson-method-in-python/
5. https://www.w3schools.com/python/python_string_formatting.asp

##  Week 6 - Count e's
### Task:
Write a program that reads in a text file and outputs the number of e's it contains.
The program should take the filename from an argument on the command line.

### Code: 
[es.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/es.py)

### Explaining the Code:
1. The program imports sys module which is used to take the argument (filename) from the command line.
2. Contents of the file are read.
3. The program specifies the characted I we are interested in.
4. The script loops through the text using a for loop adding 1 to the 'occur' number each time the character equals 'e'. This is to count a number of occurances
5. Finally, the rusult is printed back to the user.
    
### References:
1. https://realpython.com/python-command-line-arguments/
2. https://www.pythonforbeginners.com/system/python-sys-argv
3. https://realpython.com/working-with-files-in-python/#pythons-with-open-as-pattern
4. https://duckduckgo.com/?q=io.UnsupportedOperation%3A+not+readable&t=braveed&ia=web
5. https://www.tutorialspoint.com/count-occurrences-of-a-character-in-string-in-python

##  Week 7 - Extract URLs
### Task:
Write a program called extract-url.py, that will extract the URLs from an access.log file.

### Code: 
[extract-url.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/extract-url.py)

### Explaining the Code:
1. The program imports re module which allows us to use regex statements to find matches in strings 
2. We open a file.
3. We loop through each line and store results as strings in a list
4. Finally we print out results to the user.
    
### References:
1. https://cheatography.com/davechild/cheat-sheets/regular-expressions/
2. https://stackoverflow.com/questions/7411194/how-can-i-make-a-regular-expression-match-upper-and-lower-case
3. https://www.w3schools.com/python/python_regex.asp

##  Week 7 - Extra Task
### Task:
Store the URLs as a Dictionary object in the list with the resource and parameter names and values separated out.

### Code:
[extract_url_to_dict.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/extract_url_to_dict.py)

### Explaining the Code:
1. The program imports re module which allows us to use regex statements to find matches in strings.
2. Additonally, we import pprint module to print out the directory with each key in new line.
3. We specify the file with data.
4. We loop through each line and use regex split function to extract items we are interested in
5. Finally we store results in a dictionary and print it back to the user.
    
### References:
1. https://www.w3schools.com/python/python_regex.asp
2. https://stackoverflow.com/questions/20181899/how-to-make-each-key-value-of-a-dictionary-print-on-a-new-line
3. https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/

##  Week 8 - Plots
### Task:
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

### Code:
[plottask.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/plottask.py)

### Explaining the Code:
1. The program imports module needed to create plots.
2. Then it defines a range and functions which will be displayed.
3. The script defines visual parameters, title and labels.
4. Finally, the plot is displayet to the user.
    
### References:
1. https://futurestud.io/tutorials/matplotlib-getting-started-with-high-quality-plots-in-python
2. https://www.tutorialspoint.com/python_data_science/python_matplotlib.htm
3. https://realpython.com/python-matplotlib-guide/


##  Week 9 - Pandas
### Task:
Find which sessionId downloaded the most data.

### Code:
[tricky_one.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/tricky_one.py)

### Explaining the Code:
1. The program reads the sm_access.log into a dataframe.
2. Sets the date time to be the index.
3. Uses regular expressions to extract the session id from the URLs and stores them in a different column.
4. Uses groupBy to get the sum of all the data downloaded by each sessionId.
5. Creates a plot of this.
    
### References:
1.https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
2.https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html?highlight=to_date
3.https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
4.https://pandas.pydata.org/pandas-docs/version/0.13/visualization.html
5.https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot


##  Week 10 - Errors testing and logging
### Task:
Write a (bullet proof) function called averageTo(aList, toIndex)
The function should take in a list and an index. 
The function will return the average of the numbers upto and including the toIndex in the aList.

When I say "bullet proof", I would like the function to always return an integer, even if a error occurs (say return -1), but it will use logging to make a meaningful log warning, for any error that occurs (eg the aList contains an entry that is not a number/ toIndex is not valid, there are many things that could go wrong)
Write the code to test all the things that could go wrong with this function, and a test to check the function does work.

The test code can be in the same file or different file.

### Code:
[bulletProof.py](https://github.com/kodkoder/pforcs-problem-sheet/blob/main/bulletProof.py)

### Explaining the Code:
1. The program imports logging module and sets logging level
2. the program assigns two variables for later use
3. Then try/except is used to "catch" possible errors/exceptions
4. For each error/exception we create an individula logging message
5. At the end of the program assertion statements are located. This is for resting purposes
    
### References:
1. https://realpython.com/python-logging/
2. https://www.w3schools.com/python/python_try_except.asp
3. https://www.tutorialsteacher.com/python/error-types-in-python
4. https://www.w3schools.com/python/ref_keyword_assert.asp
