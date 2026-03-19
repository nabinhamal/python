# Python Tuples

# 1. Definition
# Tuples are ordered, immutable collections of items.
# They are defined using parentheses ().
my_tuple = ("apple", "banana", "cherry")
single_item_tuple = ("apple",) # Note the comma is required for a single element

print("--- Tuple Definition ---")
print(f"Tuple: {my_tuple}")
print(f"Type: {type(my_tuple)}")

# 2. Immutability
# Once a tuple is created, you cannot change, add, or remove items.
# my_tuple[0] = "orange" # This would raise a TypeError

# 3. Accessing Elements
print("\n--- Accessing Elements ---")
print(f"First item: {my_tuple[0]}")
print(f"Last item: {my_tuple[-1]}")

# 4. Tuple Packing and Unpacking
# Packing:
coordinates = 10, 20, 30 # Parentheses are optional in packing
# Unpacking:
x, y, z = coordinates
print("\n--- Unpacking ---")
print(f"x={x}, y={y}, z={z}")

# 5. Tuple Methods (Only 2)
nums = (1, 2, 3, 2, 4, 2)
print("\n--- Tuple Methods ---")
print(f"Count of 2s: {nums.count(2)}")
print(f"Index of '3': {nums.index(3)}")

# 6. Why use Tuples?
# - Faster than lists.
# - Makes code safer (immutable).
# - Can be used as keys in dictionaries (unlike lists).
location = {(40.7128, 74.0060): "New York"}
print(f"\nTuple as Dict Key: {location[(40.7128, 74.0060)]}")
