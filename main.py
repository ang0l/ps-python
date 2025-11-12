# Написать функцию calculate, которая принимает 2 числа и операцию
# "+", "-", "*", "/".

# < преподаватель
# def calculate(a: int, b: int, operation: str):
#     operations = ["+", "-", "*", "/"]

#     if operation not in operations:
#         sum = "Неверная операция"
#     if operation == "/" and b == 0:
#         sum = "Деление на ноль"

#     match operation:
#         case "+":
#             sum = a + b
#         case "-":
#             sum = a - b
#         case "*":
#             sum = a * b
#         case _:
#             sum = a / b

#     return sum

def calculate(a: float, b: float, operation: str):
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

# преподаватель >


print(calculate(2, 5, "+"))
print(calculate(2, 5, "-"))
print(calculate(2, 5, "*"))
print(calculate(2, 5, "/"))
print(calculate(2, 0, "/"))
print(calculate(2, 5, "?"))
