# =================================================================
# PYTHON CONDITIONALS: COMPLETE GUIDE
# =================================================================

# -------------------------
# 1. Basic `if` Statement
# -------------------------

# Execute code if a condition is True
age = 18
if age >= 18:
    print("You are eligible to vote!")  # Output: You are eligible to vote!

# -------------------------
# 2. `if-else` Statement
# -------------------------

# Execute one block if True, another if False
temperature = 30
if temperature > 25:
    print("It's a hot day.")  # Output: It's a hot day.
else:
    print("It's a cool day.")

# -------------------------
# 3. `if-elif-else` Ladder
# -------------------------

# Check multiple conditions
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This block executes (score=85)
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")  # Output: Grade: B

# -------------------------
# 4. Logical Operators
# -------------------------

# Combine conditions using `and`, `or`, `not`
user_age = 25
is_member = True

# Check if user is eligible for a senior discount
if user_age >= 60 or is_member:
    print("Eligible for discount!")
else:
    print("Not eligible.")  # Output: Not eligible.

# Negation with `not`
is_raining = False
if not is_raining:
    print("Enjoy the sunshine!")  # Output: Enjoy the sunshine!

# -------------------------
# 5. Nested Conditionals
# -------------------------

# Conditionals inside conditionals
username = "admin"
password = "secret123"

if username == "admin":
    if password == "secret123":
        print("Login successful!")  # Output: Login successful!
    else:
        print("Wrong password.")
else:
    print("User not found.")

# -------------------------
# 6. Ternary Operator
# -------------------------

# Shorthand for simple if-else
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(result)  # Output: Odd

# -------------------------
# 7. Truthy and Falsy Values
# -------------------------

# Falsy values: None, 0, "", [], (), {}
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("Name is empty.")  # Output: Name is empty.

# -------------------------
# 8. Common Pitfalls
# -------------------------

# Pitfall 1: Using `=` instead of `==`
x = 5
# if x = 10:  ❌ SyntaxError (use `==` for comparison)

# Pitfall 2: Indentation errors
# if x > 0:
# print("Positive")  ❌ IndentationError

# Pitfall 3: Overlapping conditions
score = 85
if score > 80:
    print("Good")  # This executes
elif score > 70:   # Overlaps with previous condition
    print("Average")

## Examples

### 1. Age Group Categorization
#Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = 65

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

### 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price for you is $", price)

### 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = 185

if score >= 101:
    print("Please verify your grade again")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

### 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")

### 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = "Sunny"

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print(activity)

### 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = 5

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport of: ", transport)

### 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)

### 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "Secure3P@ss"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)

### 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = 2023

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")

### 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = "Dog"
age = 1

if pet == "Dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"
elif pet == "Cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Adult cat food"

print("Recommended food: ", food)


# =================================================================
# KEY TAKEAWAYS:
# - Use `if`, `elif`, `else` to control code flow.
# - Combine conditions with `and`, `or`, `not`.
# - Avoid indentation errors and overlapping conditions.
# - Ternary operators simplify simple if-else logic.
# - Truthy/Falsy values help write concise checks.
# =================================================================