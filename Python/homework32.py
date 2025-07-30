#1 Задание
def make_rounder(decimals):
    def rounder(nums):
        return round(nums, decimals)
    return rounder


round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

#2 Задание
from datetime import datetime


def create_logger():
    events = []

    def log(message=None):
        if message is not None:
            event = f"{message}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            events.append(event)
        return events.copy()

    return log



log = create_logger()


log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")


for event in log():
    print(event)

#3 Задание
def simple_decorator(func): # Функция-декоратор, принимает другую функцию
 def wrapper(): # Вложенная функция, добавляющая дополнительное поведение
    print("_"*50)
    func() # Вызываем переданную функцию
    print("_"*50)
 return wrapper # Возвращаем изменённую функцию
@simple_decorator # Эквивалентно say_hello = simple_decorator(say_hello)
def say_hello():
 print("Привет, игрок!")
say_hello()
