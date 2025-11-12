def avg(*args: int):
    return sum(args) / len(args)


print(avg(1, 2, 3))
print(avg(1, 2, 3, 34, 10, 60))


def print_data(name: str, *data: str):
    print(name, data)


print_data("Андрей", "a", "b", "c")
