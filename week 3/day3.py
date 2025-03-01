# TOPICS: 
#  -CLASS AND STATIC METHODS
#  -MAGIC METHODS


# CLASS AND STATIC METHODS
# class methods are methods that are bound to the class and not the instance of the class
# class methods are defined using the @classmethod decorator
# class methods take the class as the first argument
# class methods can be called using the class name or the instance of the class
# class methods are used to create factory methods that return an instance of the class 

# AN EXAMPLE OF A CLASS METHOD
# class Company:
#     employess = 0
    
#     @classmethod 
#     def add_employee(cls):
#         cls.employess += 1
    
# Company.add_employee()
# print(Company.employess)

# in this example we have defined a class method called add_employee that increments the employess class variable by 1
# we have called the class method using the class name Company.add_employee()
# we have printed the employess class variable using the class name Company.employess 

# STATIC METHODS(@staticmethod)
# used when a method does not depend on the class state 

# example of using static method
# class Math:
#     @staticmethod
#     def add(x, y):
#         return x + y
    
# print(Math.add(5, 10))

# in this example we have defined a static method called add that takes two arguments x and y and returns the sum of x and y
# we have called the static method using the class name Math.add(5, 10)
# we have printed the result of the static method call using the print function

# Magic Methods
# magic methods are special methods that are defined by two underscores before and after the method name
# magic methods are also called dunder methods
# magic methods are used to perform special operations in python

# example of using magic methods
#  --   __str__ (string representation)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
person = Person("John", 30)
print(person)  # Output: Name: John, Age: 30

# in this example we have defined a magic method called __str__ that returns a string representation of the object
# the __str__ method is called when we use the print function to print the object
# we have created an instance of the Person class called person with the name John and age 30 
# we have printed the person object using the print function

# example of using magic methods
# --  __len__ (length)
class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def __len__(self):
        return len(self.numbers)
    
numbers = Numbers([1, 2, 3, 4, 5])
print(len(numbers))  # Output: 5
# in this example we have defined a magic method called __len__ that returns the length of the numbers list
# the __len__ method is called when we use the len function to get the length of the object
# we have created an instance of the Numbers class called numbers with a list of numbers [1, 2, 3, 4, 5]
# we have printed the length of the numbers object using the len function

# HAND ON EXERCISE 
# create a student management system using classes and inheritance
# create a parent class called Person with attributes name and age and a method called display_info that displays the name and age of a person
# create a child class called Student that inherits from the Person class with an additional attribute called roll_number and a method called display_info that displays the name, age, and roll number of a student
# create a child class called Teacher that inherits from the Person class with an additional attribute called employee_id and a method called display_info that displays the name, age, and employee id of a teacher
# create instances of the Student and Teacher classes and call the display_info method to display the information of the student and teacher
# use class and static methods to create a factory method that returns an instance of the Person class



