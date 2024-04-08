import os 
from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy (app)
migrate = Migrate(app, db)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'movies')
from app import views,models