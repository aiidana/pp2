import os

def check_access(path):
    if os.path.exists(path):
        print(f"{path} exists.")
        if os.access(path, os.R_OK):
            print(f"{path} is readable.")
        else:
            print(f"{path} is not readable.")
        if os.access(path, os.W_OK):
            print(f"{path} is writable.")
        else:
            print(f"{path} is not writable.")
        if os.access(path, os.X_OK):
            print(f"{path} is executable.")
        else:
            print(f"{path} is not executable.")
    else:
        print(f"{path} does not exist.")

path = input("Enter a path: ")
check_access(path)

"""
Enter a path: C:\Users\John\Documents
C:\Users\John\Documents exists.
C:\Users\John\Documents is readable.
C:\Users\John\Documents is writable.
C:\Users\John\Documents is executable.
"""