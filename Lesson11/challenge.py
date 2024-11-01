from abc import ABC, abstractmethod

# Abstract Base Class
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        print(f"{self.name} (Age: {self.age}) - Weight: {self._weight} kg, Height: {self._height} m")
        print(f"BMI: {bmi:.2f}, Category: {self.get_bmi_category()}")

# Adult Class
class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

# Child Class
class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi <= 18:
            return "Normal weight"
        elif 18 <= bmi <= 24:
            return "Overweight"
        else:
            return "Obese"

# BMIApp Class
class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        if age < 18:
            person = Child(name, age, weight, height)
        else:
            person = Adult(name, age, weight, height)
        self.add_person(person)

    def print_result(self):
        for person in self.people:
            person.print_info()

    def run(self):
        while True:
            cont = input("Do you want to add another person? ").strip().lower()
            if cont != "yes":
                break
            self.collect_user_data()  # Call collect_user_data if the user wants to add another person
        self.print_result()


app = BMIApp()
app.run()

import numpy as np
arr_2d=np.array([[1,2,3,24],[8,3,4,7]])
print(arr_2d)