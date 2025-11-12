# Написать функцию calculate, которая принимает 2 числа и операцию
# "+", "-", "*", "/".


def calculate(a: float, b: float, operation: str):
    """
    Математическая операция над двумя числами

    :param a: Первое число
    :param b: Второе число
    :return: Число или строка ошибки
    """
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b if b != 0 else "Ошибка: деление на ноль"
        case _:
            return "Неизвестная ошибка"


print(calculate(2, 5, "+"))
print(calculate(2, 5, "-"))
print(calculate(2, 5, "*"))
print(calculate(2, 5, "/"))
print(calculate(2, 0, "/"))
print(calculate(2, 5, "?"))
