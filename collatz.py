# collatz.py
# The program asks the user to input any positive integer,
#  then at each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd,
#  multiply it by three and add one. The program end if the current value is one
# Author: Tomasz


# ask user for input
x = int(input("Please give any positive integer: "))
print(x, end = " ")

# perform calculations until until x equals 1
while x != 1:
    if x == 1:  # end while loop when x =1
        print ("1", end = " ")
    elif x % 2 == 0: # check if x is even
        x = int(x / 2)
        print (x, end =" ")
    elif x % 2 == 1: # check if x is odd
        x = int(x * 3 + 1)
        print (x, end = " ")