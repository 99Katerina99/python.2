string = input("Введите числа через пробел: ").strip()
items = string.split()

while True:
    power = input("Введите степень: ")
    if power.isdigit():
        power = int(power)
        break
    else:
        print("Ошибка: степень может быть только неотрицательным целым числом!")

result = []
for item in items:
    if item.lstrip('-').isdigit():
        num = int(item)
        result.append(str(num ** power))
    else:
        result.append(item * power)


print("Вывод:", " ".join(result))