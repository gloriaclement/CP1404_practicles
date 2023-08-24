"""
CP1404 Prac_06
Test for Guitar class
"""

from Prac_06.guitar import Guitar


def run_test():
    """ Test for Guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    # cost = 16035.4

    guitar = Guitar(name, year)
    other = Guitar("Another Guitar", 2013)

    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {9}. Got {other.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    run_test()
