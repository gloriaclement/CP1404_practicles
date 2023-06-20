"""
CP1404/CP5632 - Practical 02
Grade according to score
"""
import random


def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))

    score = random.randint(1, 100)  # this line generates a random score
    print(score)
    print(determine_grade(score))


def determine_grade(score):
    while score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    elif score <= 89:
        return "Passable"
    else:
        return "Excellent"


main()

