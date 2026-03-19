# Python Learning Journey 🐍

This project serves as a detailed reference for core Python concepts, specifically focusing on Object-Oriented Programming (OOP) and built-in data structures.

---

## 🚀 Object-Oriented Programming (OOP)

### 1. Class Inheritance
Inheritance allows a child class to acquire the properties and behaviors (methods) of a parent class.

- **Syntax**: 
  ```python
  class Parent:
      # parent methods
  
  class Child(Parent):
      # child methods
  ```
- **When to Use**: Use inheritance when you have a "is-a" relationship (e.g., a `Dog` **is an** `Animal`). It helps avoid code duplication by sharing common logic in a parent class.
- **Example**:
  ```python
  class Vehicle:
      def start_engine(self):
          return "Engine started"

  class Car(Vehicle):
      def drive(self):
          return "Car is driving"

  my_car = Car()
  print(my_car.start_engine()) # Inherited from Vehicle
  ```
- **Reference**: [inher.py](file:///Users/d3vil/Documents/projects/python/inher.py)

### 2. Method Overriding
Method overriding allows a child class to provide a specific implementation for a method that is already defined in its parent class.

- **Syntax**: Define a method in the child class with the **exact same name** as the one in the parent.
- **When to Use**: Use this when a child class needs to behave differently from the parent for the same action (Polymorphism).
- **Example**:
  ```python
  class Shape:
      def area(self):
          return 0

  class Square(Shape):
      def __init__(self, side):
          self.side = side
      def area(self): # Overriding
          return self.side * self.side
  ```
- **Reference**: [overri.py](file:///Users/d3vil/Documents/projects/python/overri.py)

### 3. The `super()` Function
The `super()` function allows the child class to call methods from the parent class, most commonly used during initialization.

- **Syntax**: `super().method_name(args)`
- **When to Use**: 
  1. In `__init__` to initialize parent attributes while adding new child-specific ones.
  2. When you want to extend parent behavior rather than completely replacing it.
- **Example**:
  ```python
  class Employee:
      def __init__(self, name, salary):
          self.name = name
          self.salary = salary

  class Manager(Employee):
      def __init__(self, name, salary, department):
          super().__init__(name, salary) # Initialize name and salary using Employee's logic
          self.department = department   # Manager-specific attribute
  ```
- **Reference**: [adding-attr.py](file:///Users/d3vil/Documents/projects/python/adding-attr.py)

### 4. Exception Handling
Error handling allows your program to deal with unexpected situations (like a missing file or a network error) without crashing.

- **Syntax**: 
  ```python
  try:
      # Code that might cause an error
  except ValueError as e:
      # Specific error handling
  except Exception as e:
      # Catch-all for other errors
  finally:
      # Code that ALWAYS runs (e.g., closing a file)
  ```
- **When to Use**: Whenever your code interacts with external systems (files, APIs, user input) or performs risky operations (math division, index access) where something might go wrong beyond your control.
- **Example**:
  ```python
  try:
      with open("data.txt", "r") as f:
          content = f.read()
          num = int(content)
  except FileNotFoundError:
      print("Error: The file does not exist.")
  except ValueError:
      print("Error: The file contains non-numeric data.")
  finally:
      print("Execution complete.")
  ```

---

## 📦 Data Structures

Python's built-in data structures are essential for efficient data management.

### 1. Lists (`[]`)
- **Syntax**: `my_list = [1, 2, 3]`
- **When to Use**: Use for ordered collections of items that might change (mutable).
- **Key Methods**: `.append()`, `.pop()`, `.remove()`, `.sort()`.

### 2. Tuples (`()`)
- **Syntax**: `my_tuple = (10, 20)`
- **When to Use**: Use for data that should **not** change (immutable) after creation. Often used for fixed coordinates, configurations, or returning multiple values from a function.

### 3. Sets (`{}`)
- **Syntax**: `my_set = {1, 2, 3}`
- **When to Use**: Use when you need to store **unique** items and perform fast membership tests (checking if an item exists) or mathematical operations like unions and intersections.

### 4. Dictionaries (`{k: v}`)
- **Syntax**: `my_dict = {"name": "Alice", "age": 25}`
- **When to Use**: Use for mapping unique keys to values (e.g., a database record, settings).
- **Key Methods**: `.keys()`, `.values()`, `.get(key, default)`.

---

