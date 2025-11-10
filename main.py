# Угадай число

secret_number = 7
guess = 0
print("Угадай число от 1 до 10")

while guess != secret_number:
    guess = int(input("Введите число: "))
    if guess < secret_number:
        print("Загаданное число больше")
    elif guess > secret_number:
        print("Загаданное число меньше")

print("Поздравляем, вы угадали")

i = 0
while i < 10:
    print("Сломался")
    i -= 10
