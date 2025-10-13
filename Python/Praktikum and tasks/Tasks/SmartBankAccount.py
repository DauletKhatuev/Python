import datetime

from unicodedata import category


class SmartBankAccount:
    categorys = ["зарплата", "перевод", "подарок", "возврат", "прочее"]
    def __init__(self, _balance, _history):
        self._balance = _balance
        self._history = []


    def deposit(self, amount, category):
        try:
            if amount <= 0:
                raise "Сумма должна быть положительным значением"

            if category.lower() not in ["зарплата", "перевод", "подарок", "возврат", "прочее"]:
                raise  "Значение категории должна быть валидной"

        except:
            