"""
This is just a dummy code for testing purposes
After calling main.py, click on the a new file within 5 seconds
Then you'll see the code on this file being typed into the blank file
"""


import random
import math

class ComplexClass:
    def __init__(self, name):
        self.name = name
        self.data = []

    def generate_data(self, size):
        for _ in range(size):
            random_value = random.randint(1, 100)
            if random_value % 2 == 0:
                self.data.append(math.sqrt(random_value))
            else:
                self.data.append(random_value ** 2)

    def process_data(self):
        processed_data = []
        for value in self.data:
            if value < 50:
                processed_data.append(value + 10)
            elif value >= 50 and value < 80:
                processed_data.append(value * 2)
            else:
                processed_data.append(value - 5)
        self.data = processed_data

    def display_info(self):
        print(f"Name: {self.name}")
        print("Data:")
        for value in self.data:
            print(f"  - {value}")

if __name__ == "__main__":
    complex_object = ComplexClass("ExampleObject")
    complex_object.generate_data(5)
    complex_object.process_data()
    complex_object.display_info()
