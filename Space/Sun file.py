"""
Jon William Taylor
This is the Sun class design object file
"""

class Sun:
    def __init__(self, Name, Rad, Mass, Temp):
        self.__name = Name
        self.__radius = Rad
        self.__mass = Mass
        self.__temp = Temp

    def get_name(self):
        return self.__name
    def get_radius(self):
        return self.__radius
    def get_mass(self):
        return self.__radius
    def get_temp(self):
        return self.__temp

    def __str__(self):
        return self.__name
