list1 = input("Введите первый список через пробел:").split()
list2 = input("Введите второй список через пробел:").split()

num1 = [x for x in list1 if x.isdigit()]
num2 = [y for y in list2 if y.isdigit()]

if not num1 or not num2:
    print("\nОдин или оба списка не содержат чисел.")
else:
    set1 = set(num1)
    set2 = set(num2)

    print("\nОбщие элементы ' & ':", *sorted(set1 & set2), sep=" ")
    print("\nОбщие элементы '.intersection()' :", *sorted(set1.intersection(set2)), sep=" ")