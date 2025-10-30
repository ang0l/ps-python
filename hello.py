age = input("Введите возраст: ")

# if int(age) < 18:
#     print("Вы еще молодой!")
# else:
#     if int(age) < 50:
#         print("Вы в самом расцвете лет!")
#     else:
#         print("Вы же уже динозавр...")

if int(age) < 18:
    print("Вы еще молодой!")
elif int(age) < 50:
    print("Вы в самом расцвете лет!")
else:
    print("Вы же уже динозавр...")
