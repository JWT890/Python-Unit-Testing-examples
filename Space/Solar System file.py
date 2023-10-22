"""
Jon William Taylor
This is the Solar system file
"""

class SolarSystem:
    def __init__(self, aSun):
        self.__theSun = aSun
        self.__planets = []

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def showPlanets(self):
        print("Name, Radius, Mass, Distance, Volume, Surface Area, Density")
        for aPlanet in self.__planets:
            print('{}, {}, {}, {}, {}, {}, {}'.format(aPlanet.getName(), aPlanet.getRadius, aPlanet.getMass(), aPlanet.getDistance(), aPlanet.getVolume(), aPlanet.getSurfaceArea(), aPlanet.getDensity()))

