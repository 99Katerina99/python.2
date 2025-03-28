words = []

while True:
    string = input("Введите строку: ").strip()
    if not string:
        print("Строка не может быть пустой!")
        continue

    words = [word.lower() for word in string.split()]
    if words:
        break
    else:
        print("Строка не может быть пустой!")

dictionary = {}
for word in words:
    dictionary[word] = dictionary.get(word, 0) + 1

for word, count in dictionary.items():
    print(f"{word}: {count}")