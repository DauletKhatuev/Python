#1 Задание
class User:
    count = 0
    def __init__(self, username, passwort):
        if not username or not passwort:
            raise ValueError("Логин  и парроль не могут быть пустыми")
        self.username = username
        self.passwort = passwort
        User.count += 1
        if len(passwort) <= 5:
            raise ValueError("Пароль должен быть строкой длиной не менее 5 символов")

    def __str__(self):
        """Строковое представление объекта"""
        return f"Пользователь {self.username}"

    @classmethod
    def get_count(cls):
        return cls.count


try:
    user1 = User("Daulet", "fdj1234fj")
    print(user1)
    print(f"Всего пользователей: {User.get_count()}")
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    user2 = User("Daulet", "fdj")
    print(user2)
    print(f"Всего пользователей: {User.get_count()}")
except ValueError as e:
    print(f"Ошибка: {e}")