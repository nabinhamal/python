# Python Strings and String Methods

# 1. String Literals
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = """Triple quotes for
multi-line strings."""

print("--- String Literals ---")
print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s3: {s3}")

# 2. f-strings (Formatted String Literals)
name = "Alice"
age = 30
message = f"Hello, my name is {name} and I am {age} years old."
print(f"\nMessage: {message}")

# 3. String Methods
text = "  python is FUN  "

# Strip whitespace
print(f"\nOriginal: '{text}'")
print(f"Stripped: '{text.strip()}'")

# Case manipulation
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Capitalize: {text.strip().capitalize()}")

# Other methods
print(f"Replace 'FUN' with 'GREAT': {text.replace('FUN', 'GREAT')}")
print(f"Starts with ' ': {text.startswith(' ')}")
print(f"Split: {text.split()}") # Returns a list of words

# 4. String Indexing and Slicing
word = "Python"
print(f"\nWord: {word}")
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
print(f"Slice [0:2]: {word[0:2]}") # 'Py'
print(f"Slice [2:]: {word[2:]}")   # 'thon'
print(f"Slice [::2]: {word[::2]}") # 'Pto' (stride of 2)
