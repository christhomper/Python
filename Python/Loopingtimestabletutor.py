#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:01:10 2023

@author: christhompson
"""

import time

# Function to display times table
def display_times_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)
        time.sleep(1)

# Main program
while True:
    # Get user input for a number
    num = int(input("Enter a number (0 to exit): "))

    # Exit the program if the number is 0
    if num == 0:
        break

    # Call the function to display the times table
    display_times_table(num)
