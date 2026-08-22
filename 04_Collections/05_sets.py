"""
===========================================
Python Sets
===========================================

A set is an unordered collection of unique
elements.

Sets:
✔ Do not allow duplicate elements
✔ Are mutable
✔ Are unordered
✔ Do not support indexing
✔ Support mathematical set operations
✔ Can contain elements of different data types

Syntax:

set_name = {element1, element2, element3}
"""


# ===========================================
# 1. Creating a Set
# ===========================================

numbers = {10, 20, 30, 40}

print(numbers)                         # {10, 20, 30, 40}


# ===========================================
# 2. Set with Different Data Types
# ===========================================

data = {"Python", 22, 3.14, True}

print(data)
# Output order may vary because sets are unordered.


# ===========================================
# 3. Empty Set
# ===========================================

empty_set = set()

print(empty_set)                       # set()
print(type(empty_set))                 # <class 'set'>


# ===========================================
# 4. Empty Curly Braces
# ===========================================

empty = {}

print(type(empty))                     # <class 'dict'>

# {} creates an empty dictionary,
# not an empty set.

# Use set() to create an empty set.


# ===========================================
# 5. Duplicate Elements
# ===========================================

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)
# {10, 20, 30, 40}
# Output order may vary.


# ===========================================
# 6. Removing Duplicates from a List
# ===========================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)
# {10, 20, 30, 40}
# Output order may vary.


# ===========================================
# 7. Checking Set Type
# ===========================================

languages = {"Python", "Java", "C++"}

print(type(languages))                 # <class 'set'>


# ===========================================
# 8. Membership Operators
# ===========================================

languages = {"Python", "Java", "C++"}

print("Python" in languages)           # True
print("JavaScript" in languages)       # False
print("JavaScript" not in languages)   # True


# ===========================================
# 9. Iterating Through a Set
# ===========================================

languages = {"Python", "Java", "C++"}

for language in languages:
    print(language)

# Output order may vary:
# Python
# Java
# C++


# ===========================================
# 10. Sets Do Not Support Indexing
# ===========================================

numbers = {10, 20, 30}

# print(numbers[0])

# TypeError:
# 'set' object is not subscriptable


# ===========================================
# 11. Checking Length
# ===========================================

numbers = {10, 20, 30, 40}

print(len(numbers))                    # 4


# ===========================================
# 12. Sets are Mutable
# ===========================================

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
# {10, 20, 30, 40}
# Output order may vary.


# ===========================================
# 13. Removing an Element
# ===========================================

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
# {10, 30}


# ===========================================
# 14. Set Union
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a | set_b

print(result)
# {1, 2, 3, 4, 5}


# ===========================================
# 15. Set Intersection
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a & set_b

print(result)
# {3}


# ===========================================
# 16. Set Difference
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a - set_b

print(result)
# {1, 2}


# ===========================================
# 17. Symmetric Difference
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a ^ set_b

print(result)
# {1, 2, 4, 5}


# ===========================================
# 18. Subset
# ===========================================

small_set = {1, 2}
large_set = {1, 2, 3, 4}

print(small_set.issubset(large_set))   # True


# ===========================================
# 19. Superset
# ===========================================

small_set = {1, 2}
large_set = {1, 2, 3, 4}

print(large_set.issuperset(small_set)) # True


# ===========================================
# 20. Disjoint Sets
# ===========================================

set_a = {1, 2, 3}
set_b = {4, 5, 6}

print(set_a.isdisjoint(set_b))         # True


# ===========================================
# 21. Comparing Sets
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 2, 1}

print(set_a == set_b)                  # True


# ===========================================
# 22. Set with Mixed Immutable Types
# ===========================================

data = {
    10,
    "Python",
    3.14,
    True,
    (1, 2)
}

print(data)
# Output order may vary.


# ===========================================
# 23. Mutable Elements Cannot Be Set Members
# ===========================================

# numbers = {[1, 2], [3, 4]}

# TypeError: unhashable type: 'list'

# Lists cannot be elements of a set because
# lists are mutable.


# ===========================================
# 24. Tuple as a Set Element
# ===========================================

data = {
    (1, 2),
    (3, 4)
}

print(data)
# {(1, 2), (3, 4)}
# Output order may vary.


# ===========================================
# 25. Frozenset
# ===========================================

numbers = frozenset([1, 2, 3, 4])

print(numbers)
# frozenset({1, 2, 3, 4})


# ===========================================
# 26. Frozenset is Immutable
# ===========================================

numbers = frozenset([1, 2, 3])

# numbers.add(4)

# AttributeError:
# 'frozenset' object has no attribute 'add'


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Creating Sets
✔ Empty Sets
✔ set() vs {}
✔ Duplicate Removal
✔ Membership Operators
✔ Set Iteration
✔ Set Mutability
✔ Set Length
✔ Set Indexing Limitation
✔ Union
✔ Intersection
✔ Difference
✔ Symmetric Difference
✔ Subsets
✔ Supersets
✔ Disjoint Sets
✔ Set Comparison
✔ Hashable Elements
✔ Frozenset

Key Points
----------
1. Sets contain only unique elements.
2. Sets are unordered collections.
3. Sets do not support indexing or slicing.
4. Sets are mutable.
5. Set elements must be hashable.
6. Lists and dictionaries cannot be set elements.
7. Tuples can be set elements if their contents
   are hashable.
8. {} creates an empty dictionary.
9. set() creates an empty set.
10. frozenset is an immutable version of a set.

Detailed set methods are covered in:
06_set_methods.py
"""