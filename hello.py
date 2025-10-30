age = input("Введите возраст: ")

# is_legal_age = False

# if int(age) < 18:
#     is_legal_age = False
# else:
#     is_legal_age = True

# if int(age) > 18:
#     is_legal_age = True

is_legal_age = True if int(age) >= 18 else False

print(is_legal_age)