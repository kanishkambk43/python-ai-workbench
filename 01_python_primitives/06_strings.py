"""
===========================================
Python Strings
===========================================

A string is a sequence of characters enclosed
within single quotes (' '), double quotes (" "),
or triple quotes (''' ''' or """ """).

Strings are:
✔ Ordered
✔ Immutable
✔ Iterable
"""

# ===========================================
# 1. Creating Strings
# ===========================================

single_quote = 'Hello'
double_quote = "Python"
triple_quote = """Welcome to Python Programming"""

print(single_quote)
print(double_quote)
print(triple_quote)

# ===========================================
# 2. String Type
# ===========================================

language = "Python"

print(type(language))

# ===========================================
# 3. Empty String
# ===========================================

empty = ""

print(empty)
print(len(empty))

# ===========================================
# 4. Accessing Characters (Indexing)
# ===========================================

text = "Python"

print(text[0])      # P
print(text[1])      # y
print(text[-1])     # n
print(text[-2])     # o

# ===========================================
# 5. String Slicing
# ===========================================

word = "Programming"

print(word[0:6])     # Progra
print(word[3:8])     # gramm
print(word[:5])      # Progr
print(word[5:])      # amming
print(word[-4:])     # ming

# ===========================================
# 6. String Length
# ===========================================

name = "Kanishka"

print(len(name))

# ===========================================
# 7. String Concatenation
# ===========================================

first_name = "Kanishka"
last_name = "MBK"

full_name = first_name + " " + last_name

print(full_name)

# ===========================================
# 8. String Repetition
# ===========================================

print("Python " * 3)

# ===========================================
# 9. Membership Operators
# ===========================================

language = "Python Programming"

print("Python" in language)
print("Java" in language)
print("Java" not in language)

# ===========================================
# 10. String Comparison
# ===========================================

print("apple" == "apple")
print("apple" == "Apple")
print("cat" > "bat")

# ===========================================
# 11. Strings are Immutable
# ===========================================

text = "Python"

# text[0] = "J"     # ❌ Error

new_text = "J" + text[1:]

print(new_text)

# ===========================================
# 12. Iterating Through a String
# ===========================================

language = "Python"

for char in language:
    print(char)

# ===========================================
# 13. Escape Characters
# ===========================================

print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Python is awesome\"")
print('It\'s a beautiful day.')

# ===========================================
# 14. Multi-line Strings
# ===========================================

message = """
Python
is
easy
to
learn.
"""

print(message)

# ===========================================
# 15. Raw Strings
# ===========================================

path = r"C:\Users\Kanishka\Documents"

print(path)

# ===========================================
# Summary
# ===========================================

"""
Topics Covered:
✔ Creating Strings
✔ String Type
✔ Empty Strings
✔ Indexing
✔ Slicing
✔ Length
✔ Concatenation
✔ Repetition
✔ Membership Operators
✔ Comparison
✔ Immutability
✔ Iteration
✔ Escape Characters
✔ Multi-line Strings
✔ Raw Strings

String methods such as:
.upper()
.lower()
.strip()
.replace()
.find()
.split()
.join()
.startswith()
.endswith()

are covered in:
07_string_methods.py
"""