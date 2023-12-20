#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:06:50 2023

@author: christhompson
"""

from tkinter import *

class Adder:
    """
    Implements an adding machine using the Tkinter GUI.
    Call the method display to initiate the display.
    """
    def __init__(self):
        # Initialize the root window and the labels and entry fields
        self.root = Tk()
        self.first_number_label = Label(self.root, text="First Number")
        self.first_number_label.grid(sticky=E, padx=5, pady=5, row=0, column=0)
        self.first_number_entry = Entry(self.root, width=10)
        self.first_number_entry.grid(padx=5, pady=5, row=0, column=1)
        self.second_number_label = Label(self.root, text="Second Number")
        self.second_number_label.grid(sticky=E, padx=5, pady=5, row=1, column=0)
        self.second_number_entry = Entry(self.root, width=10)
        self.second_number_entry.grid(padx=5, pady=5, row=1, column=1)
        self.result_label = Label(self.root, text="Result")
        self.result_label.grid(sticky=E+W, padx=5, pady=5, row=3, column=0, columnspan=2)

        # Initialize the "Add Numbers" button and bind it to the do_add function
        self.add_button = Button(self.root, text="Add Numbers", command=self.do_add)
        self.add_button.grid(sticky=E+W, row=2, padx=5, pady=5, column=0, columnspan=2)

    def do_add(self):
        """
        Adds the values entered in the entry fields and updates the result label.
        """
        try:
            first_number = float(self.first_number_entry.get())
            second_number = float(self.second_number_entry.get())
            result = first_number + second_number
            self.result_label.config(text=str(result))
        except ValueError:
            # Handles any ValueError exceptions that may arise if the entry fields are empty or contain invalid input.
            self.result_label.config(text="Invalid input")

    def display(self):
        """
        Displays the user interface and waits for the interface to be closed by the user.
        """
        self.root.mainloop()


if __name__ == "__main__":
    # Create an instance of the Adder class and display the GUI
    app = Adder()
    app.display()