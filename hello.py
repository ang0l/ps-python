"""Экспериментальный файл"""


def divide(a: float, b: float):
    if b == 0:
        raise ZeroDivisionError('Нельзя делить на 0!')
        # Также можно передавать любой объект, например:
        # raise ZeroDivisionError({'error': 1})
    return a / b


def calculate():
    try:
        divide(10, 0)
    # except ZeroDivisionError:
    #     print('Деление на 0')
    except ZeroDivisionError as e:
        print(e)
        raise  # перебрасываем на блок выше


try:
    calculate()
except ZeroDivisionError:
    # Поймали исключение в функции calculate()
    # созданное командорй raise
    print('Поймали выше')
