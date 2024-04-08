# Add any model classes for Flask-SQLAlchemy here
import unicodedata
from datetime import datetime,timezone
from . import db

class movie(db.Model):
    __tablename__ = 'movies'

    id= db.Column(db.Integer, primary_key = True)
    movietitle= db.Column(db.String(150))
    description = db.Column(db.String(250))
    poster= db.Column(db.String(300))
    created_at= db.Column(db.DateTime, default=datetime.now(timezone.utc))


def __init__(self, movietitle,description,poster, created_at):
    self.movietitle= movietitle
    self.description= description
    self.poster= poster
    self.created_at= created_at

def get_id(self):
        try:
            return unicodedata(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

def __repr__(self):
    return '<Movie %r>' % (self.movietitle)