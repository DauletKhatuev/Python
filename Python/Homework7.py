import random
#1. Сумма цифр числа
while_num = int(input('Введите число: '))
i = 1
sum_every_num = 0
while i <= while_num:
    sum_every_num += i
    i += 1
print('Сумма цифр: ', sum_every_num)
#2. Палиндром
palindrom = input('Введите число: ')
if palindrom == palindrom[::-1]:
    print('Число', palindrom, ' является палиндромом')
else:
    print('Число', palindrom, ' не является палиндромом')
#3. Проверь интуицию
random_num = random.randint(1, 100)
attempts = 1
print('Угадайте число от 1 до 100. У вас 10 попыток.')
while attempts <= 10:
    guess_num = int(input('Ваше предположение: '))
    if guess_num > random_num:
        print("Загаданное число меньше вашего")
    elif guess_num < random_num:
        print('Загаданное число больше вашего')
    else:
        print('Поздравляем! Вы угадали число!')
        break
    attempts += 1
if attempts < 5:
    print('Вы угадали число за', attempts, 'попытки. Отличный результат!')
elif attempts <= 8:
    print('Вы угадали число за', attempts, 'попыток. Хороший результат!')
elif attempts < 10:
    print('Вы угадали число за', attempts, 'попыток. Неплохой результат!')
else:
    print('Вы не угадали. Правильный ответ ', random_num)№