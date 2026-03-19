# Python Sets

# 1. Definition
# Sets are unordered, mutable collections of UNIQUE items.
# They are defined using curly braces {} or the set() function.
my_set = {"apple", "banana", "cherry", "apple"} # Note: "apple" is repeated

print("--- Set Definition ---")
print(f"Set (duplicates removed): {my_set}")
print(f"Typed: {type(my_set)}")

# 2. Unordered Nature
# You cannot access items by index because sets are unordered.
# print(my_set[0]) # This would raise a TypeError

# 3. Adding and Removing
print("\n--- Adding and Removing ---")
my_set.add("orange")
print(f"After add: {my_set}")
my_set.remove("banana") # Raises error if item doesn't exist
my_set.discard("cherry") # Does NOT raise error if item doesn't exist
print(f"After remove/discard: {my_set}")

# 4. Set Operations (Powerful!)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\n--- Set Operations ---")
print(f"Union (all items): {set_a | set_b}") # or set_a.union(set_b)
print(f"Intersection (common items): {set_a & set_b}") # or set_a.intersection(set_b)
print(f"Difference (in A but not B): {set_a - set_b}")
print(f"Symmetric Difference (in either but not both): {set_a ^ set_b}")

# 5. Membership Testing
print("\n--- Membership Testing ---")
print(f"Is 'apple' in set? {'apple' in my_set}")

# 6. Clearing
my_set.clear()
print(f"After clear: {my_set}")
