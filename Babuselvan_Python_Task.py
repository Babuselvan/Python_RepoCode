from multiprocessing.managers import convert_to_error

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

#H. Python Operators Use cases
"""
Write a program that asks the user for:
Total monthly data limit (in GB)
Data used so far (in GB)

Calculate using arithmetic operators:
 Remaining data = limit - used
 Usage percentage = (used / limit) * 100
Print:
Remaining data
Usage percentage rounded to 2 decimals

If usage percentage is greater than or equal to 80, print:
 "Warning: High usage, consider upgrading your plan."
"""

total_data = int(input("Enter the Total Monthly data in GB :"))
data_used = float(input("Enter the Data used so far in GB"))

remaining_data = total_data - data_used
usage_percentage = (data_used / total_data) * 100
print(usage_percentage)
usage_percentage = round(usage_percentage)

print(f"Remaining data in GB : {remaining_data}, Usage percentage : {usage_percentage}%")

if usage_percentage >= 80:
    print("Warning: High usage, consider upgrading your plan.")


#Use Case 2: Shopping Discount Calculation

"""
Write a program that takes:
Original price (float)
Discount percent (int)

Using assignment and arithmetic operators, calculate:
 Discount amount = (price * discount_percent) / 100
 Final price = price - discount_amount
Print:
 Original price, discount applied, and final payable amount.
"""

original_price = float(input("Enter the Original price: "))
discount_percent = int(input("Enter the Discount percent: "))

discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount

print(f"Original Price: {original_price}, Discount applied : {discount_amount}, Final Payable Amount : {final_price}")


#Use Case 3 (Bug Fixing): Logical and Comparison Operator Errors

'''
The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
Incorrect code:
age = input("Enter age: ")
 citizen = input("Are you an Indian citizen? (yes/no)")
if age > "18" and citizen = "yes":
 print("Eligible to vote")
 else:
 print("Not eligible")
Expected behavior:
Convert age to integer before comparison.

Only print "Eligible to vote" if age is 18 or above AND citizen input is "yes" (case-insensitive).
'''

age = int(input("Enter age: "))
citizen = input("Are you an Indian citizen? (yes/no)")
if age > 18 and citizen == 'yes':
    print("Eligible to vote")
else:
    print("Not eligible")

# I. Conditional Structure

"""
Use Case 1: Banking Eligibility Check
Write a program that asks the user for:
Age
Monthly income

Conditions:
If age < 18: print "Not eligible for a bank account."
If age >= 18 and income < 15000: print "Eligible for basic savings account."
If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
If age >= 18 and income > 50000: print "Eligible for premium account."
"""

age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))

if age < 18:
    print("Not eligible for bank account.")
elif age >=28 and income <= 15000:
    print("Eligible for basic savings account.")
elif age >=18 and (income > 15000 and income < 50000):
    print("Eligible for savings + salary account.")
elif age >=18 and income >= 50000:
    print("Eligible for premium account.")

# Use Case 2: Check room availability

"""
-Check room availability
    - If available:
        - If guest is VIP
            → Offer complimentary upgrade
        - Else if member 5+ years
            → Offer discount
        - Else
            → Standard price
    - Else:
        → Show: "No rooms available"
"""

room_avail = 'true'
guest = 'nonvip'
yr_member = 3

if room_avail == 'true':
    if guest == 'vip':
        print("offer complimentary upgrade")
    elif yr_member >= 5:
        print("offer discount")
    else:
        print("Standard price")
else:
    print("No rooms available")

#Use Case 3 (Bug Fixing): Nested Condition Logic Issue

"""
Fix the following code so that it correctly determines whether the entered temperature indicates normal, fever, or high fever.
Incorrect code:
temp = input("Enter body temperature in Celsius: ")
if temp < "37":
 print("Normal temperature")
 elif temp > "37" and temp < "39":
 print("Fever")
 else
 print("High fever")
Expected behavior:
Convert temperature to float before comparison.

Conditions should print:
 Normal temperature (less than 37)
 Fever (between 37 and 39)
 High fever (39 and above)
"""

temp = float(input("Enter body temperature in Celsius: "))
if temp < 37:
    print("Normal temperature")
elif temp > 37 and temp < 39:
    print("Fever")
else:
    print("High fever")

# J. Looping Constructs

"""
Use Case 1: Table Generator
 Write a program that takes a number from the user and prints the multiplication table from 1 to 10 for that number.
Example:
 If user enters 5, output should be:
 5 x 1 = 5
 ...
 5 x 10 = 50
"""

