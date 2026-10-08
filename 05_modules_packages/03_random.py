"""
===========================================
Python Random Module
===========================================

The random module is used to generate
random values and make random selections.
"""

import random


# ===========================================
# 1. random.random()
# ===========================================

print(random.random())                 # Generates a random float between 0.0 and 1.0


# ===========================================
# 2. random.randint()
# ===========================================

print(random.randint(1, 10))           # Generates a random integer from 1 to 10


# ===========================================
# 3. random.randrange()
# ===========================================

print(random.randrange(1, 10))          # Generates a random integer from 1 to 9


# ===========================================
# 4. random.choice()
# ===========================================

fruits = ["Apple", "Banana", "Mango"]

print(random.choice(fruits))            # Selects one random item from the list


# ===========================================
# 5. random.choices()
# ===========================================

colors = ["Red", "Blue", "Green"]

print(random.choices(colors, k=2))      # Selects 2 random items, allowing duplicates


# ===========================================
# 6. random.sample()
# ===========================================

numbers = [1, 2, 3, 4, 5]

print(random.sample(numbers, 2))       # Selects 2 unique random items


# ===========================================
# 7. random.shuffle()
# ===========================================

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)                          # Randomly rearranges the list


# ===========================================
# 8. random.uniform()
# ===========================================

print(random.uniform(1, 5))             # Generates a random float between 1 and 5


# ===========================================
# 9. random.seed()
# ===========================================

random.seed(10)

print(random.randint(1, 100))            # Produces a repeatable random result


# ===========================================
# 10. Practical Example - OTP
# ===========================================

otp = random.randint(1000, 9999)

print(otp)                              # Generates a random 4-digit OTP


# ===========================================
# Summary
# ===========================================

"""
Covered:
1. random()
2. randint()
3. randrange()
4. choice()
5. choices()
6. sample()
7. shuffle()
8. uniform()
9. seed()
10. Practical OTP generation
"""