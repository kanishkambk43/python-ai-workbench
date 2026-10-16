"""
===========================================
Python Sys Module
===========================================

The sys module provides access to Python
interpreter settings and system information.
"""

import sys

# ===========================================
# 1. Python Version
# ===========================================

print(sys.version)                     # Displays the installed Python version

# ===========================================
# 2. Python Version Information
# ===========================================

print(sys.version_info.major)          # Displays the Python major version: Depends on installation

# ===========================================
# 3. Platform Information
# ===========================================

print(sys.platform)                    # Displays the operating system platform

# ===========================================
# 4. Command-Line Arguments
# ===========================================

print(sys.argv)                        # Displays arguments passed when running the script

# ===========================================
# 5. Number of Command-Line Arguments
# ===========================================

print(len(sys.argv))                   # Counts the script name and additional arguments

# ===========================================
# 6. Python Module Search Paths
# ===========================================

print(sys.path)                        # Displays directories Python searches for modules

# ===========================================
# 7. Maximum Integer Size
# ===========================================

print(sys.maxsize)                     # Displays the platform's maximum Py_ssize_t value

# ===========================================
# 8. Standard Output
# ===========================================

sys.stdout.write("Hello from Python!\n")  # Writes text directly to standard output

# ===========================================
# 9. Standard Error
# ===========================================

sys.stderr.write("This is an error message!\n")  # Writes a message to standard error

# ===========================================
# 10. Exit the Program
# ===========================================

# sys.exit()                           # Stops the program immediately when executed

# ===========================================
# Summary
# ===========================================

"""
Covered:
1. sys.version
2. sys.version_info
3. sys.platform
4. sys.argv
5. len(sys.argv)
6. sys.path
7. sys.maxsize
8. sys.stdout
9. sys.stderr
10. sys.exit()
"""