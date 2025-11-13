user = {  # type: ignore
    "age": 37,
    "name": "Андрей",
}
print(user["name"])

user["age"] = 55
print(user)

# print(user[city])
print(user.get("city", "Москва"))

# Метод удаляет элемент с ключом. возвращает значение удаленного элемента.
value = user.pop("age")
print(value)
print(user)

exist = "name" in user
print(exist)
