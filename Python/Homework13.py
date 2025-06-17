#1. Прогресс увеличения
# numbers = (3, 7, 2, 8, 5, 10, 1)
# result = []
# max_el = numbers[0]
# for i in numbers:
#     if i > max_el:
#         max_el = i
#2. Повторяющиеся элементы
numbers1 = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
repeated_nums = []
for num in numbers1:
    if numbers1.count(num) > 1 and num not in repeated_nums:
        repeated_nums.append(num)

for num in repeated_nums:
    indices = []
    for i in range(len(numbers1)): # Создаем цикл, который ищет повторяющиеся элементы в кортеже
        if numbers1[i] == num:
            indices.append(str(i)) # Добавляем индексы тех элементов, которые содержатся в спсике repeated_nums
    print(f"Индексы элемента {num}: {' '.join(indices)}")

