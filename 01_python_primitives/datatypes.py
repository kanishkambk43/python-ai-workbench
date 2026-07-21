"""
Topic: Data Types in Python

A data type defines the type of value a variable can store.
Python automatically determines the data type at runtime.
"""

# -----------------------------
# Integer (int)
# -----------------------------

age = 22
print(age)
print(type(age))


# -----------------------------
# Float (float)
# -----------------------------

height = 181.5
print(height)
print(type(height))


# -----------------------------
# Complex (complex)
# -----------------------------

number = 3 + 4j
print(number)
print(type(number))


# -----------------------------
# String (str)
# -----------------------------

name = "Kanishka"
print(name)
print(type(name))


# -----------------------------
# Boolean (bool)
# -----------------------------

is_student = True
print(is_student)
print(type(is_student))


# -----------------------------
# List (list)
# Ordered, Mutable
# -----------------------------

fruits = ["Apple", "Banana", "Mango"]
print(fruits)
print(type(fruits))


# -----------------------------
# Tuple (tuple)
# Ordered, Immutable
# -----------------------------

coordinates = (10, 20)
print(coordinates)
print(type(coordinates))


# -----------------------------
# Set (set)
# Unordered, Unique Elements
# -----------------------------

numbers = {1, 2, 3, 4}
print(numbers)
print(type(numbers))


# -----------------------------
# Dictionary (dict)
# Key-Value Pairs
# -----------------------------

student = {
    "name": "Kanishka",
    "age": 22,
    "cgpa": 7.61
}

print(student)
print(type(student))


# -----------------------------
# None Type (NoneType)
# Represents the absence of a value
# -----------------------------

result = None
print(result)
print(type(result))


# -----------------------------
# Type Checking
# -----------------------------

x = 100

print(type(x))
print(isinstance(x, int))
print(isinstance(x, float))


# -----------------------------
# Type Conversion (Preview)
# -----------------------------

number = "100"

print(type(number))

converted = int(number)

print(converted)
print(type(converted))