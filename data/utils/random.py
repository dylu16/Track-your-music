from random import choice, randint
from string import ascii_uppercase, ascii_lowercase, digits

def get_random_password():
    random_password = ""
    for i in range(0, randint(6, 30)):
        if i % 3 == 0:
            random_password += choice(ascii_uppercase)
        elif i % 3 == 1:
            random_password += choice(ascii_lowercase)
        else:
            random_password += choice(digits)
    return random_password
