""" """


def main():

    password = get_password()
    while len(password) <= 8:
        print("Password is too short")
        password = get_password()
    print("*" * len(password))


def get_password():
    password = input("password: ")
    return password


main()
