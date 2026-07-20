"""
Topic: Variables in Python

A variable is a named reference to an object in memory.
Python is dynamically typed, so the type of a variable is
determined at runtime.
"""

# -----------------------------
# Variable Declaration
# -----------------------------

name = "Kanishka"
age = 22
height = 181.5
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# -----------------------------
# Multiple Variable Assignment
# -----------------------------

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)


# -----------------------------
# Assigning the Same Value
# -----------------------------

a = b = c = 100

print(a)
print(b)
print(c)


# -----------------------------
# Variable Reassignment
# -----------------------------

language = "Python"

print(language)

language = "Java"

print(language)


# -----------------------------
# Dynamic Typing
# -----------------------------

value = 10
print(value)
print(type(value))

value = "Ten"
print(value)
print(type(value))


# -----------------------------
# Variable Naming Rules
# -----------------------------

student_name = "Alice"
studentAge = 20
_marks = 95

print(student_name)
print(studentAge)
print(_marks)


# -----------------------------
# Invalid Variable Names
# (Examples only - commented)
# -----------------------------

# 1name = "Python"
# my-variable = 100
# class = "AI"


# -----------------------------
# Constants (Convention Only) NO concept of constants in python .
# -----------------------------

PI = 3.14159
MAX_USERS = 1000

print(PI)
print(MAX_USERS)


# -----------------------------
# Deleting Variables
# -----------------------------

temp = "Temporary Variable"
print(temp)

del temp

# print(temp)   # NameError


# -----------------------------
# Checking Object Identity
# -----------------------------

a = 10
b = 10

print(id(a))
print(id(b))