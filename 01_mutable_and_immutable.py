# Python Notes: Mutable vs. Immutable Objects

"""
Theory: Mutable vs. Immutable Objects in Python
-----------------------------------------------
- **Mutable Objects**: These are objects whose value or state can be changed after creation.
  Example: Lists, Dictionaries, Sets.

- **Immutable Objects**: These are objects whose value or state cannot be changed after creation.
  Example: Integers, Strings, Tuples.

Why It Matters:
- Mutable objects can lead to unintended side effects when multiple variables refer to the same object.
- Immutable objects are safe from such side effects, as their value cannot be altered.

Key Differences:
---------------
1. **Mutability**:
   - Mutable: Can be modified in place.
   - Immutable: Cannot be modified in place; any "change" creates a new object.

2. **Memory Usage**:
   - Mutable: Changes affect the same memory location.
   - Immutable: Changes create a new object in memory.

3. **Use Cases**:
   - Mutable: Useful when frequent modifications are needed.
   - Immutable: Useful for fixed or hashable objects (e.g., keys in dictionaries).

List of Common Variable Types:
------------------------------
Mutable:
- List
- Dictionary
- Set
- bytearray

Immutable:
- Integer
- Float
- Boolean
- String
- Tuple
- Frozenset
- Bytes
"""

# Example 1: Mutable Object (List)
myListOne = [1, 2, 3]
myListTwo = myListOne  # Both variables point to the same list
print("Original List:")
print(myListOne)  # Output: [1, 2, 3]
print(myListTwo)  # Output: [1, 2, 3]

# Modifying the list
myListOne[0] = 44
print("\nAfter Modifying myListOne:")
print(myListOne)  # Output: [44, 2, 3]
print(myListTwo)  # Output: [44, 2, 3] (Both variables reflect the change)

# Reassigning `myListOne` to a new object
myListOne = 'test string'
print("\nAfter Reassigning myListOne:")
print(myListOne)  # Output: 'test string'
print(myListTwo)  # Output: [44, 2, 3] (Unaffected)

# Example 2: Immutable Object (Integer)
num_one = 10
num_two = num_one  # Both variables point to the same integer object
print("\nOriginal Integer:")
print(num_one)  # Output: 10
print(num_two)  # Output: 10

# Reassigning `num_one` to a new object
num_one = 'test string'
print("\nAfter Reassigning num_one:")
print(num_one)  # Output: 'test string'
print(num_two)  # Output: 10 (Unaffected)

"""
Object Identity and `id()` Function:
------------------------------------
- Use the `id()` function to check if two variables refer to the same object.
- Example:
  a = [1, 2, 3]
  b = a
  print(id(a) == id(b))  # Output: True (Same object)
  
  c = [1, 2, 3]
  print(id(a) == id(c))  # Output: False (Different objects)
"""

# Example: `id()` Demonstration
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("\nObject Identity Check:")
print(id(list1) == id(list2))  # Output: False (Different objects)

list3 = list1
print(id(list1) == id(list3))  # Output: True (Same object)

"""
Interning in Python:
--------------------
- Small integers and strings are cached (interned) for optimization.
- Larger integers and most objects are not interned.
"""

# Example: Interning with Small Integers
a = 10
b = 10
print("\nInterning with Small Integers:")
print(id(a) == id(b))  # Output: True (Same object)

# Example: Interning with Larger Integers
x = 257
y = 257
print("\nInterning with Larger Integers:")
print(id(x) == id(y))  # Output: Might be False (Depends on implementation)

"""
Key Takeaways:
--------------
1. Mutable objects share references, so changes affect all variables pointing to them.
2. Immutable objects always create a new object on modification or reassignment.
3. Use `id()` to check object identity, especially when working with complex structures.
4. Be mindful of mutability to avoid unintended side effects in your code.
"""

# Final Thought:
# Understanding these principles will help you write more predictable and efficient Python code!
