#1 Задание
import logging
from datetime import datetime

def setup_logging():
    """Настройка логирования в файл errors.log"""
    logging.basicConfig(
        filename='errors.log',
        format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.ERROR
    )


def division() -> float:
    """
    Выполняет безопасное деление двух чисел с логированием ошибок.
    Ошибки записываются в файл errors.log.
    """
    setup_logging()  # Инициализация логирования

    try:
        num1 = float(input("Введите делимое: "))
        num2 = float(input("Введите делитель: "))

        if num2 == 0:
            raise ZeroDivisionError("Нельзя делить на 0")

        result = num1 / num2
        print(f"Результат деления: {result}")
        return result

    except ValueError:
        error_msg = "Ошибка: Введено некорректное число."
        logging.error(error_msg)
        print(error_msg)
    except ZeroDivisionError as e:
        error_msg = f"Ошибка: {e}"
        logging.error(error_msg)
        print(error_msg)

    return None

division()