from meter import area

print(dir(area))
area.hello_world()

t = area.Triangle(3, 4, 5)
print(t.get_area())

s = area.Shape()