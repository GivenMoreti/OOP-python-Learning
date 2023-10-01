class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.width * self.length


class Cube(Square):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return super().area() * self.height
# volume = area * height


# object
area_one = Square(2, 4)
print(area_one.area())
volume_1 = Cube(3, 5, 5)
print(volume_1.volume())
