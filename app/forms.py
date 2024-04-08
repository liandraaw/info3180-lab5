# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
    movietitle = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Photo', validators=[FileRequired(), FileAllowed(['png', 'jpg'], 'Images only! (png,jpg)')])
    