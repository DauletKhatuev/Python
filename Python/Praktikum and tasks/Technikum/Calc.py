def division(num1, num2):
    return "Ergebnis die division: ", num1/num2


def multiplication(num1, num2):
    return "Ergebnis dir multiplication",  num1*num2

x, y = int(input("Geben Sie die erste Zahl ein: ")), int(input("Geben Sie die zweite Zahl ein: "))
print(division(x, y))
print(multiplication(x, y))

# 23
# Summe: 2 + 3
# Produkt: 2 * 3
user_num = int(input('Bitte geben Sie eine Zahl ein, welche zwei Ziffern hat!'))
def split_numbers(my_num):
  # Kondition um sicherzustellen, dass die Eingabezahl genau 2 Ziffern hat
  # 1. len
  # 2. größer kleiner zeichen
  if len(str(user_num)) != 2:
    raise Exception('Die Zahl hat weniger als 2 Ziffern!')
    # quit()
  if 9 < my_num < 100:
    # kleiner, größer Zeichen
    tenth = my_num // 10 # 23 // 10 = 2.3 -> 2
    single = my_num % 10 # 23 % 10 = 3
    return tenth, single # Collection? Tupel
  raise Exception('Die Zahl hat weniger als 2 Ziffern!')

my_split_nums = split_numbers(user_num) # Wir speichern unser Resultat als Tupel
result_sum = sum(my_split_nums)    #my_split_nums[0] + my_split_nums[-1]
result_prod = my_split_nums[0] * my_split_nums[-1]
print(result_sum, result_prod)

#Lösung
#Aufgabe
#3

# 1. Vom Benutzer: a b c
abc = []
for i in range(3):
    cur_side = float(input(f'Bitte geben Sie die Länge der {i + 1}ten Seite ein \n'))
    abc.append(cur_side)
print(abc)


def pytha_check(a, b, c):
    side_a = (c ** 2 + b ** 2 == a ** 2)
    side_b = (a ** 2 + c ** 2 == b ** 2)
    side_c = (a ** 2 + b ** 2 == c ** 2)
    if side_a or side_b or side_c:
        return True

    return False


# abc[0], abc[1], abc[-1]
print(pytha_check(*abc))