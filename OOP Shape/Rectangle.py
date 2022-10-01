from Shape import *


class Rectangle(Shape):
    def __init__(self, colour, side1, side2):
        """
        initializer for Rectangle shape, calls Shape (super) initializer and generates shape named Square or Rectangle
        :param colour: colour of Rectangle
        :param side1: length of rectangle side 1
        :param side2: length of rectangle side 2
        """
        if side1 == side2:
            super().__init__("Square ", colour, side1 * side2, 2 * (side1+side2))
        else:
            super().__init__("Rectangle ", colour, side1 * side2, 2 * (side1+side2))

        self.side1 = side1
        self.side2 = side2

    def get_side(self, side):
        """
        accessor for sides of the rectangle
        :param side: which side, either 1 or 2
        :return: side length or error
        """
        if side == 1:
            return self.side1
        elif side == 2:
            return self.side2
        else:
            return "Invalid Side"

    def combine(self, rect):
        """
        combines the side lengths of two rectangles and creates a new rectangle
        :param rect: rectangle whose attributes will be added to the current self rectangle
        :return: None
        """
        side1 = self.side1 + rect.side1
        side2 = self.side2 + rect.side2
        r = Rectangle("Black", side1, side2)
        print(r)

    def _str_(self):
        """
        toString method for Rectangle object
        :return: description of rectangle
        """
        return super().__str__() + " Side 1: " + str(self.side1) + " Side 2: " + str(self.side2)
