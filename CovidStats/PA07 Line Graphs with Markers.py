"""
Jon William Taylor
Date: November 4, 2021
Assignment: Line Graphs with Markers

About this program:
This program will read data from a file, draw a line graph from it, and display the output

Input: Will take the survey data from a file and process it

Output: Will draw a line graph from the input and display it
"""
print(__doc__)

from matplotlib import pyplot as plt

import csv
import numpy as np

x = []
y1 = []
y2 = []

def line_graph():
    with open(r'Demographic_Stats_By_Zip_Code.csv') as csv_file: #opens the file as a csv file
        plot_values = csv.reader(csv_file, delimiter=",") #starts reading the file
        header = next(plot_values)
        counter = 0 #starts counting the rows
        for row in plot_values:
            counter += 1 #counts the data till it gets to a number
            if counter > 20: #counts till the 20th line
                break #stops at line 20
            x.append(int(row[0]))
            y1.append(int(row[2]))
            y2.append(int(row[3]))

    the_header = str(header).strip('[') #sets up the graph
    the_header = str(the_header).strip(']') #sets up the graph
    headers = the_header.split(",")

    for header in headers:
        h = header.lstrip("'")
        h = h.strip("'")
        #print(h)

    #title_plots = title_plots.strip("'")
    print(headers[0]) #names one of the axis
    print(headers[2]) #names one of the axis
    print(headers[3]) #names one of the axis

    xValues = np.arange(len(x))
    plt.plot(xValues, y1, linestyle='--', marker='o', c='red', linewidth=2, markersize=5, mec='black', mfc='blue', label='Female') #sets up the line graph legend and graph
    plt.plot(xValues, y2, linestyle='--', marker='v', c='blue', linewidth=2, markersize=5, mec='blue', mfc='yellow', label='Male') #sets up the line graph legend and graph
    plt.legend() #prints the legend
    plt.xlabel(headers[0].strip().strip("'")) #shows the label
    plt.ylabel(headers[1].strip().strip("'")) #shows the label
    plt.xticks(np.arange(len(x)), x, rotation=90)
    #plt.xtickslabels(x, rotation=90)
    plt.title("Total and Gender Counts Per Jurisdiction") #names the line graph
    plt.tight_layout() #shows the title of the graph
    plt.savefig(r"C:\Users\JW\Desktop\OutputGraph 2.png") #saves the file as a png file
    plt.show() #shows the graph

def main():
    line_graph()


if __name__ == '__main__':
    main()
