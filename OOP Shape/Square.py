from Rectangle import *


class Square(Rectangle):
    def __init__(self, colour, side):
        """
        initializer for Square shape
        :param colour: colour of square
        :param side: length of square side
        """
        super().__init__(colour, side, side)
        self.side = side
