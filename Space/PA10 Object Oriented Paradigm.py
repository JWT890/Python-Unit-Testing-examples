"""
Jon William Taylor
November 15, 2021
Assignment: Object Oriented Paradigm program
Semester: Fall 2021
IS 310-01 Advanced Computer Programming in Business


About this program:
This program will take data from a file, calculate and process it, and display the output

Input: Will take data from a file and process

Output: Will display the calculated output
"""
print(__doc__)

from Sun import * #brings in the data from the Sun file
from Planet import * #brings in the data from the Planet file
from SolarSystem import * #bromgs in the data from the Solar System file

def celestial_data():
    infile = open(r'solarsystemdata.txt') #opens up the text file
    count = 0 #starts counting the data
    next(infile)
    for line in infile:
        line.strip('\n') #breaks into columns
        values = line.split(',') #adds a comma between the columns
        print(values) #prints the values
        v1 = values[0].strip() #determines the values for either Planet, Solar System or Sun
        v2 = values[1].strip() #determines the values for either Planet, Solar System or Sun
        v3 = values[2].strip() #determines the values for either Planet, Solar System or Sun
        v4 = values[3].strip() #determines the values for either Planet, Solar System or Sun

        if count == 0: #determines if the data is related to the Sun
            sun = Sun(v1, v2, v3, v4) #looks at the data from the Sun file
            ss = SolarSystem(sun) #shows Sun data
        else: #determines if the data is not related to the Sun
            p = Planet(v1, v2, v3, v4) #looks at the data from the Planet file
            ss.addPlanet(p) #shows Planet data
        count += 1 #continues with the data

    ss.showPlanets() #shows the data

def main():
    celestial_data()

if __name__ == '__main__':
    main()
