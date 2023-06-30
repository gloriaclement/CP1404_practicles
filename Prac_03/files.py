"""
CP1404/CP5632 - Practical
Using different ways to read files

- read()
- readline()
- readlines()
- for line in file
"""

# 1
out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt")
name = in_file.read().strip()
in_file.close()
print(f"Your name is, {name}")

# 3
in_file = open("numbers.txt")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
result = first_number + second_number
print(f"Numbers: {first_number}, {second_number} ")
print(f"Result: {result}")

# 4
total = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        total += int(line)
    print(f"Total: {total}")
