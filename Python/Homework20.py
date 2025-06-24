#1 Задание
n = 17
def prime_nums(num) -> bool:
    for i in range(2, num-1):
       if num % i == 0:
           return True
       else:
           return False
if prime_nums(n):
    print(f"Число {n} непростое")
else:
    print(f"Число {n} простое")

#2 Задание
result = []
filter_type = input("Введите тип фильтрации: ")
nums_input  = input("Введите числа через пробел: ").split()
nums = [int(num) for num in nums_input]
def filter_numbers(filter_type: str, *nums: int):
    if filter_type == "even":
        for num in nums:
            if num % 2 == 0:
                result.append(num)
    elif filter_type == "odd":
        for num in nums:
            if num % 2 != 0:
                result.append(num)
    elif filter_type == "prime":
        for num in nums:
            if num < 2:
                continue
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(num)
    else:
        raise ValueError("Неподдерживаемый тип фильтра. Допустимо: 'even', 'odd', 'prime'")
    return result
print(filter_numbers(filter_type, *nums))

#3 Задание
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

def merge_dicts(*dicts: dict):
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

print(merge_dicts(dict1, dict2, dict3))