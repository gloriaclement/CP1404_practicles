import random
print(random.randint(5, 20))  # line 1

# What did you see on line 1?
# Random number between 5 and 20

# What was the smallest number you could have seen, what was the largest?
# Largest number was 20 and smallest number was 5

print(random.randrange(3, 10, 2))  # line 2

# What did you see on line 2?
# Random numbers between 3 and 10 but will have a difference of 2 if put in order.

# What was the smallest number you could have seen, what was the largest?
# The smallest number was 3 and the largest number was 9

# Could line 2 have produced a 4? No

print(random.uniform(2.5, 5.5))  # line 3


# What did you see on line 3?
# random float between the two specified numbers

# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 2.5 and the largest number could have been 5.5

print(random.randint(1, 100))  # produce a random number between 1 and 100 inclusive
