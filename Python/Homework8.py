#1. Проверка кодировки
any_symbol = input('Введите символ: ')
print('Код Unicode:', ord(any_symbol))
print('ASCII символ:', ord(any_symbol) <= 127)
#2. Подстрока с заполнением
any_string = input('Введите строку: ')
begin_of_string = int(input('Введите начальный индекс: '))
end_of_string = int(input('Введите конечный индекс: '))
print('Подстрока: ', any_string[begin_of_string:end_of_string])
#3. Подсчёт символа
any_string2 = input('Введите строку: ')
any_symbol2 = input('Введите символ: ')
i = 0
quant_sym_in_str = 0
while i < len(any_string2):
    if any_symbol2 == any_string2[i]:
        quant_sym_in_str += 1
    i += 1
print('Символ встречается', quant_sym_in_str, 'раз(а).')
#4. Инвертирование строки без цифр
any_string3 = input('Введите строку: ')
i = len(any_string3) - 1
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
str_without_nums = ''
while i >= 0:
    if any_string3[i] not in numbers:
        str_without_nums += any_string3[i]
    i -= 1
print('Результат: ', str_without_nums)