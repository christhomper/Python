"""
Created on Mon Apr 3 09:25:30 2023

@author: christhompson
"""

import tkinter as tk

# Define a MathOperations class to perform basic arithmetic operations
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

# Define a CalculatorGUI class to create the calculator interface
class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create and display labels and entry fields for user input
        self.label1 = tk.Label(master, text="Enter the first number:")
        self.label1.pack()

        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.label2 = tk.Label(master, text="Enter the second number:")
        self.label2.pack()

        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        # Create and display buttons for math operations
        self.add_button = tk.Button(master, text="Add", command=self.add)
        self.add_button.pack()

        self.subtract_button = tk.Button(master, text="Subtract", command=self.subtract)
        self.subtract_button.pack()

        self.multiply_button = tk.Button(master, text="Multiply", command=self.multiply)
        self.multiply_button.pack()

        self.divide_button = tk.Button(master, text="Divide", command=self.divide)
        self.divide_button.pack()

        # Create and display the result label
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    # Get values from the user input fields
    def get_values(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numbers.")

    # Perform addition and display the result
    def add(self):
        values = self.get_values()
        if values:
            math_ops = MathOperations(*values)
            result = math_ops.add()
            self.display_result(result)

    # Perform subtraction and display the result
    def subtract(self):
        values = self.get_values()
        if values:
            math_ops = MathOperations(*values)
            result = math_ops.subtract()
            self.display_result(result)

    # Perform multiplication and display the result
    def multiply(self):
        values = self.get_values()
        if values:
            math_ops = MathOperations(*values)
            result = math_ops.multiply()
            self.display_result(result)

    # Perform division and display the result
    def divide(self):
        values = self.get_values()
        if values:
            math_ops = MathOperations(*values)
            try:
                result = math_ops.divide()
                self.display_result(result)
            except ZeroDivisionError:
                tk.messagebox.showerror("Error", "Cannot divide by zero.")

    # Update the result label with the result of the operation
    def display_result(self, result):
        self.result_label.configure(text="Result: " + str(result))

# Initialize the tkinter application and run the main event loop
root = tk.Tk()
calculator_gui = CalculatorGUI(root)
root.mainloop()

