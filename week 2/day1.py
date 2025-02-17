# week 2 of our 4-week course on the basics of python programming
# author: Gideon
# date: 2025-02-17
# version: 1.0
# description: This script will demonstrate the use of lists in python programming.

# we will be dealing with lists functions & file handling

# objective : to learn how to create, access, and manipulate lists in python

# 1 Lists, tuples and dictionaries

# lists
# lists are ordered collections of items that can be of any data type, including strings, integers,floats,
# lists are mutable , meaning they can be changed after creation
# lists are denoted by square brackets[]
# lists can be created using the list() function  

# lets try to create a list
# my_list = [1, 2, 3, 4, 5] # this is a list of integers
# print(my_list)  # output: [1, 2, 3, 4,

# fruits = ['apple', 'banana', 'cherry'] # this is a list of strings
# print(fruits)  # output: ['apple', 'banana', 'cherry']

# multiple data types in a list
# mixed = [1, 'apple', 3.5, True, None]
# print(mixed)

# lists operations
# accessing elements in a list
# we can access elements in a list using their index
# the index is the position of the element in the list
# the index starts at 0, so the first element is at index 0, the second element is at index 1, and so on
# lets try to access elements in a list
# my_list = [1, 2, 3, 4, 5]
# print(my_list[3])  # output: 1
    
# fruits = ['apple', 'banana', 'cherry']
# print(fruits[1])  # output: banana

# adding an item in a list
# we can add an item in a list using the append() method
# lets try to add an item in a list
# my_list = [1, 2, 3, 4, 5]
# my_list.append(6)
# print(my_list)  # output: [1, 2, 3, 4,5, 6]

#  using an example of a list of fruits
# fruits = ['apple', 'banana', 'cherry']
# fruits.append('orange')
# print(fruits)  # output: ['apple', 'banana', 'cherry', 'orange']

# how to insert an item at a specific position in a list
# we can insert an item at a specific position in a list using the insert() method
# lets try to insert an item at a specific position in a list
# my_list = [1, 2, 3, 4, 5]
# my_list.insert(2, 6)
# print(my_list)  # output: [1, 2, 6, 3, 4, 5]

# using an example of a list of fruits
# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(-2, 'orange')
# print(fruits)  # output: ['apple', 'orange', 'banana', 'cherry']

# removing an item in a list
# we can remove an item in a list using the remove() method
# lets try to remove an item in a list
# my_list = [1, 2, 3, 4, 5]
# my_list.remove(3)
# print(my_list)  # output: [1, 2, 4, 5]

# # lets try to use fruits
# fruits = ['apple', 'banana', 'cherry']
# fruits.remove('banana')
# print(fruits)  # output: ['apple', 'cherry']

# lets remove the last item in a list
# we use a function called pop() to remove the last item in a list
# # lets try to remove the last item in a list
# my_list = [1, 2, 3, 4, 5]
# my_list.pop()
# print(my_list)  # output: [1, 2, 3, 4]

# finding the length of a list
# we can find the length of a list using the len() function
# lets try to find the length of a list
# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))  # output: 5

# # lets try to use fruits
# fruits = ['apple', 'banana', 'cherry']
# print(len(fruits))  # output: 3



# looping through a list
# we can loop through a list using a for loop
# lets try to loop through a list
# my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#     print(item)  # output: 1, 2, 3, 4,5

#  lets try to use fruits
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)  # output: apple, banana, cherry
    
    
    
# lets try to use multiple lists of shopping list
# lets say we have multiple lists of shopping list
# my_list1 = ['apple', 'banana', 'cherry']
# my_list2 = ['milk', 'eggs', 'cheese']
# my_list3 = ['chicken', 'beef', 'fish']
# # lets try to loop through all the lists
# for list in [my_list1, my_list2, my_list3]:
#     for item in list:
#         print(item)  # output: apple, banana, cherry, milk, eggs, cheese,
        
        
        
# using a school managemnt system of list of students in different classes
# lets say we have a list of students in different classes

class_1 = ['John', 'Mary', 'David']
class_2 = ['Jane', 'Peter', 'Linda']
class_3 = ['Tom', 'Lucy', 'Hannah']
# lets try to loop through all the classes and print the students in each class

for class_group in [class_1, class_2, class_3]:
    for student in class_group:
        print(student)  # output: John, Mary, David, Jane, Peter, Linda,
        
        
# summarize the class of today
# lets summarize the class of today
# we have learned about lists and how to use them in python
# we have learned how to create a list, access a list, modify a list, and loop through a list
# we have also learned how to use multiple lists and loop through them
# we have also learned how to use a school management system of list of students in different classes


# END OF CLASS