"""
===========================================
Python OS Module
===========================================

The os module allows Python to interact
with the operating system.
"""

import os

# ===========================================
# 1. Current Working Directory
# ===========================================

print(os.getcwd())                     # Shows the current working directory

# ===========================================
# 2. List Files and Folders
# ===========================================

print(os.listdir())                    # Lists files and folders in the current directory

# ===========================================
# 3. Create a Folder
# ===========================================

os.mkdir("demo_folder")                # Creates a new folder named demo_folder

# ===========================================
# 4. Check if Path Exists
# ===========================================

print(os.path.exists("demo_folder"))   # Checks whether the folder exists: True

# ===========================================
# 5. Check if Path is a File
# ===========================================

print(os.path.isfile("demo.txt"))      # Checks whether demo.txt is a file: False

# ===========================================
# 6. Check if Path is a Directory
# ===========================================

print(os.path.isdir("demo_folder"))    # Checks whether demo_folder is a directory: True

# ===========================================
# 7. Join Paths
# ===========================================

path = os.path.join("demo_folder", "test.txt")
print(path)                            # Joins folder and filename into one path: demo_folder\test.txt

# ===========================================
# 8. Get File Name
# ===========================================

print(os.path.basename(path))           # Extracts the file name: test.txt

# ===========================================
# 9. Get Directory Name
# ===========================================

print(os.path.dirname(path))            # Extracts the directory name: demo_folder

# ===========================================
# 10. Rename a Folder
# ===========================================

os.rename("demo_folder", "new_folder")  # Renames demo_folder to new_folder

# ===========================================
# Summary
# ===========================================

"""
Covered:
1. getcwd()
2. listdir()
3. mkdir()
4. exists()
5. isfile()
6. isdir()
7. join()
8. basename()
9. dirname()
10. rename()
"""