"""
CP1404/CP5632 - Practical
Determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score < 50:
    print("Bad")
elif score <= 89:
    print("Passable")
else:
    print("Excellent")
