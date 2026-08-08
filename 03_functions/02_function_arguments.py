"""
===========================================
Python Function Arguments
===========================================

Function arguments are values passed to a
function when it is called.

Types of Arguments:
1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Arguments (*args)
5. Keyword Variable-Length Arguments (**kwargs)
"""

# ===========================================
# 1. Positional Arguments
# ===========================================

def introduce(name, age):
    print(name)
    print(age)

introduce("Kanishka", 22)
# Kanishka
# 22


# ===========================================
# 2. Keyword Arguments
# ===========================================

def student(name, course):
    print(name)
    print(course)

student(course="ISE", name="Kanishka")
# Kanishka
# ISE


# ===========================================
# 3. Default Arguments
# ===========================================

def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
# Hello, Guest

greet("Kanishka")
# Hello, Kanishka


# ===========================================
# 4. Multiple Default Arguments
# ===========================================

def employee(name, department="IT"):
    print(name)
    print(department)

employee("Rahul")
# Rahul
# IT

employee("Kanishka", "AI")
# Kanishka
# AI


# ===========================================
# 5. Variable-Length Arguments (*args)
# ===========================================

def add_numbers(*numbers):
    print(numbers)

add_numbers(10, 20, 30)
# (10, 20, 30)

add_numbers(5, 10, 15, 20, 25)
# (5, 10, 15, 20, 25)


# ===========================================
# 6. Using *args
# ===========================================

def calculate_sum(*numbers):
    print(sum(numbers))

calculate_sum(10, 20, 30)
# 60

calculate_sum(5, 10, 15, 20)
# 50


# ===========================================
# 7. Keyword Variable-Length Arguments (**kwargs)
# ===========================================

def student_info(**details):
    print(details)

student_info(name="Kanishka", age=22, course="ISE")
# {'name': 'Kanishka', 'age': 22, 'course': 'ISE'}


# ===========================================
# 8. Accessing **kwargs Values
# ===========================================

def display(**data):
    print(data["name"])
    print(data["city"])

display(name="Kanishka", city="Mysuru")
# Kanishka
# Mysuru


# ===========================================
# 9. Mixing Different Arguments
# ===========================================

def information(name, age=18, *skills):
    print(name)
    print(age)
    print(skills)

information("Kanishka", 22, "Python", "SQL", "React")
# Kanishka
# 22
# ('Python', 'SQL', 'React')


# ===========================================
# 10. Argument Unpacking (*)
# ===========================================

numbers = [10, 20]

def multiply(a, b):
    print(a * b)

multiply(*numbers)
# 200


# ===========================================
# 11. Dictionary Unpacking (**)
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

def details(name, age):
    print(name)
    print(age)

details(**student)
# Kanishka
# 22


# ===========================================
# 12. Keyword-Only Arguments
# ===========================================

def person(name, *, city):
    print(name)
    print(city)

person("Kanishka", city="Mysuru")
# Kanishka
# Mysuru


# ===========================================
# 13. Positional-Only Arguments
# ===========================================

def divide(a, b, /):
    print(a / b)

divide(10, 2)
# 5.0

# divide(a=10, b=2)   # TypeError


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Positional Arguments
✔ Keyword Arguments
✔ Default Arguments
✔ *args
✔ **kwargs
✔ Argument Unpacking
✔ Dictionary Unpacking
✔ Keyword-Only Arguments
✔ Positional-Only Arguments

Key Points
----------
1. Positional arguments follow the order of parameters.
2. Keyword arguments specify the parameter name explicitly.
3. Default arguments are used when no value is provided.
4. *args collects multiple positional arguments into a tuple.
5. **kwargs collects multiple keyword arguments into a dictionary.
6. * unpacks sequences like lists and tuples.
7. ** unpacks dictionaries into keyword arguments.
"""