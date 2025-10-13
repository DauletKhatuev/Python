# test_mysql.py
from mysql_connector import (search_by_keyword, search_by_year, search_by_min_rating, choose_min_rating, choose_genre_id,search_by_year_range, search_by_genre_id)
from logs_writer import log_search
from logs_stats import top5_popular
from formatter import format_films
from tabulate import tabulate



def paged(fetch_fn, log_params, search_type): #Функция пагинации, чтобы выводить список из 10 строк.
    # search_type — реализует поиск по какому-либо критерию
    # log_params - словарь, с параметрами поиска
    # fetch_fn - функция, которая достает данные
    limit, offset = 10, 0
    while True:
        rows = fetch_fn(limit = limit, offset = offset)
        print(format_films(rows)) #Преобразует в красивую таблицу список словарей
        params = {**log_params, "page": offset // limit}
        log_search(search_type, params, len(rows)) # Функция логирования, чтобы сохранить запрос в MongoDB
        if len(rows) < limit:
            break
        if input("Show yet 10? y/n: ").strip().lower() != "y":
            break
        offset += limit

def run(): # Вывод списка вариантов и основное окно программы
    while True:
        print("\n1) Search by word \n2) Search by years \n3) Search by year range \n4) Search by minimum ratings (choose 1...5)\n5) Search by genres\n6) Search top 5 popular requests\n0) Exit") #Добавить еще какую-нибудь хуйню
        try:
            cmd = input("choose: ").strip()
            print(f"You chose: {cmd}")
        except KeyboardInterrupt:
            print("Program interrupted by user")
        if cmd == "1":
            kw = input("Keyword: ").strip()
            paged(lambda **p: search_by_keyword(kw, **p),
                  {"keyword": kw}, "keyword")

        elif cmd == "2":
            year = int(input("Input year: "))
            paged(lambda **p: search_by_year(year, **p), {"year": year}, "year")

        elif cmd == "3":
            y1 = int(input("Since the year: "))
            y2 = int(input("By year: "))
            paged(lambda **p: search_by_year_range(y1, y2, **p),
                  {"from": y1, "to": y2}, "year_range")


        elif cmd == "4":
            min_rating = choose_min_rating()
            paged(lambda **p: search_by_min_rating(min_rating, **p),
                  {"min_rating": min_rating}, "min_rating")

        elif cmd == "5":
            cat_id = choose_genre_id()
            paged(lambda **p: search_by_genre_id(cat_id, **p),
                  {"category_id": cat_id}, "genre")
        elif cmd == "6":
            rows = top5_popular()
            if not rows:
                print("Логи пусты.")
            else:
                table = []
                for i, d in enumerate(rows, 1):
                    t = d["_id"]["type"]
                    params = d["_id"]["params"]
                    cnt = d["count"]
                    last = d.get("last", "")
                    table.append((i, t, params, cnt, last))
                print(tabulate(table,
                               headers=["#", "type", "params", "count", "last"],
                               tablefmt="github"))

        elif cmd == "0":
            print("Goodbye")
            break

        else:
            print("Unknown command. Try again.")

if __name__ == "__main__": #при запуске программы автоматически запускается и функция run()
    run()






