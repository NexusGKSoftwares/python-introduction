# TOPICS FOR WEEK 4 
# ADVANCED CONCEPTS ON PYTHON PROGRAMMING

# error handling in python 
# try and except values 
# finally block

# more explanation about try and except values

# try:
#     x = 10 / 0  # Division by zero error
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
    
    
# in this example the value 10 has been divided by zero and it can't so for it we use an error called ZeroDivisionError 

# we are finaly block to clean up resources

# while using the finally block we can use the try and except block together
try:
    f = open("data.txt", "r")
    content = f.read()
finally:
    f.close()  # Ensures file is closed
    
# in this example we are using the finally block to close the file after we are done with it 
# this is a good practice to avoid memory leaks 

# FILE HANDLING 
# open() function
# read() function
# write() function

# lets open a file and read it 
# f = open("data.txt", "r")
# content = f.read()
# print(content)  # prints the content of the file
# in this example we are opening a file called data.txt in read mode and then we are reading 

# we can into with statement to open a file and read it
# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)  # prints the content of the file
    
# with statement is a context manager that automatically closes the file after we are done with it 
# it is a good practice to use the with statement when working with files 
# we can also use the readlines() function to read the file line by line 
# example of using the readlines() function
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # prints each line of the file
# in this example we are using the readlines() function to read the file line by line and
# then we are printing each line of the file
# readlines fuction works alot interpretation of the file and it is not good for big files 
# we can use the read() function to read the file and then split it into lines 


# summary of todays lesson
# we learned about the try and except block and how to use it to handle errors in python 
# we learned about finally block and how to use it to clean up resources
# we learned about file handling in python and how to open and read a file 
# we learned about the with statement and how to use it to open a file and read it 
# we learned about the readlines() function and how to use it to read a file line by line 
# we learned about the read() function and how to use it to read a file and then split it into lines



