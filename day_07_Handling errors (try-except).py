# Code that might fail goes into the 'try' block
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Success! The result is {result}")

# The 'except' block catches the error and keeps the code running
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")
except ValueError:
    print("Error: Please enter a valid integer!")

# This line runs because the program did not crash
print("The program is still running safely!")
