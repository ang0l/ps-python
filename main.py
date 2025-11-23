"""Функции высшего порядка"""


def apply(func, value):
    """
    Принимает функцию и значение.
    Возвращает результат принятой функции

    :param func: функция
    :param value: число
    :return: результат вычисления принятой функции
    """
    return func(value)


def square(x: int):
    """
    Вычисляет квадрат числа

    :param x: число
    :return: квадрат принятого числа
    """
    return x * x


print(apply(square, 5))


def make_adder(n: int):
    """
    Сложение чисел

    :param n: прибавляемое число
    :return: функцию adder()
    """
    def adder(x: int):
        """
        Сложение чисел

        :param x: число
        :return: результат сложения
        """
        return x + n
    return adder


add5 = make_adder(5)
print(add5(10))
