#1 Задание
num = 43197
def sum_digits(num: int) -> int:
    if num < 10:
        return num
    return num % 10 + sum_digits(num // 10)

print(sum_digits(num))

#2 Задание
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
def sum_digits_in_list(data: list) -> int:

    total = 0
    if isinstance(data, list):
        for item in data:
            total += sum_digits_in_list(item)
    else:
        total += data
    return total

print(sum_digits_in_list(nested_numbers))