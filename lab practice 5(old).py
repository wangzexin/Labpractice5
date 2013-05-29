import math
import random

class Circle:

    version = '0.1'

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def calc_area(self):
        return math.pi * self.__radius ** 2.0

    def calc_perimeter(self):
        return 2.0 * math.pi * self.__radius

r = random.random() * 5
c = Circle(r)
print('Radius is     : ', '{0:.7f}'.format(c.get_radius()))
print('Area is         : ', '{0:.7f}'.format(c.calc_area()))
print('Perimeter is : ', '{0:.7f}'.format(c.calc_perimeter()))
