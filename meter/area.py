from abc import ABC, abstractmethod
import math


class BaseShape(ABC):
    """Abstract shape class."""

    @abstractmethod
    def get_area(self) -> float:
        """Calculate the area of the shape."""
        pass


class Circle(BaseShape):
    """Circle class."""

    def __init__(self, radius: float) -> None:
        """Initialize the circle with a radius."""
        self.radius = radius

    def get_area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius**2


class Triangle(BaseShape):
    """Triangle with sorted sides."""

    def __init__(self, a: float, b: float, c: float) -> None:
        """Iitialize the triangle with sorted sides."""
        self.sides = sorted([a, b, c])

    def get_area(self) -> float:
        """Calculate the area of the triangle."""
        a, b, c = self.sides
        if self.is_right():
            return a * b / 2
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def is_right(self) -> bool:
        """Use Pythagorean theorem with default tolerance to check if the triangle is right-angled."""
        a, b, c = self.sides
        return math.isclose(a**2 + b**2, c**2)


def are_equiareal(shape1: BaseShape, shape2: BaseShape) -> bool:
    """Check if two shapes have the same area, within default tolerance."""
    return math.isclose(shape1.get_area(), shape2.get_area())


## Debugging
my_circle = Circle(1.38197659788)
my_triangle = Triangle(3, 4, 5)

print(are_equiareal(my_circle, my_triangle))

print(type(my_circle))
print(type(my_triangle))

print(isinstance(my_circle, BaseShape))
print(isinstance(my_triangle, BaseShape))
