# a = 10
# b = a
# a = 7
# print(a)
# print(id(a))
# print(b)
# print(id(b))

a = [10, 0]
b = a
a[0] = 3
print(a)
print(id(a))
print(b)
print(id(b))
