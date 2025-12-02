"""Экспериментальный файл"""


class BankError(Exception):
    """Наследование от Exception"""
    pass


class ZeroFundError(BankError):
    """Наследование от BankError"""
    pass


try:
    1 / 0
except ZeroDivisionError:
    print("Ошибка")
except Exception:
    print('Общая ошибка')

try:
    1 / 0
except Exception:
    print('Общая ошибка')
except ZeroDivisionError:
    print("Ошибка")

try:
    1 / 0
except ArithmeticError:
    print('Арифметическая ошибка')
except ZeroDivisionError:
    print("Ошибка")

try:
    1 / 0
except (ValueError, ZeroDivisionError):
    print('Общая ошибка')
