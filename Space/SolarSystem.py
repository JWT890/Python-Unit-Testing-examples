"""
Jon William Taylor
November 15, 2021
Assignment: Object Oriented Paradigm
Semester: Fall 2021
IS 310-01 Advanced Computer Programming in Business


About this program:
This is the Solar system design file
"""

class SolarSystem: #labels the data as Solar System
    def __init__(self, aSun):
        self.__theSun = aSun
        self.__planets = [] #puts a placeholder for the data

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet) #determines the respective data of the Planet

    def showPlanets(self):
        print("Name, Radius, Mass, Distance, Volume, Surface Area, Density") #names each column of the data
        for aPlanet in self.__planets:
            print('{}, {}, {}, {}, {}, {}, {}'.format(aPlanet.getName(), aPlanet.getRadius(), aPlanet.getMass(), aPlanet.getDistance(), aPlanet.getVolume(), aPlanet.getSurfaceArea(), aPlanet.getDensity())) #formats the appropriate data

