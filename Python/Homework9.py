#1. Определяем максимальную ширину столбца
n = int(input("Введите число n: "))

max_width = len(str(n*n)) + 1 # вычисляем максимальное количество символов, требуемого для наибольшего числа

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Выравниваем каждое число по правому краю с заданной шириной
        print(f"{i * j:>{max_width}}", end=" ")
    print()  # Переход на новую строку после каждой строки таблицы

#2. Лестница чисел
num1  = int(input('Введите число: '))
for i in range(1, num1+1):
    for j in range (1, i+1):
        print(j, end=' ')
    print('')
#3. Удаление всех повторяющихся символов
any_str = input('Введите строку: ')
result = ""

for i in range(len(any_str)):
    is_first_occurrence = True
    for j in range(i):
        if any_str[i] == any_str[j]:
            is_first_occurrence = False
            break

    if is_first_occurrence:
        result += any_str[i]

print(result)