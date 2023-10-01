# super functions
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def area(self):
        return super().area()


class Cube(Square):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return super().area() * self.height


area_1 = Square(3, 3)
print(area_1.area())

vol = Cube(3, 2, 4)
print(vol.volume())

area_rec = Rectangle(23, 5)
print(area_rec.area())
