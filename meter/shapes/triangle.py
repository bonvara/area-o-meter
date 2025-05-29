import math

from meter.protocols import HasArea


class Triangle(HasArea):
    """Triangle with sorted sides."""

    def __init__(self, a: float, b: float, c: float) -> None:
        """Iitialize the triangle's sides as a sorted tuple."""
        a, b, c = sorted([a, b, c])
        if a + b < c:
            msg = (
                f"Invalid triangle sides: {a}, {b}, {c} do not satisfy the "
                "triangle inequality."
            )
            raise ValueError(msg)
        self.sides = (a, b, c)

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
