"""
Map
возводим в квадрат числа в списке
"""

num = [1, 2, 3, 4, 5]

# Ранее я сделал бы так:
# res = []

# for n in num:
#     res.append(n * n)

# print(res)

# Сейчас сделал бы так:
# def square(x: float):
#     return x * x

# squares = list(map(square, num))

# вывод в столбик, часть 1
# squares_iterator = map(lambda x: x * x, num)
# но еще лучше сделать так:
squares = list(map(lambda x: x * x, num))

print(squares)

# вывод в столбик, часть 2
# for item in squares_iterator:
#     print(item)

# использование функции map() с двумя аргументами
a = [1, 2, 3]
b = [10, 20, 30]

sums = list(map(lambda x, y: x + y, a, b))
print(sums)
