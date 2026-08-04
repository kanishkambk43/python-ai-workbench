"""
===========================================
Python for Loop
===========================================

A for loop is used to iterate over a sequence
such as a string, list, tuple, set, dictionary,
or range of numbers.

Syntax:

for variable in sequence:
    # Code
"""

# ===========================================
# 1. Basic for Loop
# ===========================================

for i in range(5):
    print(i)                  # 0 1 2 3 4

# ===========================================
# 2. range(start, stop)
# ===========================================

for i in range(1, 6):
    print(i)                  # 1 2 3 4 5

# ===========================================
# 3. range(start, stop, step)
# ===========================================

for i in range(2, 11, 2):
    print(i)                  # 2 4 6 8 10

# ===========================================
# 4. Iterating Through a String
# ===========================================

text = "Python"

for char in text:
    print(char)
# P
# y
# t
# h
# o
# n

# ===========================================
# 5. Iterating Through a List
# ===========================================

languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
# Python
# Java
# C++

# ===========================================
# 6. Iterating Through a Tuple
# ===========================================

numbers = (10, 20, 30)

for num in numbers:
    print(num)
# 10
# 20
# 30

# ===========================================
# 7. Iterating Through a Set
# ===========================================

fruits = {"Apple", "Banana", "Mango"}

for fruit in fruits:
    print(fruit)
# Order may vary because sets are unordered.

# ===========================================
# 8. Iterating Through a Dictionary
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "ISE"
}

for key in student:
    print(key)
# name
# age
# course

# ===========================================
# 9. Dictionary Keys and Values
# ===========================================

for key, value in student.items():
    print(key, value)

# name Kanishka
# age 22
# course ISE

# ===========================================
# 10. enumerate()
# ===========================================

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)

# 0 Python
# 1 Java
# 2 C++

# ===========================================
# 11. Nested for Loop
# ===========================================

for i in range(3):
    for j in range(2):
        print(i, j)

# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1

# ===========================================
# 12. Reverse Loop
# ===========================================

for i in range(5, 0, -1):
    print(i)

# 5
# 4
# 3
# 2
# 1

# ===========================================
# Summary
# ===========================================

"""
Topics Covered

✔ for Loop
✔ range()
✔ Strings
✔ Lists
✔ Tuples
✔ Sets
✔ Dictionaries
✔ enumerate()
✔ Nested Loops
✔ Reverse Loop
"""