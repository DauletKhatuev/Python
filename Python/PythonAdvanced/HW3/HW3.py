from sqlalchemy import (
    create_engine, Column, Integer, String, Numeric, Boolean,
    ForeignKey, CheckConstraint
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Движок к БД в памяти (одна сессия/процесс держит её живой)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)

# Задача 2: сессия
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
session = SessionLocal()

Base = declarative_base()

# Задача 4: модель Category
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)


    __table_args__ = (
        CheckConstraint("length(name) < 100", name="ck_category_name_len"), #функция на проверку соответствия значениям поля ограничениям
        CheckConstraint("description IS NULL OR length(description) <= 255", name="ck_category_desc_len"),
    )

    # Обратная сторона связи (Задача 5)
    products = relationship(
        "Product",
        back_populates="category",
        cascade="all, delete-orphan"
    )

# Задача 3: модель Product
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    # Число с фиксированной точностью (пример: до 10 знаков всего и 2 после запятой)
    price = Column(Numeric(10, 2), nullable=False)

    # Логическое значение; в SQLite хранится как INTEGER (0/1)
    in_stock = Column(Boolean, nullable=False, default=True)

    # Задача 5: связь с Category через внешний ключ
    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True
    )

    # ORM-связь
    category = relationship("Category", back_populates="products")

    # Защита длины имени для SQLite
    __table_args__ = (
        CheckConstraint("length(name) <= 100", name="ck_product_name_len"),
    )

# Создаём таблицы
Base.metadata.create_all(engine)


