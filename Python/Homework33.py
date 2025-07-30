import time
from functools import wraps


def measure_time(repeats=5):
    def decorator(func):
        call_count = 0
        total_time = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count, total_time

            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()

            call_count += 1
            total_time += end_time - start_time

            if call_count % repeats == 0:
                avg_time = total_time / repeats
                print(f"Среднее время выполнения за {repeats} вызовов: {avg_time:.6f} секунд")
                total_time = 0

            return result

        return wrapper

    return decorator


# Пример использования с разным количеством повторов
@measure_time(repeats=3)
def example_function(n):
    return sum(i * i for i in range(n))


# Тестируем
print("Тестируем example_function (repeats=3):")
for i in range(9):
    example_function(100000)
 