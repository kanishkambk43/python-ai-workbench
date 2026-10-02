"""
===========================================
Python Dictionary Methods
===========================================

Dictionary methods are used to access, add,
update, remove, and manipulate key-value pairs.

Main methods covered:
    get()
    keys()
    values()
    items()
    update()
    pop()
    popitem()
    setdefault()
    fromkeys()
    clear()
    copy()
"""


# ===========================================
# 1. get()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student.get("name"))                  # Kanishka
print(student.get("age"))                   # 22


# ===========================================
# 2. get() with a Missing Key
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

print(student.get("email"))                 # None


# ===========================================
# 3. get() with a Default Value
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

print(student.get("email", "Not Found"))    # Not Found


# ===========================================
# 4. keys()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student.keys())                       # dict_keys(['name', 'age', 'course'])


# ===========================================
# 5. Loop Through keys()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

for key in student.keys():
    print(key)

# name
# age
# course


# ===========================================
# 6. values()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student.values())                     # dict_values(['Kanishka', 22, 'Python'])


# ===========================================
# 7. Loop Through values()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

for value in student.values():
    print(value)

# Kanishka
# 22
# Python


# ===========================================
# 8. items()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

print(student.items())
# dict_items([('name', 'Kanishka'), ('age', 22), ('course', 'Python')])


# ===========================================
# 9. Loop Through items()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)

# name : Kanishka
# age : 22
# course : Python


# ===========================================
# 10. update()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

student.update({"course": "Python"})

print(student)                              # {'name': 'Kanishka', 'age': 22, 'course': 'Python'}


# ===========================================
# 11. update() Existing Key
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

student.update({"age": 23})

print(student)                              # {'name': 'Kanishka', 'age': 23}


# ===========================================
# 12. update() Multiple Values
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

student.update({
    "age": 23,
    "course": "Python",
    "city": "Mysuru"
})

print(student)
# {'name': 'Kanishka', 'age': 23,
#  'course': 'Python', 'city': 'Mysuru'}


# ===========================================
# 13. update() Using Keyword Arguments
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

student.update(course="Python", city="Mysuru")

print(student)
# {'name': 'Kanishka', 'age': 22,
#  'course': 'Python', 'city': 'Mysuru'}


# ===========================================
# 14. pop()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

removed_value = student.pop("age")

print(removed_value)                         # 22
print(student)                              # {'name': 'Kanishka', 'course': 'Python'}


# ===========================================
# 15. pop() with Default Value
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

result = student.pop("email", "Not Found")

print(result)                               # Not Found
print(student)                              # {'name': 'Kanishka', 'age': 22}


# ===========================================
# 16. pop() with Missing Key
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

# student.pop("email")

# KeyError: 'email'


# ===========================================
# 17. popitem()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

item = student.popitem()

print(item)                                 # ('course', 'Python')
print(student)                              # {'name': 'Kanishka', 'age': 22}

# popitem() removes and returns the last
# inserted key-value pair.


# ===========================================
# 18. clear()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22,
    "course": "Python"
}

student.clear()

print(student)                              # {}


# ===========================================
# 19. copy()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

new_student = student.copy()

new_student["age"] = 23

print(student)                              # {'name': 'Kanishka', 'age': 22}
print(new_student)                          # {'name': 'Kanishka', 'age': 23}


# ===========================================
# 20. setdefault()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

result = student.setdefault("course", "Python")

print(result)                               # Python
print(student)                              # {'name': 'Kanishka', 'age': 22, 'course': 'Python'}


# ===========================================
# 21. setdefault() with Existing Key
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

result = student.setdefault("age", 30)

print(result)                               # 22
print(student)                              # {'name': 'Kanishka', 'age': 22}

# Existing values are not replaced.


# ===========================================
# 22. setdefault() Without Default
# ===========================================

student = {
    "name": "Kanishka"
}

result = student.setdefault("age")

print(result)                               # None
print(student)                              # {'name': 'Kanishka', 'age': None}


# ===========================================
# 23. fromkeys()
# ===========================================

