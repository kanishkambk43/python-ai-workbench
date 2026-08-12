"""
===========================================
Python Variable Scope
===========================================

Scope determines where a variable can be
accessed in a Python program.

Python follows the LEGB rule:

L -> Local
E -> Enclosing
G -> Global
B -> Built-in
"""


# ===========================================
# 1. Local Scope
# ===========================================

def display_name():
    name = "Kanishka"
    print(name)                         # Kanishka

display_name()

# name cannot be accessed here because
# it belongs to the local scope of the function.


# ===========================================
# 2. Global Scope
# ===========================================

name = "Kanishka"

def display_name():
    print(name)

display_name()                          # Kanishka
print(name)                             # Kanishka


# ===========================================
# 3. Local and Global Variables
# ===========================================

name = "Global Name"

def display():
    name = "Local Name"
    print(name)

display()                               # Local Name
print(name)                             # Global Name


# ===========================================
# 4. Accessing a Global Variable
# ===========================================

language = "Python"

def show_language():
    print(language)

show_language()                         # Python


# ===========================================
# 5. Modifying a Global Variable
# ===========================================

count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)                            # 20


# ===========================================
# 6. global Keyword
# ===========================================

score = 50

def increase_score():
    global score
    score += 10

increase_score()

print(score)                            # 60


# ===========================================
# 7. Without global Keyword
# ===========================================

number = 10

def change_number():
    number = 20
    print(number)

change_number()                         # 20
print(number)                           # 10


# ===========================================
# 8. Enclosing Scope
# ===========================================

def outer_function():

    message = "Hello from outer function"

    def inner_function():
        print(message)

    inner_function()

outer_function()                        # Hello from outer function


# ===========================================
# 9. nonlocal Keyword
# ===========================================

def counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()
    increment()

counter()

# 1
# 2


# ===========================================
# 10. global vs nonlocal
# ===========================================

value = "Global"

def outer():

    value = "Enclosing"

    def inner():
        nonlocal value
        value = "Modified Enclosing"
        print(value)

    inner()
    print(value)

outer()

# Modified Enclosing
# Modified Enclosing

print(value)                            # Global


# ===========================================
# 11. LEGB Rule
# ===========================================

value = "Global"

def outer():

    value = "Enclosing"

    def inner():

        value = "Local"

        print(value)

    inner()

outer()

# Local


# ===========================================
# 12. Built-in Scope
# ===========================================

numbers = [10, 20, 30]

print(len(numbers))                     # 3

# len() is found in Python's built-in scope.


# ===========================================
# 13. LEGB Lookup
# ===========================================

name = "Global"

def outer():

    name = "Enclosing"

    def inner():

        name = "Local"

        print(name)

    inner()

outer()

# Local


# ===========================================
# 14. Deleting a Global Variable
# ===========================================

temporary = "Python"

print(temporary)                        # Python

del temporary

# print(temporary)                      # NameError


# ===========================================
# 15. Checking Global and Local Names
# ===========================================

language = "Python"

def check_scope():

    framework = "FastAPI"

    print(globals()["language"])         # Python
    print(locals()["framework"])        # FastAPI

check_scope()


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Variable Scope
✔ Local Scope
✔ Global Scope
✔ global Keyword
✔ Enclosing Scope
✔ nonlocal Keyword
✔ Built-in Scope
✔ LEGB Rule
✔ globals()
✔ locals()

Key Points
----------
1. Local variables exist inside their function.
2. Global variables are defined outside functions.
3. The global keyword allows a function to modify
   a global variable.
4. The nonlocal keyword allows an inner function
   to modify a variable from its enclosing function.
5. Python resolves variable names using the LEGB rule.

LEGB:
L -> Local
E -> Enclosing
G -> Global
B -> Built-in
"""