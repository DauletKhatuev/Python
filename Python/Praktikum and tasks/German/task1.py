class Student():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f" Receipt {self.name}: {self.amount}"

    def is_adult(self):
        if self.amount > 18:
            return f"Student {self.name} is  years old"


class Shift():
    counter_id = 1


    def __init__(self):
        self.closed = False
        self.receipts = []
        self.id = Shift.counter_id
        Shift.counter_id += 1


    def is_closed(self):
        return self.closed

    def close(self):
        self.closed = True

    def get_total(self):
        return sum(x.amount for x in self.receipts)

    def list_receipts(self):
        for i in self.receipts:
            print(i)
        