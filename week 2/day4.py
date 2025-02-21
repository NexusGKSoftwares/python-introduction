# day 4 of week 2 of python course 
# Description:
# we will deal with the following topics:
# 1- introduction to strings manipulation
# 2- string concatenation
# 3- string slicing
# 4- string formatting
# 5- string methods
# 6- working on modules and packages

# 1- introduction to strings manipulation
#  strings are a sequence of characters, they are immutable in python
#  strings are enclosed in single, double or triple quotes
#  strings can be indexed and sliced
#  strings can be concatenated
#  strings can be formatted
#  strings can be manipulated using string methods  
#  strings can be used as keys in dictionaries
#  strings can be used as values in dictionaries
#  strings can be used as elements in lists
#  strings can be used as elements in tuples
#  strings can be used as elements in sets
#  strings can be used as elements in frozen sets
#  strings can be used as elements in arrays
#  strings can be used as elements in numpy arrays
#  strings can be used as elements in pandas dataframes
#  strings can be used as elements in pandas series
#  strings can be used as elements in numpy matrices
#  strings can be used as elements in numpy tensors
#  strings can be used as elements in numpy vectors
#  strings can be used as elements in numpy scalars


#  common string methods
#  capitalize()	Converts the first character to upper case
#  casefold()	Converts string into lower case
#  center()	Returns a centered string
#  count()	Returns the number of times a specified value occurs in a string
#  encode()	Returns an encoded version of the string
#  endswith()	Returns true if the string ends with the specified value
#  expandtabs()	Sets the tab size of the string
#  find()	Searches the string for a specified value and returns the position of where it was found
#  format()	Formats specified values in a string
#  format_map()	Formats specified values in a string
#  format_spec()	Formats specified values in a string
#  index()	Searches the string for a specified value and returns the position of where it was found

# example of each method
# capitalize()
# string = "hello, world!"
# print(string.capitalize())
# output: "Hello, world!"

# casefold()
# string = "Hello, World!"
# print(string.casefold())
# output: "hello, world!"

# center()
# string = "Hello, World!"
# print(string.center(20))
# output: "   Hello, World!   "

# count()
# string = "Hello, World!"
# print(string.count("l"))
# output: 3

# encode()
# string = "Hello, World!"
# print(string.encode())
# output: b'Hello, World!'
# print(string.encode(encoding="ascii", errors="backslashreplace"))
# output: b'Hello, World!'

# endswith()
# string = "Hello, World!"
# print(string.endswith("!"))
# output: True

# expandtabs()
# string = "Hello, World!"
# print(string.expandtabs(10))
# output: "Hello, World!"

#  Note: 
# important string methods in string manipulation
# text = "Hello , Python!"
# print(text.lower()) # output: "hello , python!" it converts the string to lowercase 
# print(text.upper()) # output: "HELLO , PYTHON!" it converts the string to uppercase
# print(text.title()) # output: "Hello , Python!" it converts the string to title case
# print(text.capitalize()) # output: "Hello , python!" it converts the first character to uppercase
# print(text.strip()) # output: "Hello , Python!" it removes the leading and trailing whitespaces
# print(text.replace("Python", "World")) # output: "Hello , World!" it replaces the first string with the second string
# print(text.split(",")) # output: ["Hello ", " Python!"] it splits the string based on the specified separator

# working with python modules and packages
# a module is a file that contains python code 
# a package is a collection of modules
# a module can be imported using the import keyword
# a module can be imported using the from keyword
#  in- built modules in python
# 1- math
# 2- random
# 3- statistics
# 4- datetime

# example of using the math module
# import math
# print(math.pi) # output: 3.14159265359

# # more examples of using the math module

# print(math.ceil(2.9)) # output: 3
# print(math.floor(2.9)) # output: 2
# print(math.sqrt(4)) # output: 2.0
# print(math.pow(2, 3)) # output: 8.0
# print(math.log(10)) # output: 2.302585092994046
# print(math.log(10, 2)) # output: 3.321928094887
# print(math.log10(100)) # output: 2.0
# print(math.log2(256)) # output: 8.0
# print(math.sin(math.pi/2)) # output: 1.0
# print(math.cos(math.pi)) # output: -1.0
# print(math.tan(math.pi/4)) # output: 0.9999999999999999
# print(math.degrees(math.pi)) # output: 180.0
# print(math.radians(180)) # output: 3.141592653589793
# print(math.factorial(5)) # output: 120
# print(math.gcd(12, 18)) # output: 6
# print(math.isfinite(math.inf)) # output: False
# print(math.isinf(math.inf)) # output: True
# print(math.isnan(math.nan)) # output: True
# print(math.isclose(0.1 + 0.2, 0.3)) # output: True
# # example of using the random module

# import random
# print(random.random()) # output: a random number between 0 and 1

# # more examples of using the random module
# print(random.randint(1, 10)) # output: a random integer between 1 and 10
# print(random.choice([1, 2, 3, 4, 5])) # output: a random element from the list
# print(random.sample([1, 2, 3, 4, 5], 3 )) # output: a random sample of 3 elements from the list
# print(random.shuffle([1, 2, 3, 4, 5])) # output: a shuffled list of elements
# print(random.uniform(1, 10)) # output: a random float between 1 and 10
# # example of using the statistics module
# import statistics
# print(statistics.mean([1, 2, 3, 4, 5])) # output: 3
# print(statistics.median([1, 2, 3, 4, 5])) # output: 3
# print(statistics.mode([1, 2, 3, 4, 5])) # output: 1
# print(statistics.stdev([1, 2, 3, 4, 5])) # output: 1.5811388300841898
# print(statistics.variance([1, 2, 3, 4, 5])) # output: 2.5

# using external modules/libraries
import requests
response = requests.get("https://www.google.com")
print(response.status_code)
