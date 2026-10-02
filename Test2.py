#-----Test 1:Name and Age Greeting-----

Name=input("Enter your name: ")
age_str=input("Enter your age: ")

age=int(age_str)

next_age=age+1
print(f"Hello {Name},you will be {next_age} years old next year!")

#-----Test 2:Float Operations-----

num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

total_sum=num1 + num2
difference=num1 - num2
product=num1 * num2

print(f"sum: {total_sum}")
print(f"difference: {difference}")
print(f"product: {product}")

#-----Test 3:Score Gender-----

score=int(input("Enter an integer score:"))

if score <0 or score>100:
    print("Invalid Score")
elif score >=50:
    print("pass")
else:
    print("fail")

#-----Test 4:Variable Initializtion-----

total_cost = 0.0

#-----Test 5:Clesius to Fahrenheit Converter-----

celsius=float(input("Enter temperature in celsius:"))

fahrenheit =(celsius * 1.8)+32

print(f"Temperature in fahrenhiet:{fahrenheit:.2f}")

#-----Test 6:Even or Odd Checker-----

number =int(input("Enter"))

if number %2==0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#-----Test 7:ATM Withdrawal Logic-----

balance=float(input("Enter your account balance:"))
withdrawal=float(input("Enter the withdrawal amount:"))

if withdrawal <= balance:
    balance -= withdrawal
    print("Withdrawal successful")
else:
    print("insufficient funds")

user_string=("Enter a string:")

string_length=len(user_string)
uppercase_string=user_string .upper()

print(f"Length of the string:{string_length}")
print(f"uppercase string:{uppercase_string}")