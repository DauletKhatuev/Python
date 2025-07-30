#1 Задание
orders = [

    {"product": "Laptop", "price": 1200},

    {"product": "Mouse", "price": 50},

    {"product": "Keyboard", "price": 100},

    {"product": "Monitor", "price": 300},

    {"product": "Chair", "price": 800},

    {"product": "Desk", "price": 400}

]

more_500 = filter(lambda x: x['price'] > 500, orders)
print(list(more_500))

#2 Задание
sales = [

    ("Laptop", 5, 1200),

    ("Mouse", 50, 20),

    ("Keyboard", 30, 50),

    ("Monitor", 10, 300),

    ("Chair", 20, 800)

]

revenue = {item[0]: item[1] * item[2] for item in sales}

print(revenue)