keys = ["name", "age", "course"]

student = dict.fromkeys(keys)

print(student)                              # {'name': None, 'age': None, 'course': None}


# ===========================================
# 24. fromkeys() with a Default Value
# ===========================================

keys = ["name", "age", "course"]

student = dict.fromkeys(keys, "Unknown")

print(student)
# {'name': 'Unknown', 'age': 'Unknown', 'course': 'Unknown'}


# ===========================================
# 25. fromkeys() with 0
# ===========================================

subjects = ["Python", "SQL", "Java"]

marks = dict.fromkeys(subjects, 0)

print(marks)                                # {'Python': 0, 'SQL': 0, 'Java': 0}


# ===========================================
# 26. Combining keys() and values()
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

print(list(student.keys()))                 # ['name', 'age']
print(list(student.values()))               # ['Kanishka', 22]


# ===========================================
# 27. Converting items() to a List
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

print(list(student.items()))
# [('name', 'Kanishka'), ('age', 22)]


# ===========================================
# 28. Checking Key Before Access
# ===========================================

student = {
    "name": "Kanishka",
    "age": 22
}

if "name" in student:
    print(student["name"])                  # Kanishka


# ===========================================
# 29. Practical Example - Counting Items
# ===========================================

fruits = {
    "apple": 5,
    "banana": 3,
    "orange": 7
}

print(fruits.get("apple"))                  # 5
print(fruits.get("mango", 0))               # 0


# ===========================================
# 30. Practical Example - Updating Product
# ===========================================

product = {
    "name": "Laptop",
    "price": 75000,
    "stock": 10
}

product.update({
    "price": 70000,
    "stock": 8
})

print(product)
# {'name': 'Laptop', 'price': 70000, 'stock': 8}


# ===========================================
# 31. Practical Example - Remove User Data
# ===========================================

user = {
    "username": "kanishka",
    "email": "user@example.com",
    "age": 22
}

email = user.pop("email")

print(email)                                # user@example.com
print(user)                                 # {'username': 'kanishka', 'age': 22}


# ===========================================
# 32. Practical Example - setdefault()
# ===========================================

student = {
    "name": "Kanishka"
}

student.setdefault("skills", [])

student["skills"].append("Python")
student["skills"].append("SQL")

print(student)
# {'name': 'Kanishka', 'skills': ['Python', 'SQL']}


# ===========================================
# 33. Practical Example - Loop Through Dictionary
# ===========================================

marks = {
    "Python": 90,
    "SQL": 85,
    "Linux": 88
}

for subject, mark in marks.items():
    print(subject, "=", mark)

# Python = 90
# SQL = 85
# Linux = 88


# ===========================================
# 34. Practical Example - Find Total Marks
# ===========================================

marks = {
    "Python": 90,
    "SQL": 85,
    "Linux": 88
}

total = sum(marks.values())

print(total)                                # 263


# ===========================================
# 35. Practical Example - Find Maximum Mark
# ===========================================

marks = {
    "Python": 90,
    "SQL": 85,
    "Linux": 88
}

highest = max(marks.values())

print(highest)                              # 90


# ===========================================
# Summary
# ===========================================

"""
Dictionary Methods Covered
--------------------------
✔ get()
✔ keys()
✔ values()
✔ items()
✔ update()
✔ pop()
✔ popitem()
✔ setdefault()
✔ fromkeys()
✔ clear()
✔ copy()

Important Differences
---------------------

get()
    Safely retrieves a value.

keys()
    Returns dictionary keys.

values()
    Returns dictionary values.

items()
    Returns key-value pairs.

update()
    Adds or updates key-value pairs.

pop()
    Removes a specific key and returns its value.

popitem()
    Removes and returns the last inserted
    key-value pair.

setdefault()
    Returns the value of a key.
    If the key does not exist, it creates it.

fromkeys()
    Creates a new dictionary using given keys.

clear()
    Removes all key-value pairs.

copy()
    Creates a shallow copy of the dictionary.
"""