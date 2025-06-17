#1 задание
weekly_schedule = {

    "Monday": ["Gym", "Work", "Read book"],

    "Tuesday": ["Meeting", "Work", "Study Python"],

    "Wednesday": ["Shopping", "Work", "Watch movie"],

    "Thursday": ["Work", "Call parents", "Play guitar"],

    "Friday": ["Work", "Dinner with friends"],

    "Saturday": ["Hiking", "Rest"],

    "Sunday": ["Family time", "Rest"]

}



days = list(weekly_schedule.items())

import itertools
day_iterator = itertools.cycle(days)
while True:
    a = input("Нажмите Enter, чтобы узнать план на следующий день (или введите 'выход'): ")
    if a != "":
        break

    day, tasks = next(day_iterator)
    print(f"\n{day}: {', '.join(tasks)}\n")

#2 Задание
fruits = ["Apple", "Banana", "Orange"]

vegetables = ["Carrot", "Tomato", "Cucumber"]

dairy = ["Milk", "Cheese", "Yogurt"]


products = fruits + vegetables + dairy
a = iter(products)
for i in range(0, len(products)):
    print(next(a).lower())

#3 задание