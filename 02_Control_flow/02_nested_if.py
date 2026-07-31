"""
===========================================
Python Nested if Statement
===========================================

A nested if statement is an if statement
inside another if statement.

It is used when multiple conditions must
be checked in sequence.

Syntax:

if condition1:
    if condition2:
        # Code
    else:
        # Code
else:
    # Code
"""

# ===========================================
# 1. Basic Nested if
# ===========================================

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")                 # You can drive.
    else:
        print("You need a driving license.")
else:
    print("You are underage.")

# ===========================================
# 2. Student Eligibility
# ===========================================

marks = 85
attendance = 92

if marks >= 40:
    if attendance >= 75:
        print("Eligible for Examination.")      # Eligible for Examination.
    else:
        print("Attendance is too low.")
else:
    print("Insufficient Marks.")

# ===========================================
# 3. Login Authentication
# ===========================================

username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login Successful.")              # Login Successful.
    else:
        print("Incorrect Password.")
else:
    print("Invalid Username.")

# ===========================================
# 4. ATM Withdrawal
# ===========================================

balance = 5000
withdraw_amount = 2000

if balance >= withdraw_amount:
    if withdraw_amount > 0:
        print("Transaction Successful.")        # Transaction Successful.
    else:
        print("Invalid Amount.")
else:
    print("Insufficient Balance.")

# ===========================================
# 5. Online Shopping
# ===========================================

is_logged_in = True
has_payment_method = True

if is_logged_in:
    if has_payment_method:
        print("Order Placed Successfully.")     # Order Placed Successfully.
    else:
        print("Add a Payment Method.")
else:
    print("Please Login.")

# ===========================================
# 6. Scholarship Eligibility
# ===========================================

cgpa = 8.5
income = 180000

if cgpa >= 8.0:
    if income < 300000:
        print("Scholarship Approved.")          # Scholarship Approved.
    else:
        print("Income Limit Exceeded.")
else:
    print("CGPA Requirement Not Met.")

# ===========================================
# 7. Age and Citizenship Check
# ===========================================

age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote.")              # Eligible to Vote.
    else:
        print("Must be a Citizen.")
else:
    print("Underage.")

# ===========================================
# 8. File Access Permission
# ===========================================

is_admin = True
has_permission = True

if is_admin:
    if has_permission:
        print("Access Granted.")                # Access Granted.
    else:
        print("Permission Denied.")
else:
    print("Administrator Access Required.")

# ===========================================
# 9. Weather Decision
# ===========================================

is_raining = True
has_umbrella = True

if is_raining:
    if has_umbrella:
        print("Go Outside.")                    # Go Outside.
    else:
        print("Stay Indoors.")
else:
    print("Enjoy the Weather.")

# ===========================================
# 10. Nested if with Three Levels
# ===========================================

username = "admin"
password = "1234"
otp = 567890

if username == "admin":
    if password == "1234":
        if otp == 567890:
            print("Authentication Successful.") # Authentication Successful.
        else:
            print("Invalid OTP.")
    else:
        print("Incorrect Password.")
else:
    print("Invalid Username.")

# ===========================================
# Summary
# ===========================================

"""
Topics Covered
--------------
✔ Nested if Statement
✔ Multiple Condition Checking
✔ Login Authentication
✔ ATM Transaction
✔ Scholarship Eligibility
✔ File Permission
✔ Weather Decision
✔ Three-Level Nested if

Note:
Use nested if statements only when one
condition depends on another. Excessive
nesting can make code difficult to read.
"""