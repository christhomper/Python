
# Created on Mon Feb 20 12:33:02 2023

# author: christhompson


class Person:
    # Initialize Person object with name, age, and gender attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Greet the person with their name
    def greet(self):
        print(f"Hello, my name is {self.name}")

    # Introduce the person with their name, age, and gender
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old, and I am {self.gender}")

# create an object of Person class and set its attributes
Chris = Person("Chris", 29, "male")

# call object methods using dot notation
Chris.greet()
Chris.introduce()
