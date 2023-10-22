"""
Jon William Taylor
Date: October 17, 2021
Assignment: Data processing using dictionary

About this program:
This program will read student data as input from a file and process/calculate the data and display the output.

Input: Will take take test score data from a file and calculate it

Output: Will display the calculated data from the file
"""
print(__doc__)

### import statements here

### define the sub functions here

### the main function
import csv

student_dict = {}

with open("C:\\Users\\JW\\Desktop\\student testscores.txt", 'r') as file: #opens the file
    reader = csv.reader(file) #reads the file
    for row in reader: #reads by row
        print(row)

input_file = {}
for aline in input_file:
    values = aline.split() #splits the line into words
    id = values[0] # first word in the line
    student_dict["Name"] = float(values[1]) #takes in the name of student
    student_dict["Test 1"] = float(values[2]) #takes in the first test score
    student_dict["Test 2"] = float(values[3]) #takes in the second test score
    student_dict["Test 3"] = float(values[4]) #takes in the third test score
    print(aline.split('\n')) #splits the line into each section


def get_letter_grade(score):
    lg = ""
    if score >= 90: #if the grade is 90 or above it prints A
        lg = "A"
    elif score >= 80: #if the grade is between 80 and 89 it prints B
        lg = "B"
    elif score >= 70: #if the grade is between 70 and 79 it prints C
        lg = "C"
    elif score >= 60: #if the grade is between 60 and 69 it prints D
        lg = "D"
    else: #if the grade is lower than a 60 it prints F
        lg = "F"
    return lg #returns the letter grade

def average_test(scores):
    total = 0
    for x in scores:
        total += x #calculates the total

    average = total/len(scores) #finds the average of the scores
    return average #shows the average

test_sum = {}
for i in student_dict.keys():
    test_sum += int(i)

print("Average score is {}", test_sum/len(student_dict)) #computes average score
student_dict["Letter Grade"] = get_letter_grade(student_dict["Average Score"]) #computes letter grade
print(student_dict)
