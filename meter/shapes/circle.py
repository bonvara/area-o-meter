import math

from meter.protocols import HasArea


class Circle(HasArea):
    """Circle class."""

    def __init__(self, radius: float) -> None:
        """Initialize the circle with a radius."""
        self.radius = radius

    def get_area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius**2
