"""
Python Loops Demonstration Script
This script covers the syntax and use cases for 'for' and 'while' loops.
"""

# ==========================================
# 1. THE FOR LOOP
# Best used when you know the number of iterations in advance
# or when iterating over a sequence (list, string, range, etc.)
# ==========================================
print("--- 1. Basic For Loop with range() ---")
# range(5) generates numbers from 0 up to (but not including) 5
for i in range(5):
    print(f"Iteration {i}")

print("\n--- 2. For Loop iterating over a List ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like eating {fruit}")


# ==========================================
# 2. THE WHILE LOOP
# Best used when you want to repeat code AS LONG AS a condition is True.
# The number of iterations is usually unknown beforehand.
# ==========================================
print("\n--- 3. Basic While Loop ---")
countdown = 3
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1  # CRITICAL: Always update the condition variable to avoid infinite loops!
print("Blast off! 🚀")


# ==========================================
# 3. LOOP CONTROL STATEMENTS
# break: Exits the loop entirely immediately.
# continue: Skips the rest of the current iteration and jumps to the next one.
# ==========================================
print("\n--- 4. For Loop with 'break' and 'continue' ---")
for number in range(1, 6):
    if number == 2:
        print("Skipping 2 using 'continue'")
        continue  # Skips the print statement below for this item
    
    if number == 4:
        print("Stopping the loop entirely at 4 using 'break'")
        break  # Exits the loop completely
        
    print(f"Processing number: {number}")


# ==========================================
# 4. PRACTICAL WHILE LOOP EXAMPLE
# Great for interactive scenarios like user input validation
# ==========================================
print("\n--- 5. Practical While Loop (Simulated Input Validation) ---")
attempts = 0
authenticated = False

# Simulating a password entry loop
while not authenticated:
    attempts += 1
    print(f"Attempt #{attempts}: Checking credentials...")
    
    # In a real app, this would be user_input == "secret"
    if attempts == 3: 
        print("Access Granted!")
        authenticated = True
    else:
        print("Wrong password. Trying again.")
