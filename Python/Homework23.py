#1 Задание
from typing import Any, List
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
def invert_str (list_val: Any) -> str:

    """

    Данная функция преобразует список с входящими значениями любого типа в строковое представление

    :param list_val: аргумент функции, которая преобразуется в строковое представление

    :return: возвращает строковое представление

    """
    result = [str(item) for item in list_val]
    return " | ".join(result)
print(invert_str(data))

#2 Задание
data = [

    {"name": "Alice", "scores": [10, 20, 30]},

    {"name": "Bob", "scores": [5, 15, 25]},

    {"name": "Charlie", "scores": [7, 17, 27]}

]

def sum_marks(group: dict) -> int:
    """

    Функция суммирует баллы всех студентов

    :param group: словарь со студентами

    :return: возвращает сумму баллов студентов

    """
    result = 0
    for student in group:
        for i in student["scores"]:
            result += int(i)
    return result

print(sum_marks(data))