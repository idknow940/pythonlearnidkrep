import json
import sys

with open("users.json", "r") as j:
    users = j.read()


def login_check(func):
    def check(*args, **kwargs):
        login = input("[server]: login: ")
        password = input("[server]: password: ")
        if login in users and password in users:
            print("[client?(chgitem vorna asum)]: login successful!")
            print(f"[client?(chgitem vorna asum)]: logged in as {login}.")
            func(*args, **kwargs)
        else:
            print("[server]: forgot it? lol")
            again = input("[server]: try again(y): ")
            if again == "y":
                check(*args, **kwargs)
            else:
                print("access denied.")
                sys.exit()

    return check


@login_check
def printer(word):
    print(word)


printer("hi")
