from Shape import *


class Circle(Shape):
    def __init__(self, colour, radius):
        """
        initializer for Circle object
        :param colour: colour of circle
        :param radius: radius of circle
        """
        super().__init__("Circle ", colour, 3.14159 * radius ** 2, 3.14159 * 2 * radius)
        self.radius = radius

    def _str_(self):
        """
        toString method of circle
        :return: description of circle
        """
        return super().__str__() + " Radius: " + str(self.radius)
