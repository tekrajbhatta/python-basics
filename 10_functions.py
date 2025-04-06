# 📘 Functions in Python

# 🔹 What is a function?
# A function is a reusable block of code that performs a specific task.
# It helps organize code into smaller, manageable pieces and avoids repetition.

# 🔹 Defining a function
# Use the `def` keyword followed by the function name and parentheses.

def greet():
    print("Hello, welcome to Python functions!")

# 🔹 Calling a function
# Once defined, you call a function using its name followed by parentheses.

greet()  # Output: Hello, welcome to Python functions!

# 🔹 Function with parameters
# Parameters allow you to pass values into a function.

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")  # Output: Hello, Alice!

# 🔹 Function with return value
# Use `return` to send back a result from a function.

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# 🔹 Default parameters
# Provide default values in case no argument is passed.

def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()         # Output: Hello, Guest!
greet_user("Sita")   # Output: Hello, Sita!

# 🔹 *args (Variable number of positional arguments)
# Allows you to pass a variable number of arguments to a function.

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))        # Output: 6
print(sum_all(10, 20, 30, 40)) # Output: 100