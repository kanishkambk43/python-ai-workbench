"""
Topic: Operators in Python

Operators are symbols used to perform operations on variables and values.
"""

# -----------------------------------
# Arithmetic Operators
# -----------------------------------

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# -----------------------------------
# Comparison Operators
# -----------------------------------

x = 10
y = 20

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)


# -----------------------------------
# Assignment Operators
# -----------------------------------

num = 10
print("Initial Value:", num)

num += 5
print("After += :", num)

num -= 3
print("After -= :", num)

num *= 2
print("After *= :", num)

num /= 4
print("After /= :", num)

num //= 2
print("After //= :", num)

num %= 3
print("After %= :", num)

num **= 2
print("After **= :", num)


# -----------------------------------
# Logical Operators
# -----------------------------------

a = True
b = False

print("AND:", a and b)
print("OR :", a or b)
print("NOT:", not a)


# -----------------------------------
# Bitwise Operators
# -----------------------------------

x = 5
y = 3

print("AND:", x & y)
print("OR :", x | y)
print("XOR:", x ^ y)
print("NOT:", ~x)
print("Left Shift:", x << 1)
print("Right Shift:", x >> 1)


# -----------------------------------
# Membership Operators --->>> in, not in
# -----------------------------------

language = "Python"

print("P" in language) # Returns True if the specified value is present in the sequence.
print("Java" not in language)# Returns True if the specified value is not present in the sequence.


numbers = [10, 20, 30]

print(20 in numbers)
print(40 not in numbers)


# -----------------------------------
# Identity Operators ------>>>>> is,is not

#Identity operators are used to check whether two variables refer to the same object in memory, not whether they have the same value.
# -----------------------------------

list1 = [1, 2, 3]
list2 = list1  # does not create a new list
list3 = [1, 2, 3] # create a new list

print(list1 is list2)
print(list1 is list3)

print(list1 is not list3)


# -----------------------------------
# Operator Precedence
# -----------------------------------

result = 10 + 2 * 5

print(result)

result = (10 + 2) * 5

print(result)