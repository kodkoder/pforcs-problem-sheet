# es.py
#
# This program that reads in a text file 
# and outputs the number of e's it contains.
# Author: Tomasz

import sys

# take the filename provided
file_arg = str(sys.argv[1])

# read the file contents
with open (file_arg,'r+t') as f:
    data = f.read()
    char = 'e'  # specify character you will be counting
    occur = 0
    # loop through each characted and count all e's 
    for i in data:    
        if i == 'e':
            occur += 1     # add 1 to res for each occurance
        else:
            continue
    # print result
    print(occur)
