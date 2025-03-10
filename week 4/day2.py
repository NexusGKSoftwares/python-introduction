# Topics
# Regular expressions
#  decorators (modifying the function)
# generators (efficient way of creating sequences)


# REGULAR EXPRESSIONS
# A regular expression is a pattern used to match character combinations in strings.
# It is a sequence of characters that forms a search pattern. 
# it uses re module in python.
import re

from django.shortcuts import redirect
# search() function returns a match object if it finds the pattern in the string.
# If it does not find the pattern, it returns None.
def find_pattern(string, pattern):
    if re.search(pattern, string):
        return "Pattern found"
    else:
        return "Pattern not found"

# re.search() function returns a match object if it finds the pattern in the string.
# If it does not find the pattern, it returns None.
# re.search() function scans through the string looking for the first location where the regular expression pattern produces
# a match, and returns a corresponding match object. If no position in the string matches the pattern
# it returns None.

# print (find_pattern("Hello, world!", "world"))  # Output: Pattern found
# print (find_pattern("Hello, world!", "python"))  # Output: Pattern not found

# Finding all matches in a string
# re.findall() function returns all non-overlapping matches of pattern in string, as a list of
# strings. The string is scanned left-to-right, and matches are returned in the order found.
def find_all_matches(string, pattern):
    return re.findall(pattern, string)
# print (find_all_matches("Hello, world! world!", "world"))  # Output: 

# replacing a pattern in a string
# re.sub() function replaces the leftmost non-overlapping occurrences of pattern in string by the
# replacement repl, which is an alphanumeric string.
def replace_pattern(string, pattern, repl):
    return re.sub(pattern, repl, string)
# print (replace_pattern("Hello, world!", "world", "python"))  # Output: Hello, python!


# real -world example
# validating email addresses
# import re
# def validate_email(email):
#     pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0 -9-]+\.[a-zA-Z0-9-.]+$"
#     if re.match(pattern, email):
#         return True
#     else:
#         return False
# # taking email input from user
# email = input("Enter your email: ")
# # validating email
# if validate_email(email):
#     print("Valid email")
# else:
#     print("invalid email")
    
# in this example, we are using the ^ symbol to match the start of the string, and the $ symbol to match the end of the string.
# The [a-zA-Z0-9_.+-]+ matches one or more alphanumeric characters, dots , underscores, plus signs, or hyphens.
# The @ symbol matches the @ symbol literally.

# validating phone numbers
# import re
# def validate_phone_number(phone_number):
#     pattern = r"^\d{3}-\d{3}-\d{4}$"
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False

# # taking phone number input from user
# phone_number = input("Enter your phone number: ")
# validating phone number
# if validate_phone_number(phone_number):
#     print("Valid phone number")
# else:
#     print("invalid phone number")
    
# in this example , we are using the ^ symbol to match the start of the string, and the $ symbol to match the end of the string.
# The \d{3} matches exactly 3 digits, and the - matches the - symbol literally.
# The \d{4} matches exactly 4 digits. 

# Decorators 
# A decorator is a small function that takes another function as an argument and extends the behavior of the latter function without permanently modifying it.
# decorators are used to add a new functionality to an existing object without modifying it.

# creating a decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#     # using the decorator

# @my_decorator
# def say_hello():
#     print("Hello!")
#     # calling the function
# say_hello()
    # in this example, we are creating a decorator called my_decorator that takes a function as an argument
    # the decorator returns a new function called wrapper that calls the original function and adds some extra functionality 
    # using the decorator with the @ symbol before the function definition.
    
# using a decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator
    # using the decorator
@repeat(3)
def say_hello():
    print("Hello!")
    # calling the function
say_hello()

# in this example, we are creating a decorator called repeat that takes an argument times 
# the decorator returns a new function called wrapper that calls the original function a specified number of times
# using the decorator with the @ symbol before the function definition.

# real world example of decorators
# in the real world, decorators are used to add a new functionality to an existing object without modifying
# it. for example, in the django framework, the @login_required decorator is used to check
# if a user is logged in before allowing them to access a certain view.
# in this example, we are using the @login_required decorator to check if a user is logged
# in before allowing them to access a certain view.

# code snippet of school management system using decorators
from functools import wraps  # importing the wraps function from the functools module 
from datetime import datetime
from datetime import timedelta
# defining a decorator to check if a user is logged in
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # checking if the user is logged in
        if not is_logged_in():
            # if the user is not logged in, redirect them to the login page
            return redirect('login')
        # if the user is logged in, call the original function
        return func(*args, **kwargs)
    return wrapper
# defining a decorator to check if a user is logged in
def is_logged_in():
    # checking if the user is logged in
    # if the user is logged in, return True
    # if the user is not logged in, return False
    return True

# in this example, we are using the @login_required decorator to check if a user is logged in 
# before allowing them to access a certain view. the @login_required decorator checks if the user is
# logged in by calling the is_logged_in function. if the user is not logged in, the decorator redirects to login page
# the is_logged_in function checks if the user is logged in by checking the user's session.
# if the user is logged in, the function returns True, otherwise it returns False.


# Generators (efficient way to create iterators)
# generators are a type of iterable, like lists or tuples. however, unlike lists and tuples, generators do not
# store all the values in memory at once. instead, they generate the values on the fly, one at a time.
# generators are useful when you need to create a large number of objects, but you don't want to store them all in memory at once.

# creating a generator
# def infinite_sequence():
#     n = 0
#     while True:
#         yield n
#         n += 1
#         # using the generator
# for i in infinite_sequence():
#     print(i)
# in this example, we are creating a generator that produces an infinite sequence of numbers.
# the generator uses a while loop to keep generating numbers until it is stopped.
# the yield keyword is used to produce a value from the generator.
# the for loop is used to iterate over the generator and print the numbers.
# Generators are useful when you need to create a large number of objects, but you don't want to store them all in memory at once.

def countdown(n):
    # creating a generator that counts down from n to 0
    while n >= 0:
        yield n
        n -= 1
# using the generator
for i in countdown(10):
    print(i)

# in this example, we are creating a generator that counts down from n to 0.
# the generator uses a while loop to keep counting down until it reaches 0.
# the yield keyword is used to produce a value from the generator.
# the for loop is used to iterate over the generator and print the numbers.


