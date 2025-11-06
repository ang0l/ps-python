# Нужно просуммировать края и все, что в середине
# [10, 2, 3, 5] -> (15, 5)
# [1, 2] -> (3, 0)
res = sum([1, 2, 3])
print(res)

# l = [10, 2, 3, 5]
l = [1, 2]
first, *rest, last = l
result = (first + last, sum(rest))
print(result)
