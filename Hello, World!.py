x = 5
if x == 6:
    # indented four spaces
    print("x is 1.")
elif x == 5:
     print("wow! you found it python ,nice!")
else :
     print("okay! python stop looking!")

myint = 9
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

A = "forget about the role"
print(A)

Bestinterview = "Well" + "  " + "Done!"
print(Bestinterview)

lotsofHi = "Hi" * 10
print(lotsofHi)

Team1 = ["Red ,Black and Blue"]
Team2 = ["Pink ,Purple and Cyan"]
All_Teams = Team1 + Team2
print(All_Teams)

x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")