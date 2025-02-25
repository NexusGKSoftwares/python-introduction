# week 3 of python programming
# object oriented programming in python


# objective of this week: 
# learn about object oriented programming in python to write more efficient and readable code
# learn about classes and objects in python


# what is object oriented programming?

# OOP is a programming paradigm that uses objects to represent data and methods to manipulate the data
# OOP is based on the concept of classes and objects

# OOP will focus on the following 
#  encapsulation - hiding the data
#  inheritance - reusing the data
#  polymorphism - using the data in different ways
#  abstraction - simplifying the data



# TOPIC: CLASSES AND OBJECTS IN PYTHON
# what is a class in python?

# a class is a blueprint for creating objects
# a class is a template for creating objects
# a class is a user-defined data type that defines the properties and methods of an object
# a class is a collection of attributes and methods that define the behavior of an object 
# a class is a collection of objects that have the same properties and methods


# defining a class in terms of code
# example
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
    


# in this example is that we have defined a class called Car
# the class has three attributes: make, model, and year
# def has been used to define a method called __init__ which is a constructor method that initializes the attributes of the class
# the constructor method takes three parameters: make, model, and year 
# the constructor method initializes the attributes of the class using the values of the parameters
# the class has a method called display_info that displays the values of the attributes of the class


# what is an object in python?
# an object is an instance of a class
# an object is a variable that represents a class
# an object is a collection of attributes and methods that define the behavior of a class
# an object is a user-defined data type that defines the properties and methods of a class

# example 
# creating objects
car1 = Car("Toyota","Corolla", "2020")
car2 = Car("Honda", "Civic", "2024")

# calling the methods
car1.display_info() 
car2.display_info()

#  full code with a class and objects combined will be:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

car1 = Car("Toyota","Corolla", "2020")
car2 = Car("Honda", "Civic", "2024")
car1.display_info()
car2.display_info()

# output
# Make: Toyota
# Model: Corolla
# Year: 2020
# Make: Honda
# Model: Civic
# Year: 2024

# self keyword in python

# the self keyword is used to refer to the current instance of the class
# it is used to access the attributes and methods of the class
# it is used to pass the attributes and methods of the class to the constructor method


# TOPIC: ENCAPSULATION IN PYTHON
# what is encapsulation in python?
# encapsulation is the process of hiding the data of a class from the outside world
# encapsulation is the process of protecting the data of a class from being accessed by unauthorized users
# encapsulation is the process of restricting access to the attributes and methods of a class
# encapsulation is the process of making the attributes and methods of a class private

# how to implement encapsulation in python
# encapsulation can be implemented using the following methods:

# 1- private attributes
# in python, private attributes are attributes that are not accessible from outside the class
# private attributes are defined using the double underscore __ before the attribute name
# example:
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        def display_info(self):
            print(f"Make: {self.__make}")
            print(f"Model: {self.__model}")
            print(f"Year: {self.__year}")
car1 = Car("Toyota","Corolla", "2020")
car1.display_info()
            
# output
# Make: Toyota
# Model: Corolla
# Year: 2020

# note that the attributes make, model, and year have been made private by adding the double underscore __ before the attribute name
# this means that the attributes are not accessible from outside the class

# 2- setter and getter methods
# setter methods are used to set the value of an attribute
# getter methods are used to get the value of an attribute
# example:
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    def set_make(self, make):
        self.__make = make
    def get_make(self):
        return self.__make
    def display_info(self):
        print(f"Make: {self.__make}")
        print(f"Model: {self.__model}")
        print(f"Year: {self.__year}")
        car1 = Car("Toyota","Corolla", "2020")
        car1.set_make("Honda")
        print(car1.get_make())
        car1.display_info()
        
        
# output
# Honda
# Make: Honda
# Model: Corolla
# Year: 2020

# note that the setter method set_make is used to set the value of the attribute make to Honda
# the getter method get_make is used to get the value of the attribute make and return it to the caller
# the display_info method is used to display the values of the attributes make, model, and year


# another example of encapsulation

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        def set_name(self, name):
            self.__name = name
        def get_name(self):
            return self.__name
        def set_age(self, age):
            self.__age = age
        def get_age(self):
            return self.__age
        def display_info(self):
                    print(f"Name: {self.__name}")
                    print(f"Age: {self.__age}")
person1 = Person("John", 30)
person1.set_name("Jane")
person1.set_age(31)
print(person1.get_name())
print(person1.get_age())
person1.display_info()
                    

# output
# Jane
# 31
# Name: Jane
# Age: 31
# note that the setter methods set_name and set_age are used to set the values of the attributes name and age to Jane and 31 respectively
# the getter methods get_name and get_age are used to get the values of the attributes name and age and return them to the caller
# the display_info method is used to display the values of the attributes name and age
# In this example, the attributes name and age are private because they are preceded by double underscores.
# The setter and getter methods are used to set and get the values of the attributes name and age respectively.


# TOPIC: INHERITANCE IN PYTHON
# what is inheritance in python?
# inheritance is the process of creating a new class from an existing class
# inheritance is the process of reusing the attributes and methods of an existing class
# inheritance is the process of creating a new class that is a modified version of an existing class


# how to implement inheritance in python
# inheritance can be implemented using the following methods:
# 1. single inheritance: a class inherits from a single parent class
# 2. multiple inheritance: a class inherits from multiple parent classes
# 3. multilevel inheritance: a class inherits from a parent class, which in turn inherits from another parent class

# creating a parent class

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal is speaking")

# creating a child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self): # overriding the speak method of the parent class
        print("Dog is barking")
        
        
# the Dog class inherits from the Animal class using the syntax Dog(Animal)
# the Dog class has an attribute breed and a method speak that overrides the speak method of the Animal class using the same name
# the super() function is used to call the constructor method of the parent class Animal
# the super() function is used to call the constructor method of the parent class Animal with the parameter name 
# the super() function is used to call the constructor method of the parent class Animal with the parameter name and initialize the attribute name of the Dog class

