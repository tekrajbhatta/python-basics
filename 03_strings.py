# =================================================================
# PYTHON STRINGS: COMPREHENSIVE GUIDE (MUTABLE vs IMMUTABLE)
# =================================================================

# -------------------------
# 1. String Basics
# -------------------------

# Strings are IMMUTABLE (cannot be modified in-place)
# Defined using single ('...'), double ("..."), or triple quotes ('''...''', """...""")

# Example: String definitions
s1 = 'Single quotes allow "double quotes" inside'
s2 = "Double quotes allow 'single quotes' inside"
s3 = '''Triple quotes handle
multi-line strings
and preserve formatting like line breaks.'''
s4 = """Also works with double triple-quotes!"""

# -------------------------
# 2. Escape Characters
# -------------------------

# Use \ to escape special characters
escaped_str = "He said, \"Python is awesome!\"\nAnd we agreed.\t(Using tab)"
print(escaped_str)
print()
# Output:
# He said, "Python is awesome!"
# And we agreed.	(Using tab)

# -------------------------
# 3. Indexing & Slicing
# -------------------------

text = "PythonRocks"

# Indexing (0-based)
print(text[0])    # 'P' (first character)
print(text[-1])   # 's' (last character)

# Slicing [start:end:step]
print(text[2:5])    # 'tho' (index 2 to 4)
print(text[::2])    # 'PtoRc' (every 2nd character)
print(text[::-1])   # 'skcoRnohtyP' (reverse string)
print()

# -------------------------
# 4. Key String Methods
# -------------------------

# strip(): Remove whitespace
msg = "   Hello World!   "
print(msg.strip())  # "Hello World!"

# replace(old, new): Replace substring
sentence = "I love Java"
print(sentence.replace("Java", "Python"))  # "I love Python"

# split(delimiter): Convert to list
csv = "apple,banana,grape"
print(csv.split(","))  # ['apple', 'banana', 'grape']

# join(): Combine list into string
words = ["Python", "is", "fun"]
print(" ".join(words))  # "Python is fun"
print()

# -------------------------
# 5. Unicode & Special Characters
# -------------------------

# Python uses Unicode by default
hindi = "नमस्ते"
emoji = "Python! 🐍🔥"
print(f"{hindi} {emoji}")  # नमस्ते Python! 🐍🔥
print()

# -------------------------
# 6. Common Pitfalls
# -------------------------

# Pitfall 1: Forgetting escape characters
# wrong_str = "He said "Hello""  # Syntax Error
correct_str = "He said \"Hello\""

# Pitfall 2: Modifying strings (they're immutable!)
original = "tea"
# original[0] = "T"  # TypeError: 'str' object does not support item assignment
modified = "T" + original[1:]  # Create new string: "Tea"

# Pitfall 3: Negative indexing errors
s = "Python"
# print(s[10])  # IndexError: string index out of range
print()

# -------------------------
# 7. Practice Exercise
# -------------------------

# Task: Clean and format this string
raw_data = "   Chapati;Chai;Samosa;   "

# Steps:
# 1. Strip whitespace
# 2. Replace semicolons with commas
# 3. Split into a list
# 4. Join with " and " between items

cleaned = raw_data.strip()
formatted = cleaned.replace(";", ",")
items = formatted.split(",")
result = " and ".join(items)

print(result)  # "Chapati and Chai and Samosa"

# =================================================================
# KEY TAKEAWAYS:
# - Strings are IMMUTABLE (modification creates new objects)
# - Use slicing/indexing for extraction
# - Master methods: strip(), replace(), split(), join()
# - Always handle special characters and encoding
# =================================================================
