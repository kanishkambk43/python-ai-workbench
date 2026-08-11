"""
===========================================
Python Lambda Functions
===========================================

A lambda function is a small anonymous function
that can contain only one expression.

Syntax:

lambda arguments: expression

A lambda function:
✔ Has no function name by default
✔ Can accept multiple arguments
✔ Contains only one expression
✔ Automatically returns the result
"""

# ===========================================
# 1. Basic Lambda Function
# ===========================================

square = lambda x: x * x

print(square(5))                       # 25


# ===========================================
# 2. Lambda with Multiple Arguments
# ===========================================

add = lambda a, b: a + b

print(add(10, 20))                     # 30


# ===========================================
# 3. Lambda with Three Arguments
# ===========================================

multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))               # 24


# ===========================================
# 4. Lambda with Conditional Expression
# ===========================================

check_even = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check_even(10))                  # Even
print(check_even(7))                   # Odd


# ===========================================
# 5. Lambda for Finding Maximum
# ===========================================

maximum = lambda a, b: a if a > b else b

print(maximum(25, 40))                 # 40


# ===========================================
# 6. Lambda with Strings
# ===========================================

get_length = lambda text: len(text)

print(get_length("Python"))            # 6


# ===========================================
# 7. Lambda with Default Argument
# ===========================================

greet = lambda name="Guest": f"Hello, {name}"

print(greet())                         # Hello, Guest
print(greet("Kanishka"))               # Hello, Kanishka


# ===========================================
# 8. Lambda as an Argument
# ===========================================

def apply_operation(function, number):
    return function(number)


square = lambda x: x * x

print(apply_operation(square, 6))      # 36


# ===========================================
# 9. Lambda with map()
# ===========================================

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)                         # [1, 4, 9, 16, 25]


# ===========================================
# 10. Lambda with filter()
# ===========================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)                    # [2, 4, 6]


# ===========================================
# 11. Lambda with sorted()
# ===========================================

numbers = [50, 10, 40, 20, 30]

sorted_numbers = sorted(numbers, key=lambda x: x)

print(sorted_numbers)                  # [10, 20, 30, 40, 50]


# ===========================================
# 12. Sorting Strings by Length
# ===========================================

words = ["Python", "AI", "Programming", "SQL"]

sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)
# ['AI', 'SQL', 'Python', 'Programming']


# ===========================================
# 13. Sorting Tuples by Second Value
# ===========================================

students = [
    ("Kanishka", 85),
    ("Rahul", 92),
    ("Aman", 78)
]

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)
# [('Aman', 78), ('Kanishka', 85), ('Rahul', 92)]


# ===========================================
# 14. Lambda with Dictionary Data
# ===========================================

students = [
    {"name": "Kanishka", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Aman", "marks": 78}
]

sorted_students = sorted(
    students,
    key=lambda student: student["marks"]
)

print(sorted_students)
# [{'name': 'Aman', 'marks': 78},
#  {'name': 'Kanishka', 'marks': 85},
#  {'name': 'Rahul', 'marks': 92}]


# ===========================================
# 15. Lambda vs Regular Function
# ===========================================

def square_function(x):
    return x * x


square_lambda = lambda x: x * x

print(square_function(5))               # 25
print(square_lambda(5))                # 25


# ===========================================
# 16. Immediately Invoked Lambda
# ===========================================

result = (lambda x, y: x + y)(10, 20)

print(result)                           # 30


# ===========================================
# 17. Lambda Returning Boolean
# ===========================================

is_positive = lambda x: x > 0

print(is_positive(10))                  # True
print(is_positive(-5))                  # False


# ===========================================
# 18. Lambda with Multiple Conditions
# ===========================================

check_number = lambda x: (
    "Positive" if x > 0
    else "Negative" if x < 0
    else "Zero"
)

print(check_number(10))                 # Positive
print(check_number(-5))                 # Negative
print(check_number(0))                  # Zero


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Lambda Function Syntax
✔ Single Argument Lambda
✔ Multiple Argument Lambda
✔ Conditional Lambda
✔ Default Arguments
✔ Lambda as a Function Argument
✔ Lambda with map()
✔ Lambda with filter()
✔ Lambda with sorted()
✔ Sorting by Key
✔ Lambda with Dictionaries
✔ Lambda vs Regular Functions
✔ Immediately Invoked Lambda

Key Points
----------
1. Lambda functions are anonymous functions.
2. They are defined using the 'lambda' keyword.
3. A lambda can contain only one expression.
4. The result of the expression is returned automatically.
5. Lambda functions are useful for short, simple operations.
6. For complex logic, use a regular 'def' function instead.
"""