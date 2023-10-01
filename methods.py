# methods overwritting - allows overwritting of methods

class Animal:
    def eat(self):
        print("this animal is eating")


class Rabbit(Animal):
    # overwrite the eat method from parent
    def eat(self):
        print("this rabbit is eating vegetables")


# object uses methods closely related to it
rabbit = Rabbit()
print(rabbit.eat())
# returns : this rabbit is eating vegetables

# method chaining: calling methods sequentially


class Car:
    def start(self):
        print("car started...")
        return self

    def drive(self):
        print("car driving")
        return self

    def brake(self):
        print("car braked")
        return self

    def turn_off(self):
        print("car off")
        return self


car = Car()

car.start().\
    drive().\
    brake().\
    turn_off()
