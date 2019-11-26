import math

def area(r):
    return math.pi * r * r

radii = [1, 2, 3, 4, 5, 6, 7]
map(area, radii)
filter(lambda x: x > 2, radii)

