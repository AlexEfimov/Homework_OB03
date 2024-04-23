class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} is singing")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} is roaring")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} is hiss-hiss")

animals = [Bird("Nightingale",10), Mammal("Lion",5), Reptile("Snake",4)]
for animal in animals:
    animal.make_sound()
