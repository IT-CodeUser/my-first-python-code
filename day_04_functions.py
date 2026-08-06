# 1. Defining a basic function with a parameter and a return value
def greet_user(username):
    message = f"Hello, {username}! Welcome to Day 4."
    return message


# 2. Defining a function with multiple parameters
def calculate_area(length, width):
    area = length * width
    return area


# --- TESTING THE FUNCTIONS (Calling them) ---

# Call the greeting function and store its output
greeting_result = greet_user("Alex")
print(greeting_result)

# Call the math function and print the result directly
room_size = calculate_area(5, 4)
print(f"The room size is {room_size} square meters.")
