# Day 2 of Python Course
# Author: Gideon
# Date: 2025-02-11
# Time: 1930hrs
# Purpose: To learn about operators & conditional statements in Python
# This script will cover the basics of operators and conditional statements in Python
# It will also cover the use of if-else statements and the elif statement

# introduction
# print("Introduction to Operators and Conditional Statements in Python")

# Operators
# Operators are used to perform operations on variables and values.
# example of operators in Python
#  arithmetic operators
# + (addition)
# - (subtraction)
# * (multiplication)
# / (division)
# % (modulus)
# ** (exponentiation)
#  comparison operators
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
#  logical operators
# and (logical and)
# or (logical or)
# not (logical not)
#  assignment operators
# = (assignment)
# += (addition assignment)
# -= (subtraction assignment)
# *= (multiplication assignment)
# /= (division assignment)

#  example of arithmetic operators in Python
# print(5 + 3)  # output: 8 - addition
# print(7-1) # output: 6 - subtraction
# print(4*2) # output: 8 - multiplication
# print(10/2) # output: 5.0 - division
# print(10%3) # output: 1 - modulus

# what do i mean by modulus?
# returns the remainder of the division of the number before it by the number after it

# remainder = a % b 
# where a is the dividend and b is the divisor
# example: 17 % 5 = 2 because 17 divided by 5 leaves a remainder of 2

# real life situation of applying modulus
# time and clock calculation
# when scheduling events or setting up reminders
#  example
# hours = (15 + 10) % 12
# print(hours) # output: 1

# in the above example , we are adding 15 and 10 hours together
# and then we are taking the modulus of the result with 12 to get the hours in
# 12 hour format

#  example of comparison operators in Python
# print(5 == 5) # output: True - equal to
# print(5 != 10) # output: False - not equal to
# print(7 > 2) # output: True - greater than
# print(7 < 2) # output: False - less than
# print(7 >= 7) # output: True - greater than or equal to
# print(9 <= 8) output: False - less than or equal to

# example of logical operators in Python
# print(5 > 2 and 5 < 10) # output: True - logical and
# print(5 > 2 or 5 < 10) # output: True - logical or
# print(not 5 > 2) # output: False - logical not

# example of assignment operators
# a = 10 # output: 10 - assignment
# print(a)
# a += 3 # output: 13 - addition assignment
# print(a) # output: 13
# a -= 2 # output: 8 - subtraction assignment
# print(a) # output: 8
# a *= 2 # output: 20 - multiplication assignment
# print(a) # output: 20
# a /= 2 # output: 5.0  - division assignment
# print(a) # output: 5.0

# Control flow -- conditional statements
# if-else statement
# if condition is true then execute the code inside the if block
# else block is executed if the condition is false

# example
# x = 10
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")
    
# real world example of if-else statement
# checking if a user is eligible to vote or not
# if user's age is greater than 18 then user is eligible to vote else not
# age = 10
# if age > 18:
#     print("User is eligible to vote")
# else:
#     print("User is not eligible to vote")

# if executes when the condition is true
# else executes when the condition is false

# if --- elif --- else statement
# if condition1 is true then execute the code inside the if block
# elif condition2 is true then execute the code inside the elif block
# else block is executed if all conditions are false

# example
# age = 10
# if age > 18:
#     print("the user is adult")
# elif age > 13:
#     print("the user is almost adult")
# else:
#     print("user is minor")
    
# example of school grading system
# if student's percentage is greater than 80 then student is in A grade
# elif student's percentage is greater than 60 then student is in B grade

mark = 50
if mark > 80:
    print("A grade")
elif mark > 60:
    print("B grade")
elif mark > 40:
    print("C grade")
else:
    print("D grade")

# summary of today's lesson
# operators
# comparison operators
# logical operators
# assignment operators
# if-else statement
# if-elif-else statement