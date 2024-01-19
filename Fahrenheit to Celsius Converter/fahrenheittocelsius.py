#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:34:23 2023
# Pizza Order Calculator
@author: christhompson
"""
temperature_text = input('Enter temperature in Fahrenheit:')
temperature_int = int(temperature_text)-32 
temperature_conv = temperature_int/1.8
print('The temperature is', temperature_conv, 'Degrees Celsius')

