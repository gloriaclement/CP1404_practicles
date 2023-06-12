"""
CP1404/CP5632 - Practical
Four different Loop programs
"""
# A
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C
number_of_stars = int(input("Enter number of stars: "))
for number in range(number_of_stars):
    print("*", end="")

# D
total = 0
number_of_stars = int(input("Enter number of stars: "))
for number in range(0, number_of_stars):
    total += 1
    print("*" * total)
