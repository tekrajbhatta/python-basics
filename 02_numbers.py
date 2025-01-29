# Examples of different number types
integer_num = 42
float_num = 3.14
complex_num = 2 + 3j

print(type(integer_num))
print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Complex: {complex_num}, Type: {type(complex_num)}")
print()

# Basic Arithmetic Operations
a, b = 10, 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print(f"Floor Division: {a} // {b} = {a // b}") # Floor division returns the largest integer less than or equal to the division result.
print(f"Modulus: {a} % {b} = {a % b}")
print()

# Operator Precedence
# Python Operator Precedence (Highest to Lowest):
# 1. Parentheses `()`: Used to group expressions and override the default precedence.
# 2. Exponentiation `**`: Right-to-left associativity.
# 3. Unary Operators: `+`, `-`, `~` (positive, negative, bitwise NOT).
# 4. Multiplicative Operators: `*`, `/`, `//`, `%` (multiplication, division, floor division, modulus).
# 5. Additive Operators: `+`, `-` (addition, subtraction).
# 6. Bitwise Shift Operators: `<<`, `>>` (left shift, right shift).
# 7. Bitwise AND: `&`
# 8. Bitwise XOR: `^`
# 9. Bitwise OR: `|`
# 10. Comparison Operators: `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in`.
# 11. Logical NOT: `not`
# 12. Logical AND: `and`
# 13. Logical OR: `or`
# 14. Assignment Operators: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, etc.
# 15. Expression Separators: `,`

# Example code demonstrating precedence:
a = 5
b = 2
c = 3

# Parentheses override precedence
print((a + b) * c)  # Parentheses take highest precedence

# Exponentiation
print(a ** b)  # Exponentiation (5^2 = 25)

# Multiplicative and Additive
print(a + b * c)  # Multiplication has higher precedence than addition

# Logical Operators
print(a > b and b < c)  # Comparison happens before logical AND

# Bitwise Operations
print(a & b | c)  # Bitwise AND happens before Bitwise OR
print()

# Assignment1: Difference between `repr()`, `str()`, and `print()` functions
# Example string
text = "hello\nworld"

# repr() - Developer-friendly, detailed representation
dev_view = repr(text)  # Output: 'hello\\nworld'
print(dev_view)  # 'hello\nworld'

# str() - User-friendly, interpreted representation
user_view = str(text)  # Output: hello
                       #         world
print(user_view)  # hello
                  # world

# print() - Displays the result of str() directly to the console
print(text)  # Output: hello
             #         world
print()

# Comments for clarity:
# repr() -> Shows the raw representation(developer-friendly representation of an object, used for debugging or inpspecting the object) (e.g., escapes \n as \\n). 
# str() -> Formats the object for users(Provides a readable, user-friendly representation of an object. Designed for display to users, without extra details.) (e.g., interprets \n as a new line).
# print() -> Displays the output of str() (or whatever you pass to it) to the console. It’s not a function to process data but just shows the final output.

# Importing required libraries
import math
import random

# -----------------------------
# 1. Common Number Types
# -----------------------------

# Integer (whole numbers)
x = 10  # Example of a positive integer
y = -3  # Example of a negative integer
z = 0   # Example of zero

print(type(x))
print(type(y))
print(type(z))
print()

# Floating-point (decimal numbers)
pi = 3.14  # Example of a positive float
negative_float = -0.5  # Example of a negative float

print(type(pi))
print(type(negative_float))
print()

# Complex numbers (a + bj, where j is the imaginary part)
complex_num = 3 + 5j  # Example of a complex number

print(type(complex_num))
print()

# -----------------------------
# 2. Rounding and Truncation
# -----------------------------

# math.floor() - Rounds down to the nearest integer
print(math.floor(3.5))   # Output: 3 (closest integer below 3.5)
print(math.floor(3.6))   # Output: 3
print(math.floor(-3.6))  # Output: -4 (floor goes to the closest smaller integer)
print()

# math.trunc() - Truncates the decimal part, moving towards zero
print(math.trunc(3.6))   # Output: 3 (removes the decimal part)
print(math.trunc(-3.6))  # Output: -3 (closer to zero)
print()

# -----------------------------
# 3. Base Conversions and Representations
# -----------------------------

# Represent numbers on different bases
# Octal (base 8)
print(0o20)  # Output: 16 (20 in octal is 16 in decimal)
# Hexadecimal (base 16)
print(0xFF)  # Output: 255 (FF in hexadecimal is 255 in decimal)
# Binary (base 2)
print(0b1000)  # Output: 8 (1000 in binary is 8 in decimal)
print()

# Convert decimal to other bases
print(oct(16))  # Output: 0o20 (decimal 16 → octal 20)
print(hex(255))  # Output: 0xff (decimal 255 → hexadecimal FF)
print(bin(8))  # Output: 0b1000 (decimal 8 → binary 1000)
print()

# Base-specific conversions
print(int(64))          # Output: 64 (interpreted as decimal)
print(int('20', 8))     # Output: 16 (octal "20" → decimal 16)
print(int('FF', 16))    # Output: 255 (hex "FF" → decimal 255)
print(int('1000', 2))   # Output: 8 (binary "1000" → decimal 8)
print()

# -----------------------------
# 4. Bitwise Operations
# -----------------------------

# Bitwise AND (&) and OR (|)
x = 4  # Binary: 0100
print(x & 2)  # Output: 0 (Binary AND: 0100 & 0010 = 0000)
print(x | 2)  # Output: 6 (Binary OR: 0100 | 0010 = 0110)

# Bitwise shift left (<<)
print(x << 2)  # Output: 16 (Shift bits left: 0100 -> 10000)
print()

# -----------------------------
# 5. Generating Random Numbers
# -----------------------------

# Generate random floating-point numbers
print(random.random())  # Output: Random number between 0 and 1

# Generate random integers within a range
print(random.randint(1, 10))  # Output: Random integer between 1 and 10 (inclusive)

# Random choice from a list
l1 = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(l1))  # Output: Random item from the list

# Shuffle a list
random.shuffle(l1)
print(l1)  # Output: Shuffled list

# -----------------------------
# 6. Set Operations
# -----------------------------

# Create a set (unordered, unique elements)
setone = {1, 2, 3, 4}

# Intersection: Common elements between sets
print(setone & {1, 3})  # Output: {1, 3}

# Union: Combine elements (duplicates removed)
print(setone | {1, 3})     # Output: {1, 2, 3, 4}
print(setone | {1, 3, 7})  # Output: {1, 2, 3, 4, 7}

# Difference: Elements in setone but not in the other set
print(setone - {1, 2, 3, 4})  # Output: set() (empty set)

# Empty set vs. empty dict
print(type({}))  # Output: <class 'dict'> (use set() for empty sets)
empty_set = set()  # Correct way to create an empty set

