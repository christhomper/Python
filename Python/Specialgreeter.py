#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:57:57 2023

@author: christhompson
"""

name = input('Enter your name:')
if name == 'Chris':
    password = input('Enter the password:')
    if password == 'Koko':
        print('Hello, Oh great one')
    else:
        print('Begone. Imposter!')
