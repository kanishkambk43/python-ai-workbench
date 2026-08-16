"""
===========================================
Python List Methods
===========================================

List methods are built-in functions used to
add, remove, search, and organize elements
inside a list.

Lists are mutable, so these methods can
modify the original list.
"""


# ===========================================
# 1. append()
# ===========================================

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)                         # [10, 20, 30, 40]


# ===========================================
# 2. append() with Different Data Types
# ===========================================

items = ["Python", "SQL"]

items.append("React")

print(items)                           # ['Python', 'SQL', 'React']


# ===========================================
# 3. append() Adds One Element
# ===========================================

numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)                         # [1, 2, 3, [4, 5]]


# ===========================================
# 4. extend()
# ===========================================

numbers = [1, 2, 3]

numbers.extend([4, 5, 6])

print(numbers)                         # [1, 2, 3, 4, 5, 6]


# ===========================================
# 5. insert()
# ===========================================

numbers = [10, 20, 40]

numbers.insert(2, 30)

print(numbers)                         # [10, 20, 30, 40]


# ===========================================
# 6. remove()
# ===========================================

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)                         # [10, 30, 20]


# ===========================================
# 7. pop()
# ===========================================

numbers = [10, 20, 30]

removed = numbers.pop()

print(removed)                         # 30
print(numbers)                         # [10, 20]


# ===========================================
# 8. pop() with Index
# ===========================================

numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print(removed)                         # 20
print(numbers)                         # [10, 30, 40]


# ===========================================
# 9. clear()
# ===========================================

numbers = [10, 20, 30]

numbers.clear()

print(numbers)                         # []


# ===========================================
# 10. index()
# ===========================================

languages = ["Python", "Java", "C++", "Python"]

print(languages.index("Python"))       # 0
print(languages.index("C++"))          # 2


# ===========================================
# 11. count()
# ===========================================

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))               # 3
print(numbers.count(50))               # 0


# ===========================================
# 12. sort()
# ===========================================

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)                         # [10, 20, 30, 40]


# ===========================================
# 13. sort() in Descending Order
# ===========================================

numbers = [10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)                         # [40, 30, 20, 10]


# ===========================================
# 14. reverse()
# ===========================================

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)                         # [40, 30, 20, 10]


# ===========================================
# 15. copy()
# ===========================================

numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)                         # [10, 20, 30]
print(new_numbers)                     # [10, 20, 30, 40]


# ===========================================
# 16. Using len() with Lists
# ===========================================

languages = ["Python", "Java", "C++"]

print(len(languages))                   # 3


# ===========================================
# 17. Combining Methods
# ===========================================

numbers = [30, 10, 20]

numbers.append(40)
numbers.sort()

print(numbers)                         # [10, 20, 30, 40]


# ===========================================
# 18. Removing Duplicates Using a Set
# ===========================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)
# Output order may vary:
# [40, 10, 20, 30]


# ===========================================
# 19. sorted() vs sort()
# ===========================================

numbers = [30, 10, 20]

sorted_numbers = sorted(numbers)

print(sorted_numbers)                  # [10, 20, 30]
print(numbers)                         # [30, 10, 20]


# ===========================================
# 20. reverse() vs reversed()
# ===========================================

numbers = [1, 2, 3, 4]

reversed_numbers = list(reversed(numbers))

print(reversed_numbers)                # [4, 3, 2, 1]
print(numbers)                         # [1, 2, 3, 4]


# ===========================================
# Summary
# ===========================================

"""
List Methods Covered
--------------------
✔ append()
✔ extend()
✔ insert()
✔ remove()
✔ pop()
✔ clear()
✔ index()
✔ count()
✔ sort()
✔ reverse()
✔ copy()

Related Built-in Functions
--------------------------
✔ len()
✔ sorted()
✔ reversed()
✔ set()

Key Points
----------
1. append() adds one element to the end.
2. extend() adds multiple elements.
3. insert() adds an element at a specific index.
4. remove() removes the first matching element.
5. pop() removes and returns an element.
6. clear() removes all elements.
7. index() returns the position of an element.
8. count() returns how many times an element occurs.
9. sort() modifies the original list.
10. reverse() reverses the original list.
11. copy() creates a shallow copy of the list.
12. sorted() returns a new sorted list without
    modifying the original list.
"""