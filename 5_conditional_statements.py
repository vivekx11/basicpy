# Conditional Statements

# Basic if statement
age = 25
if age >= 18:
    print("You are an adult")

# if-else statement
num = 10
if num > 0:
    print("Number is positive")
else:
    print("Number is not positive")

# if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Nested if statements
x = 15
if x > 10:
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is between 10 and 20")
else:
    print("x is less than or equal to 10")

# Using logical operators
temp = 25
humidity = 60
if temp > 20 and humidity > 50:
    print("It's warm and humid")

if temp < 0 or humidity < 30:
    print("It's cold or dry")

if not (temp > 30):
    print("It's not too hot")

# Ternary operator (conditional expression)
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Using in operator
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")
