import random
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = string.punctuation.replace("-", "")

def generate_password(**kwargs):
    length = kwargs.get("length",12)
    character = get_character(**kwargs)

    password = ""
    for i in range(length):
        password += random.choice(character)
    
    return password


def get_character(**kwargs):
    uppercase = kwargs.get("UPPERCASE")
    lowercase = kwargs.get("LOWERCASE")
    digits = kwargs.get("DIGITS")
    symbols = kwargs.get("SYMBOLS")

    character = ""
    if uppercase:
        character += UPPERCASE
    if lowercase:
        character += LOWERCASE
    if digits:
        character += DIGITS
    if symbols:
        character += symbols
    
    if len(character) == 0:
        return UPPERCASE + LOWERCASE + DIGITS + SYMBOLS
    
    return character


    