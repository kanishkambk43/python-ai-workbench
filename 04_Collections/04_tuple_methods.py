"""
===========================================
Python Tuple Methods
===========================================

Tuples are immutable, so they have only two
built-in methods:

1. count()
2. index()

Other useful operations such as len(),
membership checking, and slicing are also
demonstrated below.
"""


# ===========================================
# 1. count()
# ===========================================

numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))                # 3
print(numbers.count(50))                # 0


# ===========================================
# 2. count() with Strings
# ===========================================

languages = ("Python", "Java", "Python", "C++")

print(languages.count("Python"))        # 2
print(languages.count("Java"))          # 1


# ===========================================
# 3. index()
# ===========================================

languages = ("Python", "Java", "C++", "Go")

print(languages.index("Python"))        # 0
print(languages.index("C++"))           # 2


# ===========================================
# 4. index() with Duplicate Values
# ===========================================

numbers = (10, 20, 30, 20, 40)

print(numbers.index(20))                # 1

# index() returns the position of the
# first occurrence of the value.


# ===========================================
# 5. index() with Start Position
# ===========================================

numbers = (10, 20, 30, 20, 40)

print(numbers.index(20, 2))             # 3

# Search starts from index 2.


# ===========================================
# 6. index() with Start and End Position
# ===========================================

numbers = (10, 20, 30, 20, 40, 20)

print(numbers.index(20, 2, 5))          # 3

# Search range:
# index 2 to index 4


# ===========================================
# 7. index() with a Missing Value
# ===========================================

numbers = (10, 20, 30)

# print(numbers.index(50))
# ValueError: tuple.index(x): x not in tuple


# ===========================================
# 8. len() with Tuple
# ===========================================

languages = ("Python", "Java", "C++")

print(len(languages))                   # 3


# ===========================================
# 9. Membership Checking
# ===========================================

languages = ("Python", "Java", "C++")

print("Python" in languages)            # True
print("JavaScript" in languages)        # False
print("JavaScript" not in languages)    # True


# ===========================================
# 10. Combining count() and index()
# ===========================================

numbers = (10, 20, 10, 30, 10, 40)

value = 10

print(numbers.count(value))             # 3
print(numbers.index(value))             # 0


# ===========================================
# 11. Tuple Methods with User Data
# ===========================================

skills = (
    "Python",
    "SQL",
    "Python",
    "React",
    "Python"
)

print(skills.count("Python"))           # 3
print(skills.index("React"))            # 3


# ===========================================
# 12. Checking Before Using index()
# ===========================================

languages = ("Python", "Java", "C++")

if "Python" in languages:
    print(languages.index("Python"))    # 0
else:
    print("Language not found")


# ===========================================
# 13. Working with Nested Tuples
# ===========================================

students = (
    ("Kanishka", 85),
    ("Rahul", 90),
    ("Aman", 78)
)

print(students.count(("Kanishka", 85))) # 1
print(students.index(("Rahul", 90)))    # 1


# ===========================================
# 14. Tuple Slicing
# ===========================================

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])                     # (20, 30, 40)
print(numbers[:3])                      # (10, 20, 30)
print(numbers[2:])                      # (30, 40, 50)


# ===========================================
# 15. Tuple Methods vs List Methods
# ===========================================

"""
Lists have many methods because they are mutable.

Lists:
✔ append()
✔ extend()
✔ insert()
✔ remove()
✔ pop()
✔ clear()
✔ sort()
✔ reverse()

Tuples:
✔ count()
✔ index()

Tuples do not have methods such as append()
or remove() because tuples cannot be modified.
"""


# ===========================================
# Summary
# ===========================================

"""
Tuple Methods Covered
---------------------
✔ count()
✔ index()

Related Operations
------------------
✔ len()
✔ in
✔ not in
✔ Slicing

Key Points
----------
1. Tuples have only two built-in methods:
   count() and index().

2. count() returns the number of times
   a value occurs.

3. index() returns the position of the
   first occurrence.

4. index() raises ValueError if the
   requested value is not found.

5. Tuples are immutable, so methods such
   as append(), remove(), and sort() do
   not exist for tuples.
"""