Flattening Lists (Nested Loops)

matrix = [[1, 2], [3, 4]]
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
        
 flat = [num for row in matrix for num in row]


Handling Alternate Values (if-else Statement)

labels = []
for x in range(5):
    if x % 2 == 0:
        labels.append("Even")
    else:
        labels.append("Odd")

labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
