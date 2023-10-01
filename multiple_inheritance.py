# Child class inherit from a child class in multi level inheritance.
class Organism:
    is_alive = True


class Animal(Organism):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"this {self.name} is eating")


class Dog(Animal):

    def bark(self):
        print(f'this {self.name} is barking')


dog = Dog("piet")
print(dog.eat())
print(dog.bark())
# example two


class Prey:
    def prey(self):
        print("this animal is a prey")


class Predator:
    def hunts(self):
        print("this animal hunts")

#  fish can be both a prey and predator


class Fish(Prey, Predator):
    pass


fish_obj = Fish()
print(fish_obj.prey())
