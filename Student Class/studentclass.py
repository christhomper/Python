#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:49:27 2023

@author: christhompson
"""

class StudentContact:
    def __init__(self, first_name, last_name, major, credits_completed):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.credits_completed = credits_completed
    
    def increment_credits(self, credits):
        self.credits_completed += credits
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.major}, {self.credits_completed} credits"

# Example usage
s = StudentContact("Chris", "Thompson", "Cloud Computing", 30)
s.increment_credits(3)
print(s)
