"""
Упражнение - Выплата зарплаты
"""

# Оставь только name и salary
# Остать только активных
# Их отсортируй по уменьшению зарплаты и выведи
# Посчитай сумму для выплат

from functools import reduce


employees = [
    {'name': 'Андрей', 'departament': 'IT', 'salary': 120000, 'active': True},
    {'name': 'Ирина', 'departament': 'HR', 'salary': 90000, 'active': False},
    {'name': 'Станислав', 'departament': 'IT', 'salary': 150000, 'active': True},
    {'name': 'Александра', 'departament': 'Finance',
        'salary': 110000, 'active': True},
    {'name': 'Екатерина', 'departament': 'IT', 'salary': 95000, 'active': False},
    {'name': 'Сергей', 'departament': 'Finance', 'salary': 130000, 'active': True},
]

employees_filter = filter(lambda a: a['active'], employees)
employees_filter = map(
    lambda a: {'name': a['name'], 'salary': a['salary']}, employees_filter)
employees_filter = sorted(employees_filter, key=lambda ef: -ef['salary'])
salary = reduce(lambda a, b: a + b['salary'], employees_filter, 0)
print(employees_filter)
print(salary)
