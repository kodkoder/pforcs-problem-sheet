# bmi.py
# This program calculates Body Mass Index
# author: Tomasz

# Take inputs from the user
weight_kg = int(input('Please give me your weight in kg: '))
height_cm = int(input('Please give me your height in cm: '))

# calculate height in meters
height_m = height_cm / 100

# calculate BMI - weight divided by their height in metres squared.
bmi = weight_kg / (height_m * height_m)
print ('BMI is {:.2f}.'.format(bmi))


