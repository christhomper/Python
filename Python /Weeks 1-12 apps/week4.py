# Created by Chris Thompson on Mon Feb 6 08:34:29 2023
# Program made to take two arguments and return a single value in the form of sum, difference, product, and quotient

import time

a = 1000  # Changeable variable
b = 1250  # Changeable variable

def sum(a, b):  # The def function takes two arguments (a, b)
    return a + b # Returns the result to the caller of the function

print("Sum =", sum(a, b)) # Prints sum of two variables 
time.sleep(1) # Give reader time to read each solution separetly

def subtract(a, b):
    return a - b

print("Difference =", subtract(a, b)) # Prints difference of two variables 
time.sleep(1) # Give reader time to read each solution separately

def multiply(a, b):
    return a * b

print("Product =", multiply(a, b)) # Prints product of two variables 
time.sleep(1) # Give reader time to read each solution separately

def divide(a, b):
    return a / b

print("Quotient =", divide(a, b)) # Prints quotient of two variables 



