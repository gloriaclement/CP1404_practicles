"""
CP1404 Practical
Colour code and names in a dictionary

"""

COLOUR_CODE_WITH_NAMES = {"AbsoluteZero": "#0048ba", "AcidGreen": "b0bf1a", "AliceBlue": "#f0f8ff",
                          "Alizarin Crimson": "#e32636", "BabyBlue": "#89cff0", "BabyPink": "#f4c2c2",
                          "Beige": "#f5f5dc", "BananaYellow": "#ffe135", "BarnRed": "#7c0a02 ", "ChromeYellow": "#ffa700"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODE_WITH_NAMES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")