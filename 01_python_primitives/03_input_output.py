"""
Topic: Input and Output in Python

Input:
    Used to accept data from the user.

Output:
    Used to display data on the screen.
"""

# -----------------------------------
# Output using print()
# -----------------------------------

print("Hello, World!")
print(100)
print(3.14)
print(True)


# -----------------------------------
# Printing Multiple Values
# -----------------------------------

name = "Kanishka"
age = 22

print(name, age)


# -----------------------------------
# Using the sep Parameter ---->>>> sep is for spacing between each print 
# -----------------------------------

print("2026", "07", "22", sep="-")
print("Python", "AI", "Workbench", sep=" | ")


# -----------------------------------
# Using the end Parameter
# -----------------------------------

print("Hello", end=" ")
print("World")


# -----------------------------------
# Taking String Input
# -----------------------------------

name = input("Enter your name: ")

print("Hello,", name)


# -----------------------------------
# Taking Integer Input
# -----------------------------------

age = int(input("Enter your age: "))

print("Age:", age)


# -----------------------------------
# Taking Float Input
# -----------------------------------

height = float(input("Enter your height: "))

print("Height:", height)


# -----------------------------------
# Taking Boolean Input
# -----------------------------------
# input() always returns a string.
# One simple approach is to compare
# the input to the expected text.

is_student = input("Are you a student? (True/False): ") == "True"

print(is_student)


# -----------------------------------
# Taking Multiple Inputs
# -----------------------------------

a, b = input("Enter two numbers: ").split()

print(a)#--->type===string
print(b)


# -----------------------------------
# Multiple Integer Inputs----->needed for multiple input values.
# -----------------------------------

x, y = map(int, input("Enter two integers: ").split())#originally taken as string split takes them as integer and stores it in list 

print(x)#-->map convert the string to desired input
print(y)


# -----------------------------------
# Reading a List of Integers
# -----------------------------------

numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)


# -----------------------------------
# Escape Characters
# -----------------------------------

print("Hello\nWorld")
print("Python\tProgramming")
print("She said, \"Hello\"")
print("C:\\Users\\Kanishka")


# -----------------------------------
# Printing Variables
# -----------------------------------

language = "Python"

print("Language:", language)


# -----------------------------------
# Type of User Input
# -----------------------------------

value = input("Enter something: ")

print(type(value))