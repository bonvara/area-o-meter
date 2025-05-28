from meter import utils

print(dir(utils))

t = utils.Triangle(3, 4, 5)
print(t.get_area())

s = utils.BaseShape()


my_circle = utils.Circle(1.38197659788)
my_triangle = utils.Triangle(3, 4, 5)

print(utils.are_equiareal(my_circle, my_triangle))
