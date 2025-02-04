# =================================================================
# PYTHON DICTIONARIES: COMPLETE GUIDE
# =================================================================

# -------------------------
# 1. Dictionary Basics
# -------------------------

# Dictionaries are an ordered collection of key-value pairs.
# Keys must be immutable (e.g., strings, numbers, or tuples), and values can be any data type.

info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)  # Output: {'name': 'Karan', 'age': 19, 'eligible': True}

# Creating an empty dictionary
empty_dict = {}
empty_dict_v2 = dict()
print(empty_dict == empty_dict_v2)  # Output: True

# Keys can be numbers, strings, or tuples (immutable types)
grades = {101: "A", 102: "B", 103: "C"}
print(grades[101])  # Output: A
print()

# -------------------------
# 2. Accessing Values
# -------------------------

# Accessing single values
print(info['name'])  # Output: Karan
print(info.get('age'))  # Output: 19

# Using get() prevents KeyError if the key doesn't exist
print(info.get('address', 'Not Found'))  # Output: Not Found

# Checking if a key exists
if 'age' in info:
    print("Age exists!")  # Output: Age exists!
    
# Accessing multiple values
print(info.values())  # Output: dict_values(['Karan', 19, True])

# Accessing keys
print(info.keys())  # Output: dict_keys(['name', 'age', 'eligible'])

# Accessing key-value pairs
print(info.items())  # Output: dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
print()

# -------------------------
# 3. Dictionary Methods
# -------------------------

# update(): Updates or adds key-value pairs
info.update({'age': 20, 'DOB': 2001})
print(info)  # Output: {'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}

# pop(): Removes a key-value pair and returns its value
removed_value = info.pop('eligible')
print(removed_value)  # Output: True
print(info)  # Output: {'name': 'Karan', 'age': 20, 'DOB': 2001}

# popitem(): Removes and returns the last key-value pair
last_item = info.popitem()
print(last_item)  # Output: ('DOB', 2001)

# clear(): Removes all items from the dictionary
info.clear()
print(info)  # Output: {}

# del: Removes a specific key or the entire dictionary
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info['age']
print(info)  # Output: {'name': 'Karan', 'eligible': True, 'DOB': 2003}

# Uncommenting the following lines will delete the dictionary entirely
# del info
# print(info)  # NameError: name 'info' is not defined

# -------------------------
# 4. Adding/Modifying Entries
# -------------------------

# Adding a new key-value pair
info['grade'] = 'A'
print(info)  # Output: {'name': 'Karan', 'eligible': True, 'DOB': 2003, 'grade': 'A'}

# Modifying an existing value
info['name'] = 'Bob'
print(info['name'])  # Output: Bob
print(info)  # Output: {'name': 'Bob', 'eligible': True, 'DOB': 2003, 'grade': 'A'}
print()

# -------------------------
# 5. Nested Dictionaries
# -------------------------

employees = {
    "emp1": {"name": "John", "role": "Developer"},
    "emp2": {"name": "Sarah", "role": "Designer"}
}
print(employees["emp1"]["name"])  # Output: John
print(employees) # Output: {'emp1': {'name': 'John', 'role': 'Developer'}, 'emp2': {'name': 'Sarah', 'role': 'Designer'}}
print()

# -------------------------
# 6. Dictionary Comprehensions
# -------------------------

# Creating a dictionary from a list
numbers = [1, 2, 3]
squared = {num: num**2 for num in numbers}
print(squared)  # Output: {1: 1, 2: 4, 3: 9}

# Filtering items with a condition
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squares)  # Output: {2: 4}
print()

# -------------------------
# 7. Merging Dictionaries
# -------------------------

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}  # Later keys override earlier ones
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
merged_v2 = dict1 | dict2  # Requires Python 3.9+
print(merged_v2)  # Output: {'a': 1, 'b': 3, 'c': 4}
print()

# -------------------------
# 8. Common Pitfalls
# -------------------------

# KeyError when accessing missing keys
# print(info['address'])  ❌ Raises KeyError

# Solution: Use get()
print(info.get('address', 'Default'))  # ✅ Output: Defaults


# Using mutable types as keys
# invalid_dict = {['key']: 'value'}  ❌ Lists are mutable (unhashable)

# -------------------------
# 9. Practice Exercise
# -------------------------

# Task: Create a dictionary of items and prices, then:
# 1. Apply a 10% discount to all prices
# 2. Create a new dictionary with items costing more than $50

prices = {"laptop": 1000, "mouse": 25, "keyboard": 45, "monitor": 300}

# Step 1: Apply discount
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)  # Output: {'laptop': 900.0, 'mouse': 22.5, 'keyboard': 40.5, 'monitor': 270.0}

# Step 2: Filter expensive items
expensive = {item: price for item, price in discounted.items() if price > 50}
print(expensive)  # Output: {'laptop': 900.0, 'monitor': 270.0}

# =================================================================
# KEY TAKEAWAYS:
# - Dictionaries store key-value pairs (keys must be immutable).
# - Use get() to safely access values.
# - Methods: keys(), values(), items(), update(), pop(), etc.
# - Dictionary comprehensions simplify transformations.
# - Avoid KeyError and mutable keys.
# =================================================================
