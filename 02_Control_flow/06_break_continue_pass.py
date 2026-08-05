"""
===========================================
Python break, continue and pass
===========================================

break
------
Terminates the loop immediately.

continue
---------
Skips the current iteration and moves
to the next iteration.

pass
----
Acts as a placeholder.
It does nothing.
"""

# ===========================================
# break Statement
# ===========================================

print("break Statement")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# ===========================================
# break in while Loop
# ===========================================

print("\nbreak in while Loop")

count = 1

while True:
    if count == 6:
        break

    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5


# ===========================================
# continue Statement
# ===========================================

print("\ncontinue Statement")

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

# Output:
# 1
# 2
# 4
# 5


# ===========================================
# continue with Even Numbers
# ===========================================

print("\nSkipping Even Numbers")

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)

# Output:
# 1
# 3
# 5
# 7
# 9


# ===========================================
# continue in while Loop
# ===========================================

print("\ncontinue in while Loop")

count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(count)

# Output:
# 1
# 2
# 4
# 5


# ===========================================
# pass Statement
# ===========================================

print("\npass Statement")

for i in range(5):

    if i == 2:
        pass

    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# ===========================================
# pass in Function
# ===========================================

def future_feature():
    pass

print("\nFunction Created Successfully")

# Output:
# Function Created Successfully


# ===========================================
# pass in Class
# ===========================================

class Student:
    pass

student = Student()

print(type(student))

# Output:
# <class '__main__.Student'>


# ===========================================
# break in Nested Loop
# ===========================================

print("\nbreak in Nested Loop")

for i in range(3):

    for j in range(3):

        if j == 1:
            break

        print(i, j)

# Output:
# 0 0
# 1 0
# 2 0


# ===========================================
# continue in Nested Loop
# ===========================================

print("\ncontinue in Nested Loop")

for i in range(3):

    for j in range(3):

        if j == 1:
            continue

        print(i, j)

# Output:
# 0 0
# 0 2
# 1 0
# 1 2
# 2 0
# 2 2


# ===========================================
# for...else with break
# ===========================================

print("\nfor...else")

for i in range(5):

    if i == 3:
        break

    print(i)

else:
    print("Loop Finished")

# Output:
# 0
# 1
# 2


# ===========================================
# while...else
# ===========================================

print("\nwhile...else")

count = 1

while count <= 3:
    print(count)
    count += 1

else:
    print("Loop Completed")

# Output:
# 1
# 2
# 3
# Loop Completed


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ break
✔ continue
✔ pass
✔ break in for Loop
✔ break in while Loop
✔ continue in for Loop
✔ continue in while Loop
✔ pass in Loop
✔ pass in Function
✔ pass in Class
✔ Nested Loops
✔ for...else
✔ while...else

Key Points
----------
1. break immediately terminates the nearest loop.
2. continue skips the current iteration.
3. pass does nothing and is used as a placeholder.
4. break only exits the innermost loop.
5. The else block executes only if the loop finishes normally
   (i.e., without encountering a break statement).
"""