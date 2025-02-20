# day 2 of  
# today we will be dealing with tuples
# tuples are similar to lists but they are immutable, meaning they cannot be changed after they are created
# tuples are defined by enclosing a sequence of values in parentheses, instead of square brackets like lists
# tuples are often used when we need to store a collection of values that should not be changed after they are created
# tuples are also faster than lists because they are immutable, which means that the python interpreter can optimize them more easily
# tuples are also more memory efficient than lists because they do not require the overhead of dynamic memory allocation
# tuples are also more readable than lists because they are defined with parentheses, which makes it clear that they are a collection of values
# tuples are also more flexible than lists because they can be used in a variety of contexts, such as in function arguments and return values
# tuples are also more efficient than lists because they are implemented in C, which makes them faster than lists which are implemented in Python


# creating a tuple
# we can create a tuple by enclosing a sequence of values in parentheses, like this: (value
# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1)  # output: (1, 2, 3, 4,5)
# we can also create a tuple with a single value, like this: (value
# tuple2 = (10)
# print(tuple2)  # output: (10,)

# accessing the elements in tuples using indexing
# we can access the elements in a tuple using the same indexing syntax as lists, like this:
# print(tuple1[0])  # output: 1


# dictionaries in python 
# dictionaries are a type of data structure in python that stores a collection of key-value pairs
# dictionaries are also known as hash tables or associative arrays
# dictionaries are mutable, meaning they can be changed after they are created
# dictionaries are defined by enclosing a sequence of key-value pairs in curly brackets, like this: { key: value, key: value, ...}
# dictionaries are often used when we need to store a collection of key-value pairs that need to be  changed after they are created


# create a dictionary
# we can create a dictionary by enclosing a sequence of key-value pairs in curly brackets, like this
# dict1 = {"name": "John", "age": 30, "city": "Nairobi" }
# print(dict1)  # output: {'name': 'John', 'age': 30, 'city': 'Nairobi'}

# another example 
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "course": "Computer Science"
}

# # output 
# print(student)

# accessing and modifying the elements in a dictionary
#  getting a value from a dictionary using the key
# print(student["name"])  # output: John
# print(student["age"]) # output: 20
# print(student["grade"]) # output: A
# print(student["course"]) # output: Computer Science
# modifying a value in a dictionary using the key
student["age"] = 21
# print(student["age"])

# adding a new key value pair to a dictionary
student["country"] = "Kenya"
# print(student)

# deleting a key value pair from a dictionary
# we can delete a key value pair from a dictionary using the del statement, like this:
del student["grade"]
# print(student) # output: {'name': 'John', 'age': 21, 'course': 'Computer Science', 'country': 'Kenya'}



# looping through a dictionary
# we can loop through a dictionary using a for loop, like this
for key in student:
    print(key, ":", student[key])
    
    
    

#  lets try to create a school management system using dictionaries
# we will create a dictionary to store the students in the school
# we will also create a dictionary to store the teachers in the school
# we will also create a dictionary to store the subjects in the school
# we will also create a dictionary to store the classes in the school

# code
school = {
    "students": {
        "John": {"age": 20, "grade": "A", "course": "Computer Science"},
        "Jane": {"age": 21, "grade": "B", "course": "Math"},
        "Bob": {"age": 22, "grade": "C", "course": " Science"},
        },
    "teachers": {
        "Mr. Smith": {"subject": "Math", "experience": 10},
        "Ms. Johnson": {"subject": "Science", "experience": 5},
        "Mr. Brown": {"subject": "Computer Science", "experience": 8},
        },
    "subjects": {
        "Math": {"description": "Mathematics is a subject that deals with numbers and their operations" },
        "Science": {"description": "Science is a subject that deals with the natural world and the laws that govern it"},
        "Computer Science": {"description": "Computer Science is a subject that deals with the design, development, and testing of computer systems"},
        },
    "classes": {
        "Class 1": {"students": ["John", "Jane"], "teacher": "Mr . Smith"},
        "Class 2": {"students": ["Bob"], "teacher": "Ms. Johnson"},
        },
    }
# print(school["students"]["John"]["age"])
# print(school["teachers"]["Mr. Smith"]["subject"])
# print(school["subjects"]["Math"]["description"])

#  lets try to loop through the school management system using a for loop to display all key value pairs in the school dictionary
#  displaying all values without curly brackets
# for key, value in school.items():
#     print(key, ":", value)
#  lets try to loop through the school management system using a for loop to display all key value pairs in the school dictionary
#  displaying all values with curly brackets
for key, value in school.items():
    print(key, ":", {key: value})
    
    
    
    
# lets see the difference in a table between lists, tuples, dictionaries 
# lets create a table to compare lists, tuples, dictionaries
#  =========================================================================================
# | Data Type | Description | Indexing | Slicing | Mutable | Example | 
# =========================================================================================
# | List      | Ordered collection of items | Yes | Yes | Yes | [1, 2, 3] |
# | Tuple     | Ordered collection of items | Yes | Yes | No  | (1, 2, 3) |
# | Dictionary| Unordered collection of key-value pairs | No | No | Yes | {"a ": 1} | 
# =========================================================================================


# summarise the key differences between lists, tuples, and dictionaries
# lists are ordered collections of items, tuples are ordered collections of items, dictionaries are unordered collections of
# key-value pairs. Lists and tuples are indexed and can be sliced, dictionaries are not indexed and cannot be sliced. Lists and
# tuples are mutable, dictionaries are mutable. Lists and tuples are defined using square brackets and parentheses respectively ,
# dictionaries are defined using curly brackets. Lists and tuples can contain any data type, dictionaries can only contain key-
# value pairs. Lists and tuples can be nested, dictionaries cannot be nested. Lists and tuples can be used as keys in a 
# dictionary, dictionaries cannot be used as keys in a dictionary. Lists and tuples can be used as values in a dictionary ,
# dictionaries can be used as values in a dictionary. Lists and tuples can be used as elements in a set, dictionaries cannot be 


# lets create a very large  table to compare lists, tuples, dictionaries
#  =================================================================================================================
#  | Data Type | Description | Indexing | Slicing | Mutable | Example | Length | Type of Elements | Nested | Keys as Values | Values as Keys | Keys as Elements | Values as Elements |
#  =================================================================================================================
#  | List      | Ordered collection of items | Yes | Yes | Yes | [1, 2, 3] | 3 | Any | Yes | Yes | Yes | No | Yes | 
#  | Tuple     | Ordered collection of items | Yes | Yes | No  | (1 , 2, 3) | 3 | Any | Yes | Yes | Yes | No | Yes |
#  | Dictionary| Unordered collection of key-value pairs | No | No | Yes | {" a ": 1} | - | Key-Value Pair | No | No | Yes | Yes | No | 
#  =================================================================================================================

