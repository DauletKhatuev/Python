from sqlalchemy.orm import joinedload



categories = (
    session.query(Category)
    .options(joinedload(Category.products))
    .all()
)