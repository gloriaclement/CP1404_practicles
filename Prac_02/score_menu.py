"""
CP1404/CP5632 - Practical 02
score_menu.py
Scores menu
"""

MENU = """G - Get score
P - Print result
S - Show score as stars
Q - Quit"""


def main():
    score = ""
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_grades(score)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").upper()
    print("Farewell")


def print_grades(score):
    if score < 50:
        print("Bad")
    elif score <= 89:
        print("Passable")
    else:
        print("Excellent")


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid input")
        score = int(input("Score: "))
    return score


main()
