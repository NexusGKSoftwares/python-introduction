# day 3 of python classes
# Topic: Loops and Functions
# Author: @gideon
# Date: 2025-02-13
# Description: This script will demonstrate the use of loops and functions in Python.

# 1. Loops
# Loops are used to execute a block of code repeatedly for a specified number of times.
# example of loops
# for loop
# what is a for loop?
# a loop that iterates over a sequence (such as a list, tuple, dictionary, set, or string)
# and executes a block of code for each item in the sequence.
# example of for loop
# for i in range(10):
#     print(i)

# while loop
# while loop is used to execute a block of code as long as a condition is true.
# example of while loop
# i = 0
# while i < 10:
#     print(i) 
#     i += 1  # --additional assignment

# break and continue statements
# break statement: used to terminate the loop prematurely.
# continue statement: used to skip the current iteration and move on to the next one.
# example of break and continue statements
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
    # output: 0, 1, 2, 3, 4


# example of continue statement
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
    # output: 0, 1, 2, 3, 4, 6
    

# 2. Functions
# Functions are blocks of code that can be executed multiple times from different parts of the program.
# functions allows the code to be reused and makes the code more modular and easier to maintain.
# defining and calling a function
# example of defining and calling a function
# def greet(name):
#     print("Hello, " + name + "!")

# greet("Grace")
# greet("John")
# greet("Cecil")

#  in this example we have called out the function greet twice with different names
#  the function greet takes one argument which is the name of the person to be greeted.
#  the function greet prints out a greeting message with the name of the person.

# functions with return values
# functions can return values to the caller.
# example of functions with return values
# def add(x, y):
#     return x + y

# result = add(5,3)
# print(result) # output: 8  

# in this example we have defined a function add that takes two arguments x and y.
# the function add returns the sum of x and y.
# we have called the function add with arguments 5 and 3 and stored the result in the variable result.

# basic debugging and error handling
# python provides several tools for debugging and error handling.
# it uses a concept called try-except blocks to handle errors.
# example of try-except block
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")


# real life example
# online payment processing
# payments fails due to invalid card number,network issues, insufficient funds etc.
# we can use try-except block to handle these errors and provide a better user experience.
# example of try-except block in online payment processing
def process_payment(amount):
    try:
        # simulate a payment processing
        if amount <= 0:
            raise ValueError("Invalid amount. Amount should be greater then zero")
        elif amount > 10000:
            raise OverflowError("Invalid amount. Amount should be less then 10000")
        elif amount % 2 == 0: # simulate a network issue or random failures
            raise ConnectionError("Network issue. Please try again later")
        
                    
    except ValueError as ve:
        print(f"Payment Error: {ve}")
    except OverflowError as oe:
        print(f"Payment Error: {oe}")
    except ConnectionError as ce:
        print(f"Payment Error: {ce}")
    except Exception as e:
        print(f"Payment Error: {e}")
    else:
        print("Payment successful")
        
        
# process_payment(0) - simulating invalid amount
# process_payment(15000) - simulating transaction limit
# process_payment(200) - simulates network issue
# process_payment(399) - transaction successful 

#  try block runs the payment logic
#  except block handles the errors and provides a better user experience
#  else block runs when there are no errors and provides a success message

# hand on exercise
# check if a number is even or odd


