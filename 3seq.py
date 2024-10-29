inp_str_1 = input('Введите элементы 1 списка через разделитель (, ; /): ')
inp_str_2 = input('Введите элементы 2 списка через разделитель (, ; /): ')
print()
out_list_1 = inp_str_1.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()
out_list_2 = inp_str_2.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()
set_1 = set(out_list_1)
set_2 = set(out_list_2)
set_1.difference_update(set_2)
my_list = list(set_1)
result_str = ''
for num in my_list:
    result_str = result_str + num
    if my_list.index(num) < (len(my_list) - 1):
        result_str = result_str + ', '
print(f'Результат: {result_str}')