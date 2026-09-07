#Lesson 1:Strings

name = "Alice"
message = "Welcome to Python!"
numbers_as_text = "99"  # Because it has quotes, Python treats this as text, not a number!

print("10" + "20")  # Outputs: "1020"

#Lesson 2:Integers

age = 25
temperature = -5
items = 0

print(10 / 2)   # Outputs: 5.0 (Float)
print(10 // 2)  # Outputs: 5 (Integer)

#lesson 3:Floats

price = 19.99
pi = 3.14159
exact_zero = 0.0  # The .0 makes this a float, not an integer


# Converting a number to text so we can print it together
age = 25
print("I am " + str(age) + " years old.")  # Outputs: I am 25 years old.

# Converting a text string to a number to do math
price_text = "10.50"
total = float(price_text) + 2.00           # Outputs: 12.50