from datetime import datetime, date

class Student:
    def __init__(self, name: str, birthday: date):
        self.name = name
        self.birthdate = datetime.strptime(birthday, "%Y-%m-%d").date()
        if not self.

