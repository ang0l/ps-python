# Пользователь вводит число раундом
# Для каждого раунда вводит камень / ножницы / бумага
# Компьютер выбирает случайно и считается результат
# Считается у кого больше побед

# 1. Спрашиваем число раундов
# 2. Для каждого раунда мы получаем выбор и сравниваем
# 3. Показываем итог
import random


def select_variant():
    user_choice = None
    while user_choice not in CHOICES:
        user_choice = input(
            "Введите ваше значение (Камень/Ножницы/Бумага): ").capitalize()
        if user_choice not in CHOICES:
            print("Некорректный выбор!")
    return user_choice


def compute_game_result(user_choice: str, comp_choice: str):
    if user_choice == comp_choice:
        print(f"У компьютера {comp_choice}. Ничья")
        return (0, 0)
    elif (user_choice == "Камень" and comp_choice == "Ножницы") or \
            (user_choice == "Ножницы" and comp_choice == "Бумага") or \
            (user_choice == "Бумага" and comp_choice == "Камень"):
        print(f"У компьютера {comp_choice}. Вы выиграли этот раунд!")
        return (1, 0)
    else:
        print(f"У компьютера {comp_choice}. Вы проиграли этот раунд!")
        return (0, 1)


def print_result(user_result: int, comp_result: int):
    print("==== Итог игры ====")
    print(f"Твой счет: {user_result}")
    print(f"Счет компьютера: {comp_result}")

    if user_result > comp_result:
        print(f"Ты победил со счетом {user_result} : {comp_result}")
    elif user_result < comp_result:
        print(f"Ты проиграл со счетом {user_result} : {comp_result}")
    else:
        print(f"У вас ничья - {user_result} : {comp_result}")


CHOICES = ("Камень", "Ножницы", "Бумага")
rounds = int(input("Сколько раундов? "))
comp_score = 0
user_score = 0

for rnd in range(rounds):
    print(f"Раунд {rnd + 1}")
    user_select = select_variant()
    comp_select = random.choice(CHOICES)
    [user_mod, comp_mod] = compute_game_result(user_select, comp_select)
    user_score += user_mod
    comp_score += comp_mod


print_result(user_score, comp_score)
