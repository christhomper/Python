#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:22:55 2023

@author: christhompson
"""

import time

time_text = input('Enter the cooking time in seconds')
time_int = int(time_text)
print('Put the egg in boiling water now')
time.sleep(time_int)
print('Take the egg out now')
