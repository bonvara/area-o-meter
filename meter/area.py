from abc import ABC, abstractmethod
import math

def hello_world():
    print("Arakadabra!")

class Shape(ABC):
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.sides = sorted([a, b, c])

    def get_area(self):
        a, b, c = self.sides
        if self.is_right():
            return a * b / 2
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    def is_right(self):
        a, b, c = self.sides
        return math.isclose(a**2 + b**2, c**2)

