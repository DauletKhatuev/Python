import os
import pymysql
from formatter import format_films
from dotenv import load_dotenv

load_dotenv()
RATINGS_ORDER = ['G', 'PG', 'PG-13', 'R', 'NC-17']

def get_conn():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        cursorclass=pymysql.cursors.DictCursor
    )

# mysql_connector.py — добавь внутрь файла
def get_year_bounds(): #Функция границ лет бд
    sql = "SELECT MIN(release_year) AS min_y, MAX(release_year) AS max_y FROM film;"
    with get_conn() as c, c.cursor() as cur:
        cur.execute(sql)
        return cur.fetchone()


def search_by_keyword(keyword, limit=10, offset=0):
    sql = """
    SELECT film_id, title, release_year, rating
    FROM film
    WHERE title LIKE %s
    ORDER BY title
    LIMIT %s OFFSET %s;
    """
    args = (f"%{keyword}%", limit, offset)
    with get_conn() as c, c.cursor() as cur:
        cur.execute(sql, args)
        return cur.fetchall()


def search_by_year(year, limit=10, offset=0): # Функция поиска по годам
    sql = """ 
    SELECT film_id, title, release_year, rating
    FROM film
    WHERE release_year = %s
    ORDER BY title
    LIMIT %s OFFSET %s;""" # Параметризированный SQL-запрос
    args = (year, limit, offset)
    with get_conn() as c, c.cursor() as cur:
        cur.execute(sql, args)
        return cur.fetchall()

def search_by_year_range(y1, y2, limit=10, offset=0):
    sql = """
    SELECT film_id, title, release_year, rating
    FROM film
    WHERE release_year BETWEEN %s AND %s
    ORDER BY title
    LIMIT %s OFFSET %s;
    """
    args = (y1, y2, limit, offset)
    with get_conn() as c, c.cursor() as cur:
        cur.execute(sql, args)
        return cur.fetchall()


RATINGS_ORDER = ['G', 'PG', 'PG-13', 'R', 'NC-17']

def search_by_min_rating(min_rating: str, limit=10, offset=0):
    min_rating = min_rating.upper().strip()
    if min_rating not in RATINGS_ORDER:
        raise ValueError("Unknown rating")
    allowed = RATINGS_ORDER[RATINGS_ORDER.index(min_rating):]
    placeholders = ",".join(["%s"] * len(allowed))
    sql = f"""
    SELECT film_id, title, release_year, rating
    FROM film
    WHERE rating IN ({placeholders})
    ORDER BY title
    LIMIT %s OFFSET %s;
    """
    args = tuple(allowed) + (limit, offset)
    with get_conn() as c, c.cursor() as cur:
        cur.execute(sql, args)
        return cur.fetchall()


def search_by_min_rating(min_rating: str, limit=10, offset=0):
    min_rating = min_rating.upper().strip()
    if min_rating not in RATINGS_ORDER:
        raise ValueError(f"Неизвестный рейтинг")

    #берём все рейтинги, которые не ниже заданного
    start = RATINGS_ORDER.index(min_rating)
    allowed = RATINGS_ORDER[start:]

    # делаем IN (...) с нужным числом плейсхолдеров
    placeholders = ", ".join(["%s"] * len(allowed))
    sql = f"""
    SELECT film_id, title, release_year, rating
    FROM film
    WHERE rating IN({placeholders})
    ORDER BY title
    LIMIT %s OFFSET %s;"""

    args = tuple(allowed) + (limit, offset)
    with get_conn() as c, c.cursor() as cur:
        cur.execute(sql, args)
        return cur.fetchall()


def list_genres():
    sql = "SELECT category_id, name FROM category ORDER BY name;"
    with get_conn() as c, c.cursor() as cur:
        cur.execute(sql)
        return cur.fetchall()

def search_by_genre_id(category_id: int, limit=10, offset=0):
    sql="""
    SELECT f.film_id, f.title, f.release_year, f.rating, c.name AS genre
    FROM film AS f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c       ON fc.category_id = c.category_id
    WHERE c.category_id = %s
    ORDER BY f.title
    LIMIT %s OFFSET %s;
    """
    args = (category_id, limit, offset)
    with get_conn() as c, c.cursor() as cur:
        cur.execute(sql, args)
        return cur.fetchall()


def choose_min_rating() -> str:
    print("\n Choose minimum rating: ")
    for i, r in enumerate(RATINGS_ORDER, start=1):
        print(f"{i}. {r}")
    while True:
        s = input("Enter number (1-5): ").strip()
        if s.isdigit():
            idx = int(s)
            if 1 <= idx <= len(RATINGS_ORDER):
                return RATINGS_ORDER[idx -1]
            print("Wrong number. Try again.")


def choose_genre_id() -> int:
    genres = list_genres()
    # пронумеруем по алфавиту
    print("\nChoose gerne: ")
    for i, g in enumerate(genres, start=1):
        print(f"{i}. {g['name']}")
    while True:
        s = input("Input number of gerne: ").strip()
        if s.isdigit():
            idx = int(s)
            if 1 <= idx <= len(genres):
                chosen = genres[idx - 1]
                print(f"Choose gerne: {chosen['name']}")
                return chosen["category_id"]
        print("")


