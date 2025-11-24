"""
Упражнение - Поиск заказов
"""

# Нужно найти те заказы, дял которых сумма > 100 и статус paid

orders = [
    {"id": 1, "user": "Андрей", "amount": 150, "status": "paid"},
    {"id": 2, "user": "Ирина", "amount": 50, "status": "canceled"},
    {"id": 3, "user": "Станислав", "amount": 200, "status": "paid"},
    {"id": 4, "user": "Сергей", "amount": 0, "status": "draft"},
    {"id": 5, "user": "Екатерина", "amount": 120, "status": "paid"}
]

# < препадаватель
# использовал лямбда-функцию
# def filter_order(order: dict) -> bool:
#     if order["amount"] > 100 and order["status"] == "paid":
#         return True
#     return False


# filtered_orders = list(filter(filter_order, orders))

filtered_orders = list(filter(
    lambda fo: fo["status"] == "paid" and fo["amount"] > 100,
    orders
))
# преподаватель >

print(filtered_orders)
