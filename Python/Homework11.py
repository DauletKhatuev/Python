#1. Звёздочки вместо чисел
text = "My number is 123-456-789"
print("Строка: ", text)
for i in range(len(text)):
    if text[i].isdigit():
        text = text.replace(text[i], '*')
print("Результат: ", text)

#2. Количество символов
text1 = "Programming in python"
text1 = text1.lower()
list_of_letters = []
for i in text1:
    if text1.count(i) > 1 and i not in list_of_letters:
        list_of_letters.append(i)
        print("Символ", i, 'встречается', text1.count(i), ' раз(а)')

#3. Увеличение чисел
text2 = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
new_str = text2.split(' ')
for i in new_str:
    if i.isdigit() and '.' not in i:
        text2 = text2.replace(i, str(float(i)*10))
    elif '.' in i and i.replace('.', '').isdigit() and i.count('.') == 1:
        text2 = text2.replace(i, str(float(i) * 10))
print(text2)