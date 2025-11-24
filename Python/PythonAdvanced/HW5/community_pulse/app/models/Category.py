#app/models/Category.py
from sqlalchemy import (
    Column, Integer, String, ForeignKey, CheckConstraint
)
from sqlalchemy.orm import declarative_base, relationship, validates

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False, unique=True)


    # связь 1→N: категория -> вопросы
    questions = relationship(
        "Question",
        back_populates="category",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Category id={self.id} name={self.name!r}>"