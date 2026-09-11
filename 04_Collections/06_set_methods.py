"""
===========================================
Python Set Methods
===========================================

Set methods are used to add, remove, combine,
and compare elements in sets.

Sets are mutable, so many set methods modify
the original set.
"""


# ===========================================
# 1. add()
# ===========================================

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)                         # {10, 20, 30, 40}


# ===========================================
# 2. add() with Existing Element
# ===========================================

numbers = {10, 20, 30}

numbers.add(20)

print(numbers)                         # {10, 20, 30}

# Sets do not allow duplicate elements.


# ===========================================
# 3. update()
# ===========================================

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)                         # {10, 20, 30, 40, 50, 60}


# ===========================================
# 4. update() with Another Set
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

set_a.update(set_b)

print(set_a)                           # {1, 2, 3, 4, 5}


# ===========================================
# 5. remove()
# ===========================================

numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)                         # {10, 30, 40}


# ===========================================
# 6. remove() with Missing Element
# ===========================================

numbers = {10, 20, 30}

# numbers.remove(50)

# KeyError: 50

# remove() raises KeyError if the element
# does not exist.


# ===========================================
# 7. discard()
# ===========================================

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)                         # {10, 30}


# ===========================================
# 8. discard() with Missing Element
# ===========================================

numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)                         # {10, 20, 30}

# discard() does not raise an error if
# the element does not exist.


# ===========================================
# 9. pop()
# ===========================================

numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)                         # Output may vary: 10, 20, or 30
print(numbers)                         # Remaining elements vary

# Sets are unordered, so pop() removes
# an arbitrary element.


# ===========================================
# 10. clear()
# ===========================================

numbers = {10, 20, 30}

numbers.clear()

print(numbers)                         # set()


# ===========================================
# 11. copy()
# ===========================================

numbers = {10, 20, 30}

new_numbers = numbers.copy()

new_numbers.add(40)

print(numbers)                         # {10, 20, 30}
print(new_numbers)                     # {10, 20, 30, 40}


# ===========================================
# 12. union()
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a.union(set_b)

print(result)                           # {1, 2, 3, 4, 5}


# ===========================================
# 13. Union with Multiple Sets
# ===========================================

set_a = {1, 2}
set_b = {3, 4}
set_c = {5, 6}

result = set_a.union(set_b, set_c)

print(result)                           # {1, 2, 3, 4, 5, 6}


# ===========================================
# 14. intersection()
# ===========================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.intersection(set_b)

print(result)                           # {3, 4}


# ===========================================
# 15. difference()
# ===========================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.difference(set_b)

print(result)                           # {1, 2}


# ===========================================
# 16. Reverse Difference
# ===========================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_b.difference(set_a)

print(result)                           # {5, 6}


# ===========================================
# 17. symmetric_difference()
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

result = set_a.symmetric_difference(set_b)

print(result)                           # {1, 2, 4, 5}


# ===========================================
# 18. intersection_update()
# ===========================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

set_a.intersection_update(set_b)

print(set_a)                           # {3, 4}


# ===========================================
# 19. difference_update()
# ===========================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

set_a.difference_update(set_b)

print(set_a)                           # {1, 2}


# ===========================================
# 20. symmetric_difference_update()
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

set_a.symmetric_difference_update(set_b)

print(set_a)                           # {1, 2, 4, 5}


# ===========================================
# 21. issubset()
# ===========================================

small_set = {1, 2}
large_set = {1, 2, 3, 4}

print(small_set.issubset(large_set))   # True
print(large_set.issubset(small_set))   # False


# ===========================================
# 22. issuperset()
# ===========================================

small_set = {1, 2}
large_set = {1, 2, 3, 4}

print(large_set.issuperset(small_set)) # True
print(small_set.issuperset(large_set)) # False


# ===========================================
# 23. isdisjoint()
# ===========================================

set_a = {1, 2, 3}
set_b = {4, 5, 6}

print(set_a.isdisjoint(set_b))         # True


set_c = {3, 4, 5}

print(set_a.isdisjoint(set_c))         # False


# ===========================================
# 24. Using Operators with Set Methods
# ===========================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)                   # {1, 2, 3, 4, 5}
print(set_a & set_b)                   # {3}
print(set_a - set_b)                   # {1, 2}
print(set_a ^ set_b)                   # {1, 2, 4, 5}


# ===========================================
# 25. Set Operations with Strings
# ===========================================

python_skills = {"Python", "SQL", "Git"}
web_skills = {"HTML", "CSS", "Git"}

print(python_skills.union(web_skills))
# {'Python', 'SQL', 'Git', 'HTML', 'CSS'}

print(python_skills.intersection(web_skills))
# {'Git'}


# ===========================================
# 26. Practical Example - Common Students
# ===========================================

python_students = {"Aman", "Rahul", "Kanishka"}
sql_students = {"Kanishka", "Rahul", "Priya"}

common_students = python_students.intersection(sql_students)

print(common_students)
# {'Rahul', 'Kanishka'}
# Output order may vary.


# ===========================================
# 27. Practical Example - Unique Students
# ===========================================

students_a = {"Aman", "Rahul", "Kanishka"}
students_b = {"Kanishka", "Priya", "Arjun"}

all_students = students_a.union(students_b)

print(all_students)
# {'Aman', 'Rahul', 'Kanishka', 'Priya', 'Arjun'}
# Output order may vary.


# ===========================================
# 28. Practical Example - Students in Only A
# ===========================================

students_a = {"Aman", "Rahul", "Kanishka"}
students_b = {"Kanishka", "Priya", "Arjun"}

only_a = students_a.difference(students_b)

print(only_a)
# {'Aman', 'Rahul'}
# Output order may vary.


# ===========================================
# Summary
# ===========================================

"""
Set Methods Covered
-------------------
✔ add()
✔ update()
✔ remove()
✔ discard()
✔ pop()
✔ clear()
✔ copy()

Set Operation Methods
---------------------
✔ union()
✔ intersection()
✔ difference()
✔ symmetric_difference()

Update Methods
--------------
✔ intersection_update()
✔ difference_update()
✔ symmetric_difference_update()

Relationship Methods
--------------------
✔ issubset()
✔ issuperset()
✔ isdisjoint()

Key Points
----------
1. add() adds one element.
2. update() adds multiple elements.
3. remove() raises KeyError if the element
   does not exist.
4. discard() does not raise an error if the
   element does not exist.
5. pop() removes an arbitrary element because
   sets are unordered.
6. clear() removes all elements.
7. copy() creates a separate set.
8. union() combines sets.
9. intersection() finds common elements.
10. difference() finds elements present only
    in the first set.
11. symmetric_difference() finds elements
    present in either set but not both.
12. The *_update() methods modify the
    original set.
13. issubset() checks whether all elements
    exist in another set.
14. issuperset() checks whether a set contains
    all elements of another set.
15. isdisjoint() checks whether two sets have
    no common elements.
"""