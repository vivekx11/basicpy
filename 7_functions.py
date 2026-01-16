# Functions

# Basic function
def greet():
    print("Hello, Welcome!")

greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with multiple parameters
def add(a, b):
    return a + b

result = add(5, 10)
print(f"5 + 10 = {result}")

# Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(f"2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")

# Function with variable number of arguments (*args)
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=25, city="NYC")

# Function with docstring
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    """
    return length * width

print(f"Area: {calculate_area(5, 10)}")

# Lambda functions
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Higher-order functions
num_list = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, num_list))
print(f"Squared: {squared}")

even_nums = list(filter(lambda x: x % 2 == 0, num_list))
print(f"Even numbers: {even_nums}")

# Nested functions
def outer():
    message = "Outer"
    def inner():
        print(message)
    inner()

outer()
