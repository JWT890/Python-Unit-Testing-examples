
"""
input_file = open("C:/Users/JW/Desktop/my_input_data.txt", "r")
for aline in input_file:
    print(aline)

input_file.close()
"""
#C:\Users\JW\Desktop\IS310\File Exercise.py
#or
#with open("my_input_data.txt") as input_file:
input_file = open("C:\\Users\\annual rainfall.txt")
number_of_lines = 0
header = next(input_file)
print(header)
print("*" * 20)
for aline in input_file:
    number_of_lines += 1
    #print(aline.rstrip())
    items = aline.split('\t')
    print(int(items[0]) * float(items[2]))

#print(number_of_lines)
