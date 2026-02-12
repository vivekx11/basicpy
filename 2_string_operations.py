# String 

# Creating strings
str1 = "Hello"
str2 = "World"

# String concatenation
print(f"Concatenation: {str1} + {str2} = {str1 + ' ' + str2}")

# String repetition
print(f"Repetition: {str1} * 3 = {str1 * 3}")

# String length
print(f"Length of '{str1}': {len(str1)}")

# String indexing
print(f"First character of '{str1}': {str1[0]}")
print(f"Last character of '{str1}': {str1[-1]}")

# String slicing
print(f"Slice [1:4] of '{str1}': {str1[1:4]}")

# String methods
text = "python programming"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Title: {text.title()}")
print(f"Replace 'python' with 'Python': {text.replace('python', 'Python')}")

# String split and join
sentence = "Python is awesome"
words = sentence.split()
print(f"Split: {words}")
print(f"Join: {'-'.join(words)}")

# String formatting
name = "Vivek"
age = 25
print(f"I am {name} and I am {age} years old")
print("Name: %s, Age: %d" % (name, age))
