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
print() # Extra line for clarity

# Python Loop Problems and Solutions

# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of Positive number is:", positive_number_count)

# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.
n = 10
sum_even = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers is:", sum_even)

# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
number = 3
for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)

# 4. Reverse a String
# Problem: Reverse a string using a loop.
input_str = "Python"
reversed_str = ""
for char in input_str:
    reversed_str = char + reversed_str  
print(reversed_str)

# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.
input_str = "teeteracdacd"
for char in input_str:
    if input_str.count(char) == 1:
        print("First non-repeated character is:", char)
        break

# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.
number = 5
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print("Factorial:", factorial)

# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.
while True:
    number = int(input("Enter value between 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")

# 8. Prime Number Checker
# Problem: Check if a number is prime.
number = 28
is_prime = True
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print("Is prime?", is_prime)

# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]
unique_items = set()
for item in items:
    if item in unique_items:
        print("Duplicate:", item)
        break
    unique_items.add(item)

# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time
wait_time = 1
max_retries = 5
attempts = 0
while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
print("All attempts finished")

