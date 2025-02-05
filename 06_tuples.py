# =================================================================
# PYTHON TUPLES: COMPLETE GUIDE (UPDATED)
# =================================================================

# -------------------------
# 1. Tuple Basics
# -------------------------

# Create a tuple using parentheses `()`
tuple1 = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)  # Output: (1, 2, 2, 3, 5, 4, 6)
print(tuple2)  # Output: ('Red', 'Green', 'Blue')

# Single-element tuple (requires a trailing comma) otherwise it's considered a string
single_item = ("Hello",)
print(type(single_item))  # Output: <class 'tuple'>
single_item_v2 = ("Hello")
print(type(single_item_v2))  # Output: <class 'str'>

# Tuple without parentheses (comma-separated values)
numbers = 1, 2, 3
print(numbers)  # Output: (1, 2, 3)
print(type(numbers))  # Output: <class 'tuple'>

# Empty tuple
empty_tuple = ()
empty_tuple_v2 = tuple()
print(empty_tuple)  # Output: ()
print(empty_tuple_v2)  # Output: ()
print(empty_tuple == empty_tuple_v2)  # Output: True
print()

# -------------------------
# 2. Accessing Elements
# -------------------------

# I. Positive Indexing
country = ("Spain", "Italy", "India")
print(country[0])  # Output: Spain
print(country[1])  # Output: Italy
print(country[2])  # Output: India


# II. Negative Indexing
country = ("Spain", "Italy", "India", "England", "Germany")
print(country[-1])  # Output: Germany
print(country[len(country)-1]) # Output: Germany (alternative way)
print(country[-3])  # Output: India
print(country[-4])  # Output: Italy

# III. Check for Item (Membership)
if "Germany" in country:
    print("Germany is present.")  # Output: Germany is present.
else:
    print("Germany is absent.")

if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")  # Output: Russia is absent.
    
# IV. Range of Index (Slicing)
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")

# Using positive indexes
print(animals[3:7])  # Output: ('mouse', 'pig', 'horse', 'donkey')

# Using negative indexes
print(animals[-7:-2])  # Output: ('bat', 'mouse', 'pig', 'horse', 'donkey')

# Printing all elements from a given index till the end
print(animals[4:])  # Output: ('pig', 'horse', 'donkey', 'goat', 'cow')
print(animals[-4:])  # Output: ('horse', 'donkey', 'goat', 'cow')

# Printing all elements from start to a given index
print(animals[:6])  # Output: ('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
print(animals[:-3])  # Output: ('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')

# Printing alternate values
print(animals[::2])  # Output: ('cat', 'bat', 'pig', 'donkey', 'cow')
print(animals[-8:-1:2])  # Output: ('dog', 'mouse', 'horse', 'goat')

# Printing every 3rd consecutive value within a given range
print(animals[1:8:3])  # Output: ('dog', 'pig', 'goat')
print(animals[-8:-1:3])  # Output: ('dog', 'pig', 'goat')
print()

# -------------------------
# 3. Immutable Nature
# -------------------------

# Tuples cannot be modified after creation
# This will raise an error:
# country[0] = "France"  ❌ TypeError: 'tuple' object does not support item assignment

# Workaround: Convert to a list, modify, and convert back to a tuple
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")  # Add item
temp.pop(3)  # Remove item
temp[2] = "Finland"  # Change item
countries = tuple(temp)
print(countries)  # Output: ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')

# Direct concatenation of tuples
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)  # Output: ('Spain', 'Italy', 'Finland', 'Germany', 'Russia', 'Vietnam', 'India', 'China')
print()

# -------------------------
# 4. Tuple Methods
# -------------------------

# count(): Count occurrences of an element
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print(Tuple1.count(3))  # Output: 3

# index(): Find the first occurrence of an element
print(Tuple1.index(3))  # Output: 3

# -------------------------
# 5. Tuple Operations
# -------------------------

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5)

# Repetition
repeated = ("Hi",) * 3
print(repeated)  # Output: ('Hi', 'Hi', 'Hi')

# Membership check
colors = ("red", "blue", "green", "yellow")
print("green" in colors)  # Output: True
print()

# -------------------------
# 6. Tuple Unpacking
# -------------------------

# Assign elements to variables
name, age, profession = ("Alice", 25, "Engineer")
print(f"{name} is a {profession} and {age} year old.")  # Output: Alice is a Engineer

# Extended unpacking (Python 3.0+)
first, *rest = combined
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5] (rest is a list)
print()

# -------------------------
# 7. Nested Tuples
# -------------------------

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(matrix[1][2])  # Output: 6 (second row, third column)
print(matrix[2][0])  # Output: 7 (third row, first column)
print()

# -------------------------
# 8. Common Pitfalls
# -------------------------

# Pitfall 1: Forgetting the comma in single-element tuples
# not_a_tuple = ("Hello")  ❌ This is a string, not a tuple

# Pitfall 2: Trying to modify a tuple
# colors[0] = "yellow"  ❌ Raises TypeError

# Pitfall 3: Confusing tuple and list syntax
# my_list = [1, 2, 3]
# my_tuple = (1, 2, 3)

# -------------------------
# 9. Practice Exercise
# -------------------------

# Task: Swap two variables using tuples
a = (5, 6, 7)
b = (10, 11)
print(type(a), type(b)) # Output: <class 'tuple'> <class 'tuple'>
a, b = b, a  # Tuple unpacking
print(f"a = {a}, b = {b}") # Output: a = (10, 11), b = (5, 6, 7)

# =================================================================
# KEY TAKEAWAYS:
# - Tuples are IMMUTABLE and ordered.
# - Use for fixed data (e.g., coordinates, configurations).
# - Methods: count(), index().
# - Tuple unpacking simplifies variable swaps and assignments.
# - Prefer tuples over lists for non-modifiable data.
# =================================================================