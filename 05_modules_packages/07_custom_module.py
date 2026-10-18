"""
===========================================
Python Custom Modules
===========================================

A custom module is a Python file created by
us that can be imported into another file.
"""

# ===========================================
# 1. Import a Custom Module
# ===========================================

# If greetings.py contains greet(), use:
# import greetings
# greetings.greet()                     # Calls greet() from greetings.py

# ===========================================
# 2. Import with an Alias
# ===========================================

# import greetings as gr
# gr.greet()                             # Calls the module using its alias

# ===========================================
# 3. Import a Specific Function
# ===========================================

# from greetings import greet
# greet()                                # Calls greet() without the module name

# ===========================================
# 4. Import Multiple Functions
# ===========================================

# from calculator import add, subtract
# print(add(10, 5))                      # Output: 15
# print(subtract(10, 5))                 # Output: 5

# ===========================================
# 5. Import Everything from a Module
# ===========================================

# from calculator import *
# print(add(2, 3))                       # Output: 5 (if add is defined)

# ===========================================
# 6. Create a Reusable Function
# ===========================================

# In calculator.py:
# def multiply(a, b):
#     return a * b
#
# In main.py:
# from calculator import multiply
# print(multiply(4, 3))                  # Output: 12

# ===========================================
# 7. Use a Variable from a Module
# ===========================================

# In settings.py:
# app_name = "Python Workbench"
#
# In main.py:
# import settings
# print(settings.app_name)               # Output: Python Workbench

# ===========================================
# 8. Protect Code with __name__
# ===========================================

# In greetings.py:
# def greet():
#     print("Hello!")
#
# if __name__ == "__main__":
#     greet()                            # Runs only when greetings.py is executed directly

# ===========================================
# 9. Import from a Package
# ===========================================

# Example structure:
# mypackage/
#     __init__.py
#     calculator.py
#
# from mypackage.calculator import add
# print(add(2, 3))                       # Output: 5 (if add returns a + b)

# ===========================================
# 10. Avoid Module Name Conflicts
# ===========================================

# Avoid naming your files after standard modules,
# such as random.py, math.py, or os.py.
# Otherwise, Python might import your file instead
# of the intended standard-library module.

# ===========================================
# Summary
# ===========================================

"""
Covered:
1. Import a custom module
2. Import using an alias
3. Import a specific function
4. Import multiple functions
5. Import all names
6. Create reusable functions
7. Access module variables
8. Use __name__ == "__main__"
9. Import from a package
10. Avoid module naming conflicts
"""