import itertools
from time import sleep

employees = ["Alice", "Bob", "Charlie"]


def generator_tasks(filename, empl):
    cycle = itertools.cycle(empl)
    attempt = 0
    while attempt < 5:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                while True:
                    line = f.readline().strip()
                    if line:
                        yield f"{next(cycle)}: {line}"
                    else:
                        sleep(5)
        except FileNotFoundError as e:
            attempt += 1
            print("Файла не существует")
            sleep(10)


tasks = generator_tasks("tasks.txt", employees)
for task in tasks:
    print(task)