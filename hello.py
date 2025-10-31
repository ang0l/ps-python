t = (1, 3, 54)
t1 = 1, 3, 5

print(t[0])
print(t[-1])

t = (1, "1", [1, 2])
print(t)
t[-1][0] = 8
print(t)
print(len(t))

l = list(t)
print(l)

t = tuple(l)
print(t)
