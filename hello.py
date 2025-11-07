name, email, age = "Andrey", "a@a.ru", 56
print("Привет " + name + " с почтой " + email + " и " + str(age) + " лет!")
print("Привет {} с почтой {} и {} лет!".format(name, email, age))
print("Привет {n} с почтой {e} и {a} лет!".format(e=email, a=age, n=name))
print(f"Привет {name} с почтой {email} и {age - 1} лет!")
print(f"Привет {name} с почтой {email} и {(age - 1):.2f} лет!")
