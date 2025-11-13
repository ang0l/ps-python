# Сделать функцию - Генератор паролей, принимающий
# length
# use_symbols
# понадобится random.choice()
import random
import string

# < преподаватель
# def gen_password(length: int, *symbols: str) -> str:
#     password = ""
#     for symbol in range(length):
#         password += random.choice(symbols)
#     return password


# print(gen_password(15, "a", "e", "d", "q", "w", "t", "y", "u", "i"))

def gen_password(lenght: int = 8, use_symbols: bool = True):
    if lenght < 3:
        return ""
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*?"

    pool = letters + digits + (symbols if use_symbols else "")

    password_chars: list[str] = []

    while len(password_chars) < lenght:
        password_chars.append(random.choice(pool))
    return "".join(password_chars)


print(gen_password())
print(gen_password(10, False))
# преподаватель >
