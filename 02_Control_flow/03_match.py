"""
===========================================
Python match...case Statement
===========================================

The match...case statement is used for
pattern matching and is similar to the
switch statement in other programming languages.

Available from Python 3.10+

Syntax:

match variable:
    case value1:
        # Code
    case value2:
        # Code
    case _:
        # Default case
"""

# ===========================================
# 1. Basic match...case
# ===========================================

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")              # Wednesday
    case _:
        print("Invalid Day")

# ===========================================
# 2. Grade Evaluation
# ===========================================

grade = "A"

match grade:
    case "A":
        print("Excellent")              # Excellent
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case _:
        print("Fail")

# ===========================================
# 3. Calculator Operation
# ===========================================

operator = "+"

match operator:
    case "+":
        print(10 + 5)                   # 15
    case "-":
        print(10 - 5)
    case "*":
        print(10 * 5)
    case "/":
        print(10 / 5)
    case _:
        print("Invalid Operator")

# ===========================================
# 4. Browser Selection
# ===========================================

browser = "Chrome"

match browser:
    case "Chrome":
        print("Launching Google Chrome")     # Launching Google Chrome
    case "Firefox":
        print("Launching Firefox")
    case "Edge":
        print("Launching Microsoft Edge")
    case _:
        print("Browser Not Found")

# ===========================================
# 5. Multiple Values in One Case
# ===========================================

day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")                # Weekend
    case _:
        print("Weekday")

# ===========================================
# 6. Default Case
# ===========================================

language = "Go"

match language:
    case "Python":
        print("Python Selected")
    case "Java":
        print("Java Selected")
    case _:
        print("Language Not Supported")     # Language Not Supported

# ===========================================
# 7. Using Guards (if)
# ===========================================

age = 25

match age:
    case age if age >= 18:
        print("Adult")                  # Adult
    case _:
        print("Minor")

# ===========================================
# 8. Matching Boolean Values
# ===========================================

is_logged_in = True

match is_logged_in:
    case True:
        print("Welcome User")           # Welcome User
    case False:
        print("Please Login")

# ===========================================
# 9. Matching Strings
# ===========================================

fruit = "Apple"

match fruit:
    case "Apple":
        print("Red Fruit")              # Red Fruit
    case "Banana":
        print("Yellow Fruit")
    case "Orange":
        print("Orange Fruit")
    case _:
        print("Unknown Fruit")

# ===========================================
# 10. Matching Integers
# ===========================================

choice = 2

match choice:
    case 1:
        print("Create")
    case 2:
        print("Read")                   # Read
    case 3:
        print("Update")
    case 4:
        print("Delete")
    case _:
        print("Invalid Choice")

# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ match...case
✔ Default Case (_)
✔ Multiple Values (|)
✔ Guards (if)
✔ Integer Matching
✔ String Matching
✔ Boolean Matching

Notes
-----
1. Introduced in Python 3.10.
2. Similar to switch-case in C, C++, and Java.
3. '_' acts as the default case.
4. '|' allows multiple patterns in a single case.
5. Guards (if) allow additional conditions.
"""