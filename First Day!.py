print("this will be written")
print("it will be written")

N = 5
T = 10
print(N / T) # Outputs: 0.5

A = "this will be written for a long time"
B = 5 + 9

# prompt user for input
print(input(f"{A} in {B} ")) 

monsters = ["Slime", "Goblin", "Dragon"]
lucky_numbers = [7, 13, 21, 42]

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

# CORRECTED: Python starts counting at 0
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# loops through and prints 1, 2, 3
for x in mylist:
    print(x)

squared = 7 ** 2
cubed = 2 ** 3
print(squared) # Outputs: 49
print(cubed)   # Outputs: 8

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
