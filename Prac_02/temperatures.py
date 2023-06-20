"""
CP1404/CP5632 - Practical 02
Temperature conversion program

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():

    print(MENU)
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_degrees_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
            # pass
        else:
            print("Invalid option")
        print(MENU)
        choice = get_choice()
    print("Thank you.")


def calculate_degrees_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def calculate_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_choice():
    choice = input(">>> ").upper()
    return choice


main()
