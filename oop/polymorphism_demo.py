import math

class Shape:
    def area(self):
        """This method should be overridden in derived classes."""
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Constructor to initialize the dimensions of the rectangle."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Constructor to initialize the radius of the circle."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
