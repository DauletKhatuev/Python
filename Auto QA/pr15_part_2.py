while True:
    task = input("Введите задачу: ")
    if task == "exit":
        break
    with open("tasks.txt", "a", encoding="utf-8") as f:
        f.write(task + "\n")
