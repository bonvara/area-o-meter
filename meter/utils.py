import math

from .protocols import HasArea


def are_equiareal(shape1: HasArea, shape2: HasArea) -> bool:
    """Check if two shapes have the same area, within default tolerance."""
    # To showcase polymorphism
    return math.isclose(shape1.get_area(), shape2.get_area())
