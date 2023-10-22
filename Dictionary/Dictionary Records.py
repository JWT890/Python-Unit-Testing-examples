MAX = 2
student_dictionary = {} # this is to  temporary hold a record
student_records = {} # this holds several records

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



for i in range(MAX):
    rec_id = input("Enter a 2 digit number: ")
    student_dictionary["Name"] = input("Enter the student's name: ")
    student_dictionary["Course Number"] = input("Enter Course Number: ")
    student_dictionary["Test 1"] = float(input("Enter test 1 score: "))
    student_dictionary["Test 2"] = float(input("Enter test 2 score: "))

    student_records["A00" + rec_id] = student_dictionary
    student_dictionary = {}

for rec_id, rec in student_records.items():
    print(rec_id, ": ", rec)
    rec["Average Score"] = (rec["Test 1"] + rec["Test 2"]) / 2
    rec["Letter Grade"] = get_letter_grade(rec["Average Score"])
    for key, val in rec.items():
        print(key, ": ", val)

for rec_id, rec in student_records.items():
    print(rec_id, ": ", rec)

print(student_records)
