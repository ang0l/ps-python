# Пользователь вводит число раундом
# Для каждого раунда вводит камень / ножницы / бумага
# Компьютер выбирает случайно и считается результат
# Считается у кого больше побед

# 1. Спрашиваем число раундов
# 2. Для каждого раунда мы получаем выбор и сравниваем
# 3. Показываем итог
import random

CHOICES = ("Камень", "Ножницы", "Бумага")
rounds = int(input("Сколько раундов? "))
comp_score = 0
user_score = 0

# < преподаватель
# user_select = ""
# преподаватель >

for r in range(rounds):
    print(f"Раунд {r + 1}")

    # < преподаватель
    user_select = ""
    # преподаватель >

    while user_select not in CHOICES:
        user_select = input(
            "Введите ваше значение (Камень/Ножницы/Бумага): ").capitalize()
        if user_select not in CHOICES:
            print("Некорректный выбор!")

    comp_select = random.choice(CHOICES)
    if user_select == comp_select:
        print(f"У компьютера {comp_select}. Ничья")
    elif (user_select == "Камень" and comp_select == "Ножницы") or \
            (user_select == "Ножницы" and comp_select == "Бумага") or \
            (user_select == "Бумага" and comp_select == "Камень"):
        print(f"У компьютера {comp_select}. Вы выиграли этот раунд!")
        user_score += 1
    else:
        print(f"У компьютера {comp_select}. Вы проиграли этот раунд!")
        comp_score += 1

    # < преподаватель
    # user_select = ""
    # преподаватель >

print(f"{"Вы проиграли" if comp_score > user_score else "Вы выиграли"} со счетом {user_score} : {comp_score}")
