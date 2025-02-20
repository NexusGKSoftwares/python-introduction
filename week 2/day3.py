# welcome to todays class
# we will be learning about functions in python which is the continuation of our discussion on functions
# we had already discussed about functions in python in our previous class
# we will be discussing more about functions in python today
# we will be discussing about the following topics
# 1. functions in python
# 2. function arguments
# 3. function return values
# 4. function scope

# functions in python
# functions are a type of code block that can be called by name to perform a specific task
# functions are used to organize code into logical blocks that can be reused throughout a program
# functions are defined using the def keyword followed by the function name and a set of parentheses
# functions can take arguments and return values
# functions can also have default arguments and keyword arguments
# functions can be defined inside other functions
# functions can be passed as arguments to other functions
# functions can be assigned to variables 
# functions can be defined using lambda expressions  

# defining a function in python
# we can define a function in python using the def keyword followed by the function name and a set of parentheses
# we can also define a function with a set of parameters, like this: 
# def greet(name):
#     print(f"Hello, {name}!")
    #  this is a function that takes a single argument, name, and prints a greeting message to the console 
    #  the function is defined using the def keyword followed by the function name, greet, and a set of parentheses containing the parameter name 
    
# calling a function in python
# we can call a function in python by using the function name followed by a set of parentheses
# we can also pass arguments to the function inside the parentheses, like this:
# greet("John")
# output: Hello, John!
# this is an example of calling the greet function with the argument "John"
# the function prints the message "Hello, John!" to the console 

# returning a value from a function in python
# we can return a value from a function in python using the return keyword
# the return keyword is followed by the value that we want to return from the function
# we can then assign the return value to a variable or use it in an expression, like this:
# def add(a, b):
#     return a + b
# this is a function that takes two arguments, a and b, and returns the sum of the two numbers
# the return keyword is used to return the sum of the two numbers
# we can then assign the return value to a variable or use it in an expression, like this:
# result = add(3, 5)
# print(result)  # output: 8 
# this is an example of calling the add function with the arguments 3 and 5 
# the function returns the sum of the two numbers, which is then assigned to the variable result 
# the value of the variable result is printed to the console, which outputs 8  

# default arguments in python functions
# we can specify default values for function arguments in python
# default values are used when the function is called without passing a value for the argument
# we can specify default values for function arguments by using the assignment operator (=) in the function definition
# def greet(name="World"):
#     print(f"Hello, {name}!")
# this is a function that takes a single argument, name, and prints a greeting message to the console
# the function has a default value of "World" for the name argument
# if the function is called without passing a value for the name argument, the default value "World" is used 
# other arguments can also have default values, like this:
# add can be the function name which displays the sum of two numbers - and this is the default function

# default parameters in python functions
#  we can call out some functions with default parameters such as add, subtract, multiply, divide etc
# lets have a look at the example below
# def add(a, b=0):
#     return a + b
# result = add(3)
# print(result)  # output: 3
# this is an example of calling the add function with a single argument, 3
# the function has a default value of 0 for the b argument
# since the b argument is not passed when calling the function, the default value of 0 is used

# #  more examples of default parameters in python functions
# def subtract(a, b=0):
#     return a - b
# result = subtract(3)
# print(result)  # output: 3
 
# def multiply(a, b=1):
#     return a * b
# result = multiply(3)
# print(result)  # output: 3

# def divide(a, b=1):
#     return a / b
# result = divide(3)
# print(result)  # output: 3

# def power(a, b=2):
#     return a ** b
# result = power(3)
# print(result)  # output: 9

# using the keyword arguments in python functions
# we can pass arguments to a function using keyword arguments in python
# keyword arguments are arguments that are passed to a function using the argument name
# we can specify the argument name followed by the value we want to pass to the function
# def greet(name, message):
#     print(f"Hello, {name}! {message}")
# greet(name="John", message="Good morning!")
# this is an example of calling the greet function with keyword arguments
# the function takes two arguments, name and message
# the arguments are passed using the argument names, name and message
# the function prints the message "Hello, John! Good morning!" to the console

