# app/routers/questions.py
from flask import Blueprint, jsonify,  request
from unicodedata import category

from HW5.community_pulse.app.models.questions import Question
from HW5.community_pulse.app.models import db, Category
from HW5.community_pulse.app.schemas.question import QuestionResponse # Pydantic модель для ответа


questions_bp = Blueprint('questions', __name__, url_prefix='/questions')

@questions_bp.route('/', methods=['GET'])
def get_questions():
    """Получение списка всех вопросов."""
    # Используем SQLAlchemy ORM для загрузки всех вопросов
    questions = Question.query.all()
    # Преобразуем список объектов вопросов в список словарей
    results = [QuestionResponse.from_orm(question).dict() for question in
               questions]
    return jsonify(results)


@questions_bp.route('/', methods=['POST'])
def  create_question():
    """Создание нового вопроса."""

    data = request.get_json()  # Получаем данные из запроса в формате JSON
    category = Category.query.get_or_404(data.category_id)
    if not data or 'text' not in data:
        # Проверяем, что текст вопроса присутствует в данных
        return jsonify({'error': 'No question text provided'}), 400
    # Создаем экземпляр вопроса
    question = Question(
        text=data['text'],
        category_id=category.id
    )
    db.session.add(question)  # Добавляем вопрос в сессию для записи
    db.session.commit()  # Фиксируем изменения в базе данных

    return jsonify({'message': 'Вопрос создан', 'id': question.id}), 201

@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    """Получение деталей конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message':"Вопрос с таким ID не найден"}), 404
    return jsonify({'message': f"Вопрос: {question.text}"}), 200

@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    """Обновление конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404
    data = request.get_json()
    if 'text' in data:
        question.text = data['text']
        db.session.commit()
        return jsonify({'message': f"Вопрос обновлен: {question.text}"}), 200
    else:
        return jsonify({'message': "Текст вопроса не предоставлен"}), 400


@questions_bp.route('/<int:id>', methods = ['DELETE'])
def delete_question(id):
    """Удаление конкретного вопроса по его ID."""
    question = Question.query.get(id)
    if question is None:
        return jsonify({'message': "Вопрос с таким ID не найден"}), 404
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': f"Вопрос с ID {id} удален"}), 200