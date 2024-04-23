import pickle
from typing import BinaryIO
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
        print(f"{self.name} tweets")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} roars")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} hiss-hiss")


class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ZooKeeper(Human):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}")

class Veterinarian(Human):
    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}")


class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []


    def add_animal(self, animal):
        self.animals.append(animal)


    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print("No such animal")



    def add_staff(self, staff):
        self.staff.append(staff)

    def remove_staff(self, staff):
        if staff in self.staff:
            self.staff.remove(staff)
        else:
            print("No such staff member")


    def animals_info(self):
        for animal in self.animals:
            print(f"Animal {animal.name} of age {animal.age} is {animal.__class__.__name__}")

    def staff_info(self):
        for staff in self.staff:
            print(f" Staff member {staff.name} of age {staff.age} is {staff.__class__.__name__} ")

    def save_zoo_state(self, file_name = "zoo_state.pkl"):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)
            print(f"Zoo state saved!")

    def load_zoo_state(file_name = "zoo_state.pkl"):
        try:
            with open(file_name, 'rb') as file:
                return pickle.load(file)

        except FileNotFoundError:
            print("No saved zoo state file found.")
            return Zoo()

zoo = Zoo.load_zoo_state()

animal1 = Bird("Kesha", 8)
animal2 = Mammal("Barsik", 5)
animal3 = Reptile("Nag", 3)
animal4 = Mammal("Tuzik", 6)
animal5 = Mammal("Ashley",3)

staff1 = Veterinarian("Petruccio",30)
staff2 = ZooKeeper("Malvina", 19)
staff3 = ZooKeeper("Eva", 28)
staff4 = ZooKeeper("Bob", 24)

zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_animal(animal3)
zoo.add_animal(animal4)

zoo.add_staff(staff1)
zoo.add_staff(staff2)
zoo.add_staff(staff3)

zoo.animals_info()
zoo.staff_info()

zoo.remove_animal(animal5)
zoo.remove_animal(animal2)
zoo.animals_info()

zoo.remove_staff(staff4)
zoo.remove_staff(staff2)
zoo.staff_info()

zoo.save_zoo_state()






