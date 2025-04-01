# =================================================================
# PYTHON LOOPS: COMPLETE GUIDE
# =================================================================

# -------------------------
# 1. `for` Loop
# -------------------------

# Used for iterating over a sequence (list, tuple, string, etc.)
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)  # Output: 0 1 2 3 4
print() # Extra line for clarity

# -------------------------
# 2. `while` Loop
# -------------------------

# Repeats while a condition is True
count = 0
while count < 5:
    print(count)  # Output: 0 1 2 3 4
    count += 1
print() # Extra line for clarity

# -------------------------
# 3. `range()` Function
# -------------------------

# Generates a sequence of numbers
for i in range(5):
    print(i)  # Output: 0 1 2 3 4
print() # Extra line for clarity

# -------------------------
# 4. Loop Control Statements
# -------------------------

# `break`: Exit loop immediately
for num in range(10):
    if num == 5:
        break
    print(num)  # Output: 0 1 2 3 4
print() # Extra line for clarity

# `continue`: Skip current iteration
for num in range(5):
    if num == 2:
        continue
    print(num)  # Output: 0 1 3 4
print() # Extra line for clarity

# `pass`: Placeholder for future code
# The pass statement is used as a placeholder for future code.
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
for i in range(3):
    pass  # having an empty for loop like this, would raise an error without the pass statement
print() # Extra line for clarity

# -------------------------
# 5. Nested Loops
# -------------------------

# Loop inside another loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print() # Extra line for clarity

# -------------------------
# 6. Iterating Over Different Data Types
# -------------------------

# Strings
for char in "Python":
    print(char)
print() # Extra line for clarity

# Lists
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)
print() # Extra line for clarity

# Tuples
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"x={x}, y={y}")
print() # Extra line for clarity

# long method same problem as above
for cord in coordinates:
    print(f"x={cord[0]}, y={cord[1]}")
print() # Extra line for clarity

# Dictionaries
details = {"name": "Alice", "age": 25}
for key, value in details.items():
    print(f"{key}: {value}")
print() # Extra line for clarity

# -------------------------
# 7. `else` Clause in Loops
# -------------------------

# Runs when loop completes normally (without `break`)
for num in range(3):
    print(num)
else:
    print("Loop finished successfully!")
print() # Extra line for clarity

# -------------------------
# 8. Common Pitfalls
# -------------------------

# Pitfall 1: Infinite loops (forgot to update condition)
# while True:
#     print("This will run forever!") ❌

# Pitfall 2: Modifying list while iterating
numbers = [1, 2, 3, 4]
# for num in numbers:
#     numbers.remove(num)  ❌ Unexpected behavior

# Pitfall 3: Off-by-one errors
for i in range(1, 5):
    print(i)  # Correctly prints 1 to 4 (not including 5)

## Examples (To be added later)