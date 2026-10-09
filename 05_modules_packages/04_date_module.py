"""
===========================================
Python DateTime Module
===========================================

The datetime module is used to work with
dates, times, and date calculations.
"""

from datetime import datetime, date, timedelta

# ===========================================
# 1. datetime.now()
# ===========================================

print(datetime.now())                  # Returns the current local date and time: Current date/time

# ===========================================
# 2. date.today()
# ===========================================

print(date.today())                    # Returns today's date: Current date

# ===========================================
# 3. Creating a Date
# ===========================================

my_date = date(2025, 1, 15)
print(my_date)                         # Creates a specific date: 2025-01-15

# ===========================================
# 4. Creating a DateTime
# ===========================================

my_datetime = datetime(2025, 1, 15, 10, 30)
print(my_datetime)                     # Creates a specific date and time: 2025-01-15 10:30:00

# ===========================================
# 5. Accessing Date Components
# ===========================================

print(my_date.year, my_date.month, my_date.day)  # Gets year, month, and day: 2025 1 15

# ===========================================
# 6. Accessing Time Components
# ===========================================

print(my_datetime.hour, my_datetime.minute)       # Gets hour and minute: 10 30

# ===========================================
# 7. strftime()
# ===========================================

print(my_date.strftime("%d-%m-%Y"))     # Formats a date as day-month-year: 15-01-2025

# ===========================================
# 8. strptime()
# ===========================================

converted = datetime.strptime("15-01-2025", "%d-%m-%Y")
print(converted)                        # Converts a string into datetime: 2025-01-15 00:00:00

# ===========================================
# 9. Adding Days with timedelta
# ===========================================

new_date = my_date + timedelta(days=7)
print(new_date)                         # Adds 7 days to the date: 2025-01-22

# ===========================================
# 10. Subtracting Days with timedelta
# ===========================================

old_date = my_date - timedelta(days=5)
print(old_date)                         # Subtracts 5 days from the date: 2025-01-10

# ===========================================
# Summary
# ===========================================

"""
Covered:
1. datetime.now()
2. date.today()
3. Creating dates
4. Creating datetime objects
5. Date components
6. Time components
7. strftime()
8. strptime()
9. timedelta addition
10. timedelta subtraction
"""