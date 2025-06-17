#1 Математическое округление
float_num = float(input('Введите вещественное число: '))
if float_num - int(float_num) >= 0.5 and float_num > 0:
    print(int(float_num)+1)
elif abs(float_num - int(float_num)) >= 0.5 and float_num < 0:
    print(int(float_num) - 1)
else:
    print(int(float_num))

#2 Гипотенуза треугольника
first_side = float(input("Введите длину первого катета: "))
second_side = float(input("Введите длину второго катета: "))
hypotenuse = (first_side**2 + second_side**2)**(1/2)
print(hypotenuse)