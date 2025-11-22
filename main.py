"""Frozenset"""

a = frozenset([1, 2, 3, 4, 5, 5])
b = frozenset([1, 2, 3, 4, 5, 5])

print(a)
print(a == b)

c = a | b
print(c)
# c.add(3)  # Ошибка: метод add() отсутствует. Переменная c является frozenset`ом
