from flask import Blueprint, request, jsonify

from HW4.HW4 import categories
from HW5.community_pulse.app.models import db, Category
from HW5.community_pulse.app.schemas.question import CategoryCreate,  CategoryResponse

categories_bp = Blueprint("categories", __name__, url_prefix="/categories")

# POST /categories
@categories_bp.post("/")
def create_category():
    data = CategoryCreate(**request.json)
    cat = Category(name=data.name)
    db.session.add(cat)
    db.session.commit()
    return CategoryResponse.from_orm(cat).dict(), 201

# GET/ categories
@categories_bp.get("/")
def list_categories():
    cats = Category.query.all()
    return [CategoryResponse.from_orm(c).dict() for c in cats], 200

# PUT /categories/{id}
@categories_bp.put("/<int:cat_id>")
def update_category(cat_id):
    cat = Category.query.get(cat_id)
    if cat is None:
        return jsonify({'error': 'No content'}), 404
    data = CategoryCreate(**request.json)
    cat.name = data.name
    db.session.commit()
    return CategoryResponse.from_orm(cat).dict()

# DELETE /categories/{id}
@categories_bp.delete("/<int:cat_id>")
def delete_category(cat_id):
    cat = Category.query.get_or_404(cat_id)
    db.session.delete(cat)
    db.session.commit()
    return {"deleted": cat_id}