class Shape:
    def __init__(self, name="", colour="", area=1, perimeter=1):
        """
        initializer for Shape object
        :param name: name of the shape, either rectangle, square, or circle
        :param colour: colour of the shape
        :param area: area of the shape
        :param perimeter: perimeter of the shape
        """
        self.colour = colour
        self.area = area
        self.perimeter = perimeter
        self.name = name

    def set_colour(self, colour):
        """
        mutator for colour attribute
        :param colour: colour to update as the shapes colour
        :return: None
        """
        self.colour = colour

    def get_colour(self):
        """
        accessor for colour attribute
        :return: colour
        """
        return self.colour

    def get_perimeter(self):
        """
        accessor for perimeter attribute
        :return: perimeter
        """
        return self.perimeter

    def get_area(self):
        """
        accessor for area attribute
        :return: area
        """
        return self.area

    def __str__(self):
        """
        toString function for Shape object
        :return: Description of shape
        """
        return self.name + "Attributes:\n Colour: " + self.colour +\
            ", Area: " + str(self.area) + ", Perimeter: " + str(self.perimeter)
