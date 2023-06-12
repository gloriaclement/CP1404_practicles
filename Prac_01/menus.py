
"""
CP1404/CP5632 - Practical
Gree ting Menu

Pseudocode for menus

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input("Name: ")
print("(H)ello (G)oodbye (Q)uit")
choice = input(">>> ")
while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print("(H)ello (G)oodbye (Q)uit")
    choice = input(">>> ")
print("Finished")
