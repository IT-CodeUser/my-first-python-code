# INVALID CODE (Will cause SyntaxError)
if x == 5
    print("Hello'

# VALID CODE
if x == 5:
    print("Hello")


# INVALID CODE (Will cause IndentationError)
def my_function():
print("Missing indent")

# VALID CODE
def my_function():
    print("Correct indent")
