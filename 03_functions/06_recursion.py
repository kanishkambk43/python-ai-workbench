"""
===========================================
Python Recursion
===========================================

Recursion is a technique where a function
calls itself to solve a problem.

Every recursive function should have:

1. Base Case
   -> Stops the recursion.

2. Recursive Case
   -> Calls the function again with
      a smaller or simpler problem.

Syntax:

def function():
    if base_condition:
        return
    function()
"""


# ===========================================
# 1. Basic Recursion
# ===========================================

def countdown(number):

    if number == 0:
        return

    print(number)
    countdown(number - 1)


countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1


# ===========================================
# 2. Recursion with a Base Case
# ===========================================

def count_up(number):

    if number > 5:
        return

    print(number)
    count_up(number + 1)


count_up(1)

# Output:
# 1
# 2
# 3
# 4
# 5


# ===========================================
# 3. Factorial Using Recursion
# ===========================================

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))                  # 120


# ===========================================
# 4. Sum of Natural Numbers
# ===========================================

def natural_sum(number):

    if number == 0:
        return 0

    return number + natural_sum(number - 1)


print(natural_sum(5))                # 15


# ===========================================
# 5. Power Using Recursion
# ===========================================

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print(power(2, 5))                   # 32


# ===========================================
# 6. Fibonacci Using Recursion
# ===========================================

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(7))                  # 13


# ===========================================
# 7. Print Fibonacci Sequence
# ===========================================

def print_fibonacci(number, a=0, b=1):

    if number == 0:
        return

    print(a)

    print_fibonacci(number - 1, b, a + b)


print_fibonacci(6)

# Output:
# 0
# 1
# 1
# 2
# 3
# 5


# ===========================================
# 8. Reverse a String Using Recursion
# ===========================================

def reverse_string(text):

    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


print(reverse_string("Python"))       # nohtyP


# ===========================================
# 9. Check Palindrome Using Recursion
# ===========================================

def is_palindrome(text):

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


print(is_palindrome("level"))         # True
print(is_palindrome("python"))        # False


# ===========================================
# 10. Find Maximum in a List
# ===========================================

def find_max(numbers, index=0):

    if index == len(numbers) - 1:
        return numbers[index]

    maximum = find_max(numbers, index + 1)

    if numbers[index] > maximum:
        return numbers[index]

    return maximum


numbers = [10, 25, 7, 42, 18]

print(find_max(numbers))              # 42


# ===========================================
# 11. Count Digits Using Recursion
# ===========================================

def count_digits(number):

    number = abs(number)

    if number < 10:
        return 1

    return 1 + count_digits(number // 10)


print(count_digits(12345))            # 5


# ===========================================
# 12. Sum of Digits
# ===========================================

def sum_digits(number):

    number = abs(number)

    if number == 0:
        return 0

    return (number % 10) + sum_digits(number // 10)


print(sum_digits(12345))              # 15


# ===========================================
# 13. Greatest Common Divisor (GCD)
# ===========================================

def gcd(a, b):

    if b == 0:
        return abs(a)

    return gcd(b, a % b)


print(gcd(48, 18))                    # 6


# ===========================================
# 14. Recursion Without a Base Case
# ===========================================

# WARNING:
# Never run a recursive function without
# a condition that eventually stops it.

# def infinite_recursion():
#     infinite_recursion()

# infinite_recursion()

# This eventually raises:
# RecursionError: maximum recursion depth exceeded


# ===========================================
# 15. Understanding the Call Stack
# ===========================================

def show_numbers(number):

    if number == 0:
        return

    print(f"Calling: {number}")
    show_numbers(number - 1)
    print(f"Returning: {number}")


show_numbers(3)

# Output:
# Calling: 3
# Calling: 2
# Calling: 1
# Returning: 1
# Returning: 2
# Returning: 3


# ===========================================
# 16. Recursion vs Iteration
# ===========================================

# Recursive approach

def recursive_sum(number):

    if number == 0:
        return 0

    return number + recursive_sum(number - 1)


print(recursive_sum(5))               # 15


# Iterative approach

def iterative_sum(number):

    total = 0

    for i in range(1, number + 1):
        total += i

    return total


print(iterative_sum(5))               # 15


# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Recursion
✔ Base Case
✔ Recursive Case
✔ Countdown
✔ Factorial
✔ Sum of Natural Numbers
✔ Power Calculation
✔ Fibonacci Sequence
✔ String Reversal
✔ Palindrome Checking
✔ Finding Maximum
✔ Counting Digits
✔ Sum of Digits
✔ GCD
✔ RecursionError
✔ Call Stack
✔ Recursion vs Iteration

Key Points
----------
1. Recursion means a function calls itself.
2. Every recursive solution needs a base case.
3. The base case prevents infinite recursion.
4. Each recursive call should move toward the base case.
5. Too many recursive calls can cause a RecursionError.
6. Recursion is useful for problems that can be
   divided into smaller versions of the same problem.
7. Recursion is not always better than iteration.
"""