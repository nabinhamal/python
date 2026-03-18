# Python Variables, Booleans, and Types

# 1. Variable Assignment
# Variables are used to store data. In Python, you don't need to declare types.
name = "Alice"  # String
age = 30        # Integer
is_student = True # Boolean
price = 19.99   # Float

print("--- Variable Assignment ---")
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Price: {price}, Type: {type(price)}")

# 2. Re-assignment
# Python variables are dynamic; you can change their value and type.
x = 10
print(f"\nx is {x}")
x = "Now I'm a string"
print(f"x is {x}")

# 3. Multiple Assignment
a, b, c = 1, 2, "three"
print(f"\na={a}, b={b}, c={c}")

# 4. Constants
# By convention, constants are written in ALL_CAPS.
PI = 3.14159
MAX_CONNECTIONS = 100
print(f"\nPI: {PI}, Max Connections: {MAX_CONNECTIONS}")
