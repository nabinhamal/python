# Python Boolean Operators and Control Flow

# 1. Comparison Operators
a = 10
b = 20
print("--- Comparison Operators ---")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a < b: {a < b}")
print(f"a > b: {a > b}")
print(f"a <= b: {a <= b}")
print(f"a >= b: {a >= b}")

# 2. Boolean Operators (and, or, not)
is_sunny = True
is_warm = False

print("\n--- Boolean Operators ---")
print(f"is_sunny and is_warm: {is_sunny and is_warm}") # True if both are True
print(f"is_sunny or is_warm: {is_sunny or is_warm}")   # True if at least one is True
print(f"not is_sunny: {not is_sunny}")                 # Reverse boolean

# 3. Control Flow (if, elif, else)
x = 15
print("\n--- Control Flow ---")
if x > 20:
    print("x is greater than 20")
elif x > 10:
    print("x is greater than 10 but less than or equal to 20")
else:
    print("x is 10 or less")

# 4. Identity and Membership
nums = [1, 2, 3]
y = 1
print("\n--- Identity and Membership ---")
print(f"y in nums: {y in nums}")
print(f"5 not in nums: {5 not in nums}")
print(f"nums is [1, 2, 3]: {nums is [1, 2, 3]}") # False (different objects in memory)
print(f"nums == [1, 2, 3]: {nums == [1, 2, 3]}") # True (same values)
