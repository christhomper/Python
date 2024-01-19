# Created by Chris Thompson on Thu Feb 16 07:29:24 2023
# Program made to demonstrate how to create a class with various methods for performing math operations
# And how to use an instance of that class to perform those operations on defined values


# import the time module
import time

# Defines a class for performing math operations
class MathOperations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

# Defines the values to use for the math operations
a = 1000
b = 1250

# Creates an instance of the MathOperations class with the defined values
math_ops = MathOperations(a, b)

# Prints the results of each operation with a 1 second time delay for readability
print("Sum =", math_ops.add())
time.sleep(1) 

print("Difference =", math_ops.subtract())
time.sleep(1)

print("Product =", math_ops.multiply())
time.sleep(1)

print("Quotient =", math_ops.divide())

