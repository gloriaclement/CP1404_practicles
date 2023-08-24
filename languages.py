"""
CP1404 - Prac_06
client code for programming languages
"""
from Prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print( python)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(f"{language.name}")


main()
