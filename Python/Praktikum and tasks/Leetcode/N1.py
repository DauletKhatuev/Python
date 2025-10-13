def longestPalindrome(s: str) -> str:
    left = 0
    seen = set()
    max_length = 0
    start_index = 0  # Для хранения начальной позиции самой длинной подстроки

    for right in range(len(s)):
        # Если символ уже в текущем окне, двигаем левый указатель
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # Добавляем текущий символ в множество
        seen.add(s[right])

        # Проверяем, если длина текущего окна больше максимальной
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left  # Запоминаем начальную позицию самой длинной подстроки

    # Возвращаем саму подстроку
    return s[start_index:start_index + max_length]
