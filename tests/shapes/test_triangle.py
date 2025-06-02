import math

import pytest

from meter.shapes.triangle import Triangle


def test_triangle_area_right():
    triangle = Triangle(5, 13, 12)
    assert math.isclose(triangle.get_area(), 30)
    assert triangle.is_right()


def test_triangle_area_equilateral():
    triangle = Triangle(2, 2, 2)
    expected_area = 1.7320508075688772
    assert math.isclose(triangle.get_area(), expected_area)
    assert not triangle.is_right()


def test_triangle_area_scalene():
    triangle = Triangle(5, 6, 7)
    expected_area = 14.696938456699069
    assert math.isclose(triangle.get_area(), expected_area)
    assert not triangle.is_right()


def test_triangle_degenerate():
    triangle = Triangle(1, 2, 3)
    assert triangle.get_area() == 0
    assert not triangle.is_right()


def test_triangle_invalid():
    with pytest.raises(ValueError, match="Invalid"):
        Triangle(1, 2, 4)


def test_triangle_invalid_side_length():
    with pytest.raises(ValueError, match="non-negative."):
        Triangle(1, -2, 3)
