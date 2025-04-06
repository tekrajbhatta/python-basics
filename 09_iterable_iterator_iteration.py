# 🔁 1. Iterable
# An iterable is any Python object capable of returning its members one at a time.
# These are objects you can loop over using a for loop.
# 
# ✅ Examples of iterable objects:
# - Lists: [1, 2, 3]
# - Tuples: (1, 2)
# - Strings: 'hello'
# - Dictionaries
# - Files
# - Sets
# 
# Under the hood, Python uses the built-in `iter()` function to convert an iterable into an iterator.
# iter() is a built-in function that takes an iterable (like list, string, tuple, etc.) and returns an iterator object that can return items one at a time.
# next() is a built-in function that takes an iterator and returns the next item, raising StopIteration if no items are left.

# Example of an iterable(String):
my_string = "Hi, I am Saggy."
# my_string is an iterable
iterator_obj_str = iter(my_string)  # converting to an iterator
print(next(iterator_obj_str))     # Output: H
print(next(iterator_obj_str))     # Output: i
print(next(iterator_obj_str))     # Output: ,
print(next(iterator_obj_str))     # Output:
print(next(iterator_obj_str))     # Output: I
print(next(iterator_obj_str))     # Output:
print(next(iterator_obj_str))     # Output: a
print(next(iterator_obj_str))     # Output: m
print(next(iterator_obj_str))     # Output:
print(next(iterator_obj_str))     # Output: S
print(next(iterator_obj_str))     # Output: a
print(next(iterator_obj_str))     # Output: g
print(next(iterator_obj_str))     # Output: g
print(next(iterator_obj_str))     # Output: y
print(next(iterator_obj_str))     # Output: .
# print(next(iterator_obj_str))   # This would raise StopIteration
print() # Extra line for clarity

# Example of an iterable(List):
my_list = [1, 2, 3, 4]

# my_list is an iterable
iterator_obj = iter(my_list)  # converting to an iterator
print(next(iterator_obj))     # Output: 1
print(next(iterator_obj))     # Output: 2
print(next(iterator_obj))     # Output: 3
print(next(iterator_obj))     # Output: 4
# print(next(iterator_obj))   # This would raise StopIteration
print() # Extra line for clarity

my_file = open('hello.py')
# print(my_file.readline()) # Output: <built-in method readline of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readlines()) # Output: ['# Path: 09_iterable_iterator_iteration.py\n', '# Compare this snippet from hello.py:\n', '# print("Hello World!")\n', '# \n', '# def test(param):\n', '#     print(param)\n', '# \n', '# test("Hello from test function!")\n', '# \n', '# # we can acess this variables too from python shell\n', '# test_one = "First Test"\n', '# test_two = "Second Test"\n', '# test_three = "Third Test"\n', '# test_four = "Fourth test"\n']

# __next__() is a built-in function that takes an iterator and returns the next item, raising StopIteration if no items are left.
new_file = open('hello.py')
# print(new_file.__next__()) # Output: <built-in method __next__ of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(new_file.__next__()) # Output: <built-in method __next__ of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(new_file.__next__()) # Output: <built-in method __next__ of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(new_file.__next__()) # Output: <built-in method __next__ of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(new_file.__next__()) # Output: <built-in method __next__ of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(new_file.__next__()) # Output: <built-in method __next__ of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(new_file.__next__()) # Output: <built-in method __next__ of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(new_file.__next__()) # Output: <built-in method __next__ of _io.TextIOWrapper object at 0x7f8c1c0b3d60>
# print(new_file.__next__())
# print(new_file.__next__())
# print(new_file.__next__())
# print(new_file.__next__())
# print(new_file.__next__()) # This would raise StopIteration exception
# print(new_file.__next__()) # This would raise StopIteration exception

# # Example of an iterable(File):
# with open('hello.py', 'r') as file:
#     for line in file:
#         print(line.strip())  # Print each line from the file
# print() # Extra line for clarity

# # Example of file using for loop
# for line in open('hello.py'):
    # print(line)  # Print each line from the file

# Some note:- While printing the line using for loop, at the end of loop, it wont raise StopIteration exception because file is iterable object and it will return None.

# Example using while loop
hello_file = open('hello.py')
while True:
    line = hello_file.readline()
    if not line:
        break
    print(line.strip())  # Print each line from the file
print() # Extra line for clarity

# Dictionary Example:
my_dict = {'name': 'Saggy', 'age': 25, 'city': 'Kathmandu'}
# my_dict is an iterable
iterator_obj_dict = iter(my_dict)  # converting to an iterator
print(next(iterator_obj_dict))     # Output: name
print(next(iterator_obj_dict))     # Output: age
print(next(iterator_obj_dict))     # Output: city
# print(next(iterator_obj_dict))   # This would raise StopIteration exception
print() # Extra line for clarity

# Range Example:
my_range = range(5)  # Creates an iterable object
# my_range is an iterable
iterator_obj_range = iter(my_range)  # converting to an iterator
print(next(iterator_obj_range))     # Output: 0
print(next(iterator_obj_range))     # Output: 1
print(next(iterator_obj_range))     # Output: 2
print(next(iterator_obj_range))     # Output: 3
print(next(iterator_obj_range))     # Output: 4
# print(next(iterator_obj_range))   # This would raise StopIteration exception
print() # Extra line for clarity

# 🔂 2. Iterator
# An iterator is an object with:
# - A `__next__()` method to return the next item.
# - An internal state to keep track of where it is during iteration.
# 
# Iterators raise a StopIteration exception when there are no more items.
# 
# ✅ How Python uses iterators in a `for` loop:
# 1. Calls iter() on the iterable.
# 2. Calls next() on the iterator repeatedly until StopIteration is raised.

# ✅ Custom Iterator Example:

# class CountUpTo:
#     def __init__(self, max):
#         self.max = max
#         self.counter = 1

#     def __iter__(self):
#         return self  # returns the iterator object

#     def __next__(self):
#         if self.counter <= self.max:
#             value = self.counter
#             self.counter += 1
#             return value
#         else:
#             raise StopIteration

# for num in CountUpTo(3):
#     print(num)  # Output: 1 2 3
# print() # Extra line for clarity
