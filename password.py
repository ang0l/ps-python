import random
import string

passwords = {}


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


def get_password() -> str:
    password_new = input("Введите пароль (пустой для генерации): ")
    if password_new == "":
        password_new = gen_password()
    return password_new


def is_resource(resource: str, prt_falses: bool = False) -> bool:
    if resource in passwords:
        if prt_falses:
            print("Такой ресурс уже существует.")
        return True
    if prt_falses:
        print("Такого ресурса нет")
    return False


def passwords_show():
    print(passwords)


def password_add():
    resource_new = input("Введите ресурс: ")
    if is_resource(resource_new):
        return
    passwords[resource_new] = get_password()


def password_del():
    resource_erase = input("Введите ресурс: ")
    if not is_resource(resource_erase, True):
        return
    passwords.pop(resource_erase)
    print("Пароль удален")


def password_update():
    resource_update = input("Введите ресурс: ")
    if not is_resource(resource_update, True):
        return
    passwords[resource_update] = get_password()
    print("Пароль обновлен")


def menu_show():
    print(
        """1. Показать пароли
2. Добавить пароль
3. Удалить пароль
4. Оновить пароль
5. Выход
"""
    )

    user_select = input("Ваш выбор: ")

    match user_select:
        case "1":
            passwords_show()

        case "2":
            password_add()

        case "3":
            password_del()

        case "4":
            password_update()

        case "5":
            exit()
        case _:
            print("Некорректный выбор")


while True:
    menu_show()
