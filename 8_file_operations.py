# File Operations

# Writing to a file
print("Writing to file...")
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file!\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

print("File written successfully!")

# Reading from a file
print("\nReading from file...")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("\nReading line by line...")
with open("example.txt", "r") as file:
    for line in file:
        print(f"Line: {line.strip()}")

# Appending to a file
print("\nAppending to file...")
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

print("File appended successfully!")

# Reading all lines into a list
print("\nReading all lines as list...")
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# File information
import os
print("\nFile Information...")
if os.path.exists("example.txt"):
    file_size = os.path.getsize("example.txt")
    print(f"File exists: Yes")
    print(f"File size: {file_size} bytes")
else:
    print("File does not exist")

# Copying a file
import shutil
print("\nCopying file...")
shutil.copy("example.txt", "example_copy.txt")
print("File copied successfully!")

# Deleting a file
print("\nDeleting files...")
if os.path.exists("example_copy.txt"):
    os.remove("example_copy.txt")
    print("File deleted successfully!")

# Working with different file modes
print("\nFile modes examples:")
print("'r'  - Read mode (default)")
print("'w'  - Write mode (overwrites existing content)")
print("'a'  - Append mode")
print("'x'  - Exclusive creation mode")
print("'b'  - Binary mode")
print("'t'  - Text mode (default)")

# Clean up
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("\nCleanup: example.txt deleted")
