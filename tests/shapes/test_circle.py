import math
import pytest

from meter import Circle


def test_circle_area_positive_radius():
    radius = 2.0
    circle = Circle(radius)
    expected_area = math.pi * radius**2
    assert math.isclose(circle.get_area(), expected_area)


def test_circle_area_zero_radius():
    circle = Circle(0)
    assert circle.get_area() == 0


def test_circle_area_negative_radius():
    with pytest.raises(ValueError, match="Radius must be non-negative."):
        Circle(-3)


def test_circle_radius_storage():
    radius = 5.5
    circle = Circle(radius)
    assert circle.radius == radius
