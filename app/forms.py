from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Proceed')

class PostForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    picture = FileField('Picture', validators=[DataRequired()])
    submit = SubmitField('Submit')