"""
Reduce
"""
from functools import reduce


nums = [1, 2, 3, 4, 5]
print(sum(nums))

res = 0
for n in nums:
    res += n
print(res)

total = reduce(lambda a, b: a + b, nums)
print(total)

words = ["Привет!", "Как", "дела?"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(sentence)


# Разбор, что такое a и b в лямбде
# в функцию передается данные из итератора: аккумулятор и следующий элемент:
# сначала acc = 0 и к нему прибавляется 1 (из нашего примера)
# далее к acc = 1 прибавляется следующий 2 и acc = 3
# далее к acc = 3 прибавляется следующий 4 и acc = 7
# и т.д
# acc можно задать начальное значение, например 7 в функции reduce и acc будет изначально равен 7
# и итоговое значение будет не 15, а 22
def sum_custom(acc: int, next_item: int):
    return acc + next_item


total = reduce(sum_custom, nums, 7)
print(total)
