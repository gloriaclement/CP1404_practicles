numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] Result is 3
# numbers[-1] Result is 2
# numbers[3] Result is 1
# numbers[:-1] Result is [3, 1, 4, 1, 5, 9]
# numbers[3:4] Result is [1]
# 5 in numbers Result is True
# 7 in numbers Result is False
# "3" in numbers Result is False
# numbers + [6, 5, 3] Result is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1.Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers)
# 2.Change the last element of numbers to 1
numbers[6] = 1
print(numbers)
# 3.Print all the elements from numbers except the first two (slice)
print(numbers[2:])
# 4.Print whether 9 is an element of numbers
if 9 not in numbers:
    print(f" 9 is  not located in the list of numbers")
else:
    print(f"9 is located in the list")
