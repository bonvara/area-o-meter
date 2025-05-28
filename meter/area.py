from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract shape class."""

    @abstractmethod
    def get_area(self) -> float:
        """Calculate the area of the shape."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius: float) -> None:
        """Initialize the circle with a radius."""
        self.radius = radius

    def get_area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius**2


class Triangle(Shape):
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
        """Check if the triangle is right-angled."""
        a, b, c = self.sides
        return math.isclose(a**2 + b**2, c**2)
