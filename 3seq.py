# Пользователь вводит два списка чисел (числа должны быть разделены пробелом)
# Программа удаляет из первого списка элементы, присутствующие во втором и выводит результат на экран

first_list = input('Введите через пробел первый набор чисел: ')
while True:
    if all(i in '0123456789 ' for i in first_list):
        first_numbers_list = first_list.split()
        break
    else:
        print('Неверный ввод данных. Список должен состоять из чисел, вводимых через пробел')
        first_list = input('Введите через пробел первый набор чисел: ')

first_numbers_list = [int(num) for num in first_numbers_list]

second_list = input('Введите через пробел второй набор чисел: ')
while True:
    if all(i in '0123456789 ' for i in second_list):
        second_numbers_list = second_list.split()
        break
    else:
        print('Неверный ввод данных. Список должен состоять из чисел, вводимых через пробел')
        second_list = input('Введите через пробел второй набор чисел: ')

second_numbers_list = [int(num) for num in second_numbers_list]

result_list = [num for num in first_numbers_list if not num in second_numbers_list]

if len(result_list) != 0:
    print('Результат: ', set(result_list))
else:
    print('Все элементы первого списка входят во второй список')
