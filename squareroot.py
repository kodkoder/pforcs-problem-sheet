# squareroot.py
# This program takes a positive floating-point number 
# as input and outputs an approximation of its square root
# which is calculated using Newton method
# 
# Author: Tomasz

# define a function to calculate square root
def sq_root(number):
    num = float (number)  # number to get sqare root of
    for i in range (1000):  # iteration number
        # x_(n+1) = 0.5 * (x_n +a / x_n) - formula
        number = 0.5 * (number + (num /number))
    return number   

# get the number and transoft it to a float
num = float(input("Please enter a positive number: "))

# print out the number and the square root formatted to display one decimel only
print("The square root of {} is approx. {:.1f}.".format(num, sq_root(num)))