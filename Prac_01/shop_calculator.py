"""
CP1404/CP5632 - Practical
Shop calculator to calculate discount and total price of items
"""
total = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of items: $"))
    total += price
if total > 100:
    discount = total * 0.1
    total -= discount
print(f"Total price  of {number_of_items} is ${total:.2f}")
