#1 Задание
import os
import sys

def list_directory_contents(path):
    try:
        # Проверяем, что путь существует и это директория
        if not os.path.isdir(path):
            print(f"Ошибка: '{path}' не является директорией или путь не существует.")
            return

        print(f"\nСодержимое директории '{path}':\n")

        # Получаем список всех элементов в директории
        items = os.listdir(path)

        # Разделяем на папки и файлы
        folders = []
        files = []

        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                folders.append(item)
            else:
                files.append(item)

        # Выводим папки
        print("Папки:")
        for folder in folders:
            print(f"- {folder}")

        # Выводим файлы
        print("\nФайлы:")
        for file in files:
            print(f"- {file}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if len(sys.argv) != 2:
    print(f"Использование: python homework26.py {sys.argv[1]}")
    sys.exit(1)

directory_path = sys.argv[1]
list_directory_contents(directory_path)

#2 Задание
import os
import sys

def find_files_by_extension(directory, extension):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files

def delete_files(files):
    for file in files:
        try:
            os.remove(file)
            print(f"Удалён: {file}")
        except Exception as e:
            print(f"Ошибка при удалении {file}: {e}")

def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <директория> <расширение>")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.isdir(directory):
        print(f"Ошибка: '{directory}' не является директорией или не существует.")
        sys.exit(1)


    found_files = find_files_by_extension(directory, extension)

    if not found_files:
        print(f"Файлы с расширением '{extension}' не найдены.")
        return

    print(f"\nНайдены файлы с расширением '{extension}':")
    for file in found_files:
        print(f"- {file}")

    answer = input("\nХотите удалить эти файлы? (y/n): ").strip().lower()
    if answer == 'y':
        delete_files(found_files)
        print("Удаление завершено.")
    else:
        print("Удаление отменено.")

if __name__ == "__main__":
    main()