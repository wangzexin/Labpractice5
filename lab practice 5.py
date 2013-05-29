import math
import random

class Circle(object):

    version = '0.1'

    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * self.radius ** 2.0

    def calc_perimeter(self):
        return 2.0 * math.pi * self.radius

r = random.random() * 5
c = Circle(r)
print('Radius is     : ', '{0:.7f}'.format(c.radius))
print('Area is         : ', '{0:.7f}'.format(c.calc_area()))
print('Perimeter is : ', '{0:.7f}'.format(c.calc_perimeter()))
