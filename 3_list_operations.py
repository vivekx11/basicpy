# List 

# Creating lists
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
list3 = [1, "hello", 3.14, True]

# List length
print(f"Length of {list1}: {len(list1)}")

# Accessing elements
print(f"First element: {list1[0]}")
print(f"Last element: {list1[-1]}")
print(f"Index 2: {list1[2]}")

# Slicing
print(f"Slice [1:4]: {list1[1:4]}")

# Adding elements
list1.append(6)
print(f"After append(6): {list1}")

list1.extend([7, 8])
print(f"After extend([7, 8]): {list1}")

list1.insert(0, 0)
print(f"After insert(0, 0): {list1}")

# Removing elements
list1.remove(0)
print(f"After remove(0): {list1}")

popped = list1.pop()
print(f"Popped element: {popped}, List: {list1}")

# Finding elements
list_test = [1, 2, 3, 2, 4]
print(f"Index of 2: {list_test.index(2)}")
print(f"Count of 2: {list_test.count(2)}")

# Sorting and reversing
list_sort = [3, 1, 4, 1, 5]
print(f"Original: {list_sort}")
list_sort.sort()
print(f"Sorted: {list_sort}")
list_sort.reverse()
print(f"Reversed: {list_sort}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")
