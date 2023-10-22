"""
Jon William Taylor
Date: November 1 2021
Assignment: Visualization Output and Line Graph

About the program:
This program will read data from a file, draw a line graph from it, and display the output

Input: Will take survey data from a file and process it

Output: Will draw a line graph from the survey data
"""
print(__doc__)

### import statements here

### define sub functions here

### the main function

from matplotlib import pyplot as plt

import csv
import numpy as np

#get two lists of random numbers
from random import randint

x = [] #places the data for the x axis
y1 = [] #places the data for the first y axis
y2 = [] #places the data for the second y axis
def line_graph():
    with open(r'Demographic_Stats_By_Zip_Code.csv') as csv_file: #opens the file
        plot_values = csv.reader(csv_file, delimiter = ",")
        header = next(plot_values) #starts plotting the values
        counter = 0 #starts the process of reading the values
        for row in plot_values:
            counter += 1 #counts each row for data
            #if counter > 20:
                #break
            x.append(int(row[0]))
            y1.append(int(row[2])) #total female participants
            y2.append(int(row[3])) #total male participants

    the_header = str(header).strip('[')
    the_header = str(the_header).strip(']')
    headers = the_header.split(',') #splits the data

    for header in headers:
        h = header.lstrip("'") #splits the data
        h = h.rstrip("'") #splits the data
        #print(h)
    #title_plots = title_plots.strip("'")
    print(headers[0])
    print(headers[2])
    print(headers[3])

    xValues = np.arange(len(x)) #starts arranging the values on the graph
    plt.plot(xValues, y1, linestyle='--', marker='o', c='red', linewidth=2, markersize=5, mec='black', mfc='blue', label="Female") #determines the characteristics of first y axis
    plt.plot(xValues, y2, linestyle=':', marker='v', c='green', linewidth=2, markersize=5, mec='blue', mfc='yellow', label='Male') #determines the characteristics of second y axis
    plt.legend() #places the legend on the graph
    plt.xlabel(headers[0].strip().strip("'"))
    plt.ylabel(headers[1].strip().strip("'"))
    plt.xticks(np.arange(len(x)), x) #arranges the data into a graph
    #plt.set_xtickslabels(x, rotation=90)
    plt.title("Female and Male Survey Participants") #names the top of the graph
    plt.tight_layout()
    plt.savefig(r"C:\Users\Desktop\OutputGraph.png") #outputs the graph into a png file at file location
    plt.show() #shows the graph as a png file

def main():
    line_graph()


if __name__ == '__main__':
    main()
