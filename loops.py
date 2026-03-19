"""Module providing a function printing python version."""
# 1. For Loop
fruits = ["apple", "banana", "cherry"]
print("--- For Loop over List ---")
for fruit in fruits:
    print(fruit)

# 2. Range Function
# range(start, stop, step)
print("\n--- Range Loop (0 to 4) ---")
for i in range(5):
    print(i)

print("\n--- Range Loop (1 to 10 with step 2) ---")
for i in range(1, 11, 2):
    print(i)

# 3. While Loop
COUNT = 0
print("\n--- While Loop ---")
while COUNT < 3:
    print(f"Count: {COUNT}")
    COUNT += 1

# 4. Break and Continue
print("\n--- Break and Continue ---")
print("Using continue for odd numbers (0-4):")
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

print("\nUsing break when i == 2:")
for i in range(5):
    if i == 2:
        break
    print(i)

# 5. Nested Loops
print("\n--- Nested Loops ---")
for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")
