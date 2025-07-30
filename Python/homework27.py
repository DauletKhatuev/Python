import os
filename = input("Введите имя файла для поиска: ")
keyword = input("Введите ключевое слово: ")

new_file = f"{os.path.splitext(keyword)[0]}_filename"
try:
    with(open(filename, "r", encoding="utf-8") as infile, open(new_file, "w", encoding="utf-8") as outfile):
        for line in infile:
            if keyword in line:
                outfile.writelines(line)
    print(f"Все строки с ключевым словом записаны в {new_file}")
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}'не найден. ")

#2 Задание
import os


def remove_duplicates(input_filename):
    base, ext = os.path.splitext(input_filename)
    output_filename = f"unique_{base}{ext}"

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        seen = set()
        unique_lines = []
        duplicates_count = 0

        for line in lines:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)
            else:
                duplicates_count += 1

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.writelines(unique_lines)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден.")



filename = input("Введите имя файла: ")
remove_duplicates(filename)