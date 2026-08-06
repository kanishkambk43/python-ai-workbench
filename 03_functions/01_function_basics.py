"""
===========================================
Python Function Basics
===========================================

A function is a reusable block of code that
performs a specific task.

Advantages:
✔ Code Reusability
✔ Better Readability
✔ Easier Maintenance

Syntax:

def function_name():
    # Function Body

function_name()
"""

# ===========================================
# 1. Defining and Calling a Function
# ===========================================

def greet():
    print("Hello, World!")

greet()                         # Hello, World!


# ===========================================
# 2. Function with One Parameter
# ===========================================

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Kanishka")          # Hello, Kanishka


# ===========================================
# 3. Function with Multiple Parameters
# ===========================================

def add(a, b):
    print(a + b)

add(10, 20)                     # 30


# ===========================================
# 4. Function Returning a Value
# ===========================================

def square(number):
    return number * number

result = square(5)

print(result)                   # 25


# ===========================================
# 5. Function Without Return
# ===========================================

def display():
    print("Learning Python")

display()                       # Learning Python


# ===========================================
# 6. Returning Multiple Values
# ===========================================

def calculate(a, b):
    return a + b, a - b

sum_value, difference = calculate(20, 10)

print(sum_value)                # 30
print(difference)               # 10


# ===========================================
# 7. Calling a Function Multiple Times
# ===========================================

def welcome():
    print("Welcome!")

welcome()                       # Welcome!
welcome()                       # Welcome!
welcome()                       # Welcome!


# ===========================================
# 8. Local Variables
# ===========================================

def student():
    name = "Kanishka"
    print(name)

student()                       # Kanishka

# print(name)                   # NameError


# ===========================================
# 9. Global Variable
# ===========================================

college = "NIE"

def show_college():
    print(college)

show_college()                  # NIE


# ===========================================
# 10. Function Calling Another Function
# ===========================================

def message():
    print("Python")

def display_message():
    message()

display_message()               # Python


# ===========================================
# 11. Checking Return Type
# ===========================================

def multiply(a, b):
    return a * b

value = multiply(5, 6)

print(type(value))              # <class 'int'>


# ===========================================
# 12. Empty Function
# ===========================================

def future_feature():
    pass

print("Function Created Successfully")
# Function Created Successfully


# ===========================================
# 13. Built-in Function Example
# ===========================================

numbers = [10, 20, 30, 40]

print(len(numbers))             # 4
print(max(numbers))             # 40
print(min(numbers))             # 10


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Defining Functions
✔ Calling Functions
✔ Parameters
✔ Return Statement
✔ Multiple Return Values
✔ Local Variables
✔ Global Variables
✔ Nested Function Calls
✔ Built-in Functions
✔ pass Statement

Key Points
----------
1. A function is defined using the 'def' keyword.
2. A function executes only when it is called.
3. 'return' sends a value back to the caller.
4. Local variables exist only inside a function.
5. Global variables can be accessed throughout the program.
6. Functions improve code reusability and readability.
"""