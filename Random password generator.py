# ask user if they want to generate password or not
# if yes, then ask for password length
# generate password
# print the password
# if initial response is no, then exit the program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    password_length = int(input("How long do you want the password to be? : "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(characters)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password? :")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
else:
    print("Invalid input, please enter Yes/No")
    quit()