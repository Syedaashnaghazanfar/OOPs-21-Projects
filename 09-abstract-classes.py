from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
# Create instances of Rectangle and Circle
rectangle = Rectangle(5, 10)
circle = Circle(7)
# Calculate and print the area of the rectangle and circle
print(f"Area of Rectangle: {rectangle.area()}")  # Output: Area of Rectangle: 50
print(f"Area of Circle: {circle.area()}")  # Output: Area of Circle: 153.86
# The Shape class is an abstract class that defines an abstract method area.
# The Rectangle and Circle classes inherit from Shape and provide their own implementations of the area method.
# This allows for polymorphism, where different shapes can be treated uniformly through the Shape interface.
# Abstract classes are useful for defining a common interface for a group of related classes.
# They cannot be instantiated directly and must be subclassed.
