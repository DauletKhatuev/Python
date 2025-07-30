#1 Задание
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

rec = Rectangle(4, 5)
print("Площадь: ", rec.get_area())

rec.width = 5
rec.height = 7
print("Новая площадь: ", rec.get_area())

#2 Задание
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        print(f"Значение увеличено, текущее: {self.value}")
        return self.value

    def decrement(self):
        self.value -= 1
        print(f"Значение уменьшено, текущее: {self.value}")
        return self.value

    def get_value(self):
        print(f"Текущее значение: {self.value}")
        return self.value

count = Counter()

count.increment()
count.increment()
count.increment()
count.decrement()
count.get_value()
