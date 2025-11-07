# Проверка email
# a@a.ru = True
# d@.ru - False
# d@a.r - False
# d@com - False
# @s.com - False
# d@.com - False
# print("a" in "ztd")

# Закомментировано мое решение, чем-то не совпадающее с решением преподавателя
email = input("Введите email: ").lower()
if email == "нет":
    exit("Программа завершена")
elif email.count("@") != 1:
    exit("Email не корректный")

# email = email.split("@")
# if not (email[0]):
#     exit("Email не корректный")
name, domain = email.split("@")
if name:
    exit("Email не корректный")

# if domain.find(".") == -1:
#     exit("Email не корректный")
if "." not in domain:
    exit("Email не корректный")

domain_name, domain_country = domain.split(".")
if len(domain_country) < 2:
    exit("Email не корректный")

if not domain_name:
    exit("Email не корректный")

print("Email корректный")
