"""
===========================================
Python Tuples
===========================================

A tuple is an ordered and immutable collection
of elements.

Tuples can:
✔ Store multiple values
✔ Store different data types
✔ Contain duplicate values
✔ Be indexed and sliced
✔ Be nested
✔ Be unpacked

Unlike lists, tuples cannot be modified
after they are created.

Syntax:

tuple_name = (element1, element2, element3)
"""


# ===========================================
# 1. Creating a Tuple
# ===========================================

numbers = (10, 20, 30, 40)

print(numbers)                         # (10, 20, 30, 40)


# ===========================================
# 2. Tuple with Different Data Types
# ===========================================

data = ("Python", 22, 3.14, True)

print(data)                            # ('Python', 22, 3.14, True)


# ===========================================
# 3. Empty Tuple
# ===========================================

empty_tuple = ()

print(empty_tuple)                     # ()


# ===========================================
# 4. Single-Element Tuple
# ===========================================

number = (10,)

print(number)                          # (10,)
print(type(number))                    # <class 'tuple'>


# Without the comma, it is an integer

number = (10)

print(type(number))                    # <class 'int'>


# ===========================================
# 5. Creating Tuple Without Parentheses
# ===========================================

numbers = 10, 20, 30

print(numbers)                         # (10, 20, 30)
print(type(numbers))                   # <class 'tuple'>


# ===========================================
# 6. Accessing Tuple Elements
# ===========================================

languages = ("Python", "Java", "C++", "Go")

print(languages[0])                    # Python
print(languages[1])                    # Java
print(languages[-1])                   # Go


# ===========================================
# 7. Tuple Slicing
# ===========================================

numbers = (10, 20, 30, 40, 50)

print(numbers[0:3])                    # (10, 20, 30)
print(numbers[:3])                     # (10, 20, 30)
print(numbers[2:])                     # (30, 40, 50)
print(numbers[-3:])                    # (30, 40, 50)


# ===========================================
# 8. Tuple Slicing with Step
# ===========================================

numbers = (1, 2, 3, 4, 5, 6)

print(numbers[::2])                    # (1, 3, 5)
print(numbers[1::2])                   # (2, 4, 6)
print(numbers[::-1])                   # (6, 5, 4, 3, 2, 1)


# ===========================================
# 9. Tuples are Immutable
# ===========================================

numbers = (10, 20, 30)

# numbers[1] = 200

# TypeError: 'tuple' object does not support
# item assignment


# ===========================================
# 10. Tuple Length
# ===========================================

languages = ("Python", "Java", "C++")

print(len(languages))                  # 3


# ===========================================
# 11. Membership Operators
# ===========================================

languages = ("Python", "Java", "C++")

print("Python" in languages)           # True
print("JavaScript" in languages)       # False
print("JavaScript" not in languages)   # True


# ===========================================
# 12. Tuples Can Contain Duplicates
# ===========================================

numbers = (10, 20, 10, 30, 20)

print(numbers)                         # (10, 20, 10, 30, 20)


# ===========================================
# 13. Nested Tuples
# ===========================================

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix)                          # ((1, 2, 3), (4, 5, 6), (7, 8, 9))


# ===========================================
# 14. Accessing Nested Tuple Elements
# ===========================================

matrix = (
    (1, 2, 3),
    (4, 5, 6)
)

print(matrix[0])                       # (1, 2, 3)
print(matrix[0][1])                    # 2
print(matrix[1][2])                    # 6


# ===========================================
# 15. Iterating Through a Tuple
# ===========================================

languages = ("Python", "Java", "C++")

for language in languages:
    print(language)

# Python
# Java
# C++


# ===========================================
# 16. Tuple Concatenation
# ===========================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print(combined)                        # (1, 2, 3, 4, 5, 6)


# ===========================================
# 17. Tuple Repetition
# ===========================================

numbers = (1, 2, 3)

print(numbers * 2)                     # (1, 2, 3, 1, 2, 3)


# ===========================================
# 18. Tuple Packing
# ===========================================

student = "Kanishka", 22, "ISE"

print(student)                         # ('Kanishka', 22, 'ISE')


# ===========================================
# 19. Tuple Unpacking
# ===========================================

student = ("Kanishka", 22, "ISE")

name, age, course = student

print(name)                            # Kanishka
print(age)                             # 22
print(course)                          # ISE


# ===========================================
# 20. Extended Tuple Unpacking
# ===========================================

numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)                           # 1
print(middle)                          # [2, 3, 4]
print(last)                            # 5


# ===========================================
# 21. Swapping Variables Using Tuples
# ===========================================

a = 10
b = 20

a, b = b, a

print(a)                              # 20
print(b)                              # 10


# ===========================================
# 22. Converting List to Tuple
# ===========================================

numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)                   # (10, 20, 30)


# ===========================================
# 23. Converting Tuple to List
# ===========================================

numbers_tuple = (10, 20, 30)

numbers_list = list(numbers_tuple)

print(numbers_list)                    # [10, 20, 30]


# ===========================================
# 24. Comparing Tuples
# ===========================================

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)                # True


# ===========================================
# 25. Tuple as a Dictionary Key
# ===========================================

locations = {
    (12.97, 77.59): "Bangalore",
    (19.07, 72.87): "Mumbai"
}

print(locations[(12.97, 77.59)])       # Bangalore


# ===========================================
# 26. Tuple of Lists
# ===========================================

data = (
    [10, 20],
    [30, 40]
)

data[0].append(30)

print(data)                            # ([10, 20, 30], [30, 40])


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Creating Tuples
✔ Empty Tuples
✔ Single-Element Tuples
✔ Tuple Indexing
✔ Negative Indexing
✔ Tuple Slicing
✔ Tuple Immutability
✔ len()
✔ Membership Operators
✔ Duplicate Elements
✔ Nested Tuples
✔ Tuple Iteration
✔ Tuple Concatenation
✔ Tuple Repetition
✔ Tuple Packing
✔ Tuple Unpacking
✔ Extended Unpacking
✔ Variable Swapping
✔ List <-> Tuple Conversion
✔ Tuple Comparison
✔ Tuples as Dictionary Keys
✔ Mutable Objects Inside Tuples

Key Points
----------
1. Tuples are ordered collections.
2. Tuples are immutable.
3. Tuples allow duplicate elements.
4. Tuples can contain different data types.
5. A single-element tuple requires a comma.
6. Tuples support indexing and slicing.
7. Tuples can contain mutable objects such as lists.
8. Tuples can be used as dictionary keys when all
   their elements are hashable.
9. Tuple methods are covered separately in
   04_tuple_methods.py.
"""