#app/models/__init__.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
from HW5.community_pulse.app.models.response import *
from HW5.community_pulse.app.models.questions import *
from HW5.community_pulse.app.models.Category import *