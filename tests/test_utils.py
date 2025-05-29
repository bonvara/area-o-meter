from meter.shapes.circle import Circle
from meter.shapes.triangle import Triangle
from meter.utils import are_equiareal


def test_are_equiareal_same_circle():
    circle1 = Circle(2)
    circle2 = Circle(2)
    assert are_equiareal(circle1, circle2)


def test_are_equiareal_different_circles():
    circle1 = Circle(2)
    circle2 = Circle(3)
    assert not are_equiareal(circle1, circle2)


def test_are_equiareal_triangle_self():
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(3, 4, 5)
    assert are_equiareal(triangle1, triangle2)


def test_are_equiareal_triangle_different():
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(5, 6, 7)
    assert not are_equiareal(triangle1, triangle2)


def test_are_equiareal_circle_triangle():
    circle = Circle(1.38197659788)
    triangle = Triangle(3, 4, 5)
    assert are_equiareal(circle, triangle)


def test_are_equiareal_circle_triangle_not():
    circle = Circle(1)
    triangle = Triangle(2, 2, 2)
    assert not are_equiareal(circle, triangle)
