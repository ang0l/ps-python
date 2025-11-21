"""Упражнение
Посетители конференции
"""

# Посчитать для каждого дня - всего визитов, уникальных визитов.
# Найти ID, кто посетили оба дня
# Найти ID, кто посетили только первый день
# Найти ID, кто посетили только второй день
# Найти ID, кто были только 1 раз

visitors_day1 = [101, 102, 103, 101, 104, 102, 105, 101]
visitors_day2 = [101, 108, 100, 101, 105, 107]

s_visitors_day1 = set(visitors_day1)
s_visitors_day2 = set(visitors_day2)

# < преподаватель
# подсчет количества посетителей для каждого дня
print(
    f"Входов в день 1: {len(visitors_day1)}, уникальных {len(s_visitors_day1)}")
print(
    f"Входов в день 2: {len(visitors_day2)}, уникальных {len(s_visitors_day2)}")
# преподаватель >

# < преподаватель
# не делает запись ID уникальных за все дни.
# print(f"Всего уникальных визитов: {s_visitors_day1.union(s_visitors_day2)}")
# преподаватель >

print(f"Оба дня посещали: {s_visitors_day1.intersection(s_visitors_day2)}")
print(
    f"Только первый день посещали: {s_visitors_day1.difference(s_visitors_day2)}")
print(
    f"Только второй день посещали: {s_visitors_day2.difference(s_visitors_day1)}")
print(
    f"только один раз были: {s_visitors_day1.symmetric_difference(s_visitors_day2)}")
