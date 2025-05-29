import math

import pytest

from meter.shapes.circle import Circle


def test_circle_area_zero_radius():
    circle = Circle(0)
    assert math.isclose(circle.get_area(), 0)


def test_circle_area_negative_radius():
    with pytest.raises(ValueError, match="Radius must be non-negative."):
        Circle(-3)


def test_circle_area_positive_radius():
    radius = 2
    circle = Circle(radius)
    assert circle.radius == radius
    assert math.isclose(circle.get_area(), 12.566370614359172)
