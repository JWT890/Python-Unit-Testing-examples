"""
Jon William Taylor
November 15, 2021
Assignment: Object Oriented Paradigm
Semester: Fall 2021
IS 310-01 Advanced Computer Programming in Business

About this program:
This is the planet class design file
"""

import math

class Planet: #labels the data as the Planet class
    def __init__(self, Name, Rad, Mass, Distance): #determines the respective data categories for each Planet
        self.__name = Name #looks for the Planet name
        self.__radius = Rad #looks for the Planet radius
        self.__mass = Mass #looks for the Planet mass
        self.__distance = Distance #looks for the Planet distance

    def get_name(self):
        return self.__name #determines the name of the Planet from the data

    def get_radius(self):
        return self.__radius #determines the radius of the Planet from the data

    def get_mass(self):
        return self.__mass #determines the mass of the Planet from the data

    def get_distance(self):
        return self.__distance #determines the distance from the Sun of the Planet from the data

    def get_volume(self):
        v = (4/3) * math.pi * (self.__radius ** 3) #computes the volume of the planet
        return v #shows the result

    def get_surface_area(self):
        sa = 4 * math.pi * (self.__radius ** 2) #computes the surface area of the planet
        return sa #shows the result

    def get_density(self):
        density = self.__mass / self.get_volume() #computes the density of the planet
        return density #shows the result
