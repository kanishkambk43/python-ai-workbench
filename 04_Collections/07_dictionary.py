"""
===========================================
Python Dictionaries
===========================================

A dictionary stores data in KEY-VALUE pairs.

Syntax:
    dictionary = {
        "key": "value",
        "key": "value"
    }

Keys must be unique and hashable.
Values can be of any data type.

Dictionaries are mutable.
"""


# ===========================================
# 1. Creating a Dictionary
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student)                          # {'name': 'Kanishka', 'age': 22, 'course': 'Python'}


# ===========================================
# 2. Empty Dictionary
# ===========================================

empty_dict = {}

print(empty_dict)                       # {}


# ===========================================
# 3. Dictionary Type
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

print(type(student))                    # <class 'dict'>


# ===========================================
# 4. Accessing Values
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student["name"])                  # Kanishka
print(student["age"])                   # 22
print(student["course"])                # Python


# ===========================================
# 5. Accessing a Missing Key
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

# print(student["email"])
# KeyError: 'email'


# ===========================================
# 6. get() for Safe Access
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

print(student.get("name"))              # Kanishka
print(student.get("email"))             # None
print(student.get("email", "Not Found")) # Not Found


# ===========================================
# 7. Dictionary Keys Must Be Unique
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "age": 23
}

print(student)                          # {'name': 'Kanishka', 'age': 23}

# If a key is repeated, the last value is kept.


# ===========================================
# 8. Dictionary with Different Value Types
# ===========================================

data = {
    "name": "Kanishka",
    "age": 22,
    "height": 5.8,
    "is_student": True,
    "skills": ["Python", "SQL"],
    "address": {"city": "Bangalore"}
}

print(data)
# {'name': 'Kanishka', 'age': 22, 'height': 5.8,
#  'is_student': True, 'skills': ['Python', 'SQL'],
#  'address': {'city': 'Bangalore'}}


# ===========================================
# 9. Dictionary with Integer Keys
# ===========================================

numbers = {
    1: "One",
    2: "Two",
    3: "Three"
}

print(numbers[1])                       # One
print(numbers[3])                       # Three


# ===========================================
# 10. Dictionary Keys Can Be Different Types
# ===========================================

data = {
    "name": "Kanishka",
    1: "Python",
    2.5: "Float"
}

print(data["name"])                     # Kanishka
print(data[1])                          # Python
print(data[2.5])                        # Float


# ===========================================
# 11. Dictionary Keys Must Be Hashable
# ===========================================

valid_dict = {
    "name": "Kanishka",
    (1, 2): "Tuple Key"
}

print(valid_dict[(1, 2)])               # Tuple Key

# Lists cannot be dictionary keys because
# lists are mutable and unhashable.

# invalid_dict = {
#     [1, 2]: "List Key"
# }

# TypeError: unhashable type: 'list'


# ===========================================
# 12. Checking if a Key Exists
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

print("name" in student)                # True
print("email" in student)               # False


# ===========================================
# 13. Checking if a Key Does Not Exist
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

print("email" not in student)            # True
print("name" not in student)             # False


# ===========================================
# 14. Adding a New Key-Value Pair
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

student["course"] = "Python"

print(student)                          # {'name': 'Kanishka', 'age': 22, 'course': 'Python'}


# ===========================================
# 15. Updating an Existing Value
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

student["age"] = 23

print(student)                          # {'name': 'Kanishka', 'age': 23}


# ===========================================
# 16. Dictionary Is Mutable
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

student["name"] = "Rahul"

print(student)                          # {'name': 'Rahul', 'age': 22}


# ===========================================
# 17. Dictionary Length
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(len(student))                     # 3


# ===========================================
# 18. Dictionary Iteration - Keys
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

for key in student:
    print(key)

# name
# age
# course


# ===========================================
# 19. Dictionary Iteration - Values
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

for key in student:
    print(student[key])

# Kanishka
# 22
# Python


# ===========================================
# 20. Dictionary Keys
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student.keys())                   # dict_keys(['name', 'age', 'course'])


# ===========================================
# 21. Dictionary Values
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student.values())                 # dict_values(['Kanishka', 22, 'Python'])


# ===========================================
# 22. Dictionary Items
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student.items())
# dict_items([('name', 'Kanishka'), ('age', 22), ('course', 'Python')])


# ===========================================
# 23. Iterating Through Keys and Values
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)

# name : Kanishka
# age : 22
# course : Python


