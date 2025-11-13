import random
import string


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


# 1. Показать пароли
# 2. Добавить пароль
# 3. Удалить пароль
# 4. Оновить пароль
# 5. Выход

def menu_show():
    print(
        """1. Показать пароли
2. Добавить пароль
3. Удалить пароль
4. Оновить пароль
5. Выход
"""
    )

    user_select = int(input("Ваш выбор: "))

    match user_select:
        case 1:
            print("Показать пароли")

        case 2:
            print("Добавить пароль")

        case 3:
            print("Удалить пароль")

        case 4:
            print("Оновить пароль")

        case _:
            exit()


while True:
    menu_show()
