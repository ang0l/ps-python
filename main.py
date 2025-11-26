"""
Sorted
"""

nums = [5, 2, 9, 1, 7, 10]
print(sorted(nums))  # сортировка цифр
print(sorted(nums, reverse=True))  # обратная сортировка цифр

words = ["banana", "apple", "pear", "ab"]
words_rus = ["банан", "яблоко", "груша", "баа"]
print(sorted(words))  # сортировка английских строк
print(sorted(words_rus))  # сортировка русских строк

users = [
    {"name": "Андрей", "age": 55},
    {"name": "Ирина", "age": 56},
    {"name": "Станислав", "age": 37},
    {"name": "Денис", "age": 37}
]
print(sorted(users, key=lambda u: u["age"]))  # сортировка по возрасту
# сортировка по возрасту и имени
print(sorted(users, key=lambda u: (u["age"], u["name"])))
# обратная сортировка по возрасту и прямая по имени
print(sorted(users, key=lambda u: (-u["age"], u["name"])))
