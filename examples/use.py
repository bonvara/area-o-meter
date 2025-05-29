from meter.shapes.circle import Circle
from meter.shapes.triangle import Triangle
from meter.utils import are_equiareal


my_circle = Circle(1.38197659788)
my_triangle = Triangle(3, 4, 5)

print(are_equiareal(my_circle, my_triangle))
