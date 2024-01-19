#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:34:23 2023
# Temperature Converter
@author: christhompson
"""

flag = True
while flag:
    
    temperature_fahr = input('Enter temperature in Degrees Fahrenheit:')
    temperature_int = float(temperature_fahr)-32 
    temperature_conv = temperature_int/1.8
    print('The temperature is', temperature_conv, 'Degrees Celsius')
    temperature_cels = input('Enter temperature in Degrees Celsius:')
    temperature_int = float(temperature_cels)*1.8 
    temperature_conv = temperature_int+32
    print('The temperature is', temperature_conv, 'Degrees Fahrenheit')
