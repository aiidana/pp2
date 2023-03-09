import os

def list_all(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"Directory: {item_path}")
        elif os.path.isfile(item_path):
            print(f"File: {item_path}")

def list_directories(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"Directory: {item_path}")

def list_files(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            print(f"File: {item_path}")

path = input("Enter a path: ")
print("All Directories and Files:")
list_all(path)
print("Directories only:")
list_directories(path)
print("Files only:")
list_files(path)

"""
Enter a path: C:\Users\John\Documents
All Directories and Files:
Directory: C:\Users\John\Documents\Folder1
Directory: C:\Users\John\Documents\Folder2
File: C:\Users\John\Documents\file1.txt
File: C:\Users\John\Documents\file2.txt
Directories only:
Directory: C:\Users\John\Documents\Folder1
Directory: C:\Users\John\Documents\Folder2
Files only:
File: C:\Users\John\Documents\file1.txt
File: C:\Users\John\Documents\file2.txt
"""