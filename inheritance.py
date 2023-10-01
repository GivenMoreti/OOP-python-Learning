# inheritance
# class
class Animal:
    name = ""
    is_alive = True

    # constructor
    def __init__(self, name, is_alive):
        self.name = name  # instance
        self.is_alive = is_alive  # instance

# methods/functions within classes.
    def eat(self):
        print(f" this {self.name} is eating")

    def sleep(self):
        print(f"this {self.name} is sleeping")

# inheritance part


class Cow(Animal):
    pass


cow_1 = Cow("zxc", True)
print(cow_1.eat())
