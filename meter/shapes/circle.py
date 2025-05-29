import math

from meter.protocols import HasArea


class Circle(HasArea):
    """Circle class."""

    def __init__(self, r: float) -> None:
        """Initialize the circle with a radius.

        Raises ValueError if radius is negative.
        """
        if r < 0:
            msg = "Radius must be non-negative."
            raise ValueError(msg)
        self.radius = r

    def get_area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius**2
