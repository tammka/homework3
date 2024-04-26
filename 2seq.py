# Программа принимает на вход строку с числами и возвращает уникальные значения

numbers = input('Введите числа через запятую, точку с запятой или слэш: ')

while True:
    if all(i in '0123456789,/;' for i in numbers):
        if ',' in numbers and not '/' in numbers and not ';' in numbers:
            numbers_list = numbers.split(',')
            break
        elif ';' in numbers and not '/' in numbers and not ',' in numbers:
            numbers_list = numbers.split(';')
            break
        elif '/' in numbers and not ';' in numbers and not ',' in numbers:
            numbers_list = numbers.split('/')
            break
        else:
            print("Неверный ввод данных. Можно использовать только ОДИН из следующих разделителей:',' или ';' или '/'")
    else:
        print("Неверный ввод данных. Можно использовать только ОДИН из следующих разделителей:',' или ';' или '/'")
    numbers = input('Введите числа через разделитель: ')


unique_numbers = [num for num in numbers_list if numbers_list.count(num)==1]

result = ', '.join(unique_numbers)
print('Результат:', result)

#print('Результат:', *unique_numbers)
