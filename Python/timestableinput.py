#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 08:13:25 2023

@author: christhompson
"""

def print_times_table(times_value, limit):
    count = 1 
    while count < limit+1:
        result = times_value * count
        print(count, 'times', times_value, 'equals', result)
        count = count + 1
        

        
            