no = int(input("Enter a number to display respective Table: "))

for i in range(1,11):
    print(f"{no} X {i} = {i * no}")

# Use Case 2: Sum of Even and Odd Numbers
'''
Write a program that asks the user for a positive integer n.
 Using a loop, calculate and print:
Sum of all even numbers from 1 to n
Sum of all odd numbers from 1 to n
'''

#Sum of all Even Number
no = int(input("Enter the positive Integer: "))
j = 0

for i in range(1,no):
    if i % 2 == 0:
        j += i
print(f"Sum of all even numbers from 1 to {no} : {j}")


#Sum of all Odd Number
no = int(input("Enter the positive Integer: "))
j = 0

for i in range(1,no):
    if i % 2 != 0:
        j += i
print(f"Sum of all odd numbers from 1 to {no} : {j}")

# Use Case 3 (Bug Fixing): Infinite Loop Issue
"""
Fix the code below so that it prints numbers from 1 to 10 and stops correctly.
Incorrect code:
i = 1
 while i <= 10:
 print(i)
Expected behavior:
 The program must increment i and stop when 10 is printed.
"""

i = 1
while i < 10:
    i += 1
    print(i)

# K. Collection Types
'''
Use Case 1: Product Price Lookup
Create a dictionary with at least 5 products and their prices.
Ask the user to enter a product name.
If found, print the price.
If not found, print: "Product not available." (Hint: use dictionary_var.get(key) function)
'''
product = {"Rice":100,"Wheat":200,"Oil":300,"Millets":400,"Soap":500}
user_prod = input("Enter product name: ")
print(product)

dic_value = product.get(user_prod)
dic_keys = product.keys()

print(user_prod)
print(dic_value)
print(dic_keys)

if user_prod in product.keys():
        print("Keyed in Product Price: ",product.get(user_prod))
else:
    print("Product not available")

#Use Case 2: City Entry and Duplicate Removal
"""
Ask the user to enter city names repeatedly.
Stop when the user types "exit".
Requirements:
Store every entered city name in a list (even if it's repeated).
Also store the cities in a set to maintain only unique values.

Finally print:
The complete list of entered cities (with duplicates).
The set of unique cities (duplicates removed).
"""
city_list = []

while True:
    city = input("Enter city name: ")

    if city == 'exit':
        break
    else:
        city_list.insert(0, city)

print("Entered City List :",city_list)

uniq_cities = set(city_list)
print("Unique City List:",uniq_cities)
print("Program ends")


#  Use Case 3 (Bug Fixing): List Index Error
'''
 Fix the following code so that it prints all items correctly without an index error:
Incorrect code:
items = ["Pen", "Book", "Mouse", "Keyboard"]
 i = 0
 while i <= len(items):
 print(items[i])
 i = i + 1
Expected behavior:
 The loop should print all the items exactly once and exit without an error.
'''

items = ["Pen", "Book", "Mouse", "Keyboard"]

print(len(items))
i = 0
while i < len(items):
    print(items[i])
    i += 1
print("Program ends")

# L. Exception Handling

'''
Use Case 1: Division Safe Calculator
 Ask the user for two numbers.
 Perform division and print the result.
 If the user tries to divide by 0, print:
 "Error: Division by zero is not allowed."
'''

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    res = num1/num2
    print(f"Result of 2 number divison:{res}")
except ZeroDivisionError as e:
   print("Error: Cannot divide by zero.")
except ValueError as e:
   print("Error: Invalid input. Please enter a valid number.")


#Use Case 2: Safe Integer Input
"""
Ask the user to enter a number.
Try converting it to an integer.
If conversion fails, print:Invalid input. Please enter a numeric value.
"""

try:
    num = input("Enter a number: ")
    num = int(num)
    print("Entered Number : ",num)
except ValueError as e:
    print("Error. Type conversion error. Please enter a valid number.")


# Use Case 3 (Bug Fixing): Multiple Exception Handling

'''
 Fix the below code so it handles both invalid input and division by zero correctly.
Incorrect code:
num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 result = num1 / num2
 print("Result:", result)
Expected behavior:
If user enters non-numeric values → print "Invalid input"
If num2 is zero → print "Cannot divide by zero."
Otherwise print the result.
'''

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    res = num1/num2
    print(f"Result of 2 number divison:{res}")
except ZeroDivisionError as e:
   print("Error: Cannot divide by zero.")
except ValueError as e:
   print("Error: Invalid input")
