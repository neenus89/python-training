# Take input from user:
# Name
# Age
# Course
# Marks (out of 100)
# Convert:
# Age → int
# Marks → float
# Display output like:
# ----- Student Details -----
# Name   : John
# Age    : 20
# Course : Python
# Marks  : 85.5
# Status : Pass
print('Enter your name:')
name = input()
print('Enter your age:')
age = int(input())
print('Enter your course:')
course = input()
print('Enter your marks:')
marks = float(input())
print('----- Student Details -----')
print('Name   :', name) 
print('Age    :', age)
print('Course :', course)       
print('Marks  :', marks)

if marks >= 50:
    print('Status : Pass')
else:
    print('Status : Fail')
