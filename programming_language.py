"""
CP1404 Prac_06
Simple class for a programming language
Start time: 10pm
Finish time: 10:48am
 """


class ProgrammingLanguage:
    def __init__(self, name="", typing="Static", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing , Reflection = {self.reflection}. First appeared in  {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
