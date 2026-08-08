# Day 6 Reading and Writing Text Files in Python

# 1. WRITING TO A FILE
# Mode 'w' creates a new file or overwrites an existing file.
lines_to_write = [First line of data.n, Second line of data.n]

with open(day6_example.txt, w) as file
    # write() takes a single string
    file.write(Header Welcome to Day 6!n)
    # writelines() takes an iterable list of strings
    file.writelines(lines_to_write)

print(--- File successfully written ---)


# 2. APPENDING TO A FILE
# Mode 'a' adds text to the end of the file without deleting existing data.
with open(day6_example.txt, a) as file
    file.write(Third line of data (Appended).n)

print(--- Data successfully appended ---)


# 3. READING A FILE (Method A Reading the entire file at once)
# Mode 'r' is for reading. It throws an error if the file doesn't exist.
print(n--- Reading entire file content ---)
with open(day6_example.txt, r) as file
    content = file.read()
    print(content)


# 4. READING A FILE (Method B Line by Line via a Loop)
# Best approach for handling large files efficiently.
print(--- Reading line-by-line using a loop ---)
with open(day6_example.txt, r) as file
    for line in file
        # strip() removes the trailing newline character (n)
        print(line.strip())


# 5. READING A FILE (Method C Storing lines in a List)
# readlines() reads all lines and stores them as individual list elements.
print(n--- Reading all lines into a Python list ---)
with open(day6_example.txt, r) as file
    lines_list = file.readlines()
    print(lines_list)
