\# Search Films (sakila)

Консольное приложение для поиска фильмов в базе данных sakila.

Поддерживает поиск по слову, году, диапазону лет и минимальному рейтингу.

Все поисковые запросы логируются в MongoDB.



Стек технологий:



* Python 3.11+



* MySQL (sakila)



* MongoDB (логи)



* pymysql, pymongo, python-dotenv, tabulate



Структура проекта:

search\_films/

├── main.py              # главное меню, запуск программы

├── mysql\_connector.py   # функции подключения к MySQL и запросы

├── log\_writer.py        # логирование в MongoDB

├── table\_formatter.py   # красивый вывод таблиц

├── .env.example         # пример конфигурации

└── README.md            # документация



Требования к окружению:

* Python 3.11+



* доступ к MySQL с базой sakila



* доступ к MongoDB



