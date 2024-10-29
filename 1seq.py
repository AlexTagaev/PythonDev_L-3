size_list = int(input("Введите колличество элементов списка: "))
print()
you_list = []
for i in range(size_list):
    you_list.append(input(f'Введите {i+1} элемент: '))
you_list.sort()
print()
print(f'Вывод: {you_list}')