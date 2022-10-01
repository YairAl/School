import random
from Square import *
from Circle import *


class Container:
    def __init__(self):
        self.colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Brown", "Grey", "Black"]
        self.container = []

    def generate(self, x):
        for i in range(x):
            s = random.randint(0, 2)
            c = random.randint(0, len(self.colours)-1)
            s1 = random.randint(1, 100)
            s2 = random.randint(1, 100)
            if s == 0:
                self.container.append(Rectangle(colour=self.colours[c], side1=s1, side2=s2))
            elif s == 1:
                self.container.append(Square(colour=self.colours[c], side=s1))
            else:
                self.container.append(Circle(colour=self.colours[c], radius=s1,))

        for i in self.container:
            print(i)

    def sum_areas(self):
        suma = 0
        for i in self.container:
            suma += i.get_area()
        return f"Sum of Areas: {suma}"

    def sum_perimeters(self):
        sump = 0
        for i in self.container:
            sump += i.get_perimeter()
        return f"Sum of Perimeters: {sump}"

    def count_colours(self):
        colour_library = {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 0, "Blue": 0,
                          "Purple": 0, "Brown": 0, "Grey": 0, "Black": 0}

        for i in self.colours:
            count = 0
            for j in self.container:
                if j.get_colour() == i:
                    count += 1
            colour_library[i] = count

        return colour_library
