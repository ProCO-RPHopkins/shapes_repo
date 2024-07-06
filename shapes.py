from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, color, shape_name):
        # initiates the shape with a color parameter
        self.color = color
        self.shape_name = shape_name

    @abstractmethod
    def area(self):
        # abstract method calculates area of shape
        raise NotImplementedError("Subclass must implement area method")
    
    @abstractmethod
    def perimeter(self):
        # abstract method calculates perimeter of shape
        raise NotImplementedError("Subclass must implement perimeter method")
    
    def get_color(self):
        # returns the color of shape
        return self.color
    
    def set_color(self, color):
        # sets the color of shape
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        # initiates circle with color and radius parameters
        super().__init__(color, "Circle")
        self.radius = radius

    def area(self):
        # calculates area of circle
        return round(math.pi * self.radius ** 2, 2)
    
    def perimeter(self):
        # calculates perimeter of circle
        return round(2 * math.pi * self.radius, 2)
    
class Rectangle(Shape):
    def __init__(self, color, length, width):
        # initiates rectangle with color, length, and width parameters
        super().__init__(color, "Rectangle")
        self.length = length
        self.width = width
    
    def area(self):
        # calculates area of rectangle
        return round(self.length * self.width, 2)
    
    def perimeter(self):
        # calculates perimeter of rectangle
        return round(2 * (self.length + self.width), 2)
    
class Triangle(Shape):
    def __init__(self, color, sideA, sideB, sideC):
        # initiates triangle with color, sideA, sideB, and sideC parameters
        super().__init__(color, "Triangle")
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
    
    def area(self):
        # calculates area of triangle using Heron's formula
        '''used Heron's formula rather than traditional method (1/2 base * height) since 
        all three side parameters are necessary to find perimeter'''
        s = (self.sideA + self.sideB + self.sideC) / 2
        return round(math.sqrt(s * (s - self.sideA) * (s - self.sideB) * (s - self.sideC)), 2)
    
    def perimeter(self):
        # calculates perimeter of triangle
        return round(self.sideA + self.sideB + self.sideC, 2)

def main():
    # creates instances of shapes
    circle = Circle("blue", 5)
    rectangle = Rectangle("green", 5, 10)
    triangle = Triangle("yellow", 3, 4, 5)

    # store shape objects in a list
    shapes = [circle, rectangle, triangle]

    # iterate through list of shapes and print information about each shape
    # spaces align colons for user friendly output
    for shape in shapes:
        print(f"    Shape: {shape.shape_name}")
        print(f"    Color: {shape.get_color()}")
        print(f"     Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
        print("-" * 30)

if __name__ == "__main__":
    main()