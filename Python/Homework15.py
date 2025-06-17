"""
Напишите программу, которая обрабатывает список из строк и удаляет все строки,
содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
"""
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
i = len(text_list) - 1

while i >=0:
    if ' ' in text_list[i]:
        del text_list[i]
    else:
        text_list[i] = text_list[i].lower()
    i -= 1

print(text_list)

"""
Дан список товаров с ценами. Программа должна применить скидку к каждому товару и 
добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
"""

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
sale = input("Введите скиду (в процентах): ")
max_name_len = max(len(item[0]) for item in products)
prob = ' '
print(f"Товар {prob:>4} Старая цена {prob:>4} Новая цена")
for i in products:
    print(f'{i[0]:<{max_name_len}} {prob:>4} {i[1]:>3}$ {prob:>4} {i[1]-(i[1]/100*float(sale))}$')

