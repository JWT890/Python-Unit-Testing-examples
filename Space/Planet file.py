"""
Jon William Taylor
This is the planet class design file
"""

import math

class Planet:
    def __init__(self, Name, Rad, Mass, Distance):
        self.__name = Name
        self.__radius = Rad
        self.__mass = Mass
        self.__distance = Distance

    def get_name(self):
        return self.__name

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass

    def get_distance(self):
        return self.__distance

    def get_volume(self):
        v = (4/3) * math.pi * (self.__radius ** 3)
        return v

    def get_surface_area(self):
        sa = 4 * math.pi * (self.__radius ** 2)
        return sa

    def get_density(self):
        density = self.__mass / self.get_volume()
        return density