#  more examples of using keyword arguments in python functions
# def add(a, b):
#     return a + b
# result = add(a=3, b=5)
# print(result)  # output: 8

# def subtract(a, b):
#     return a - b
# result = subtract(a=3, b=1)
# print(result)  # output: 2
# in this example, the add and subtract functions take two arguments, a and b
# the arguments are passed using the argument names, a and b
# the functions return the sum and difference of the two numbers, which are then assigned to the variable result
# the value of the variable result is printed to the console


# file handling in python - reading and writing files
# file handling is an important part of programming in python
# file handling allows us to read and write data to and from files
# python provides built-in functions for file handling, such as open(), read(), write(), and close()
# we can open a file using the open() function, read data from the file using the read() function, write data to the file using the write() function, and close the file using the close() function
# we can also use the with statement to open a file, read or write data to the file, and automatically close the file when we are done 

# writing to a file in python
# we can write data to a file in python using the write() function
# the write() function is used to write data to a file

#  example of writing to a file in python
# with open("data.txt", "w") as file:
#     file.write("Hello, World!")
#     file.write("\n")
#     file.write("This is a test file.")  
#     file.write("\n")
#     file.write("Goodbye, World!")
# this is an example of writing data to a file in python
# we open a file named data.txt in write mode using the open() function
# we write three lines of text to the file using the write() function
# we use the newline character "\n" to write each line of text on a new line

# opening a file in python
# we can open a file in python using the open() function
# the open() function takes two arguments: the file name and the mode
# the mode specifies how the file should be opened, such as read mode, write mode, or append mode
# with open("data.txt", "r") as file:
#     data = file.read()
#     print(data)
    
# this is an example of opening a file in python
# we open a file named data.txt in read mode using the open() function
# we read the contents of the file using the read() function
# we assign the contents of the file to the variable data
# we print the contents of the file

#  lets try to create a simple dataset and write it to a file 
# with open("dataset.csv", "w") as file:
#     file.write("Name, Age, Grade\n")
#     file.write("John, 20, A\n")
#     file.write("Jane, 22, B\n")
#     file.write("Bob, 21, C\n")
# this is an example of writing a simple dataset to a file in python
# we open a file named data.txt in write mode using the open() function
# we write a header row to the file containing the column names
# we write three rows of data to the file, each row containing the name, age, and grade of a student
# we use the newline character "\n" to write each row of
# data on a new line


# a very good example of school management system to create a dataset and write it to a file

# with open("school_management_system.csv", "w") as file:
#     file.write("Student ID, Name, Age, Grade\n")
#     file.write("1, John, 20, A\n")
#     file.write("2, Jane, 22, B\n")
#     file.write("3, Bob, 21, C\n")
#     file.write("4, Alice, 23, A\n")
#     file.write("5, Mary, 24, B\n")
#     file.write("6, Peter, 25, C\n")
#     file.write("7, David, 26, A\n")
#     file.write("8, Sarah, 27, B\n")
#     file.write("9, James, 28, C\n")
#     file.write("10, Emily, 29, A\n")
#     file.write("11, Michael, 30, B\n")
#     file.write("12, Grace, 31, C\n")
#     file.write("13, Joseph, 32, A\n")
#     file.write("14, Elizabeth, 33, B\n")
#     file.write("15, Samuel, 34, C\n")

# appending to a file in python 
# we can append data to a file in python using the append mode
# the append mode is used to add data to the end of a file without overwriting the existing data
# we can open a file in append mode using the "a" mode
# with open("data.txt", "a") as file:
#     file.write("\n") 
#     file.write("This is a new line of text.")
#     file.write("\n")
#     file.write("This is another new line of text.")
# this is an example of appending data to a file in python
# we open a file named data.txt in append mode using the open() function
# we write two lines of text to the file using the write() function
# we use the newline character "\n" to write each line of text on a new line