try:
    names = ["A", "B", "C", "D"]
    number = int(input(f"Enter number, up to {len(names)}:"))
    print(names[number - 1])
except IndexError:
    print("Invalid number")


