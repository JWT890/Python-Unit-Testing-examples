"""
Jon William Taylor
Date: November 8 2021
Assignment: Bar Graph Output Visualization

About this program:
This program will take data from a file, draw a bar graph from it, and display the output

Input: Will take the survey data from a file and process it

Output: Will draw a bar graph from the input and display it
"""
print(__doc__)

from matplotlib import pyplot as plt

import csv
import numpy as np

x = [] #provides a place for the data to be inserted as a bar
y1 = [] #provides a place for the data to be inserted as a bar
y2 = [] #provides a place for the data to be inserted as a bar
total_participants = [] #provides a place for the data to be inserted as a bar
def bar_graph():
    with open(r'Demographic_Stats_By_Zip_Code.csv') as csv_file: #opens the file as a csv file
        plot_values = csv.reader(csv_file, delimiter=",") #starts reading the file
        header = next(plot_values)
        counter = 0 #starts reading the data from the first line
        for row in plot_values:
            counter += 1 #counts each line for the data
            if counter > 20: #stops counting at line 20 of the survey results
                break
            x.append(int(row[0]))
            total_participants.append(int(row[1]))
            y1.append(int(row[2])) #total female particpants
            y2.append(int(row[3])) #total male participants

    the_header = str(header).strip('[')
    the_header = str(the_header).strip(']')
    headers = the_header.split(",")
    bar1 = header[2].strip("'") #takes one of the first three names from the results
    bar2 = header[3].strip("'") #takes one of the first three names from the results
    bar3 = header[1].strip("'") #takes one of the first three names from the results
    for header in headers:
        h = header.lstrip("'")
        h = h.strip("'")

    width = 0.25 #space between each bar on the graph
    xValues = np.arange(len(x))
    p1 = plt.bar(xValues - width, y1, width, color='red', label=bar1) #places and labels the first bar
    p2 = plt.bar(xValues, y2, width, color='green', label=bar2) #places and labels the second bar
    p3 = plt.bar(xValues + width, total_participants, width, color='blue', label=bar3) #places and labels the third bar
    plt.xlabel(headers[0].strip("'"))
    plt.ylabel('Participants') #names one of the axis
    plt.xticks(xValues, x, rotation=90) #shows the number data on the axis
    plt.title('Survey Results of Participants: Bar Graph') #names the bar graph
    plt.legend() #prints the bar graph legend
    plt.tight_layout()
    plt.show() #shows the bar graph
    plt.savefig(r"C:\Users\Desktop\Bar Graph.png") #saves the graph as a png file

def main():
    bar_graph()


if __name__ == '__main__':
    main()
