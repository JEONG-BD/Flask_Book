from flask_wtf import FlaskForm 
from wtforms import PasswordField, StringField, SubmitField 
from wtforms.validators import DataRequired, Email, Length 


class SignUpForm(FlaskForm):
   
    username = StringField(
        'User Name',
        validators=[DataRequired(message='The User name is required'), 
                    Length(1, 30, 'Please enter no more then 30 characters')])
    email = StringField(
        'E-Mail', 
        validators=[DataRequired('The E-Mail is required'),
                    Email('Please enter the format of your email address')])
    password = PasswordField(
        'Password',
        validators=[DataRequired('The password is required')]
    )

    submit = SubmitField("New registrations")