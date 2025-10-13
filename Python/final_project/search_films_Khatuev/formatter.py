from tabulate import tabulate

def format_films(rows):
    if not rows:
        return "Not founded"
    data = [(r["film_id"], r["title"], r.get("genre", ""), r["rating"], r["release_year"]) for r in rows] # Присваивает переменной data
    return tabulate(data, headers =["ID", "Title", "Rating", "Year"], tablefmt="github") #