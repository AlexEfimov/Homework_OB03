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

class Humans():
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender

    def job(self):
        pass

class ZooKeeper(Humans):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}")

class Veterinarian(Humans):
    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}")

Person1=Veterinarian("John","male",30)
Person2=ZooKeeper("Anna","female",25)

for animal in animals:
    Person1.heal_animal(animal)
    Person2.feed_animal(animal)
