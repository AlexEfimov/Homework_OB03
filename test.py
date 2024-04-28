import math


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def greets():
            print(f"Привет {self.name}")


class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print(self.species)

class Shape:
    def __init__(self, name)
        self.name = name

    def display_name(self):
        print({self.name})

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.1415926*(self.radius ** 2)

    def calculate_circumference(self):
        return 2*3.1415926*(self.radius)