# ===========================================
# 24. Nested Dictionary
# ===========================================

students = {
    "student1": {
        "name": "Kanishka",
        "age": 22
    },
    "student2": {
        "name": "Rahul",
        "age": 23
    }
}

print(students["student1"]["name"])      # Kanishka
print(students["student2"]["age"])       # 23


# ===========================================
# 25. Dictionary Containing a List
# ===========================================

student = {
    "name": "Kanishka",
    "skills": ["Python", "SQL", "Git"]
}

print(student["skills"])                # ['Python', 'SQL', 'Git']
print(student["skills"][0])             # Python
print(student["skills"][1])             # SQL


# ===========================================
# 26. Dictionary Containing a Tuple
# ===========================================

student = {
    "name": "Kanishka",
    "marks": (85, 90, 95)
}

print(student["marks"])                 # (85, 90, 95)
print(student["marks"][0])              # 85


# ===========================================
# 27. Dictionary Containing a Set
# ===========================================

student = {
    "name": "Kanishka",
    "skills": {"Python", "SQL", "Git"}
}

print(student["skills"])                # {'Python', 'SQL', 'Git'}
# Set order may vary.


# ===========================================
# 28. Removing a Key Using del
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

del student["age"]

print(student)                          # {'name': 'Kanishka', 'course': 'Python'}


# ===========================================
# 29. Dictionary Assignment Creates a Reference
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

another_student = student

another_student["age"] = 23

print(student)                          # {'name': 'Kanishka', 'age': 23}
print(another_student)                  # {'name': 'Kanishka', 'age': 23}

# Both variables refer to the same dictionary.


# ===========================================
# 30. Creating an Independent Copy
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

another_student = student.copy()

another_student["age"] = 23

print(student)                          # {'name': 'Kanishka', 'age': 22}
print(another_student)                  # {'name': 'Kanishka', 'age': 23}


# ===========================================
# 31. Dictionary from a List of Tuples
# ===========================================

data = [
    ("name", "Kanishka"),
    ("age", 22),
    ("course", "Python")
]

student = dict(data)

print(student)                          # {'name': 'Kanishka', 'age': 22, 'course': 'Python'}


# ===========================================
# 32. Dictionary from Two Lists
# ===========================================

keys = ["name", "age", "course"]
values = ["Kanishka", 22, "Python"]

student = dict(zip(keys, values))

print(student)                          # {'name': 'Kanishka', 'age': 22, 'course': 'Python'}


# ===========================================
# 33. Dictionary Comprehension Preview
# ===========================================

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)                          # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehensions will be covered
# in more detail in advanced Python.


# ===========================================
# 34. Practical Example - Student
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Computer Science",
    "marks": 92
}

print("Name:", student["name"])         # Name: Kanishka
print("Age:", student["age"])           # Age: 22
print("Course:", student["course"])     # Course: Computer Science
print("Marks:", student["marks"])       # Marks: 92


# ===========================================
# 35. Practical Example - Product
# ===========================================

product = {
    "name": "Laptop",
    "price": 75000,
    "brand": "Dell",
    "in_stock": True
}

print(product["name"])                  # Laptop
print(product["price"])                 # 75000
print(product["in_stock"])              # True


# ===========================================
# Summary
# ===========================================

"""
Dictionary Concepts Covered
----------------------------
✔ Dictionary creation
✔ Empty dictionaries
✔ Key-value pairs
✔ Accessing values
✔ get()
✔ Unique keys
✔ Different value types
✔ Different key types
✔ Hashable keys
✔ Checking keys
✔ Adding values
✔ Updating values
✔ Mutability
✔ len()
✔ Dictionary iteration
✔ keys()
✔ values()
✔ items()
✔ Nested dictionaries
✔ Lists inside dictionaries
✔ Tuples inside dictionaries
✔ Sets inside dictionaries
✔ del
✔ References
✔ copy()
✔ dict()
✔ zip()
✔ Dictionary comprehension preview

Important Points
----------------
1. Dictionaries store key-value pairs.
2. Keys must be unique.
3. Keys must be hashable.
4. Values can be any data type.
5. Dictionaries are mutable.
6. dictionary[key] raises KeyError if the
   key does not exist.
7. get() safely accesses a key.
8. Dictionaries can contain other dictionaries.
9. Dictionaries can contain lists, tuples,
   sets, and other objects.
10. Dictionary methods will be covered in
    08_dictionary_methods.py.
"""