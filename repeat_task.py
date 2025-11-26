"""
Упражнение - Статистика заказов
"""
# Список покупок
# 1. Общую сумму всех заказов.
# 2. Количество всех проданных товаров.

from functools import reduce


orders = [
    {"id": 1, "user": "Андрей", "items": [
        {"name": "Laptop", "price": 1000},
        {"name": "Mouse", "price": 50}
    ]},
    {"id": 2, "user": "Ирина", "items": [
        {"name": "Phone", "price": 700}
    ]},
    {"id": 3, "user": "Станислав", "items": [
        {"name": "Monitor", "price": 300},
        {"name": "keyboard", "price": 100}
    ]}
]


def aggregate(acc: dict, order: dict) -> dict:
    """
    Агрегируем данные
    """
    # суммируем "price" проходя в цикле for по списку словарей в элементе "items"
    # for item in order["items"] -- проходим в цикле по списку содержащему словари
    # sum(item["price"]... -- суммируем значения "price"
    price_total = sum(item["price"] for item in order["items"])
    # в счетчик добавляем значение длины словаря из элемента "items"
    count_total = len(order["items"])
    # возвращаем словарь для сбора данных с обновленными данными
    return {
        "price_total": acc["price_total"] + price_total,
        "count_total": acc["count_total"] + count_total
    }


# reduce -- передаем aggregate, соварь orders, словарь для сбора данных с нулевыми значениями
order_list = reduce(aggregate, orders, {"price_total": 0, "count_total": 0})
print(order_list)
