from flask_wtf import FlaskForm

# not used to with this syntax of importing modules
from wtforms.validators import DataRequired

from wtforms import StringField, PasswordField, SubmitField, BooleanField

class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')

    # multiple validators are allowed
    password = PasswordField('Password', validators=[DataRequired()]) 

    # probably little unique in flask_wtf because there's a field for submit button
    submit = SubmitField('Sign In')
