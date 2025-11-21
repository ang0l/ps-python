"""Операции над множествами
Union difference и другие
"""

a = {1, 2, 3}
b = {3, 4, 5}

# Объединение множеств
print(a | b)
print(a.union(b))  # итентичная запись с методом union()

# Пересечение множеств
print(a & b)
print(a.intersection(b))  # итентичная запись с методом intresection()

a = {1, 2, 3, 4}
b = {3, 4, 5}

# Разница множеств
print(a - b)
print(b - a)

# Симметричная разница
print(a ^ b)
# итентичная запись с методом symmetric_difference()
print(a.symmetric_difference(b))
