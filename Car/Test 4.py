import csv

outputTable = []
columns = ["Brand", "Price", "Body", "Mileage", "EngineV", "Engine Type", "Registration", "Year", "Model"]

with open(r"User Car Dealership.csv") as csv_file:
    reader = csv.reader(csv_file)
    line_Count = 0
    for row in reader:
        car_id = 0
        car_make = 0
        rowValues = str(",".join(row)).split(',')
        if line_Count == 0:
            print(rowValues[0], " ", rowValues[1], " ", rowValues[2], " ", rowValues[3])
            line_Count += 1

