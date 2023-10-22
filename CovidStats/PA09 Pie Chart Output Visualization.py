"""
Jon William Taylor
Date: November 8, 2021
Assignment: Pie Chart Graph visualization output

About this program:
This program will take data from a file, process it, and show it as a pie graph

Input: Will take data from a file and process it

Output: Will display a pie chart from the data
"""
print(__doc__)

import matplotlib.pyplot as plt
import csv
import numpy as np

x = [] #empty space for data on x axis
y = [] #empty space for data on y axis
header = ""

def pie_chart():
    row_count = 0 #starts the row count at 0
    with open(r"stateTerritoriesUSACovid.csv") as csv_file: #opens the file
        plot_values = csv.reader(csv_file, delimiter=',') #reads the file
        header = next(plot_values)
        for row in plot_values:
            row_count += 1 #starts counting the rows
            if row_count > 20: #finds line 20
                break #stops at line 20
            x.append(row[0])
            y.append(int(row[1]))

    title_pattern = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] #sets up the data for the pie graph
    p1 = plt.pie(y, labels=x, labeldistance=1.0, rotatelabels=True, startangle=110) #sets up the pie graph
    plt.title("Statewide COVID-19 Data Cases", y=1.1) #names the title of the graph
    plt.show() #shows the title of the graph
    fig = plt.figure(figsize=(10, 8)) #sets the figure size of the graph

    plt.savefig(r"C:\Users\JW\Desktop\Pie Chart.png") #saves the graph as a png file and saves it at location

def main():
    pie_chart()

if __name__ == '__main__':
    main()
