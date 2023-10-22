"""
Jon William Taylor
Date: October 25, 2021
Assignment: Processing CSV files

About this program:
This program read demographic zip data from a file and process/calculate it and display the output

Input: Will take demographic data from a file and calculate it

Output: Will display the calculated data from the file
"""
print(__doc__)

### import statements here

### define sub functions here

### the main function
import csv

outputTable = [] #formats the data
columns = ["JURISDICTION NAME","COUNT PARTICIPANTS","COUNT FEMALE","PERCENT FEMALE","COUNT MALE", "PERCENT MALE"] #determines the column names
def zip_code_data():
    with open(r"C:\Users\Demographic_Stats_By_Zip_Code.csv") as csv_file: #opens the spreadsheet in pycharm
        reader = csv.reader(csv_file) #reads the csv file
        line_Count = 0 #starts reading the lines
        for row in reader:
            percent_females = 0 #checks for stats for females
            percent_males = 0 #checks for stats for males
            rowValues = str(",".join(row)).split(',') #splits the values by the rows
            if line_Count == 0: #determines if each row
                print(rowValues[0], " ", rowValues[1], " ", rowValues[2], " ", rowValues[3]) #prints the data for the respective rows
                line_Count += 1 #counts and adds each line
            else:
                if int(rowValues[1]) != 0: #determines if each row is similar or not
                    percent_females = round(((float(rowValues[2]) / float(rowValues[1])) * 100), 2) #calculates the percentage of females from the data
                    percent_males = round(((float(rowValues[3]) / float(rowValues[1])) * 100), 2) #calculates the percentage of males from the data
                    outputTable.append(rowValues[0] + "," + rowValues[1] + "," + rowValues[2] + "," + str(percent_females) + "," + rowValues[3] + "," + str(percent_males)) #formats the data into rows and columns
                    line_Count += 1 #counts and adds each line
            print(row)

    columnHeader = ", ".join(columns) #adds a comma between the columns
    print(columnHeader) #prints each column of data
    with open(r"C:\Users\PA05 Processing CSV Files.csv", "w") as output_file: #starts the process of exporting the file to Excel
        output_file.writelines(columnHeader) #splits the data into columns
        output_file.write('\n') #separates each section
        for record in outputTable:
            output_file.write(record) #records the data for the new file
            print(record)
            output_file.write('\n') #splits the data into rows
    print("Total records processed are: ", line_Count - 1) #counts how many lines are being processed

def main():
    zip_code_data()

if __name__ == '__main__':
    main()
