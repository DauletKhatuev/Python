#1. Сумма положительных чисел
numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
result = 0

for i in numbers:
    if i > 0:
        result += i
result_text = "Сумма положительных чисел: $%.2f" % (result)
print(result_text)

#2. Счета клиентов
data_list = [

    "John 23 12345.678",

    "Alice 30 200.50",

    "Bob 35 15000.3",

    "Charlie 40 500.75" ]

for person in data_list:
    data_pers = person.split()
    print(f'Имя: {data_pers[0]:<10} | Возраст: {data_pers[1]:<3} | Баланс: {round(float(data_pers[2]), 2):<10}')
