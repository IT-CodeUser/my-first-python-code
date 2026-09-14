username = "admin"
password = "secure_password123"

# Nested conditionals
if username == "admin":
    if password == "secure_password123":
        print("Login successful. Welcome Admin!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")