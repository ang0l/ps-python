# user = ("Andrey", 55)
# name = user[0]
# age = user[1]
name, age = ("Andrey", 55)
# name, age = ["Andrey", 55]
# Количество переменных должно совпадать с числом элементов списка, кортежа, строки
print(name)
print(age)

a, b = "cd"
print(a)
print(b)

# Смена значений местами
a, b = (1, 2)
temp1 = a
temp2 = b
a = temp2
b = temp1
print(a, b)
# Другой вариант
a, b = (1, 2)
temp = (a, b)
b, a = temp
print(a, b)
# Еще вариант
a, b = (1, 2)
b, a = (a, b)
print(a, b)

# Смена переменных
a, b = (1, 2)
b, a = a, b
print(a, b)
