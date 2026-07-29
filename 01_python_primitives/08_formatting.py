"""
===========================================
Python String Formatting
===========================================

String formatting is used to insert variables
or values into a string in a readable way.
"""

# ===========================================
# 1. Comma-Separated print()
# ===========================================

name = "Kanishka"
age = 22

print(name, age)                     # Kanishka 22

# ===========================================
# 2. String Concatenation
# ===========================================

name = "Kanishka"

print("Hello " + name)               # Hello Kanishka

# ===========================================
# 3. f-Strings (Recommended)
# ===========================================

name = "Kanishka"
age = 22

print(f"My name is {name}.")         # My name is Kanishka.
print(f"I am {age} years old.")      # I am 22 years old.

# ===========================================
# 4. Expressions inside f-Strings
# ===========================================

a = 10
b = 20

print(f"Sum = {a + b}")              # Sum = 30

# ===========================================
# 5. Floating Point Precision
# ===========================================

pi = 3.14159265359

print(f"{pi:.2f}")                   # 3.14
print(f"{pi:.4f}")                   # 3.1416

# ===========================================
# 6. Integer Formatting
# ===========================================

number = 1234567

print(f"{number:,}")                 # 1,234,567

# ===========================================
# 7. Percentage Formatting
# ===========================================

score = 0.875

print(f"{score:.1%}")                # 87.5%

# ===========================================
# 8. Width Formatting
# ===========================================

name = "Python"

print(f"|{name:15}|")                # |Python         |
print(f"|{name:<15}|")               # |Python         |
print(f"|{name:>15}|")               # |         Python|
print(f"|{name:^15}|")               # |    Python     |

# ===========================================
# 9. Leading Zeros
# ===========================================

number = 25

print(f"{number:05}")                # 00025

# ===========================================
# 10. Binary, Octal and Hexadecimal
# ===========================================

num = 25

print(f"Binary      : {num:b}")      # Binary      : 11001
print(f"Octal       : {num:o}")      # Octal       : 31
print(f"Hexadecimal : {num:x}")      # Hexadecimal : 19

# ===========================================
# 11. str.format()
# ===========================================

name = "Kanishka"
age = 22

print("My name is {}.".format(name))                 # My name is Kanishka.
print("I am {} years old.".format(age))              # I am 22 years old.
print("My name is {} and I am {}.".format(name, age))
# My name is Kanishka and I am 22.

# ===========================================
# 12. Positional Arguments
# ===========================================

print("{1} {0}".format("World", "Hello"))            # Hello World

# ===========================================
# 13. Keyword Arguments
# ===========================================

print("{name} is {age} years old.".format(name="Kanishka", age=22))
# Kanishka is 22 years old.

# ===========================================
# 14. Old Style Formatting (%)
# ===========================================

name = "Python"
version = 3.13

print("Language: %s" % name)         # Language: Python
print("Version: %.1f" % version)     # Version: 3.1

# ===========================================
# 15. Formatting Multiple Values
# ===========================================

name = "Kanishka"
college = "NIE"

print(f"Name    : {name}")           # Name    : Kanishka
print(f"College : {college}")        # College : NIE

# ===========================================
# 16. Escaping Braces
# ===========================================

print(f"{{Python}}")                 # {Python}

# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ print() formatting
✔ String concatenation
✔ f-Strings
✔ Expressions in f-Strings
✔ Floating-point precision
✔ Integer formatting
✔ Percentage formatting
✔ Width alignment
✔ Leading zeros
✔ Binary, Octal, Hexadecimal formatting
✔ str.format()
✔ Positional arguments
✔ Keyword arguments
✔ Old-style (%) formatting
✔ Escaping braces
"""