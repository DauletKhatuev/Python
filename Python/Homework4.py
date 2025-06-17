#1. Логические операции
a = int(input('Введите первое логическое значение(1/0): '))
b = int(input('Введите второе логическое значение(1/0): '))
print(f'and: {bool(a*b)}')
print(f'or: {bool(a+b)}')
print(f'not: {bool(not a)}')
print(f'equal: {bool(a==b)}')
print(f'not equal: {bool(a!=b)}')
#2. Проверка условий
light = input('Свет включён? ')
window = input('Окно открыто? ')
if light == 'Да' or light == 'да':
    light_bool = 1
else:
    light_bool = 0
if window == 'Да' or window == 'да':
    window_bool = 1
else:
    window_bool = 0

print(f'Оба условия выполнены? {bool(window_bool and light_bool)}')
print(f'Хотя бы одно условие выполнено? {bool(window_bool or light_bool)}')


#3. Стоимость мобильного тарифа
tarif = int(input('Введите использованные мегабайты: '))
if tarif >= 500:
    print(f'Общая стоимость: {(tarif-500)*0.2+30} евро')
else:
    print('Общая стоимость: 30 евро')
