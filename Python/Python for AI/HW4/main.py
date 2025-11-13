from sqlalchemy import (create_engine, Column, Integer, String, Float, Boolean,
                        ForeignKey, func)

from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload

from unicodedata import category

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

    products = relationship("Product", back_populates="category") #Вопрос

    def __repr__(self):
        return f"Category(id={self.id}, name={self.nume!r}"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return  f"Product(id={self.id}, name={self.name!r}, price={self.price})"

#Создание движка и сессии
engine = create_engine("sqlite:///:memory:", echo=False)
Session = sessionmaker(bind=engine)

#Создание таблиц
Base.metadata.create_all(engine)


session = Session()

#Добавление категорий
electronics = Category(name="Электроника", description="Гаджеты и устройства")
books = Category(name="Книги", description="Книги")
clothes = Category(name="Одежда", description="Одежда для мужчин и женщин.")

session.add_all([electronics, books, clothes])
session.commit()

#Добавление товаров
smartphone = Product(
    name = "Смартфон",
    price = 299.99,
    in_stock = True,
    category = electronics
)

laptop = Product(
    name = "Ноутбук",
    price=499.99,
    in_stock=True,
    category = electronics
)

scifi_book = Product(
    name = "Научно-фантастический роман",
    price=15.99,
    in_stock = True,
    category=books,
)

jeans = Product(
    name="Джинсы",
    price=40.50,
    in_stock=True,
    category=clothes,
)

tshirt = Product(
    name="Футболка",
    price = 20.00,
    in_stock=True,
    category=clothes,
)
session.add_all([smartphone, laptop, scifi_book, jeans, tshirt])
session.commit()

categories = (
    session.query(Category)
    .options(joinedload(Category.products))
    .all()
)
print("\n___________________2___________________")
for cat in categories:
    print(f"Категория: {cat.name} ({cat.description})")
    if not cat.products:
        print(" Нет товаров")
    else:
        for p in cat.products:
            print(f"Товар: {p.name}, цена: {p.price}")

smartphone = (
    session.query(Product)
    .filter(Product.name == "Смартфон")
    .order_by(Product.id)
    .first()
)


print("\n___________________3___________________")


#Изменение цены на смартфон
if smartphone:
    smartphone.price = 349.99
    session.commit()
    print("Цена  обновлена: ", smartphone)
else:
    print("Смартфон не найден")

#Подсчитать общее количество продуктов в каждой категории
results = (
    session.query(
        Category.name,
        func.count(Product.id).label("product_count")
    )
    .outerjoin(Product, Category.id == Product.category_id)
    .group_by(Category.id, Category.name)
    .all()
)


print("\n___________________4___________________")
for name, count in results:
    print(f"Категория: {name},  количество продуктов: {count}")


print("\n___________________5___________________")
#Вывести только те категории, в которых более одного продукта
results = (
    session.query(
        Category.name,
        func.count(Product.id).label("product_count")
    )
    .outerjoin(Product, Category.id == Product.category_id)
    .group_by(Category.id, Category.name)
    .having(func.count(Product.id) > 1)
    .all()
)

for name, count in results:
    print(f"Категория: {name}, продуктов: {count}")