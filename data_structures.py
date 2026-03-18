# Python Data Structures (List, Tuple, Set, Dict)

# 1. Lists: Ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[0] = "avocado"
print("--- Lists ---")
print(f"List: {fruits}")
print(f"Length: {len(fruits)}")
print(f"Popped: {fruits.pop()}")

# 2. Tuples: Ordered, immutable, allows duplicates
point = (10, 20)
# point[0] = 30 # This would raise an error
print("\n--- Tuples ---")
print(f"Tuple: {point}")
print(f"First element: {point[0]}")

# 3. Sets: Unordered, mutable, NO duplicates
unique_nums = {1, 2, 3, 3, 3, 4}
unique_nums.add(5)
unique_nums.remove(4)
print("\n--- Sets ---")
print(f"Set: {unique_nums}") # Notice duplicates are gone
print(f"Is 2 in set: {2 in unique_nums}")

# 4. Dictionaries: Key-Value pairs, unordered (preserves insertion order in 3.7+), mutable
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
person["email"] = "alice@example.com"
print("\n--- Dictionaries ---")
print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")

# Dictionary methods
print(f"Get age (safe): {person.get('age')}")
print(f"Get salary (default if missing): {person.get('salary', 0)}")
