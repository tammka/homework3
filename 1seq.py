# Пользователь вводит количество элементов будущего списка и сами элементы (каждый с новой строки)
# Программа возвращает введенные элементы в виде отсортированного списка

number = int(input('Введите количество чисел: '))

user_list = [int(input(f'Введите {i+1} число: ')) for i in range(number)]

print('Отсортированный список:', sorted(user_list))