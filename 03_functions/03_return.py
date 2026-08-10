"""
===========================================
Python return Statement
===========================================

The return statement is used to send a value
from a function back to the place where the
function was called.

A function can return:
- A single value
- Multiple values
- Different data types
- No value explicitly
"""

# ===========================================
# 1. Basic return Statement
# ===========================================

def add(a, b):
    return a + b

result = add(10, 20)

print(result)                       # 30


# ===========================================
# 2. return vs print
# ===========================================

def add_with_print(a, b):
    print(a + b)

def add_with_return(a, b):
    return a + b

add_with_print(10, 20)              # 30

result = add_with_return(10, 20)

print(result)                       # 30


# ===========================================
# 3. Using Returned Value in an Expression
# ===========================================

def square(number):
    return number * number

result = square(5) + 10

print(result)                       # 35


# ===========================================
# 4. Returning Multiple Values
# ===========================================

def calculate(a, b):
    return a + b, a - b

result = calculate(20, 10)

print(result)                       # (30, 10)


# ===========================================
# 5. Unpacking Multiple Return Values
# ===========================================

def operations(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = operations(10, 5)

print(addition)                     # 15
print(subtraction)                  # 5
print(multiplication)               # 50


# ===========================================
# 6. Returning Different Data Types
# ===========================================

def get_name():
    return "Kanishka"

def get_age():
    return 22

def get_skills():
    return ["Python", "SQL", "React"]

print(get_name())                   # Kanishka
print(get_age())                    # 22
print(get_skills())                 # ['Python', 'SQL', 'React']


# ===========================================
# 7. Returning a Dictionary
# ===========================================

def get_student():
    return {
        "name": "Kanishka",
        "age": 22,
        "course": "ISE"
    }

student = get_student()

print(student)                      # {'name': 'Kanishka', 'age': 22, 'course': 'ISE'}


# ===========================================
# 8. return Ends Function Execution
# ===========================================

def check_number(number):

    if number > 0:
        return "Positive"

    print("This line executes only for zero or negative values.")

    return "Not Positive"

result = check_number(10)

print(result)                       # Positive


# ===========================================
# 9. Multiple return Statements
# ===========================================

def check_age(age):

    if age >= 18:
        return "Adult"

    return "Minor"

print(check_age(22))                # Adult
print(check_age(15))                # Minor


# ===========================================
# 10. Conditional return
# ===========================================

def get_status(age):

    if age >= 18:
        return "Eligible"

    return "Not Eligible"

print(get_status(20))               # Eligible
print(get_status(16))               # Not Eligible


# ===========================================
# 11. Returning None
# ===========================================

def display_message():
    print("Hello")

result = display_message()

print(result)                       # Hello
                                    # None


# ===========================================
# 12. Explicit return None
# ===========================================

def no_value():
    return None

result = no_value()

print(result)                       # None
print(type(result))                 # <class 'NoneType'>


# ===========================================
# 13. Returning a Boolean
# ===========================================

def is_even(number):
    return number % 2 == 0

print(is_even(10))                  # True
print(is_even(7))                   # False


# ===========================================
# 14. Returning from a Loop
# ===========================================

def find_number(numbers, target):

    for number in numbers:

        if number == target:
            return True

    return False


numbers = [10, 20, 30, 40]

print(find_number(numbers, 30))     # True
print(find_number(numbers, 50))     # False


# ===========================================
# 15. Returning from Nested Conditions
# ===========================================

def login(username, password):

    if username == "admin":

        if password == "python123":
            return "Login Successful"

        return "Incorrect Password"

    return "Invalid Username"


print(login("admin", "python123"))   # Login Successful
print(login("admin", "wrong"))      # Incorrect Password
print(login("user", "python123"))   # Invalid Username


# ===========================================
# 16. Function Returning Another Function
# ===========================================

def create_multiplier():

    def multiply(number):
        return number * 2

    return multiply


double = create_multiplier()

print(double(5))                    # 10


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Basic return statement
✔ return vs print()
✔ Using returned values
✔ Multiple return values
✔ Value unpacking
✔ Returning different data types
✔ Returning dictionaries
✔ return and function execution
✔ Multiple return statements
✔ Conditional return
✔ Returning None
✔ Returning Boolean values
✔ Returning from loops
✔ Returning from nested conditions
✔ Returning a function

Key Points
----------
1. return sends a value back to the caller.
2. return immediately terminates the function.
3. A function can return multiple values.
4. Multiple returned values are packed into a tuple.
5. A function without an explicit return returns None.
6. return is different from print().
"""