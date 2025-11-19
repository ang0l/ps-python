user = {  # type: ignore
    "age": 37,
    "name": "Андрей",
}
user["city"] = "Краснодар"
user["age"] = 55

for key in user:
    print(key)

for key in user.keys():
    print(key)

for key, value in user.items():
    print(f"{key}: {value}")

for value in user.values():
    print(value)
