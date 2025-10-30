# Максимум среди 3-х чисел с плавающей точкой
number_one   = float(input("Введите первое число: "))
number_two   = float(input("Введите второе число: "))
number_three = float(input("Введите третье число: "))

# number_max = 0.0

# number_max = number_one if number_one > number_max else number_max
# number_max = number_two if number_two > number_max else number_max
# number_max = number_three if number_three > number_max else number_max

# print(number_max)

if number_one >= number_two and number_one >= number_three:
    print(number_one)
elif number_two >= number_one and number_two >= number_three:
    print(number_two)
else:
    print(number_three)
