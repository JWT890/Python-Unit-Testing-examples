
from Car import *

infile = open(r"C:\Users\PycharmProjects\User Car Dealership.csv")
count = 0
next(infile)
for line in infile:
    line.strip('\n')
    values = line.split(',')
    print(values)
    v1 = values[0].strip()
    v2 = values[1].strip()
    v3 = values[2].strip()
    v4 = values[3].strip()
    v5 = values[4].strip()
    v6 = values[5].strip()
    v7 = values[6].strip()
    v8 = values[7].strip()
    v9 = values[8].strip()

if count == 0:
    car = Car(v1, v2, v3, v4, v5, v6, v7, v8, v9)
    cc = Car(car)
cc.showCars()

