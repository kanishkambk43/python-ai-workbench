"""
===========================================
Python Lists
===========================================

A list is an ordered and mutable collection
of elements.

Lists can:
✔ Store multiple values
✔ Store different data types
✔ Contain duplicate values
✔ Be modified after creation
✔ Be indexed and sliced

Syntax:

list_name = [element1, element2, element3]
"""


# ===========================================
# 1. Creating a List
# ===========================================

numbers = [10, 20, 30, 40, 50]

print(numbers)                          # [10, 20, 30, 40, 50]


# ===========================================
# 2. List with Different Data Types
# ===========================================

data = ["Python", 22, 3.14, True]

print(data)                             # ['Python', 22, 3.14, True]


# ===========================================
# 3. Empty List
# ===========================================

empty_list = []

print(empty_list)                       # []


# ===========================================
# 4. Checking List Type
# ===========================================

languages = ["Python", "Java", "C++"]

print(type(languages))                   # <class 'list'>


# ===========================================
# 5. Accessing List Elements
# ===========================================

languages = ["Python", "Java", "C++", "JavaScript"]

print(languages[0])                      # Python
print(languages[1])                      # Java
print(languages[2])                      # C++
print(languages[-1])                     # JavaScript


# ===========================================
# 6. List Indexing
# ===========================================

numbers = [10, 20, 30, 40, 50]

print(numbers[0])                        # 10
print(numbers[-1])                       # 50


# ===========================================
# 7. List Slicing
# ===========================================

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])                      # [10, 20, 30]
print(numbers[:3])                       # [10, 20, 30]
print(numbers[2:])                       # [30, 40, 50]
print(numbers[-3:])                      # [30, 40, 50]


# ===========================================
# 8. List Slicing with Step
# ===========================================

numbers = [1, 2, 3, 4, 5, 6]

print(numbers[::2])                      # [1, 3, 5]
print(numbers[1::2])                     # [2, 4, 6]
print(numbers[::-1])                     # [6, 5, 4, 3, 2, 1]


# ===========================================
# 9. Lists are Mutable
# ===========================================

numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)                           # [10, 200, 30]


# ===========================================
# 10. List Length
# ===========================================

languages = ["Python", "Java", "C++"]

print(len(languages))                     # 3


# ===========================================
# 11. Checking Membership
# ===========================================

languages = ["Python", "Java", "C++"]

print("Python" in languages)              # True
print("JavaScript" in languages)         # False
print("JavaScript" not in languages)     # True


# ===========================================
# 12. Lists Can Contain Duplicates
# ===========================================

numbers = [10, 20, 10, 30, 20]

print(numbers)                           # [10, 20, 10, 30, 20]


# ===========================================
# 13. Nested Lists
# ===========================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)                            # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# ===========================================
# 14. Accessing Nested List Elements
# ===========================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0])                         # [1, 2, 3]
print(matrix[0][1])                      # 2
print(matrix[1][2])                      # 6


# ===========================================
# 15. Iterating Through a List
# ===========================================

languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)

# Python
# Java
# C++


# ===========================================
# 16. Iterating with Index
# ===========================================

languages = ["Python", "Java", "C++"]

for index in range(len(languages)):
    print(index, languages[index])

# 0 Python
# 1 Java
# 2 C++


# ===========================================
# 17. Combining Lists
# ===========================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2

print(combined)                          # [1, 2, 3, 4, 5, 6]


# ===========================================
# 18. Repeating a List
# ===========================================

numbers = [1, 2, 3]

print(numbers * 2)                       # [1, 2, 3, 1, 2, 3]


# ===========================================
# 19. Comparing Lists
# ===========================================

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)                    # True


# ===========================================
# 20. List with Mixed Nested Data
# ===========================================

student = [
    "Kanishka",
    22,
    ["Python", "SQL", "React"],
    True
]

print(student[0])                        # Kanishka
print(student[2])                        # ['Python', 'SQL', 'React']
print(student[2][1])                     # SQL


# ===========================================
# 21. Copying a List Reference
# ===========================================

list1 = [10, 20, 30]
list2 = list1

list2[0] = 100

print(list1)                             # [100, 20, 30]
print(list2)                             # [100, 20, 30]


# ===========================================
# 22. Creating an Independent Copy
# ===========================================

list1 = [10, 20, 30]
list2 = list1.copy()

list2[0] = 100

print(list1)                             # [10, 20, 30]
print(list2)                             # [100, 20, 30]


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Creating Lists
✔ Empty Lists
✔ Multiple Data Types
✔ Indexing
✔ Negative Indexing
✔ Slicing
✔ Step Slicing
✔ List Mutability
✔ len()
✔ Membership Operators
✔ Duplicate Elements
✔ Nested Lists
✔ List Iteration
✔ Combining Lists
✔ List Repetition
✔ List Comparison
✔ List References
✔ Copying Lists

Key Points
----------
1. Lists are ordered collections.
2. Lists are mutable.
3. Lists allow duplicate elements.
4. Lists can contain different data types.
5. List indexing starts from 0.
6. Negative indexing starts from -1.
7. Lists can contain other lists.
"""