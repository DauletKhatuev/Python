# app/__init__.py
from flask import Flask
from HW5.community_pulse.app.routers.questions import questions_bp
from HW5.community_pulse.app.routers.response import response_bp
from HW5.community_pulse.config import DevelopmentConfig
from HW5.community_pulse.app.models import db
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app,db) 
    app.register_blueprint(questions_bp)
    app.register_blueprint(response_bp)
    return app