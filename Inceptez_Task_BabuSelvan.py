
# Task A

# The following program throws an indentation error. Correct it and make sure it prints properly.

teams = ['Data', 'AI', 'DevOps']
for t in teams:
    print('Hello', t, 'Team from Inceptez Technologies')
print('Keep Learning and Exploring!')

teams = ['Data', 'AI', 'DevOps']
for t in teams:
    print('Hello', t, 'Team from Inceptez Technologies')
    print('Keep Learning and Exploring!')

# Task B

"""
Use Case 1:
Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies’ training tracker.
"""

# Here Summing the value of Students and Trainers and store the output in the total variable
students = 100
trainers = 2
total = students + trainers
# Total = students - trainers
print(total)

''' This is the end of this task'''


"""Use Case 2:
Convert the below block into a “dead code” using comments, then re-activate it later to print
"""

# print("Welcome to Inceptez Python Learning")
print("Welcome to Inceptez Python Learning - Babu Selvan")


# Task C. Playing with Quotes

'''Use Case 1:
Create three string variables that correctly store and print:

This is Inceptez's "Python" class for Data Engineers & AI Engineers
→ Use single, double, and triple quotes appropriately.
'''

print('''This is Inceptez's "Python" class for Data Engineers & AI Engineers''')

### use Case 2:

'''Write a multiline string using triple quotes that prints:

Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.
'''

print ('''
Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.
''')

# Task D : Let's learn all about VARIABLES

'''Use Case 1:
Declare variables to store the following details:
- Student Name
- Course Name (e.g., “Python Fundamentals”)
- Training Institute Name (Inceptez Technologies)
Then print a formatted message:
Name: Babu is learning the course Python Fundamentals at the institute Inceptez Technologies
'''

student = 'Babu'
course = 'Python Fundamentals'
Train_Inst = "Inceptez Technologies"

print("Babu is learning the course Python Fundamentals at the institute Inceptez Technologies")

print(f"{student} is learning the course {course} at the institute {Train_Inst}")

print(student+ " is learning the course " +course+ " at the institute " +Train_Inst)

print(student, "is learning the course" ,course, "at the institute" ,Train_Inst)
# Here Space automatically amending


# Use Case 2:
'''
Demonstrate dynamic inference, dynamic typing using with fee by applying .18 gst  and prove strongly typing character also by operating it with Eighteen percent gst
fee = 45000
'''

# Dynamic Inference
fee = 45000
gst = .18
total = fee * gst
print(total)
print(type(total))
total = "Dynamic Typing"
print(total)
print(type(total))

# E. Variables Naming Conventions

"""
Use Case 1:
Identify which variable names below are invalid for Inceptez’s student database:
1) 2student = 'Ravi'
2) _student_id = 1001
3) studentName = 'Priya'
4) class name = 'Python'
5) inceptez_batch = 'Morning'
"""

### Number 1 (starting with Number) and 4 (key words and spaces) are Invalid

# Use Case 2:

"""
Declare 3 variables following naming styles for Inceptez projects:

PascalCase: DataEngineeringBatch
camelCase: dataEngineeringBatch
snake_case: data_engineering_batch
"""
InceptezProjects = "DataEngineeringBatch"
inceptezProjects = 'dataEngineeringBatch'
inceptez_projects = "data_engineering_batch"

print(InceptezProjects)
print(inceptezProjects)
print(inceptez_projects)



# Day Task = 12 09 2026

# F. Type identification & Casting
""" Use Case 1:
Write a program that asks for an employee’s age.
1. Checks its type is of string (think about using isinstance() function)
2. Converts it to int (continue writing your program from here..)
3. Prints the years pending for retirement, for eg. 60 is the retirement age.
Example:
Enter your age: 40
You will retire in 20 years at Inceptez Technologies.
"""

age = (input("Enter your age : "))
print(age)
print(type(age))
print(isinstance(age,str))
if isinstance(age,str):
    print(age,"is a string")
else:
    print(age,"is not a string")
age_dtype = int(age)
print(age_dtype)
print(type(age_dtype))
yr_pending = 60-age_dtype
print("you will retire in",yr_pending,"years at Standard Chartered Bank")

#Use Case 2 (Debug):
"""
Fix the type error in the following code for salary calculation:
salary = '50000'
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)
"""

salary = 50000
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)

"""
G. Data types and casting
Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
Employee Salary Breakdown
a. Write a program that asks the user for:
employee_name (string)
base_salary (float)
hra_percent (integer)
bonus_amount (float)
"""

name:str = input("Enter your employee name: ")
bs= input("Enter your Basic salary: ")
bs = float(bs)
hra_per = input("Enter your HRA Percent: ")
hra_per = int(hra_per)
ba = input("Enter your BA Percent: ")
ba = float(ba)

print("Employee Name is",name)
print("Employee Basic salary is ",bs)
print("Employee HRA Percent is",hra_per)
print("Employee Bonus Amount is ",ba)

'''
B. Convert inputs to the correct datatype if required.
Calculate:
 HRA = base_salary * (hra_percent / 100)
 Total Salary = base_salary + HRA + bonus_amount
C. Print the output like this:
Employee: Arun
Base Salary: 40000.0
HRA @ 20%: 8000.0
Bonus: 5000.0
Total Salary Payable: ₹53000.0
'''

hra = bs * (hra_per/100)
ts = bs + hra + ba

print("Employee :",name)
print("Basic salary :",bs)
print("HRA @ 20%",hra)
print("Total Salary Payable:",ts)

# Use Case 2: Student Result Classification
"""
a. Write a program that takes marks as input (initially as a string).
B. Check if the value can be converted to float.
C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
Marks >= 90 --> Outstanding
 Marks >= 75 --> Excellent
 Marks >= 50 --> Pass
 Marks < 50 --> Fail
D. If the input is not numeric, print:
 Invalid marks entered — Please provide numeric input.
"""

# a.
mark:str = input("Enter your mark:")
print(type(mark))
print("Your mark is",mark)

# b.
mark = float(mark)
print(type(mark))

# c.
if (mark >= 90):
    print("You are Outstanding")
elif (mark >= 75):
    print("You are Excellent")
elif (mark >= 50):
    print("You are just Pass")
elif (mark < 50):
    print("You are Fail")
else:
    print("Invalid marks entered — Please provide numeric input.")


# Use Case 3: Bug Fixing — Datatype Mismatch
#The below code is intended to calculate total price, but it has datatype errors. Fix it.

item_name = input("Enter product name: ")
price =input("Enter price per item: ")
price = float(price)
quantity = input("Enter quantity: ")
quantity = int(quantity)
total_cost = price * quantity
print(f"You purchased {quantity} units of " + item_name)
print("Total payable: ", total_cost)





