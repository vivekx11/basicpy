# Loop Operations

# While loop
print("=== While Loop ===")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# For loop with range
print("\n=== For Loop with range ===")
for i in range(5):
    print(f"i = {i}")

# For loop with range(start, stop, step)
print("\n=== For Loop with range(start, stop, step) ===")
for i in range(1, 10, 2):
    print(f"i = {i}")

# For loop with list
print("\n=== For Loop with List ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# For loop with enumerate
print("\n=== For Loop with enumerate ===")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# For loop with dictionary
print("\n=== For Loop with Dictionary ===")
person = {"name": "John", "age": 25, "city": "NYC"}
for key, value in person.items():
    print(f"{key}: {value}")

# Nested loops
print("\n=== Nested Loops ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()

# Break and continue
print("\n=== Break and Continue ===")
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i, end=" ")

# For-else loop
print("\n\n=== For-Else Loop ===")
for i in range(5):
    print(i)
else:
    print("Loop completed")

# While-else loop
print("\n=== While-Else Loop ===")
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("While loop completed")
