# Dictionary 

# Creating dictionaries
dict1 = {"name": "John", "age": 25, "city": "New York"}
dict2 = dict(key1="value1", key2="value2")

print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")

# Accessing values
print(f"Name: {dict1['name']}")
print(f"Age: {dict1.get('age')}")
print(f"Country (default): {dict1.get('country', 'Not found')}")

# Dictionary length
print(f"Length of dict1: {len(dict1)}")

# Adding/updating elements
dict1["country"] = "USA"
dict1.update({"age": 26, "email": "john@example.com"})
print(f"After updates: {dict1}")

# Removing elements
del dict1["email"]
dict1.pop("country")
print(f"After removals: {dict1}")

# Dictionary methods
print(f"Keys: {dict1.keys()}")
print(f"Values: {dict1.values()}")
print(f"Items: {dict1.items()}")

# Checking if key exists
if "name" in dict1:
    print("Key 'name' exists")

# Iterating through dictionary
for key, value in dict1.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")
