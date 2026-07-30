"""
===========================================
Python if...else Statement
===========================================

The if...else statement is used to execute
different blocks of code based on a condition.

Syntax:

if condition:
    # Code if condition is True
else:
    # Code if condition is False
"""

# ===========================================
# 1. Simple if Statement
# ===========================================

age = 20

if age >= 18:
    print("You are eligible to vote.")      # You are eligible to vote.

# ===========================================
# 2. if...else Statement
# ===========================================

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")               # You cannot vote.

# ===========================================
# 3. Checking Positive or Negative Number
# ===========================================

number = -5

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")                # Negative Number

# ===========================================
# 4. Checking Even or Odd
# ===========================================

number = 12

if number % 2 == 0:
    print("Even Number")                    # Even Number
else:
    print("Odd Number")

# ===========================================
# 5. Checking Password
# ===========================================

password = "python123"

if password == "python123":
    print("Access Granted")                 # Access Granted
else:
    print("Access Denied")

# ===========================================
# 6. Comparing Two Numbers
# ===========================================

a = 25
b = 15

if a > b:
    print("a is greater than b")            # a is greater than b
else:
    print("b is greater than or equal to a")

# ===========================================
# 7. Using Boolean Values
# ===========================================

is_logged_in = True

if is_logged_in:
    print("Welcome User!")                  # Welcome User!
else:
    print("Please Login.")

# ===========================================
# 8. Checking Empty String
# ===========================================

name = ""

if name:
    print("Name Entered")
else:
    print("Name is Empty")                  # Name is Empty

# ===========================================
# 9. Checking Membership
# ===========================================

language = "Python"

if "Py" in language:
    print("Found")                          # Found
else:
    print("Not Found")

# ===========================================
# 10. Ternary (Conditional) Expression
# ===========================================

age = 21

result = "Adult" if age >= 18 else "Minor"

print(result)                               # Adult

# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Simple if Statement
✔ if...else Statement
✔ Comparison Operators
✔ Logical Conditions
✔ Even/Odd Check
✔ Positive/Negative Check
✔ Boolean Conditions
✔ Empty String Check
✔ Membership Check
✔ Ternary Operator
"""