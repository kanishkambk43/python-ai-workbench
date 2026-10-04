"""
===========================================
Python Modules - import
===========================================

A module is a Python file containing code
such as variables, functions, and classes.

We can use code from another module by
importing it.

Basic syntax:

    import module_name

    module_name.function_name()

Python provides many built-in modules such as:
    math
    random
    datetime
    os
    sys

Custom modules can also be created.
"""


# ===========================================
# 1. Importing a Module
# ===========================================

import math

print(math.pi)                         # 3.141592653589793


# ===========================================
# 2. Using a Function from a Module
# ===========================================

import math

print(math.sqrt(25))                   # 5.0
print(math.factorial(5))               # 120


# ===========================================
# 3. Using Multiple Functions
# ===========================================

import math

print(math.sqrt(16))                   # 4.0
print(math.pow(2, 3))                  # 8.0
print(math.ceil(4.2))                  # 5
print(math.floor(4.8))                 # 4


# ===========================================
# 4. Importing Multiple Modules
# ===========================================

import math
import random

print(math.pi)                         # 3.141592653589793
print(random.randint(1, 10))            # Random number between 1 and 10


# ===========================================
# 5. Importing a Module with an Alias
# ===========================================

import math as m

print(m.pi)                            # 3.141592653589793
print(m.sqrt(49))                      # 7.0

# "m" is an alias for the math module.


# ===========================================
# 6. Another Alias Example
# ===========================================

import datetime as dt

current_date = dt.date.today()

print(current_date)                    # Current date


# ===========================================
# 7. from ... import
# ===========================================

from math import sqrt

print(sqrt(25))                        # 5.0

# We can directly use sqrt()
# instead of math.sqrt().


# ===========================================
# 8. Importing Multiple Items
# ===========================================

from math import sqrt, pi

print(sqrt(36))                        # 6.0
print(pi)                              # 3.141592653589793


# ===========================================
# 9. Importing with an Alias
# ===========================================

from math import sqrt as square_root

print(square_root(64))                 # 8.0


# ===========================================
# 10. Importing Everything
# ===========================================

# You can technically use:
#
# from math import *
#
# print(sqrt(25))
# print(pi)
#
# However, this is generally NOT recommended
# because it can make it difficult to know
# where names came from.


# ===========================================
# 11. Built-in Module Example - math
# ===========================================

import math

number = 5

print(math.factorial(number))           # 120
print(math.sqrt(number))                # 2.23606797749979


# ===========================================
# 12. Built-in Module Example - random
# ===========================================

import random

print(random.randint(1, 10))            # Random integer from 1 to 10


# ===========================================
# 13. random.choice()
# ===========================================

import random

colors = ["red", "blue", "green"]

print(random.choice(colors))             # Randomly: red / blue / green


# ===========================================
# 14. Built-in Module Example - datetime
# ===========================================

import datetime

today = datetime.date.today()

print(today)                            # Current date


# ===========================================
# 15. datetime.date
# ===========================================

import datetime

date = datetime.date(2026, 10, 4)

print(date)                             # 2026-10-04
print(date.year)                        # 2026
print(date.month)                       # 10
print(date.day)                         # 4


# ===========================================
# 16. Importing Specific Class
# ===========================================

from datetime import date

today = date.today()

print(today)                            # Current date


# ===========================================
# 17. Built-in Module Example - os
# ===========================================

import os

print(os.name)                          # nt (Windows)


# ===========================================
# 18. Current Working Directory
# ===========================================

import os

print(os.getcwd())                      # Current working directory


# ===========================================
# 19. Environment Variables
# ===========================================

import os

# Example:
#
# print(os.getenv("PATH"))
#
# Output will depend on your computer.


# ===========================================
# 20. Built-in Module Example - sys
# ===========================================

import sys

print(sys.version)                      # Your installed Python version


# ===========================================
# 21. Python Platform
# ===========================================

import sys

print(sys.platform)                     # win32 (on Windows)


# ===========================================
# 22. Module Aliases in Practice
# ===========================================

import math as mathematics

number = 81

print(mathematics.sqrt(number))         # 9.0


# ===========================================
# 23. Importing Functions Directly
# ===========================================

from math import sqrt, ceil, floor

print(sqrt(100))                        # 10.0
print(ceil(4.1))                        # 5
print(floor(4.9))                       # 4


# ===========================================
# 24. Checking Whether a Module Exists
# ===========================================

import math

print(math.__name__)                    # math


# ===========================================
# 25. Module Documentation
# ===========================================

import math

print(math.__doc__[:50])

# Output begins with something similar to:
# This module provides access to the mathematical functions...


# ===========================================
# 26. Module Location
# ===========================================

import math

print(math.__file__)

# Output depends on your Python installation.
# Some built-in/extension modules may not have
# a normal .py file path.


# ===========================================
# 27. Custom Module Concept
# ===========================================

"""
Suppose we create:

my_module.py

with:

def greet():
    print("Hello!")

Then another Python file can use:

import my_module

my_module.greet()

Output:
Hello!

This is called importing a custom module.
"""


# ===========================================
# 28. Example Custom Module
# ===========================================

"""
File 1: calculator.py

def add(a, b):
    return a + b


File 2: main.py

import calculator

print(calculator.add(10, 20))

Output:
30

Both files should normally be in the
same directory for this simple example.
"""


# ===========================================
# 29. Why Modules Are Useful
# ===========================================

"""
Without modules:

    main.py
        ↓
    hundreds of lines of code

With modules:

    main.py
        ↓
    calculator.py
    database.py
    utilities.py
    authentication.py

This makes programs easier to:

✔ Organize
✔ Reuse
✔ Maintain
✔ Debug
✔ Test
"""


# ===========================================
# 30. Module vs Package
# ===========================================

"""
MODULE
------
A single Python file.

Example:

calculator.py


PACKAGE
-------
A collection of related Python modules.

Example:

utilities/
    __init__.py
    calculator.py
    converter.py
    validator.py


So:

    Module  → one .py file
    Package → collection of modules
"""


# ===========================================
# 31. Importing from a Package - Preview
# ===========================================

"""
Suppose we have:

utilities/
    __init__.py
    calculator.py

Then we can write:

from utilities import calculator

print(calculator.add(10, 20))

Output:
30

Packages will be covered in more detail
in this section.
"""


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------

✔ What is a module?
✔ import
✔ import module
✔ import with alias
✔ from module import
✔ Importing multiple items
✔ Importing with alias
✔ Built-in modules
✔ math module
✔ random module
✔ datetime module
✔ os module
✔ sys module
✔ Custom modules
✔ Module organization
✔ Module vs package
✔ Package import preview

Important Syntax
----------------

1. Import entire module:

    import math

    math.sqrt(25)


2. Import with alias:

    import math as m

    m.sqrt(25)


3. Import specific function:

    from math import sqrt

    sqrt(25)


4. Import multiple functions:

    from math import sqrt, pi


5. Import with function alias:

    from math import sqrt as square_root

    square_root(25)


Key Idea
--------
A module allows us to organize and reuse
Python code instead of putting everything
inside one huge Python file.
"""