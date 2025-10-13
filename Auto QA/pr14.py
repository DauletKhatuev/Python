import random
#Задача №1
from random import choice

first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]

def generator_names():
    yield choice(first_names) + " " + choice(last_names)

gen = generator_names()
print(gen.__next__())


#Задача №2
month = list(range(1, 31))
month1 = list(range(1, 30))

month_and_day = {
    1: month,
    2: list(range(1, 28)),
    3: month,
    4: month1,
    5: month,
    6: month1,
    7: month,
    8: month,
    9: month1,
    10: month,
    11: month1,
    12: month,
}
def gen_data(year):
    while True:
        month = choice(list(month_and_day.keys()))
        day = choice(month_and_day[month])
        yield f"{year}-{month:02d}-{day:02d}"



gen = gen_data(2025)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

#Задача №3

while True:
    task = input("Введите задачу: ")
    if task == "exit":
        break
    with open("tasks.txt", "a", encoding="utf-8") as f:
        f.write(task + "\n")


def generator_tasks(filename):
    with open(filename, "r", encoding="utf-8") as f:
        while True:
            line = f.readline().strip()
            if line:
                yield line

tasks = generator_tasks("tasks.txt")
for task in tasks:
    print(task)


while True:
    task = input("Введите задачу: ")
    if task == "exit":
        break
    with open("tasks.txt", "a", encoding="utf-8") as f:
        f.write(task + "\n")
def generator_tasks(filename):
    with open(filename, "r", encoding="utf-8") as f:
        while True:
            line = f.readline().strip()
            if line:
                yield line

tasks = generator_tasks("tasks.txt")
for task in tasks:
    print(task)