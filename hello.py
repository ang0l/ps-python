password = "hello, PurpleSchool! "
# Возвращает количество вхождений (int)
print(password.count("o"))
# Проверяет заканчивается ли строка указкнным символом (bool)
print(password.endswith("h"))
# Проверяет начинается ли строка указкнным символом (bool)
print(password.startswith("h"))
# Возвращает индеск первого вхождения в строке (int)
print(password.find("o"))
# Возвращает индеск первого вхождения в строке начиная от указанного индекса (int)
print(password.find("o", 10))
print(password.find("---[]"))  # Вернет "-1" (нет вхождений) (int)
print(password.index("o"))  # Работает аналогично методу find()
# Возвращает индекс первого вхождения символа в строке справа. Вернет 17, т.к. первое вхождение символа "o" справа имеет индекс 17
print(password.rfind("o"))
# Проверяет является ли значение числом. (bool). Вернет False
print(password.isnumeric())
print("123".isnumeric())  # Вернет True

t = password.split("o")  # Разделит строку по заданному символу. (list)
print(t)

role = ("Admin", "User")
all_role = " ".join(role)  # Соединяет значения в tuple, list в одну строку
print(all_role)
