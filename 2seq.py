inp_str = input('Введите элементы списка через разделитель (, ; /): ')
print()
out_list = inp_str.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()
my_list = list(set(out_list))
result_str = ''
for num in my_list:
    result_str = result_str + num
    if my_list.index(num) < (len(my_list) - 1):
        result_str = result_str + ', '
print(f'Результат: {result_str}')