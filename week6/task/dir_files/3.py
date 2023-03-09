import os

def check_path(path):
    if os.path.exists(path):
        print(f"{path} exists.")
        dirname, filename = os.path.split(path)
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"{path} does not exist.")

path = input("Enter a path: ")
check_path(path)



"""
We then define a function called check_path that takes a path as input. We use the os.path.exists() function to check if the path exists. If it exists, we use the os.path.split() function to get the directory and filename portions of the path.

The os.path.split() function takes a path as input and returns a tuple containing the directory and filename portions of the path.
"""

