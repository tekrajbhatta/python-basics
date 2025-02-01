# =================================================================
# PYTHON LISTS: COMPLETE GUIDE
# =================================================================

# -------------------------
# 1. List Basics
# -------------------------

# Lists are ordered, MUTABLE collections of items (can hold mixed data types).
# Defined using square brackets `[]`.

# Example 1: Creating lists
numbers = [1, 2, 3, 4, 5]
colors = ["Red", "Green", "Blue"]
mixed_list = ["Python", 3.14, True, [1, 2, 3]]  # Nested list
print(mixed_list)  # Output: ['Python', 3.14, True, [1, 2, 3]]
print(mixed_list[-1][0]) # Output: 1

# -------------------------
# 2. List Indexing & Slicing
# -------------------------

# Indexing (0-based)
print(colors[0])    # "Red" (positive index)
print(colors[-1])   # "Blue" (negative index: -1 = last item)

# Slicing [start:end:step]
animals = ["cat", "dog", "bat", "mouse", "pig", "horse"]

# Basic slicing
print(animals[1:4])    # ['dog', 'bat', 'mouse'] (index 1 to 3)
print(animals[::2])     # ['cat', 'bat', 'pig'] (every 2nd item)
print(animals[::-1])    # ['horse', 'pig', 'mouse', 'bat', 'dog', 'cat'] (reverse)

# Step/Jump Index
print(animals[1:5:2])   # ['dog', 'mouse'] (step=2 from index 1 to 4)
print()

# -------------------------
# 3. List Operations
# -------------------------

# Check if an item exists (using `in`)
if "dog" in animals:
    print("Dog is present!")  # Output: Dog is present!
    
# Modify elements
colors[1] = "Yellow"  # Change index 1 to "Yellow"
print(colors)  # ['Red', 'Yellow', 'Blue']

# Insert elements
colors.insert(2, "Green")  # Insert at index 2
print(colors)  # ['Red', 'Yellow', 'Green', 'Blue']
print()

# -------------------------
# 4. List Methods (Key Methods)
# -------------------------

# append(): Add to the end
colors.append("Black")
print(colors)  # ['Red', 'Yellow', 'Green', 'Blue', 'Black']

# extend(): Add elements from another list
rainbow = ["Orange", "Violet"]
colors.extend(rainbow)
print(colors)  # ['Red', 'Yellow', 'Green', 'Blue', 'Black', 'Orange', 'Violet']

# Concatenation (creates a new list)
new_list = colors + ["White", "Gray"]
print(new_list)  # ['Red', 'Yellow', 'Green', 'Blue', 'Black', 'Orange', 'Violet', 'White', 'Gray']

# remove(): Delete by value
colors.remove("Black")
print(colors)  # ['Red', 'Yellow', 'Green', 'Blue', 'Orange', 'Violet']

# pop(): Remove by index (default: last item)
popped_item = colors.pop(1)
print(popped_item)  # "Yellow"
print(colors)  # ['Red', 'Green', 'Blue', 'Orange', 'Violet']

# sort(): Sort in-place
numbers = [4, 2, 9, 1, 5]
numbers.sort()  # Ascending
print(numbers)  # [1, 2, 4, 5, 9]

# reverse(): Reverse the list in-place
numbers.sort(reverse=True)  # Descending
print(numbers)  # [9, 5, 4, 2, 1]

# reverse(): Reverse the list
colors.reverse()
print(colors)  # ['Violet', 'Orange', 'Blue', 'Green', 'Red']

# index(): Find first occurrence
print(colors.index("Blue"))  # 2

# count(): Count occurrences
print(colors.count("Green"))  # 1
# copy(): Shallow copy
original = [1, 2, 3]
copied = original.copy()
copied[0] = 99
print(copied)  # [99, 2, 3]
print(original)  # [1, 2, 3] (unchanged)

# clear(): Remove all items
colors.clear()
print(colors)  # []
print()

# -------------------------
# 5. List Comprehension
# -------------------------

# Create a new list with conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Filter items with a condition
names = ["Milo", "Sarah", "Bruno", "Anastasia"]
long_names = [name for name in names if len(name) > 4]
print(long_names)  # ['Sarah', 'Bruno', 'Anastasia']
print()

# -------------------------
# 6. Memory Management (Shallow vs Deep Copy)
# -------------------------

# Assignment creates a reference (not a copy)
list1 = [1, 2, 3]
list2 = list1
list2[0] = 99
print(list1)  # [99, 2, 3] (original modified!)

# Deep copy for nested lists
import copy
nested_list = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested_list)
deep_copy[0][0] = 100
print(deep_copy)  # [[100, 2], [3, 4]]
print(nested_list)  # [[1, 2], [3, 4]] (original unchanged)
print()

# -------------------------
# 7. Common Pitfalls
# -------------------------

# Pitfall 1: Modifying a list while iterating
numbers = [1, 2, 3, 4, 6]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # Causes unexpected behavior
# print(numbers)  # [1, 3, 6], 6 is even but its skipped!

# Solution: Iterate over a copy
for num in numbers.copy():
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # [1, 3]
print()

# # Pitfall 2: Forgetting list references
# # Use `copy()` or `deepcopy()` to avoid unintended changes.

# -------------------------
# 8. Practice Exercise
# -------------------------

# Task: Create a list of numbers, filter even numbers, and square them
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Steps:
# 1. Filter even numbers (x % 2 == 0)
# 2. Square the remaining numbers
# 3. Store the result in a new list

result = [x**2 for x in numbers if x % 2 == 0]  # Corrected condition
print(result)  # Output: [4, 16, 36, 64, 100]

# =================================================================
# KEY TAKEAWAYS:
# - Lists are MUTABLE, ordered collections.
# - Use indexing/slicing (`[start:end:step]`) and methods (`append()`, `sort()`, etc.).
# - List comprehensions simplify list creation with conditions.
# - Copy lists carefully to avoid unintended references.
# =================================================================
