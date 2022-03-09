from abc import abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print(self.name + " says Wooof")

class Cat(Animal):
    def sound(self):
        print(self.name + " says Mieow")


animals = []
animals.append(Dog("Pluto"))
animals.append(Dog("Snowy"))
animals.append(Cat("Sylvester"))

for a in animals:
    a.sound()

