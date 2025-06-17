#1 СУММА ЦИФР ЧИСЛА
num = int(input('Введите четырехзначное число: '))
num1 = num // 1000
num2 = (num % 1000) // 100
num3 = (num % 100) // 10
num4 = num % 10
sumnum = num1 + num2 + num3 + num4
print(f'Сумма цифр числа: {sumnum}')
#2 УМНОЖЕНИЕ ЧИСЕЛ
num11 = int(input('Введите первое число'))
num22 = int(input('Введите второе число'))
print(num1*num2, num1, num2, sep='-')
#3 Вычисление без операторов % и //
num111 = int(input('Введите первое число: '))
num222 = int(input('Введите второе число: '))
print('Остаток от деления: ', num111 - int(num111/num222)*num222)
print('Целочисленное деление: ', int(num111/num222))