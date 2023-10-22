"""
Jon William Taylor
November 15, 2021
Assignment: Object Oriented Paradigm
Semester: Fall 2021
IS 310-01 Advanced Computer Programming in Business

About this program:
This is the Sun class design object file
"""

class Sun:
    def __init__(self, Name, Rad, Mass, Temp):
        self.__name = Name #determines the name of the celestial body
        self.__radius = Rad #determines the radius of the celestial body
        self.__mass = Mass #determines the mass of the celestial body
        self.__temp = Temp #determines the temperature of the celestial body

    def get_name(self):
        return self.__name #provides the name of the Sun

    def get_radius(self):
        return self.__radius #provides the radius of the Sn

    def get_mass(self):
        return self.__mass #provides the mass of the Sun

    def get_temp(self):
        return self.__temp #provides the temperature of the Sun

    def __str__(self):
        return self.__name #provides the name of the Sun as a string
