import datetime
from functools import total_ordering


@total_ordering
class Email:
    def __init__(self, sender: str, recipient: str, theme: str, body: str, date: datetime):
        self.sender = sender
        self.recipient = recipient
        self.theme = theme
        self.body = body
        self.date = date #Объект datetime

    def __eq__(self, other):
        return self.date == other.date

    def __len__(self):
        return len(self.body)

    def __str__(self):
        result = f"From: {self.sender} \n To: {self.recipient}\n Theme: {self.theme} \n - {self.body} -\n"

    def __bool__(self):
        return bool(self.body.strip())



class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        return Money(max(result, 0))

    def __str__(self):
        return f"${self.amount}"