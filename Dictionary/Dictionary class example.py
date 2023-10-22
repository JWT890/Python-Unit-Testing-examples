# Storing a student record as a dict

student_dict = {}
def get_letter_grade(score):
    lg = ""
    if score >= 90:
        lg = "A"
    elif score >= 80:
        lg = "B"
    elif score >= 70:
        lg = "C"
    elif score >= 60:
        lg = "D"
    else:
        lg = "F"
    return lg


student_dict["Name"] = input("Enter student's name: ")
student_dict["Course Number"] = input("Enter a course number: ")
student_dict["Test 1"] = float(input("Enter test score for test 1: "))
student_dict["Test 2"] = float(input("Enter test score for test 2: "))

print(student_dict)


###Calculate the average score and the letter grade
student_dict["Average Score"] = student_dict["Test 1"] + student_dict["Test 2"] / 2
student_dict["Letter Grade"] = get_letter_grade(student_dict["Average Score"])
print(student_dict)

