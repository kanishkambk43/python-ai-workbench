"""
Topic: Type Casting in Python

Type casting is the process of converting one data type into another.
Python supports:
1. Implicit Type Casting (Automatic)
2. Explicit Type Casting (Manual)
"""

# -----------------------------------
# Implicit Type Casting
# -----------------------------------

num1 = 10          # int
num2 = 5.5         # float

result = num1 + num2

print(result)
print(type(result))


# -----------------------------------
# Explicit Type Casting
# -----------------------------------

number = "100"

converted_number = int(number)

print(converted_number)
print(type(converted_number))


# -----------------------------------
# Integer to Float
# -----------------------------------

age = 22

height = float(age)

print(height)
print(type(height))


# -----------------------------------
# Float to Integer
# -----------------------------------

price = 99.99

whole_price = int(price)

print(whole_price)
print(type(whole_price))


# -----------------------------------
# Integer to String
# -----------------------------------

marks = 95

marks_string = str(marks)

print(marks_string)
print(type(marks_string))


# -----------------------------------
# Float to String
# -----------------------------------

pi = 3.14159

pi_string = str(pi)

print(pi_string)
print(type(pi_string))


# -----------------------------------
# String to Float
# -----------------------------------

value = "12.75"

number = float(value)

print(number)
print(type(number))


# -----------------------------------
# Boolean Type Casting
# -----------------------------------

print(bool(1))
print(bool(0))

print(bool("Python"))
print(bool(""))

print(bool([]))
print(bool([1, 2, 3]))

print(bool(None))


# -----------------------------------
# List Type Casting
# -----------------------------------

text = "Python"

characters = list(text)

print(characters)


# -----------------------------------
# Tuple Type Casting
# -----------------------------------

numbers = [10, 20, 30]

numbers_tuple = tuple(numbers)

print(numbers_tuple)


# -----------------------------------
# Set Type Casting
# -----------------------------------

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)


# -----------------------------------
# Dictionary Type Casting
# -----------------------------------

pairs = [("name", "Kanishka"), ("age", 22)]

student = dict(pairs)

print(student)


# -----------------------------------
# Invalid Type Casting
# -----------------------------------

# Uncomment to see the error

# value = "Python"
# print(int(value))

# ValueError: invalid literal for int()


# -----------------------------------
# User Input Type Casting
# -----------------------------------

age = int(input("Enter your age: "))

print(age)
print(type(age))