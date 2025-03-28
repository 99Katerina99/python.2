dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys_set = set(dct.keys())
values_set = set(dct.values())

combined_set = keys_set.union(values_set)

print("\nМножество ключей:", keys_set)
print("\nМножество значений:", values_set)
print("\nОбъединение множеств:",combined_set)