from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import Email, InputRequired, Length, URL

class PostForm(FlaskForm):
    """Guestbook form."""
    name = StringField('Name', [
        InputRequired()])
    email = StringField('Email', [
        # Email(message=('Not a valid email address.')),
        InputRequired()])
    post = TextField('Message', [
        InputRequired(),
        Length(min=4, message=('Your message is too short.'))])
    # recaptcha = RecaptchaField()
    submit = SubmitField('Submit')