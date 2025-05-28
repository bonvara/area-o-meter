import meter
from meter.shapes.circle import Circle
import meter.utils

print(dir(meter))
print(dir(meter.shapes))

# print(dir(meter.__all__))

# from meter.shapes.circle import Circle

c = Circle(1.38197659788)
print(c.get_area())

# t = Triangle(3, 4, 5)
# print(t.get_area())


# my_circle = utils.Circle(1.38197659788)
# my_triangle = utils.Triangle(3, 4, 5)

# print(utils.are_equiareal(my_circle, my_triangle))
