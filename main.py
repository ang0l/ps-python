"""
Упражнение - Нормализация данных
"""

# Нужно нормвлизовать даннные, убрав пробелы и приведя age к числу
users = [
    {"name": "  андрей ", "age": "55"},
    {"name": "ИРИНА", "age": "56"},
    {"name": "Станислав", "age": "37"},
]


def normalize_data(user) -> dict:
    return {
        "name": user["name"].lstrip().capitalize(),
        "age": int(user["age"].lstrip())
    }


normalized_users = list(map(normalize_data, users))
print(normalized_users)
