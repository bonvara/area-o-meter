"""Defines shapes and their area calculations."""

import math
from abc import ABC, abstractmethod


class BaseShape(ABC):
    """Abstract shape class."""

    @abstractmethod
    def get_area(self) -> float:
        """Calculate the area of the shape."""


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
        """Check if the triangle is right-angled.

        Uses Pythagorean theorem with default tolerance.
        """
        a, b, c = self.sides
        return math.isclose(a**2 + b**2, c**2)


def are_equiareal(shape1: BaseShape, shape2: BaseShape) -> bool:
    """Check if two shapes have the same area, within default tolerance."""
    return math.isclose(shape1.get_area(), shape2.get_area())
