from flask_wtf import FlaskForm 
from wtforms import PasswordField, StringField, SubmitField 
from wtforms.validators import DataRequired, Email, Length 

class UserForm(FlaskForm):

    username = StringField(
        "User Name",
        validators=[DataRequired(message='The User name is required'),
                    Length(max=30, message='Please enter no more than 30 characters'),],)
    email = StringField(
        "E-Mail",
        validators=[DataRequired(message='The E-mail is required'),
                    Email(message='Please enter the format of your email address '),],)
    password = PasswordField(
        "Password",
        validators=[DataRequired(message='The Password is required')])
    
    submit = SubmitField("New registrations ")