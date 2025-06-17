#1. Торговый автомат
price = int(input('Введите стоимость товара: '))

nominals = [50, 10, 5, 2]
quant_of_nom = [0] * 4
if price // nominals[0] > 0:
    quant_of_nom[0] += price // nominals[0]
if price % nominals[0] // nominals[1] > 0:
    quant_of_nom[1] += price % nominals[0] // nominals[1]
if price % nominals[0] % nominals[1] // nominals[2]:
    quant_of_nom[2] += price % nominals[0] % nominals[1] // nominals[2]
if price % nominals[0] % nominals[1] % nominals[2] // nominals[3]:
    quant_of_nom[3] += price % nominals[0] % nominals[1] % nominals[2] // nominals[3]
print('Внесите монеты номиналом 50: ', quant_of_nom[0])
print('Внесите монеты номиналом 10: ', quant_of_nom[1])
print('Внесите монеты номиналом 5: ', quant_of_nom[2])
print('Внесите монеты номиналом 2: ', quant_of_nom[3])

#2. Квадрат нечётных чисел
numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
for i in range(len(numbers)-1):
    if numbers[i] % 2 != 0:
        numbers[i] = numbers[i]**2
print(numbers)
