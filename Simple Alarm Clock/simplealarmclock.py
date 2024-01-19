#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:00:02 2023

@author: christhompson
"""

import time
current_time =  time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
if (hour>7) or (hour==7 and minute>29):
    print('IT IS TIME TO GET UP')
    print('RISE AND SHINE')
    print('THE EARLY BIRD GETS THE WORM')
print('The time is', hour,':',minute)