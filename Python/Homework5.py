#1. Сортировка чисел

num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
num3 = int(input('Введите третье число:'))

if num1 >= num2 >= num3:
    print(f'{num3}, {num2}, {num1}')
elif num1 >= num3 >= num2:
    print(f'{num2}, {num3}, {num1}')
elif num2 >= num1 >= num3:
    print(f'{num3}, {num1}, {num2}')
elif num2 >= num3 >= num1:
    print(f'{num1}, {num3}, {num2}')
elif num3 >= num1 >= num2:
    print(f'{num2}, {num1}, {num3}')
elif num3 >= num3 >= num1:
    print(f'{num1}, {num2}, {num3}')

#2. Високосный год
years = int(input('Введите год: '))
if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
    print('Год является високосным')
else:
    print('Год не является високосным')
