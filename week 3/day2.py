# day 2 of week 3
# oop in python 
#  we learn classes and objects in python
#  we learn about inheritance in python
#  we learn about encapsulation in python

# TOPIC: POLYMORPHISM IN PYTHON( SAME NAME BUT DIFFERENT BEHAVIOR)
# what is polymorphism in python?
# polymorphism is the ability of an object to take on many forms
# polymorphism is the ability of an object to behave in different ways depending on the context
# polymorphism is the ability of an object to use the same method name to perform different actions depending on the context 
# polymorphism is the ability of an object to use the same method name to perform different actions depending on the arguments passed to the method

# example of polymorphism in python

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " says woof"
    
# # using polymorphism 
# for pet in [Dog("Rex"), Dog("Tom")]:
#     print(pet.speak())

# in the above example, we have defined a class called Dog with a constructor method that initializes the name attribute of the class 
# the class has a method called speak that returns the name of the dog followed by the word "woof" 
# we have created a list of Dog objects with different names and called the speak method on each object
# the speak method returns the name of the dog followed by the word "woof" for objects of the Dog class
# this is an example of polymorphism in python where the same method name is used to perform different actions depending on the context

# NOTE - polymorphism is a key concept in object-oriented programming that allows objects to behave in different ways depending on the context
# polymorphism is achieved by using the same method name to perform different actions depending on the arguments passed to the method

# real world example of polymorphism in data processing
# polymorphism is used in data processing to perform different operations on data depending on the type of data being processed
# for example, a data processing system may have different methods to process text data, image data, and audio data
# each method may have the same name but perform different actions depending on the type of data being processed
# this allows the system to handle different types of data in a consistent
# and efficient manner

# full code example of polymorphism in python om data processing
# class DataProcessor:
#     def process_data(self, data):
#         raise NotImplementedError("Subclass must implement abstract method")
# class TextDataProcessor(DataProcessor):
#     def process_data(self, data):
#         print(f"Processing text data: {data}")
# class ImageDataProcessor(DataProcessor):
#     def process_data(self, data):
#         print(f"Processing image data: {data}")

# for processor in [TextDataProcessor(), ImageDataProcessor()]:
#     processor.process_data("data")

# in the above example, we have defined an abstract class called DataProcessor with an abstract method called process_data
# the process_data method raises a NotImplementedError to indicate that it is an abstract method that must be implemented by subclasses
# we have defined two concrete subclasses of DataProcessor called TextDataProcessor and ImageDataProcessor
# each subclass implements the process_data method to process text data and image data respectively
# we have created a list of DataProcessor objects with instances of TextDataProcessor and ImageDataProcessor
# we have called the process_data method on each object to process the data

# TOPIC: ABSTRACTION IN PYTHON( hiding implementation)

# what is abstraction in python?
# abstraction is the process of hiding the implementation details of a class and showing
# only the essential features of the class
# abstraction is the process of hiding the internal complexity of a class and showing
# only the external interface of the class
# abstraction is the process of hiding the internal data and methods of a class and exposing
# only the public data and methods of the class

# why is abstraction important in python?
# abstraction is important in python because it allows us to focus on the essential features of a class
# and ignore the implementation details of the class
# abstraction allows us to hide the internal complexity of a class and provide
# a simple and easy-to-use interface for interacting with the class
# abstraction allows us to separate the interface of a class from its implementation
# which makes the class more flexible and easier to maintain

# how to achieve abstraction in python?
# abstraction can be achieved in python by using abstract classes and abstract methods
# an abstract class is a class that cannot be instantiated and is used as a base class for other classes

# example of abstraction in python
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass 

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width

# circle = Circle(5)
# print(circle.area())

# rectangle = Rectangle(4, 6)
# print(rectangle.area())

#  Note: in the above example, we have defined an abstract class called Shape with an abstract method called area
# the area method is an abstract method that must be implemented by subclasses of Shape

# SUPER() FUNCTION IN PYTHON (calling Parent Methods)
# what is the super() function in python?
# the super() function is used to call a method from a parent class
# the super() function is used to call the constructor of a parent class

# example of using the super() function in python

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Make: {self.make}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")

# class Car(Vehicle):
#     def __init__(self, make, model, year, color):
#         super().__init__(make, model, year)
#         self.color = color

#     def display_info(self):
#         super().display_info()
#         print(f"Color: {self.color}")
        
# car = Car("Toyota", "Corolla", "2020", "Red")
# car.display_info()


# real world example of inheritance in python
# inheritance is used in software development to create new classes that inherit the attributes and methods of existing classes
# inheritance allows us to reuse code and create new classes that are based on existing classes
# inheritance allows us to create a hierarchy of classes with parent and child classes
# inheritance allows us to create specialized classes that have additional attributes and methods

# example of inheritance in python using school management system
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display_info(self):
        super().display_info()
        print(f"Roll Number: {self.roll_number}")

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

student = Student("John", 15, "S001")
student.display_info()

teacher = Teacher("Jane", 30, "T001")
teacher.display_info()

# in the above example, we have defined a parent class called Person with attributes name and age 
# the Person class has a method called display_info that displays the name and age of a person
# we have defined two child classes called Student and Teacher that inherit from the Person class
# the Student class has an additional attribute called roll_number and the Teacher class has an additional attribute called employee_id
# each child class has a display_info method that calls the display_info method of the parent class and displays the additional attributes