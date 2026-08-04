"""
===========================================
Python while Loop
===========================================

A while loop executes a block of code
as long as the given condition is True.

Syntax:

while condition:
    # Code
"""

# ===========================================
# 1. Basic while Loop
# ===========================================

count = 1

while count <= 5:
    print(count)
    count += 1

# 1
# 2
# 3
# 4
# 5

# ===========================================
# 2. Countdown
# ===========================================

number = 5

while number > 0:
    print(number)
    number -= 1

# 5
# 4
# 3
# 2
# 1

# ===========================================
# 3. Even Numbers
# ===========================================

num = 2

while num <= 10:
    print(num)
    num += 2

# 2
# 4
# 6
# 8
# 10

# ===========================================
# 4. Sum of First Five Numbers
# ===========================================

i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print(total)             # 15

# ===========================================
# 5. Multiplication Table
# ===========================================

number = 5
i = 1

while i <= 10:
    print(f"{number} x {i} = {number*i}")
    i += 1

# 5 x 1 = 5
# ...
# 5 x 10 = 50

# ===========================================
# 6. Iterating Through a String
# ===========================================

text = "Python"

index = 0

while index < len(text):
    print(text[index])
    index += 1

# P
# y
# t
# h
# o
# n

# ===========================================
# 7. Infinite Loop (Example)
# ===========================================

# while True:
#     print("Running Forever")

# ===========================================
# 8. User Input Example
# ===========================================

password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted")

# ===========================================
# 9. while...else
# ===========================================

count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop Finished")

# 1
# 2
# 3
# Loop Finished

# ===========================================
# Summary
# ===========================================

"""
Topics Covered

✔ while Loop
✔ Counter Controlled Loop
✔ Countdown
✔ Sum Calculation
✔ Multiplication Table
✔ String Traversal
✔ Infinite Loop
✔ User Input Loop
✔ while...else
"""